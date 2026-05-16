# Response Improvement Backlog

## Priority Backlog

| ID | Item | Priority | ATT&CK focus | Owner | Expected outcome |
|---|---|---|---|---|---|
| CTI-001 | Require independent verification for password resets, MFA transfers, and MFA device enrollment. | Critical | T1566.004, T1598.004, T1556.006 | IT Help Desk / Identity Owner | Reduces risk of help desk social engineering and unauthorized MFA takeover. |
| CTI-002 | Enforce phishing-resistant MFA for privileged, help desk, remote access, and executive accounts. | Critical | T1621, T1078 | Identity Owner / Security | Reduces effectiveness of MFA fatigue and credential phishing. |
| CTI-003 | Alert on new MFA methods, new devices, and MFA changes for privileged or high-risk users. | Critical | T1556.006, T1098 | Security Operations | Improves detection of identity persistence. |
| CTI-004 | Build an approved remote access and RMM tool inventory. | High | T1219.002 | IT Operations / Security | Enables detection of unauthorized remote control tooling. |
| CTI-005 | Block or alert on unauthorized remote access tools and tunneling utilities. | High | T1219.002, T1572, T1090 | Security Operations | Reduces attacker persistence and command-and-control options. |
| CTI-006 | Monitor SharePoint, OneDrive, Teams, Slack, GitHub, and email for abnormal access after risky sign-ins. | High | T1213.002, T1213.003, T1213.005, T1114 | Security Operations / SaaS Owners | Detects collection of sensitive files and incident-response discussions. |
| CTI-007 | Create account takeover playbook covering session revocation, MFA removal, mailbox rule review, and OAuth review. | High | T1078, T1114.003 | Security Operations | Standardizes response to identity compromise. |
| CTI-008 | Add help desk social engineering scenarios to tabletop exercises. | Medium | T1656 | Security / IT Leadership | Tests decision-making and escalation under pressure. |
| CTI-009 | Review vendor and contracted support reset authority. | Medium | T1199 | Vendor Owner / IT Leadership | Reduces third-party support pathway risk. |
| CTI-010 | Separate incident-response communications from potentially compromised email and chat channels. | Medium | T1114, T1213.005 | Incident Commander | Reduces attacker visibility into defender actions. |
| CTI-011 | Test recovery from ransomware affecting identity, SaaS, and virtual infrastructure dependencies. | Medium | T1486, T1490 | IT Operations / Security | Improves recovery confidence for extortion or encryption scenarios. |
| CTI-012 | Scan shared drives, repositories, and wikis for credentials and sensitive setup procedures. | Medium | T1552.001, T1213.003 | Security / Platform Owners | Reduces discovery value if an account is compromised. |

## 30 / 60 / 90-Day Sequencing

| Timeframe | Focus | Deliverables |
|---|---|---|
| 0-30 days | Close the highest-risk identity and help desk gaps. | Reset verification procedure, MFA enrollment alerts, privileged phishing-resistant MFA plan, account takeover playbook draft. |
| 31-60 days | Improve monitoring across SaaS, remote access, and collaboration tools. | RMM inventory, unauthorized tool alerts, SaaS audit log use cases, incident communications procedure. |
| 61-90 days | Test response and recovery. | Tabletop exercise, ransomware recovery test, vendor reset authority review, metrics dashboard. |

## Definition Of Done

Each backlog item should have:

- named owner
- implementation date
- evidence source
- detection or control validation step
- exception process if the control cannot be fully implemented
