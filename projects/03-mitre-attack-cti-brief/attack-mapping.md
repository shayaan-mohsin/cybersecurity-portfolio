# Selected source-supported ATT&CK mappings

[Project overview](README.md) · [Method](sources-and-methodology.md) · [Candidate mappings](proposed-mappings.md)

These 11 selected techniques have direct G1015 uses relationships in Enterprise ATT&CK v17.0. This is a research selection, not an exhaustive profile or detection-coverage measurement. Technique names and tactics below use that pinned version.

| Technique | Name in v17.0 | Selected tactic |
| --- | --- | --- |
| T1598.004 | Spearphishing Voice | reconnaissance |
| T1556.006 | Multi-Factor Authentication | persistence |
| T1136 | Create Account | persistence |
| T1656 | Impersonation | defense-evasion |
| T1621 | Multi-Factor Authentication Request Generation | credential-access |
| T1552.001 | Credentials In Files | credential-access |
| T1213.003 | Code Repositories | collection |
| T1114 | Email Collection | collection |
| T1213.005 | Messaging Applications | collection |
| T1567.002 | Exfiltration to Cloud Storage | exfiltration |
| T1486 | Data Encrypted for Impact | impact |

The [evidence index](evidence/selected-relationships.json) retains STIX identifiers and underlying source references. The [Navigator layer](attack-navigator-layer.json) contains the same 11 entries. T1213.003 is Collection, not Discovery.
