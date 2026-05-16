# Detection And Response Plan

## Priority Log Sources

| Source | Why it matters |
|---|---|
| Identity provider logs | Detect unusual sign-ins, MFA changes, new devices, risky sessions, privilege changes, and conditional access changes. |
| Help desk ticketing and call records | Detect suspicious password reset, MFA transfer, device enrollment, and identity verification failures. |
| Endpoint detection and response | Detect remote access tools, script execution, credential dumping, and ransomware precursors. |
| SaaS audit logs | Detect abnormal SharePoint, OneDrive, Teams, Slack, GitHub, email, and cloud storage access. |
| Email and collaboration logs | Detect mailbox search, forwarding rules, incident thread access, and suspicious account activity notifications. |
| Cloud control plane logs | Detect IAM changes, new instances, access key use, storage access, and large exports. |
| Network, proxy, and DNS logs | Detect unauthorized remote access tooling, tunneling, and file-sharing destinations. |
| Backup and recovery logs | Detect deletion attempts, failed backups, unusual admin access, and restore readiness gaps. |

## Detection Use Cases

| Use case | ATT&CK mapping | Detection idea | Response action |
|---|---|---|---|
| MFA fatigue followed by successful login | T1621, T1078 | Multiple MFA denials or prompts followed by approval from a new location/device. | Disable sessions, reset credentials, revoke MFA methods, contact user through verified channel. |
| New MFA device after help desk interaction | T1556.006, T1566.004 | MFA method added shortly after password reset or support ticket. | Validate support request, review ticket evidence, revoke unauthorized method. |
| High-risk help desk reset | T1598.004, T1656 | Password reset for privileged user, executive, remote worker, or vendor account without strong verification. | Require supervisor approval and independent callback before completion. |
| Unauthorized remote access tool | T1219.002 | New AnyDesk, TeamViewer, ConnectWise, LogMeIn, ngrok, or similar execution outside approved inventory. | Isolate endpoint, collect process/network evidence, block hash/domain where appropriate. |
| Abnormal SaaS repository access | T1213.002, T1213.003, T1213.005 | Bulk access to SharePoint, code repositories, or messaging spaces after new login. | Suspend account, revoke sessions, review accessed files, identify data exposure. |
| Mailbox rule manipulation | T1114, T1114.003 | New inbox forwarding, deletion, or hiding rules, especially for security alerts. | Remove rules, preserve mailbox evidence, reset account and OAuth grants. |
| Cloud storage exfiltration pattern | T1567.002 | Large upload/download volume to unusual cloud storage or file-sharing service. | Block destination, suspend token, preserve logs, initiate data exposure review. |
| Ransomware recovery interference | T1486, T1490 | Backup deletion, shadow copy modification, mass file rename/encryption, or admin access to recovery systems. | Isolate impacted hosts, protect backups, activate ransomware playbook. |

## Response Playbooks

### 1. Suspected Help Desk Social Engineering

1. Pause requested reset, MFA transfer, or device enrollment.
2. Verify requester identity through an independent channel.
3. Review recent account risk events, failed MFA prompts, and previous tickets.
4. Escalate privileged, executive, vendor, or security-team account requests.
5. Preserve ticket notes and call metadata.
6. Notify security operations if social engineering is suspected.

### 2. Suspected Account Takeover

1. Disable account or revoke active sessions.
2. Reset password and remove unauthorized MFA methods.
3. Review sign-in logs, token use, mailbox rules, OAuth consent, and privilege changes.
4. Identify accessed files, SaaS applications, cloud resources, and repositories.
5. Check for lateral movement through remote access tools or cloud services.
6. Document scope and communicate with privacy/legal teams if sensitive data may be involved.

### 3. Unauthorized Remote Access Tool

1. Isolate the endpoint or server if active compromise is suspected.
2. Collect process, command line, network, installer, and user context.
3. Compare against approved remote access inventory.
4. Remove tool if unauthorized and block known infrastructure.
5. Review related account activity and remote sessions.
6. Hunt for the same tool across endpoints and servers.

### 4. Cloud/SaaS Data Theft Concern

1. Revoke suspicious sessions and access tokens.
2. Preserve SaaS audit logs and cloud storage access logs.
3. Identify files, repositories, messages, mailboxes, or buckets accessed.
4. Review bulk exports, unusual queries, and file-sharing destinations.
5. Determine whether legal, privacy, or customer notification review is required.
6. Increase monitoring for follow-on extortion or account reuse.

### 5. Ransomware Or Extortion Event

1. Activate incident command and preserve communications out of compromised channels.
2. Isolate impacted systems and protect backup infrastructure.
3. Identify data theft indicators before focusing only on encryption.
4. Prioritize recovery of critical services.
5. Coordinate legal, privacy, executive, communications, and insurance stakeholders.
6. Conduct after-action review and update controls.

## Metrics

| Metric | Why it matters |
|---|---|
| Percent of privileged accounts protected by phishing-resistant MFA | Measures resistance to MFA abuse. |
| Number of high-risk help desk resets per month | Shows exposure through support workflows. |
| Percent of MFA resets with independent verification evidence | Measures help desk control quality. |
| Mean time to revoke sessions after suspected account takeover | Measures containment speed. |
| Unauthorized remote access tool detections | Measures visibility into legitimate tool abuse. |
| SaaS bulk-download alert volume and closure rate | Measures cloud/SaaS monitoring maturity. |
| Backup restore success rate | Measures recovery readiness if ransomware occurs. |
