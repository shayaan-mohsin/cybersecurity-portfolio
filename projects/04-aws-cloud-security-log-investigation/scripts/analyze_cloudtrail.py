"""Offline CloudTrail-style JSON review. No AWS SDK, deployment, or automatic response.
Supported formats: Records, Events/CloudTrailEvent, list, or one event. CSV is deliberately unsupported.
Severity means review urgency, not confirmed compromise.
"""
from __future__ import annotations
import argparse, csv, hashlib, ipaddress, json
from collections import Counter
from pathlib import Path
EXPECTED = {'ConsoleLogin': 'signin.amazonaws.com', 'CreateAccessKey': 'iam.amazonaws.com', 'AttachUserPolicy': 'iam.amazonaws.com', 'AttachRolePolicy': 'iam.amazonaws.com', 'PutUserPolicy': 'iam.amazonaws.com', 'PutRolePolicy': 'iam.amazonaws.com', 'AuthorizeSecurityGroupIngress': 'ec2.amazonaws.com', 'RevokeSecurityGroupIngress': 'ec2.amazonaws.com', 'DeletePublicAccessBlock': 's3.amazonaws.com', 'PutPublicAccessBlock': 's3.amazonaws.com', 'PutBucketPolicy': 's3.amazonaws.com', 'StopLogging': 'cloudtrail.amazonaws.com', 'DeleteTrail': 'cloudtrail.amazonaws.com', 'UpdateTrail': 'cloudtrail.amazonaws.com', 'PutEventSelectors': 'cloudtrail.amazonaws.com', 'StartLogging': 'cloudtrail.amazonaws.com', 'CreateDetector': 'guardduty.amazonaws.com', 'UpdateDetector': 'guardduty.amazonaws.com', 'DeleteDetector': 'guardduty.amazonaws.com'}
ORDER = {'High': 0, 'Medium': 1, 'Informational': 2}

def load_events(path):
    """Normalize supported JSON containers and reject structurally unusable records."""
    if Path(path).suffix.lower() != '.json':
        raise ValueError('Only JSON exports are supported; CSV lacks necessary nested evidence')
    data = json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if isinstance(data, dict) and 'Records' in data:
        data = data['Records']
    elif isinstance(data, dict) and 'Events' in data:
        data = data['Events']
    elif isinstance(data, dict):
        data = [data]
    if not isinstance(data, list) or not data:
        raise ValueError('Expected a nonempty event list')
    out = []
    for event in data:
        if not isinstance(event, dict):
            raise ValueError('Event must be an object')
        if 'CloudTrailEvent' in event:
            event = json.loads(event['CloudTrailEvent'])
        if not isinstance(event, dict) or not all((isinstance(event.get(k), str) and event[k] for k in ['eventTime', 'eventName', 'eventSource'])):
            raise ValueError('Missing eventTime/eventName/eventSource')
        for k in ['userIdentity', 'requestParameters', 'responseElements']:
            if event.get(k) is not None and (not isinstance(event[k], dict)):
                raise ValueError('Expected nested object: ' + k)
        out.append(event)
    return out

def deduplicate(events):
    """Use provider ID with account/Region, or exact-payload hashing if no ID exists."""
    seen = set()
    out = []
    for e in events:
        key = (e.get('recipientAccountId'), e.get('awsRegion'), e['eventID']) if e.get('eventID') else hashlib.sha256(json.dumps(e, sort_keys=True).encode()).hexdigest()
        if key not in seen:
            seen.add(key)
            out.append(e)
    return (out, len(events) - len(out))

def actor(e):
    """Preserve the full assumed-role session identifier when available."""
    u = e.get('userIdentity') or {}
    return u.get('arn') or u.get('principalId') or u.get('userName') or u.get('type', 'Unknown')

def public_permissions(e):
    """Match the CIDR and port within each permission, never across rules."""
    p = e.get('requestParameters') or {}
    perms = p.get('ipPermissions', {})
    perms = perms.get('items', []) if isinstance(perms, dict) else perms
    if not isinstance(perms, list):
        raise ValueError('ipPermissions must contain items/list')
    found = []
    for rule in perms:
        if not isinstance(rule, dict):
            raise ValueError('Invalid ingress rule')
        public = False
        for key, cidrkey in [('ipRanges', 'cidrIp'), ('ipv6Ranges', 'cidrIpv6')]:
            ranges = rule.get(key, {})
            ranges = ranges.get('items', []) if isinstance(ranges, dict) else ranges
            for item in ranges or []:
                try:
                    net = ipaddress.ip_network(item.get(cidrkey, ''), strict=False)
                    public = public or net.prefixlen == 0
                except ValueError:
                    raise ValueError('Invalid ingress CIDR')
        if public:
            proto = str(rule.get('ipProtocol', ''))
            lo, hi = (rule.get('fromPort'), rule.get('toPort'))
            admin = proto == '-1' or (proto in {'tcp', '6'} and isinstance(lo, int) and isinstance(hi, int) and any((lo <= port <= hi for port in [22, 3389])))
            found.append(admin)
    return found

def public_allow_policy(p):
    """Flag wildcard Allow for review without claiming effective public access."""
    policy = p.get('policy', p.get('bucketPolicy'))
    if policy is None:
        return False
    if isinstance(policy, str):
        policy = json.loads(policy)
    if not isinstance(policy, dict):
        raise ValueError('Policy must be a JSON object')
    statements = policy.get('Statement', [])
    if isinstance(statements, dict):
        statements = [statements]
    for s in statements:
        principal = s.get('Principal')
        wild = principal == '*' or (isinstance(principal, dict) and (principal.get('AWS') == '*' or (isinstance(principal.get('AWS'), list) and '*' in principal['AWS'])))
        if s.get('Effect') == 'Allow' and wild:
            return True
    return False

def analyze_event(e):
    """Interpret error outcome first; emit review signals, not incident verdicts."""
    n = e.get('eventName')
    service = e.get('eventSource')
    p = e.get('requestParameters') or {}
    out = []

    def add(severity, signal, why, next_step):
        out.append(dict(severity=severity, signal=signal, event_id=e.get('eventID', 'not supplied'), event_time=e.get('eventTime', ''), event_name=n, event_source=service, region=e.get('awsRegion', 'not supplied'), actor=actor(e), source_ip=e.get('sourceIPAddress', 'not supplied'), outcome='Denied/error' if e.get('errorCode') else 'Sign-in failure' if (e.get('responseElements') or {}).get('ConsoleLogin') == 'Failure' else 'API recorded without error; final state unverified', why_it_matters=why, recommendation=next_step))
    if e.get('errorCode'):
        if n in EXPECTED and service == EXPECTED[n]:
            add('Medium', 'Action denied or failed', 'No successful change is established by this record. Error: ' + str(e['errorCode']), 'Review authorization, intent and related successful events; do not claim exposure or remediation.')
        return out
    if n in EXPECTED and service != EXPECTED[n]:
        return out
    if (e.get('userIdentity') or {}).get('type') == 'Root':
        add('High', 'Root identity activity', 'Root identity is recorded; approval/MFA/intent are unknown.', 'Verify sign-in result, MFA evidence, approval and scope.')
    if n == 'ConsoleLogin' and (e.get('responseElements') or {}).get('ConsoleLogin') == 'Failure':
        add('Medium', 'Failed console sign-in', 'A failed sign-in does not establish account compromise.', 'Correlate attempts, successes and identity context.')
    elif n == 'CreateAccessKey':
        add('High', 'Access key creation', 'Creation request recorded without error; ownership and need require review.', 'Check target identity, inventory, approval, use and rotation; never publish keys.')
    elif n in {'AttachUserPolicy', 'AttachRolePolicy', 'PutUserPolicy', 'PutRolePolicy'}:
        admin = str(p.get('policyArn', '')).endswith(':policy/AdministratorAccess')
        add('High' if admin else 'Medium', 'IAM policy change', 'AdministratorAccess attachment' if admin else 'Policy semantics and effective permission change are not determined.', 'Compare before/after policies and effective authorization with approval.')
    elif n == 'AuthorizeSecurityGroupIngress':
        perms = public_permissions(e)
        if perms:
            add('High' if any(perms) else 'Medium', 'World-CIDR ingress rule', 'Administrative port/range/all protocols allowed to world CIDR.' if any(perms) else 'Public ingress rule recorded.', 'Check rule IDs, attached resources, routes/listeners and approval. A detached group does not prove reachable exposure.')
    elif n == 'RevokeSecurityGroupIngress':
        add('Informational', 'Ingress removal request', 'Recorded removal is follow-up evidence, not proof that every risky rule is gone.', 'Compare exact rules and verify final group/asset state.')
    elif n == 'DeletePublicAccessBlock':
        add('High', 'Bucket public-access-block deletion', 'Bucket layer changed; account/organization controls and effective access remain unknown.', 'Check all BPA layers, bucket policy/ACL and intended access.')
    elif n == 'PutPublicAccessBlock':
        cfg = p.get('PublicAccessBlockConfiguration') or p.get('publicAccessBlockConfiguration') or {}
        vals = [cfg.get(k) for k in ['BlockPublicAcls', 'IgnorePublicAcls', 'BlockPublicPolicy', 'RestrictPublicBuckets']]
        if all((v is True for v in vals)):
            add('Informational', 'Bucket public-access-block protections requested', 'All four bucket settings are true in the request.', 'Verify effective settings and intended authorized access.')
        else:
            add('Medium', 'Public-access-block configuration review', 'False or missing settings prevent a claim of complete protection.', 'Inspect actual bucket/account/organization settings.')
    elif n == 'PutBucketPolicy' and public_allow_policy(p):
        add('Medium', 'Wildcard Allow policy needs review', 'Wildcard Allow found; conditions, resource/action and BPA determine effective public access.', 'Review exact policy and external-access findings; do not infer public access from wildcard alone.')
    elif n in {'StopLogging', 'DeleteTrail'}:
        add('High', 'Trail disruption request', 'Trail stop/delete recorded without API error; other trails and event history may still exist.', 'Verify trail status/delivery/selectors/regions and approved changes.')
    elif n in {'UpdateTrail', 'PutEventSelectors'}:
        add('Medium', 'Logging configuration review', 'A configuration change can strengthen or reduce visibility.', 'Compare prior settings, required coverage and observed delivery.')
    elif n == 'StartLogging':
        add('Informational', 'Logging start request', 'A start request is not proof of delivery.', 'Verify trail status and new delivered log files.')
    elif n in {'CreateDetector', 'UpdateDetector', 'DeleteDetector'}:
        disabled = n == 'DeleteDetector' or p.get('enable') is False
        add('High' if disabled else 'Informational', 'GuardDuty disable/delete request' if disabled else 'GuardDuty configuration review', 'Explicit disable/delete requested.' if disabled else 'Enable/setup or unclassified update; no reduction is established.', 'Verify detector status, enabled data sources, approval and finding delivery.')
    return out

def write_csv(path, rows, fields):
    with path.open('w', newline='', encoding='utf-8') as h:
        w = csv.DictWriter(h, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('inputs', nargs='+', type=Path)
    ap.add_argument('--output-dir', type=Path, default=Path('outputs'))
    a = ap.parse_args()
    raw = [e for p in a.inputs for e in load_events(p)]
    events, dupes = deduplicate(raw)
    findings = sorted([f for e in events for f in analyze_event(e)], key=lambda f: (ORDER[f['severity']], f['event_time'], f['event_id'], f['signal']))
    a.output_dir.mkdir(parents=True, exist_ok=True)
    fields = ['severity', 'signal', 'event_id', 'event_time', 'event_name', 'event_source', 'region', 'actor', 'source_ip', 'outcome', 'why_it_matters', 'recommendation']
    write_csv(a.output_dir / 'cloudtrail-findings.csv', findings, fields)
    for filename, key, label in [('event-name-frequency.csv', 'eventName', 'event_name'), ('event-source-frequency.csv', 'eventSource', 'event_source')]:
        write_csv(a.output_dir / filename, [{label: k, 'count': v} for k, v in Counter((e[key] for e in events)).most_common()], [label, 'count'])
    write_csv(a.output_dir / 'actor-frequency.csv', [{'actor': k, 'count': v} for k, v in Counter((actor(e) for e in events)).most_common()], ['actor', 'count'])
    lines = ['# Offline CloudTrail-style investigation', '', f'Input records: {len(raw)}; unique records: {len(events)}; duplicate copies excluded: {dupes}.', f"Review signals: {len(findings)}. Severity counts: {dict(Counter((f['severity'] for f in findings)))}.", '', 'The repository sample is synthetic and composite; other inputs require their own provenance. No AWS deployment, live export, compromise, reachable exposure, or completed remediation is established. Event IDs are absent in the original fixture; the analyzer preserves that limitation. Management events do not establish object reads or data exfiltration.', '', '| Urgency | Event / outcome | Interpretation | Follow-up |', '| --- | --- | --- | --- |']
    for f in findings:
        lines.append('| ' + ' | '.join((str(x).replace('|', '\\|').replace('\n', ' ') for x in [f['severity'], f['event_name'] + ' / ' + f['outcome'], f['why_it_matters'], f['recommendation']])) + ' |')
    (a.output_dir / 'sample-cloudtrail-investigation-report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'events': len(events), 'duplicates': dupes, 'signals': len(findings), 'severity': dict(Counter((f['severity'] for f in findings)))}))
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
