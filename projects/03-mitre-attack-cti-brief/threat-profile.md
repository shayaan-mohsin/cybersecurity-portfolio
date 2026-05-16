# Threat Profile

## Threat Actor

Scattered Spider is a cybercriminal group tracked by MITRE ATT&CK as `G1015`. CISA and partner agencies describe the group as targeting large companies and contracted IT help desks, using social engineering to obtain access, bypass MFA, deploy remote access tools, exfiltrate data, and support extortion or ransomware activity.

Associated names include UNC3944, Scatter Swine, Oktapus, Octo Tempest, Storm-0875, and Muddled Libra.

## Why This Threat Matters

Scattered Spider tradecraft is important because it targets the human and process layer around identity systems. The group does not rely only on malware or technical exploitation. It uses believable impersonation, help desk workflows, MFA enrollment gaps, remote access tooling, and cloud/SaaS access to turn legitimate business processes into intrusion paths.

For defenders, the key lesson is that identity governance and help desk procedure are security controls. Weak password reset, MFA reset, device enrollment, vendor access, and remote access approval processes can become high-impact exposure points.

## Reported Objectives

| Objective | Defensive relevance |
|---|---|
| Obtain credentials and MFA access | Prioritize phishing-resistant MFA, help desk verification, and identity provider monitoring. |
| Establish persistent access | Monitor account changes, MFA method registration, remote access tools, and new identities. |
| Discover sensitive systems and data | Watch for unusual access to SharePoint, cloud storage, code repositories, messaging tools, and email. |
| Exfiltrate data for extortion | Detect bulk downloads, unusual file-sharing destinations, and abnormal cloud queries. |
| Deploy ransomware or create impact | Prepare containment, recovery, legal/privacy coordination, and executive communications. |

## Targeted Environments And Workflows

| Target area | Why it matters |
|---|---|
| IT help desks and contracted support providers | Password resets and MFA changes can grant the attacker legitimate access. |
| Identity providers and SSO tenants | Compromise can enable broad access across SaaS and cloud services. |
| Remote access and RMM tools | Legitimate tools can blend into normal administration activity. |
| Cloud storage and SaaS platforms | Sensitive data may be collected without touching traditional endpoints. |
| Collaboration tools | Incident response discussions may reveal defender plans. |
| Code repositories and credential documentation | Source code, keys, setup guides, and infrastructure notes can support follow-on access. |
| Backups and virtual infrastructure | Ransomware impact can expand if recovery systems are reachable or poorly segmented. |

## Priority Intelligence Requirements

1. Which help desk workflows can reset passwords, transfer MFA tokens, or enroll new MFA devices?
2. Which accounts can administer identity provider, SSO, remote access, cloud, and collaboration platforms?
3. Which SaaS platforms contain sensitive files, source code, credentials, incident-response notes, or executive communications?
4. Which remote access tools are approved, and how is unauthorized use detected?
5. Which alerts would identify MFA fatigue, new MFA registration, impossible travel, suspicious OAuth consent, or abnormal cloud downloads?
6. Which recovery systems are isolated from domain, SSO, and remote access compromise?

## Business Impact

Potential business impact includes account takeover, sensitive data exposure, operational disruption, extortion, ransomware encryption, legal/privacy notification pressure, reputational harm, and loss of confidence in internal support processes.
