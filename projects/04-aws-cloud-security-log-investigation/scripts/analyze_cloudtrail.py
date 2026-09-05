"""
Analyze CloudTrail JSON or CSV exports and generate investigation artifacts.

The script is intentionally dependency-free. It supports common CloudTrail shapes:
- S3-delivered trail files with a top-level "Records" list
- lookup-events output with a top-level "Events" list and "CloudTrailEvent"
- a plain JSON list of event objects
- CSV exports with common CloudTrail/Event History column names
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SEVERITY_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Informational": 4}

LOGGING_EVENTS = {"StopLogging", "DeleteTrail", "UpdateTrail", "PutEventSelectors"}
PRIVILEGE_EVENTS = {"AttachUserPolicy", "AttachRolePolicy", "PutUserPolicy", "PutRolePolicy"}
S3_EXPOSURE_EVENTS = {"DeletePublicAccessBlock", "PutBucketPolicy", "PutBucketAcl"}
GUARDDUTY_EVENTS = {"CreateDetector", "UpdateDetector", "DeleteDetector"}
REMEDIATION_EVENTS = {"RevokeSecurityGroupIngress", "PutPublicAccessBlock", "StartLogging"}
DENIED_PATTERNS = ("AccessDenied", "UnauthorizedOperation", "AccessDeniedException")
PUBLIC_CIDRS = ("0.0.0.0/0", "::/0")
ADMIN_PORTS = {22, 3389}


@dataclass
class Finding:
    severity: str
    category: str
    signal: str
    event_time: str
    event_name: str
    event_source: str
    actor: str
    source_ip: str
    why_it_matters: str
    recommendation: str

    def sort_key(self) -> tuple[int, str]:
        return (SEVERITY_ORDER.get(self.severity, 99), self.event_time)


def load_events(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".csv":
        return load_csv_events(path)
    with path.open(encoding="utf-8-sig") as handle:
        payload = json.load(handle)
    return normalize_json_payload(payload)


def normalize_json_payload(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [event for event in payload if isinstance(event, dict)]
    if not isinstance(payload, dict):
        return []
    if isinstance(payload.get("Records"), list):
        return [event for event in payload["Records"] if isinstance(event, dict)]
    if isinstance(payload.get("Events"), list):
        events: list[dict[str, Any]] = []
        for wrapper in payload["Events"]:
            if not isinstance(wrapper, dict):
                continue
            cloudtrail_event = wrapper.get("CloudTrailEvent")
            if isinstance(cloudtrail_event, str):
                try:
                    parsed = json.loads(cloudtrail_event)
                    if isinstance(parsed, dict):
                        events.append(parsed)
                        continue
                except json.JSONDecodeError:
                    pass
            events.append(wrapper)
        return events
    return [payload]


def load_csv_events(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    return [normalize_csv_row(row) for row in rows]


def pick(row: dict[str, str], *names: str) -> str:
    lower_map = {key.lower().replace(" ", "").replace("_", ""): value for key, value in row.items()}
    for name in names:
        normalized = name.lower().replace(" ", "").replace("_", "")
        if normalized in lower_map:
            return lower_map[normalized] or ""
    return ""


def normalize_csv_row(row: dict[str, str]) -> dict[str, Any]:
    event_name = pick(row, "eventName", "Event name", "EventName")
    event_source = pick(row, "eventSource", "Event source", "EventSource")
    event_time = pick(row, "eventTime", "Event time", "EventTime")
    actor = pick(row, "userName", "User name", "Username", "User")
    source_ip = pick(row, "sourceIPAddress", "Source IP address", "Source IP")
    error_code = pick(row, "errorCode", "Error code")
    return {
        "eventTime": event_time,
        "eventName": event_name,
        "eventSource": event_source,
        "sourceIPAddress": source_ip,
        "errorCode": error_code,
        "userIdentity": {"type": pick(row, "User type", "userIdentity.type"), "userName": actor},
        "requestParameters": row,
        "responseElements": row,
    }


def flatten_text(value: Any) -> str:
    try:
        return json.dumps(value, sort_keys=True)
    except TypeError:
        return str(value)


def event_name(event: dict[str, Any]) -> str:
    return str(event.get("eventName") or "Unknown")


def event_source(event: dict[str, Any]) -> str:
    return str(event.get("eventSource") or "Unknown")


def event_time(event: dict[str, Any]) -> str:
    return str(event.get("eventTime") or "Unknown")


def source_ip(event: dict[str, Any]) -> str:
    return str(event.get("sourceIPAddress") or "Unknown")


def identity(event: dict[str, Any]) -> dict[str, Any]:
    raw = event.get("userIdentity")
    return raw if isinstance(raw, dict) else {}


def actor(event: dict[str, Any]) -> str:
    ident = identity(event)
    if ident.get("type") == "Root":
        return "Root"
    if ident.get("userName"):
        return str(ident["userName"])
    session_context = ident.get("sessionContext")
    if isinstance(session_context, dict):
        issuer = session_context.get("sessionIssuer")
        if isinstance(issuer, dict) and issuer.get("userName"):
            return str(issuer["userName"])
    if ident.get("arn"):
        return str(ident["arn"]).split("/")[-1]
    return str(ident.get("type") or "Unknown")


def identity_type(event: dict[str, Any]) -> str:
    return str(identity(event).get("type") or "Unknown")


def error_code(event: dict[str, Any]) -> str:
    return str(event.get("errorCode") or "")


def console_login_result(event: dict[str, Any]) -> str:
    response = event.get("responseElements")
    if isinstance(response, dict):
        return str(response.get("ConsoleLogin") or "")
    return ""


def contains_public_cidr(event: dict[str, Any]) -> bool:
    text = flatten_text(event)
    return any(cidr in text for cidr in PUBLIC_CIDRS)


def contains_admin_port(event: dict[str, Any]) -> bool:
    text = flatten_text(event)
    for port in ADMIN_PORTS:
        if re.search(rf'("fromPort"|fromPort|port)["\s:]*{port}\b', text) or re.search(rf'("toPort"|toPort|port)["\s:]*{port}\b', text):
            return True
    return False


def public_bucket_policy(event: dict[str, Any]) -> bool:
    if event_name(event) not in {"PutBucketPolicy", "PutBucketAcl"}:
        return False
    text = flatten_text(event.get("requestParameters", event))
    return '"Principal": "*"' in text or '"Principal":"*"' in text or "AllUsers" in text or "AuthenticatedUsers" in text


def add_finding(findings: list[Finding], event: dict[str, Any], severity: str, category: str, signal: str, why: str, recommendation: str) -> None:
    findings.append(
        Finding(
            severity=severity,
            category=category,
            signal=signal,
            event_time=event_time(event),
            event_name=event_name(event),
            event_source=event_source(event),
            actor=actor(event),
            source_ip=source_ip(event),
            why_it_matters=why,
            recommendation=recommendation,
        )
    )


def analyze_event(event: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    name = event_name(event)
    err = error_code(event)

    if identity_type(event) == "Root":
        add_finding(
            findings,
            event,
            "High",
            "Identity",
            "Root account activity",
            "Root account activity is high impact and should be rare, intentional, and protected by MFA.",
            "Confirm the activity was expected, verify MFA, and review actions that followed the login.",
        )

    if name == "ConsoleLogin" and console_login_result(event) == "Failure":
        add_finding(
            findings,
            event,
            "Medium",
            "Identity",
            "Failed console login",
            "Failed sign-in activity can indicate user error, misconfiguration, or attempted access.",
            "Review the identity, source IP, repeated attempts, and any successful login after the failure.",
        )

    if name == "CreateAccessKey":
        add_finding(
            findings,
            event,
            "High",
            "Credential",
            "Access key created",
            "Long-lived access keys can become persistence or data access risk when they are unnecessary or unmanaged.",
            "Validate business need, remove unused keys, rotate keys as needed, and prefer temporary credentials.",
        )

    if name in PRIVILEGE_EVENTS:
        add_finding(
            findings,
            event,
            "High",
            "Privilege",
            "Privilege policy changed",
            "IAM policy changes can expand what an identity is allowed to do.",
            "Confirm approval, scope the granted permissions, and replace broad access with least privilege.",
        )

    if name == "AuthorizeSecurityGroupIngress" and contains_public_cidr(event):
        severity = "Critical" if contains_admin_port(event) else "High"
        add_finding(
            findings,
            event,
            severity,
            "Network Exposure",
            "Public security group ingress",
            "Public inbound access can expose cloud resources to internet scanning and unauthorized access attempts.",
            "Revoke unnecessary public access, restrict source ranges, and alert on public administrative ports.",
        )

    if name in S3_EXPOSURE_EVENTS and (name == "DeletePublicAccessBlock" or public_bucket_policy(event)):
        add_finding(
            findings,
            event,
            "High",
            "Data Exposure",
            "S3 public access control weakened",
            "S3 public-access changes can expose sensitive data if not reviewed and tightly controlled.",
            "Keep Block Public Access enabled, validate bucket policy scope, and review Access Analyzer findings.",
        )

    if name in LOGGING_EVENTS:
        add_finding(
            findings,
            event,
            "Critical",
            "Logging",
            "CloudTrail logging changed",
            "CloudTrail changes can reduce the ability to reconstruct account activity during an investigation.",
            "Validate change approval, restore logging if needed, and restrict CloudTrail administration.",
        )

    if name in GUARDDUTY_EVENTS:
        add_finding(
            findings,
            event,
            "High",
            "Detection",
            "GuardDuty configuration changed",
            "Detection coverage changes should be intentional, documented, and reviewed.",
            "Confirm GuardDuty status matches the lab plan and document the reason for the change.",
        )

    if any(pattern in err for pattern in DENIED_PATTERNS):
        add_finding(
            findings,
            event,
            "Medium",
            "Denied Activity",
            "Access denied activity",
            "Denied actions are useful investigation signals because they show attempted behavior even when blocked.",
            "Review whether the denied action was expected, misconfigured, or suspicious.",
        )

    if name in REMEDIATION_EVENTS:
        add_finding(
            findings,
            event,
            "Informational",
            "Remediation",
            "Remediation evidence",
            "Corrective events help complete the timeline and show whether a risky change was reversed.",
            "Document the remediation and confirm the final resource state.",
        )

    return findings


def write_counter_csv(path: Path, header: tuple[str, str], counter: Counter[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        for key, value in counter.most_common():
            writer.writerow([key, value])


def write_findings_csv(path: Path, findings: list[Finding]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["severity", "category", "signal", "event_time", "event_name", "event_source", "actor", "source_ip", "why_it_matters", "recommendation"])
        for finding in findings:
            writer.writerow([
                finding.severity,
                finding.category,
                finding.signal,
                finding.event_time,
                finding.event_name,
                finding.event_source,
                finding.actor,
                finding.source_ip,
                finding.why_it_matters,
                finding.recommendation,
            ])


def markdown_table(rows: list[list[str]]) -> list[str]:
    if not rows:
        return []
    header = rows[0]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    for row in rows[1:]:
        escaped = [str(value).replace("|", "\\|") for value in row]
        lines.append("| " + " | ".join(escaped) + " |")
    return lines


def build_report(events: list[dict[str, Any]], findings: list[Finding]) -> str:
    event_names = Counter(event_name(event) for event in events)
    event_sources = Counter(event_source(event) for event in events)
    actors = Counter(actor(event) for event in events)
    source_ips = Counter(source_ip(event) for event in events)
    severities = Counter(finding.severity for finding in findings)

    lines = [
        "# CloudTrail Investigation Report",
        "",
        "Generated by `scripts/analyze_cloudtrail.py`.",
        "",
        "## Dataset Summary",
        "",
        f"- Events reviewed: {len(events)}",
        f"- Findings generated: {len(findings)}",
        f"- Unique event names: {len(event_names)}",
        f"- Unique event sources: {len(event_sources)}",
        f"- Unique actors: {len(actors)}",
        f"- Unique source IPs: {len(source_ips)}",
        "",
        "## Finding Severity Summary",
        "",
    ]

    severity_rows = [["Severity", "Count"]]
    for severity in ["Critical", "High", "Medium", "Low", "Informational"]:
        severity_rows.append([severity, str(severities.get(severity, 0))])
    lines.extend(markdown_table(severity_rows))

    lines.extend(["", "## Top Event Names", ""])
    name_rows = [["Event name", "Count"]]
    for name, count in event_names.most_common(10):
        name_rows.append([name, str(count)])
    lines.extend(markdown_table(name_rows))

    lines.extend(["", "## Top Event Sources", ""])
    source_rows = [["Event source", "Count"]]
    for source, count in event_sources.most_common(10):
        source_rows.append([source, str(count)])
    lines.extend(markdown_table(source_rows))

    lines.extend(["", "## Findings", ""])
    finding_rows = [["Severity", "Signal", "Time", "Event", "Actor", "Why it matters", "Recommended action"]]
    for finding in sorted(findings, key=lambda item: item.sort_key()):
        finding_rows.append([
            finding.severity,
            finding.signal,
            finding.event_time,
            finding.event_name,
            finding.actor,
            finding.why_it_matters,
            finding.recommendation,
        ])
    lines.extend(markdown_table(finding_rows))

    lines.extend(
        [
            "",
            "## Analyst Summary",
            "",
            "The highest-priority review items are events that affect visibility, privilege, public exposure, or long-lived credentials. Denied actions are also useful because they show behavior that AWS blocked but an analyst should still understand.",
            "",
            "## Recommended Follow-Up",
            "",
            "- Confirm root activity was expected and MFA protected.",
            "- Review IAM policy changes and remove unnecessary broad permissions.",
            "- Confirm access keys are needed, rotated, and monitored.",
            "- Revoke public administrative ingress and validate final security group state.",
            "- Keep S3 Block Public Access enabled and review any public policy attempts.",
            "- Alert on CloudTrail and GuardDuty configuration changes.",
            "",
            "## Boundary Statement",
            "",
            "This report is based on lab or sanitized CloudTrail evidence. It does not prove compromise and does not assess any production organization.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze CloudTrail JSON/CSV exports.")
    parser.add_argument("inputs", nargs="+", type=Path, help="CloudTrail JSON or CSV files to analyze.")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()

    events: list[dict[str, Any]] = []
    for path in args.inputs:
        events.extend(load_events(path))

    findings: list[Finding] = []
    for event in events:
        findings.extend(analyze_event(event))
    findings.sort(key=lambda item: item.sort_key())

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_findings_csv(args.output_dir / "cloudtrail-findings.csv", findings)
    write_counter_csv(args.output_dir / "event-name-frequency.csv", ("event_name", "count"), Counter(event_name(event) for event in events))
    write_counter_csv(args.output_dir / "event-source-frequency.csv", ("event_source", "count"), Counter(event_source(event) for event in events))
    write_counter_csv(args.output_dir / "actor-frequency.csv", ("actor", "count"), Counter(actor(event) for event in events))
    report = build_report(events, findings)
    report_path = args.output_dir / "sample-cloudtrail-investigation-report.md"
    report_path.write_text(report, encoding="utf-8")

    print(f"Events reviewed: {len(events)}")
    print(f"Findings generated: {len(findings)}")
    print(f"Report written: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
