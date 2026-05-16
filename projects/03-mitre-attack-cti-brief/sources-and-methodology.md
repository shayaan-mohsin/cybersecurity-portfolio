# Sources And Methodology

## Collection Date

May 16, 2026.

## Sources Used

| Source | Why it was used |
|---|---|
| CISA AA23-320A, Scattered Spider | Primary public advisory for recent Scattered Spider tactics, techniques, procedures, mitigations, and defensive recommendations. |
| CISA alert on updated Scattered Spider advisory | Confirms the July 29, 2025 update and summarizes the advisory's emphasis on phishing, push bombing, SIM swap, remote access tools, and ransomware. |
| MITRE ATT&CK Group G1015, Scattered Spider | Primary ATT&CK reference for group aliases, associated techniques, software, and behavior mappings. |
| CISA Best Practices for MITRE ATT&CK Mapping | Method reference for mapping adversary behavior to ATT&CK consistently. |
| MITRE ATT&CK framework | Shared language for tactics, techniques, and defensive gap analysis. |

## Analytical Method

1. Identify a public-source threat focus with enough official reporting to support a useful CTI brief.
2. Extract observed behaviors from CISA AA23-320A and MITRE ATT&CK G1015.
3. Map behaviors to ATT&CK tactics and techniques only when the source reporting supports the mapping.
4. Translate mapped behaviors into defensive use cases, log sources, response actions, and backlog items.
5. Separate observed source-backed activity from analyst interpretation.

## Confidence Levels

| Assessment type | Confidence | Reason |
|---|---|---|
| Scattered Spider uses social engineering, help desk abuse, MFA bypass, and remote access tooling | High | Directly supported by CISA and MITRE ATT&CK references. |
| Identity provider, help desk, SaaS, EDR, and collaboration logs are priority detection sources | High | These sources align directly to the documented behaviors. |
| Organizations with weak MFA reset controls are at elevated risk from this tradecraft | Moderate to high | Strongly implied by CISA reporting, but local risk depends on actual process maturity. |
| Specific business impact for an individual organization | Moderate | Impact depends on sector, identity architecture, data access, and response maturity. |

## Scope

The report covers defensive CTI for identity-focused intrusion patterns associated with Scattered Spider:

- social engineering and help desk abuse
- MFA bypass and token transfer
- valid account abuse
- remote access tooling
- cloud, SaaS, collaboration, and code repository discovery
- data exfiltration and ransomware impact

## Limitations

This brief is based on public reporting. It does not include organization-specific telemetry, victim data, malware reverse engineering, live incident response evidence, or private intelligence feeds.

ATT&CK mappings are used to structure defensive analysis. A mapping does not prove that a local control detects the technique unless the detection is tested against relevant telemetry.

## Ethical Handling

The report avoids exploit instructions, credential theft details, and operational steps that would enable abuse. Recommendations are framed for prevention, detection, response, governance, and recovery.
