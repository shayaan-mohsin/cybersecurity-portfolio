# Candidate mappings outside the supported layer

[Project overview](README.md) · [Supported mappings](attack-mapping.md)

These eight IDs are valid in ATT&CK v17.0, but no direct relationship from G1015 to that exact technique was established in the pinned dataset. That does not prove the behavior never occurred. A parent technique, campaign relationship, or separate report may provide relevant evidence; each candidate needs that source-specific work before inclusion.

| Candidate | Name | Tactic in v17.0 |
| --- | --- | --- |
| T1589 | Gather Victim Identity Information | reconnaissance |
| T1566.004 | Spearphishing Voice | initial-access |
| T1078.002 | Domain Accounts | initial-access |
| T1199 | Trusted Relationship | initial-access |
| T1219.002 | Remote Desktop Software | command-and-control |
| T1087.004 | Cloud Account | discovery |
| T1213.002 | Sharepoint | collection |
| T1490 | Inhibit System Recovery | impact |

T1219.002 belongs to Command and Control and T1213.002 to Collection in this version. None of these eight candidates contributes to the supported layer count.
