# Scattered Spider CTI Brief Using MITRE ATT&CK

## Overview

This project builds a cyber threat intelligence brief on Scattered Spider, tracked in MITRE ATT&CK as `G1015`. The brief translates public reporting from CISA and MITRE ATT&CK into business risk, ATT&CK technique mapping, detection priorities, and incident-response improvements.

The analysis focuses on one practical question:

> How should an organization prepare for identity-focused social engineering, help desk abuse, MFA bypass, cloud/SaaS discovery, data theft, and ransomware activity associated with Scattered Spider tradecraft?

## Evidence Base

The brief uses public-source reporting collected on May 16, 2026:

- CISA Joint Cybersecurity Advisory AA23-320A, Scattered Spider
- MITRE ATT&CK Group G1015, Scattered Spider
- CISA Best Practices for MITRE ATT&CK Mapping
- MITRE ATT&CK framework references

## Key Findings

| Finding | Public-source basis | Defensive implication |
|---|---|---|
| Identity and help desk workflows are a primary attack surface | CISA reports phishing, vishing, push bombing, SIM swap, password reset, and MFA token transfer activity. | Help desk identity verification and MFA reset governance need explicit controls. |
| Valid accounts and MFA manipulation are central to persistence | MITRE maps Scattered Spider to Valid Accounts, MFA request generation, and authentication process modification. | Identity provider logs and MFA enrollment events should be high-priority detection sources. |
| Legitimate remote access tools can become persistence channels | CISA and MITRE describe use of remote monitoring and management tools. | RMM inventory, application control, and unauthorized remote tool alerts should be operationalized. |
| Cloud, SaaS, collaboration, and code repositories can become collection targets | MITRE maps the group to cloud storage, SharePoint, code repositories, messaging applications, and email collection. | Cloud/SaaS audit logs need monitoring for bulk access, unusual searches, and suspicious downloads. |
| The activity can escalate to extortion and ransomware impact | CISA describes data theft, extortion, and ransomware variants, and MITRE maps data encryption for impact. | Incident response should include data-theft containment, executive communications, legal/privacy coordination, and recovery testing. |

## Deliverables

- [`sources-and-methodology.md`](sources-and-methodology.md): sources, collection date, method, confidence, and limitations
- [`threat-profile.md`](threat-profile.md): threat actor overview, target patterns, objectives, and priority intelligence requirements
- [`attack-mapping.md`](attack-mapping.md): ATT&CK tactic/technique mapping with detection and response notes
- [`detection-and-response.md`](detection-and-response.md): detection use cases, log sources, response playbooks, and metrics
- [`response-backlog.md`](response-backlog.md): prioritized defensive improvement backlog
- [`executive-summary.md`](executive-summary.md): leadership-facing summary
- [`attack-navigator-layer.json`](attack-navigator-layer.json): ATT&CK Navigator layer for selected techniques

## Source References

- CISA AA23-320A, Scattered Spider: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- CISA alert on updated Scattered Spider advisory: https://www.cisa.gov/news-events/alerts/2025/07/29/cisa-and-partners-release-updated-advisory-scattered-spider-group
- MITRE ATT&CK Group G1015, Scattered Spider: https://attack.mitre.org/groups/G1015/
- CISA Best Practices for MITRE ATT&CK Mapping: https://www.cisa.gov/news-events/news/best-practices-mitre-attckr-mapping
- MITRE ATT&CK overview: https://attack.mitre.org/

## Boundary Statement

This report is a public-source CTI brief. It does not attribute activity against any specific organization, confirm compromise, test exploitability, or include nonpublic indicators.
