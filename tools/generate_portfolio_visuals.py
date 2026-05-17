"""
Generate portfolio SVG visuals.

This script intentionally keeps visual generation deterministic and dependency-free.
It reads the public data snapshots already stored in the repository and writes SVG
artifacts that can be embedded directly in GitHub Markdown.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
from collections import Counter, defaultdict
from pathlib import Path


INK = "#172033"
MUTED = "#667085"
LINE = "#d8dee9"
PAPER = "#ffffff"
CANVAS = "#f5f7fb"
BLUE = "#1f5eff"
TEAL = "#0f9f9a"
GREEN = "#1f9d55"
AMBER = "#c97a10"
RED = "#cc3f3f"
PURPLE = "#6f56d9"
SLATE = "#475569"
PALETTE = [BLUE, TEAL, GREEN, AMBER, RED, PURPLE, SLATE]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def parse_int(value: str) -> int:
    cleaned = (value or "").replace(",", "").strip()
    return int(cleaned) if cleaned else 0


def parse_date(value: str) -> dt.date | None:
    value = (value or "").strip()
    if not value:
        return None
    return dt.date.fromisoformat(value)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def wrap_words(value: str, max_chars: int) -> list[str]:
    words = str(value).split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        candidate = " ".join(current + [word])
        if len(candidate) <= max_chars:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines or [str(value)]


def compact_number(value: int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return f"{value:,}"


class Svg:
    def __init__(self, width: int, height: int, title: str, desc: str) -> None:
        self.width = width
        self.height = height
        self.footer_added = False
        self.parts: list[str] = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc" data-qc-version="2" data-qc-polish="true">',
            f"<title id=\"title\">{esc(title)}</title>",
            f"<desc id=\"desc\">{esc(desc)}</desc>",
            "<defs>",
            '<linearGradient id="canvasGrad" x1="0" x2="1" y1="0" y2="1">',
            '<stop offset="0%" stop-color="#f8fbff"/>',
            '<stop offset="100%" stop-color="#eef3f8"/>',
            "</linearGradient>",
            '<filter id="cardShadow" x="-8%" y="-8%" width="116%" height="116%">',
            '<feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#0f172a" flood-opacity="0.08"/>',
            "</filter>",
            '<marker id="arrowHead" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto" markerUnits="strokeWidth">',
            '<path d="M2,2 L12,7 L2,12 Z" fill="#172033"/>',
            "</marker>",
            "<style>",
            ".font { font-family: Segoe UI, Arial, Helvetica, sans-serif; }",
            "</style>",
            "</defs>",
            f'<rect width="100%" height="100%" fill="{PAPER}"/>',
            f'<rect data-qc-frame="true" x="24" y="24" width="{width - 48}" height="{height - 48}" rx="28" fill="url(#canvasGrad)" stroke="{LINE}"/>',
            '<path d="M44 122 H1236" stroke="#dde6f3" stroke-width="1"/>',
        ]

    def text(self, x: int, y: int, value: str, size: int = 14, weight: int = 400, color: str = INK, anchor: str = "start") -> None:
        self.parts.append(
            f'<text class="font" x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{esc(value)}</text>'
        )

    def line(self, x1: int, y1: int, x2: int, y2: int, color: str = LINE, width: int = 1) -> None:
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')

    def arrow(self, d: str) -> None:
        self.parts.append(
            f'<path data-qc-arrow="true" d="{esc(d)}" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrowHead)"/>'
        )

    def header(self, title: str, subtitle: str, eyebrow: str | None = None) -> None:
        if eyebrow:
            self.parts.append(f'<rect x="64" y="58" width="168" height="28" rx="14" fill="#e8eefc"/>')
            self.text(84, 78, eyebrow, 12, 700, BLUE)
        self.parts.append(f'<rect x="{self.width - 270}" y="58" width="198" height="30" rx="15" fill="#ecfdf5" stroke="#b8e7d6"/>')
        self.text(self.width - 250, 78, "QC-ready artifact", 12, 700, "#087f5b")
        self.text(64, 126 if eyebrow else 88, title, 34, 800)
        self.text(64, 158 if eyebrow else 120, subtitle, 16, 400, MUTED)

    def card_start(self, x: int, y: int, w: int, h: int, accent: str | None = None) -> None:
        self.parts.append(f'<g data-qc-card="true">')
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{PAPER}" stroke="{LINE}" filter="url(#cardShadow)"/>')
        if accent:
            self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="7" rx="3.5" fill="{accent}"/>')

    def card_end(self) -> None:
        self.parts.append("</g>")

    def metric_card(self, x: int, y: int, w: int, h: int, label: str, value: str, note: str, color: str) -> None:
        self.card_start(x, y, w, h, color)
        self.text(x + 24, y + 38, label, 13, 700, SLATE)
        self.text(x + 24, y + 80, value, 31, 800, color)
        for index, line in enumerate(wrap_words(note, 30)[:2]):
            self.text(x + 24, y + 109 + index * 16, line, 12, 400, MUTED)
        self.card_end()

    def narrative_card(self, x: int, y: int, w: int, h: int, title: str, lines: list[str], color: str) -> None:
        self.card_start(x, y, w, h, color)
        self.text(x + 24, y + 42, title, 16, 800)
        max_chars = min(60, max(24, int((w - 64) / (13 * 0.55))))
        wrapped: list[str] = []
        for line in lines:
            wrapped.extend(wrap_words(line, max_chars))
        for index, line in enumerate(wrapped[:4]):
            self.text(x + 24, y + 72 + index * 20, line, 13, 400, MUTED)
        self.card_end()

    def bar_panel(self, x: int, y: int, w: int, h: int, title: str, subtitle: str, rows: list[tuple[str, int]], color: str, max_rows: int = 6) -> None:
        rows = rows[:max_rows]
        self.card_start(x, y, w, h, color)
        self.text(x + 26, y + 42, title, 18, 800)
        self.text(x + 26, y + 66, subtitle, 13, 400, MUTED)
        chart_x = x + 26
        label_w = min(260, int(w * 0.33))
        bar_x = chart_x + label_w + 18
        bar_w = w - label_w - 146
        top = y + 102
        row_h = max(46, int((h - 132) / max(len(rows), 1)))
        max_value = max([value for _, value in rows] + [1])
        for tick in [0.25, 0.5, 0.75, 1.0]:
            gx = bar_x + int(bar_w * tick)
            self.parts.append(f'<line x1="{gx}" y1="{top - 12}" x2="{gx}" y2="{top + len(rows) * row_h - 18}" stroke="#edf1f7" stroke-width="1"/>')
        for index, (label, value) in enumerate(rows):
            yy = top + index * row_h
            label_lines = wrap_words(label, 26)[:2]
            self.parts.append(f'<rect x="{chart_x}" y="{yy - 4}" width="28" height="28" rx="14" fill="#eef3ff"/>')
            self.text(chart_x + 14, yy + 17, str(index + 1), 11, 800, BLUE, "middle")
            for line_index, line in enumerate(label_lines):
                self.text(chart_x + 40, yy + 18 + line_index * 15, line, 12, 600, INK)
            self.parts.append(f'<rect x="{bar_x}" y="{yy}" width="{bar_w}" height="24" rx="12" fill="#e6ebf2"/>')
            actual = max(4, int((value / max_value) * bar_w))
            self.parts.append(f'<rect x="{bar_x}" y="{yy}" width="{actual}" height="24" rx="12" fill="{PALETTE[index % len(PALETTE)] if color == "multi" else color}"/>')
            self.text(bar_x + bar_w + 14, yy + 18, compact_number(value), 12, 800, INK)
        self.card_end()

    def footer(self, source: str, note: str) -> None:
        self.footer_added = True
        y = self.height - 54
        self.parts.append('<g data-qc-footer="true">')
        self.parts.append(f'<rect x="48" y="{y - 22}" width="{self.width - 96}" height="34" rx="17" fill="#ffffff" stroke="#dbe3ef"/>')
        self.text(70, y, f"Source: {source}", 12, 600, MUTED)
        self.text(self.width - 70, y, note, 12, 700, "#087f5b", "end")
        self.parts.append("</g>")

    def save(self, path: Path) -> None:
        if not self.footer_added:
            self.footer("public-source analysis", "QC-ready")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(self.parts + ["</svg>"]), encoding="utf-8")


def counter_by(rows: list[dict[str, str]], field: str) -> Counter[str]:
    return Counter((row.get(field) or "Unknown").strip() or "Unknown" for row in rows)


def affected_by(rows: list[dict[str, str]], field: str) -> dict[str, int]:
    totals: dict[str, int] = defaultdict(int)
    for row in rows:
        key = (row.get(field) or "Unknown").strip() or "Unknown"
        totals[key] += parse_int(row.get("individuals_affected", "0"))
    return dict(totals)


def cwe_counter(rows: list[dict[str, str]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        raw = row.get("cwes", "")
        for part in raw.replace("[", "").replace("]", "").replace("'", "").split(","):
            cwe = part.strip()
            if cwe:
                counts[cwe] += 1
    return counts


def project1_dashboard(rows: list[dict[str, str]], path: Path) -> None:
    breach_counts = counter_by(rows, "type_of_breach")
    location_counts = counter_by(rows, "location_of_breached_information")
    entity_counts = counter_by(rows, "covered_entity_type")
    total_affected = sum(parse_int(row.get("individuals_affected", "0")) for row in rows)
    ba_present = sum(1 for row in rows if row.get("business_associate_present", "").strip().lower() == "yes")

    svg = Svg(1280, 860, "Healthcare breach risk dashboard", "Premium visual summary of the HHS OCR healthcare breach sample.")
    svg.header("Healthcare Breach Risk Snapshot", "Public HHS OCR sample translated into near-term risk priorities.", "Project 1")
    metrics = [
        ("Records", f"{len(rows):,}", "Recent HHS OCR breach reports sampled.", BLUE),
        ("Individuals", compact_number(total_affected), "Affected individuals across the sample.", TEAL),
        ("Hacking/IT", f"{breach_counts.get('Hacking/IT Incident', 0)}%", "Dominant reported breach type.", RED),
        ("BA present", f"{ba_present}", "Records with business associate involvement.", AMBER),
    ]
    for index, metric in enumerate(metrics):
        svg.metric_card(64 + index * 294, 190, 260, 154, *metric)
    svg.bar_panel(64, 374, 552, 344, "Reported Breach Type", "Frequency by public OCR category", breach_counts.most_common(), BLUE, 4)
    svg.bar_panel(664, 374, 552, 344, "Information Location", "Where breached information was reported", location_counts.most_common(5), TEAL, 5)
    svg.narrative_card(64, 730, 356, 110, "Primary Read", ["Server and email controls drive the first risk conversation."], BLUE)
    svg.narrative_card(462, 730, 356, 110, "Governance Angle", ["Third-party involvement needs ownership, cadence, and evidence."], AMBER)
    svg.narrative_card(860, 730, 356, 110, "Executive Lens", ["A few large events can dominate patient and business impact."], RED)
    svg.footer("HHS OCR sample, collected 2026-05-16", "QC gate enforced")
    svg.save(path)


def project1_bar(path: Path, title: str, subtitle: str, rows: list[tuple[str, int]], color: str, max_rows: int = 8) -> None:
    panel_rows = min(max_rows, len(rows))
    panel_h = 214 + panel_rows * 48
    height = 258 + panel_h + 116
    svg = Svg(1120, height, title, subtitle)
    svg.header(title, subtitle, "Project 1")
    svg.bar_panel(72, 178, 976, panel_h, "Evidence View", "Generated from the local HHS OCR sample.", rows, color, max_rows)
    svg.narrative_card(72, 198 + panel_h, 976, 112, "How To Read It", ["Use the chart as a prioritization signal, then validate local controls, ownership, and exposure."], color)
    svg.footer("HHS OCR sample, collected 2026-05-16", "QC gate enforced")
    svg.save(path)


def generate_project1(root: Path) -> None:
    project = root / "projects" / "01-nist-csf-risk-assessment"
    rows = read_csv(project / "data" / "hhs-ocr-breach-sample-2026-05-16.csv")
    visuals = project / "visuals"
    project1_dashboard(rows, visuals / "healthcare-breach-dashboard.svg")
    project1_bar(visuals / "breach-type-distribution.svg", "Breach Type Distribution", "Public OCR records grouped by reported breach type.", counter_by(rows, "type_of_breach").most_common(), BLUE, 4)
    project1_bar(visuals / "information-location-records.svg", "Location Of Breached Information", "Reported information locations in the sampled records.", counter_by(rows, "location_of_breached_information").most_common(), TEAL, 8)
    project1_bar(visuals / "affected-individuals-by-breach-type.svg", "Affected Individuals By Breach Type", "Impact scale grouped by reported breach type.", sorted(affected_by(rows, "type_of_breach").items(), key=lambda item: item[1], reverse=True), RED, 4)
    project1_bar(visuals / "entity-type-distribution.svg", "Covered Entity Type Distribution", "Sampled reports grouped by covered entity type.", counter_by(rows, "covered_entity_type").most_common(), GREEN, 4)


def exposure_category(row: dict[str, str]) -> tuple[str, int]:
    text = " ".join([row.get("vendorProject", ""), row.get("product", ""), row.get("vulnerabilityName", ""), row.get("shortDescription", "")]).lower()
    if any(term in text for term in ["exchange", "fortinet", "pan-os", "cisco", "citrix", "ivanti", "vpn", "firewall", "router", "sd-wan", "gateway", "zimbra", "confluence", "weblogic", "wordpress", "apache"]):
        return "Internet-facing or edge technology", 18
    if any(term in text for term in ["active directory", "defender", "endpoint manager", "identity", "screenconnect", "simplehelp", "vcenter", "vmware", "security appliance"]):
        return "Identity, security, or remote management tool", 16
    if any(term in text for term in ["windows", "linux kernel", "macos", "ios", "android", "chrome", "chromium", "safari", "firefox", "office", "acrobat", "reader"]):
        return "Endpoint, operating system, or browser", 10
    if any(term in text for term in ["sql injection", "remote code execution", "command injection"]):
        return "Application exploit path", 12
    return "Requires asset validation", 5


def score_kev(row: dict[str, str], as_of: dt.date) -> str:
    date_added = parse_date(row.get("dateAdded", ""))
    due_date = parse_date(row.get("dueDate", ""))
    score = 50
    if row.get("knownRansomwareCampaignUse", "").strip().lower() == "known":
        score += 20
    if date_added:
        age_days = (as_of - date_added).days
        if age_days <= 30:
            score += 15
        elif age_days <= 90:
            score += 10
        elif age_days <= 365:
            score += 5
    if due_date:
        due_delta = (due_date - as_of).days
        if 0 <= due_delta <= 7:
            score += 15
        elif 8 <= due_delta <= 30:
            score += 10
        elif -30 <= due_delta < 0:
            score += 8
        elif -90 <= due_delta < -30:
            score += 4
    score += exposure_category(row)[1]
    if score >= 95:
        return "Critical"
    if score >= 80:
        return "High"
    if score >= 65:
        return "Medium"
    return "Watch"


def project2_dashboard(rows: list[dict[str, str]], path: Path, as_of: dt.date) -> None:
    dates = [parse_date(row.get("dateAdded", "")) for row in rows]
    dates = [value for value in dates if value]
    ransomware = Counter(row.get("knownRansomwareCampaignUse", "Unknown") for row in rows)
    vendors = Counter(row.get("vendorProject", "Unknown") for row in rows)
    priorities = Counter(score_kev(row, as_of) for row in rows)
    added_30 = sum(1 for value in dates if (as_of - value).days <= 30)
    top_vendor, top_vendor_count = vendors.most_common(1)[0]

    svg = Svg(1280, 860, "CISA KEV prioritization dashboard", "Premium visual summary of the CISA KEV snapshot.")
    svg.header("CISA KEV Prioritization Snapshot", "Confirmed exploitation translated into workflow, urgency, and ownership signals.", "Project 2")
    metrics = [
        ("KEV entries", f"{len(rows):,}", "Confirmed exploited vulnerabilities.", BLUE),
        ("Ransomware", f"{ransomware.get('Known', 0):,}", "Known campaign-use escalation group.", RED),
        ("Last 30 days", f"{added_30}", "New catalog additions requiring review.", TEAL),
        ("Top vendor", top_vendor, f"{top_vendor_count:,} entries in snapshot.", PURPLE),
    ]
    for index, metric in enumerate(metrics):
        svg.metric_card(64 + index * 294, 190, 260, 154, *metric)
    svg.bar_panel(64, 374, 552, 344, "Vendor Concentration", "Top vendors by KEV count", vendors.most_common(5), BLUE, 5)
    priority_order = [("Critical", priorities.get("Critical", 0)), ("High", priorities.get("High", 0)), ("Medium", priorities.get("Medium", 0)), ("Watch", priorities.get("Watch", 0))]
    svg.bar_panel(664, 374, 552, 344, "Portfolio Triage Output", "Priority distribution from the scoring model", priority_order, RED, 4)
    svg.narrative_card(64, 730, 356, 110, "Primary Read", ["KEV still needs sequencing, ownership, and escalation rules."], BLUE)
    svg.narrative_card(462, 730, 356, 110, "Risk Signal", ["Ransomware linkage raises urgency and leadership visibility."], RED)
    svg.narrative_card(860, 730, 356, 110, "Operating Rhythm", ["New entries make this a recurring workflow, not cleanup."], TEAL)
    svg.footer("CISA KEV snapshot, collected 2026-05-16", "QC gate enforced")
    svg.save(path)


def project2_bar(path: Path, title: str, subtitle: str, rows: list[tuple[str, int]], color: str, max_rows: int = 8) -> None:
    panel_rows = min(max_rows, len(rows))
    panel_h = 214 + panel_rows * 48
    height = 258 + panel_h + 116
    svg = Svg(1120, height, title, subtitle)
    svg.header(title, subtitle, "Project 2")
    svg.bar_panel(72, 178, 976, panel_h, "Evidence View", "Generated from the local CISA KEV snapshot.", rows, color, max_rows)
    svg.narrative_card(72, 198 + panel_h, 976, 112, "How To Read It", ["Use this as a workflow signal, then confirm local asset exposure and business ownership."], color)
    svg.footer("CISA KEV snapshot, collected 2026-05-16", "QC gate enforced")
    svg.save(path)


def generate_project2(root: Path) -> None:
    project = root / "projects" / "02-cisa-kev-vulnerability-prioritization"
    rows = read_csv(project / "data" / "known_exploited_vulnerabilities-2026-05-16.csv")
    visuals = project / "visuals"
    as_of = dt.date(2026, 5, 16)
    vendors = Counter(row.get("vendorProject", "Unknown") for row in rows)
    ransomware = Counter(row.get("knownRansomwareCampaignUse", "Unknown") for row in rows)
    priorities = Counter(score_kev(row, as_of) for row in rows)
    years = Counter(str(parse_date(row.get("dateAdded", "")).year) for row in rows if parse_date(row.get("dateAdded", "")))
    project2_dashboard(rows, visuals / "kev-dashboard.svg", as_of)
    project2_bar(visuals / "vendor-kev-counts.svg", "Top Vendors By KEV Count", "Catalog entries grouped by vendor or project.", vendors.most_common(10), BLUE, 10)
    project2_bar(visuals / "cwe-patterns.svg", "Top CWE Patterns In KEV", "Weakness categories that repeat across exploited vulnerabilities.", cwe_counter(rows).most_common(10), PURPLE, 10)
    project2_bar(visuals / "ransomware-use.svg", "Known Ransomware Campaign Use", "Ransomware-use field grouped by CISA KEV value.", ransomware.most_common(), RED, 3)
    project2_bar(visuals / "kev-additions-by-year.svg", "KEV Additions By Year", "Catalog entries grouped by dateAdded year.", sorted(years.items()), TEAL, 8)
    priority_order = [("Critical", priorities.get("Critical", 0)), ("High", priorities.get("High", 0)), ("Medium", priorities.get("Medium", 0)), ("Watch", priorities.get("Watch", 0))]
    project2_bar(visuals / "priority-distribution.svg", "Priority Distribution", "Portfolio scoring model applied to the KEV snapshot.", priority_order, RED, 4)


def generate_project3(root: Path) -> None:
    visuals = root / "projects" / "03-mitre-attack-cti-brief" / "visuals"

    svg = Svg(1280, 760, "Scattered Spider identity tradecraft flow", "Premium visual attack-flow summary for Scattered Spider CTI.")
    svg.header("Identity Tradecraft Flow", "A public-source CTI view of how trust abuse can become business impact.", "Project 3")
    cards = [
        (76, 198, 242, 126, "Identity Research", ["Names, roles, routines", "and support context"], BLUE),
        (384, 198, 242, 126, "Trust Manipulation", ["Voice phishing and", "help desk pressure"], TEAL),
        (692, 198, 242, 126, "Account Takeover", ["Reset credentials or", "reuse active sessions"], GREEN),
        (384, 414, 242, 126, "MFA Change", ["New factors, fatigue,", "or auth process abuse"], AMBER),
        (692, 414, 242, 126, "SaaS Discovery", ["Mail, files, repos,", "and response channels"], PURPLE),
        (1000, 414, 204, 126, "Data Pressure", ["Exfiltration", "and recovery impact"], RED),
    ]
    for x, y, w, h, title, lines, color in cards:
        svg.narrative_card(x, y, w, h, title, lines, color)
    svg.arrow("M318 261 H374")
    svg.arrow("M626 261 H682")
    svg.arrow("M813 324 C813 366 505 366 505 404")
    svg.arrow("M626 477 H682")
    svg.arrow("M934 477 H990")
    svg.narrative_card(76, 596, 1128, 132, "Defensive Focus", ["Harden identity proofing, govern MFA changes, watch SaaS access, control remote tools, and rehearse data-theft response."], BLUE)
    svg.footer("CISA AA23-320A and MITRE ATT&CK G1015", "QC gate enforced")
    svg.save(visuals / "scattered-spider-attack-flow.svg")

    svg = Svg(1280, 760, "Identity defense workflow", "Premium defender workflow for identity-centered Scattered Spider tradecraft.")
    svg.header("Identity Defense Workflow", "A practical control path for help desk abuse, MFA manipulation, and SaaS data theft.", "Project 3")
    cards = [
        (76, 198, 318, 126, "Proof The Request", ["Independent callback", "for high-risk resets"], BLUE),
        (482, 198, 318, 126, "Guard MFA Changes", ["Alert on new factors", "and repeated prompts"], TEAL),
        (888, 198, 318, 126, "Watch SaaS Behavior", ["Searches, exports,", "and repository access"], GREEN),
        (76, 444, 318, 126, "Control Remote Tools", ["Approved RMM inventory", "and blocked unknown tools"], AMBER),
        (482, 444, 318, 126, "Prepare Data Response", ["Legal, privacy, comms,", "and leadership paths"], RED),
        (888, 444, 318, 126, "Test Recovery", ["Backups, privileged access,", "and decision timing"], PURPLE),
    ]
    for x, y, w, h, title, lines, color in cards:
        svg.narrative_card(x, y, w, h, title, lines, color)
    svg.arrow("M394 261 H472")
    svg.arrow("M800 261 H878")
    svg.arrow("M1047 324 C1047 388 236 388 236 434")
    svg.arrow("M394 507 H472")
    svg.arrow("M800 507 H878")
    svg.narrative_card(76, 620, 1130, 132, "Program Outcome", ["Fewer risky reset paths, stronger detection coverage, clearer escalation ownership, and faster containment."], TEAL)
    svg.footer("CISA AA23-320A and MITRE ATT&CK G1015", "QC gate enforced")
    svg.save(visuals / "identity-defense-workflow.svg")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate portfolio SVG visuals.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.repo_root.resolve()
    generate_project1(root)
    generate_project2(root)
    generate_project3(root)
    print("Portfolio visuals regenerated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
