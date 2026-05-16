# MITRE ATT&CK Mapping

This mapping translates public Scattered Spider reporting into defensive analysis. The selected techniques are not a complete list of every technique associated with the group; they are the techniques most relevant to an identity, help desk, SaaS, and incident-response readiness brief.

| Tactic | ATT&CK ID | Technique | Source-backed behavior | Detection and response focus |
|---|---|---|---|---|
| Reconnaissance | T1589 | Gather Victim Identity Information | Public reporting describes gathering usernames, passwords, PII, and employee role information to support social engineering. | Monitor exposed executive/help desk identity data; limit public process details; train support teams on identity-proofing abuse. |
| Reconnaissance | T1598.004 | Phishing for Information: Spearphishing Voice | CISA describes layered phone-based social engineering against employees and help desks. | Track suspicious help desk calls, reset requests, and repeated identity verification failures. |
| Initial Access | T1566.004 | Phishing: Spearphishing Voice | CISA reports calls to convince help desks to reset passwords or transfer MFA tokens. | Require strong caller verification, callback controls, and supervisor approval for high-risk resets. |
| Initial Access | T1078.002 | Valid Accounts: Domain Accounts | CISA reports account takeover after password/MFA reset abuse; MITRE maps the group to valid accounts. | Alert on unusual login source, device, user agent, impossible travel, and post-reset login anomalies. |
| Initial Access | T1199 | Trusted Relationship | CISA reports targeting contracted IT help desks and third-party services. | Review vendor support access, reset authority, and incident notification requirements. |
| Persistence | T1556.006 | Modify Authentication Process: Multi-Factor Authentication | CISA and MITRE describe registering attacker-controlled MFA tokens. | Alert on new MFA method registration, MFA device changes, and high-risk user enrollment changes. |
| Persistence | T1219.002 | Remote Access Tools: Remote Desktop Software | CISA and MITRE describe deployment or abuse of RMM tools. | Maintain approved RMM inventory; block unauthorized tools; alert on new remote-control software execution. |
| Persistence | T1136 | Create Account | MITRE reports creation of new identities in compromised environments. | Alert on new privileged users, new external users, and unusual account creation patterns. |
| Defense Evasion | T1656 | Impersonation | CISA maps layered social engineering to impersonation; MITRE documents impersonation of IT and help desk personnel. | Treat support workflow abuse as a detection surface, not only a training issue. |
| Credential Access | T1621 | Multi-Factor Authentication Request Generation | CISA reports MFA fatigue through repeated prompts. | Alert on repeated MFA push denials, high-frequency prompts, and eventual approval after repeated denials. |
| Credential Access | T1552.001 | Unsecured Credentials: Credentials In Files | CISA and MITRE report searches for credential documentation and private information. | Scan repositories and shared drives for secrets; monitor access to password documents and onboarding guides. |
| Discovery | T1087.004 | Account Discovery: Cloud Account | MITRE reports cloud account and privileged user discovery. | Monitor bulk directory exports, privileged group enumeration, and unusual Entra ID or cloud IAM queries. |
| Discovery | T1213.002 | Data from Information Repositories: SharePoint | CISA and MITRE report SharePoint searches for VPN, MFA, and help desk information. | Alert on unusual SharePoint search volume, access to IT procedure libraries, and bulk download behavior. |
| Discovery | T1213.003 | Data from Information Repositories: Code Repositories | CISA and MITRE describe discovery and exfiltration of code repositories. | Monitor repository cloning, unusual token use, and access to secrets or deployment documentation. |
| Collection | T1114 | Email Collection | CISA and MITRE report searching Exchange Online and email for security-response information. | Alert on unusual mailbox search, eDiscovery export, mailbox delegation, and access to security incident threads. |
| Collection | T1213.005 | Data from Information Repositories: Messaging Applications | MITRE reports searches of Slack and Microsoft Teams for intrusion and response conversations. | Monitor access to incident channels, bulk export, and suspicious joins to response spaces. |
| Exfiltration | T1567.002 | Exfiltration Over Web Service: Exfiltration to Cloud Storage | MITRE reports exfiltration to file sharing and cloud storage services. | Alert on large uploads, unusual cloud storage destinations, and anomalous SaaS export activity. |
| Impact | T1486 | Data Encrypted for Impact | CISA reports ransomware deployment and encryption of systems, including virtual infrastructure. | Maintain tested offline backups, EDR coverage, segmentation, and ransomware tabletop procedures. |
| Impact | T1490 | Inhibit System Recovery | MITRE associates related ransomware tooling with recovery inhibition. | Monitor backup deletion, shadow copy changes, and administrative access to recovery systems. |

## Technique Themes

| Theme | Techniques | Defensive takeaway |
|---|---|---|
| Identity trust abuse | T1078.002, T1556.006, T1621, T1656 | Identity-provider and help desk telemetry are first-class security data sources. |
| Support process compromise | T1566.004, T1598.004, T1199 | Help desk procedures should require evidence, callback controls, and high-risk workflow approval. |
| Legitimate tool abuse | T1219.002 | Application control and approved-tool inventory reduce attacker ability to blend in. |
| SaaS and cloud discovery | T1087.004, T1213.002, T1213.003, T1114, T1213.005 | SaaS audit logs should be reviewed for abnormal searches, downloads, and incident-response snooping. |
| Extortion and impact | T1567.002, T1486, T1490 | Data-theft response and recovery testing must be part of the same incident plan. |

## Navigator Artifact

The selected techniques are also represented in [`attack-navigator-layer.json`](attack-navigator-layer.json) for use with MITRE ATT&CK Navigator.
