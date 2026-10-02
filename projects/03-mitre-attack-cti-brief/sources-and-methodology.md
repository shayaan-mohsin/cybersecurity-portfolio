# Sources and mapping method

[Project overview](README.md) · [Supported table](attack-mapping.md) · [Candidates](proposed-mappings.md)

The analysis is pinned to **Enterprise ATT&CK v17.0**, rather than silently mixing a historical layer with today’s live pages. Later releases may rename, move, revoke, or replace techniques.

## Evidence chain

1. Use the official [v17.0 STIX dataset](https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-17.0.json). STIX is a structured format for threat information.
2. Resolve group G1015 and each selected technique ID.
3. Require a non-revoked, non-deprecated direct group-to-technique “uses” relationship for inclusion in the supported layer.
4. Preserve the selected tactic from that version and the relationship identifiers and source references in [the evidence file](evidence/selected-relationships.json).
5. Keep candidates without that exact relationship outside the supported layer.

The evidence file is a small derived index, not the complete MITRE dataset. Its recorded SHA-256 identifies the full dataset used. It allows source tracing; it is not independent corroboration of MITRE’s underlying reporting.

## Primary references

- [CISA advisory AA23-320A: Scattered Spider](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a), for reported identity and support-process abuse.
- [MITRE ATT&CK group G1015](https://attack.mitre.org/groups/G1015/), for current navigation; use the pinned dataset for this layer’s historical meaning.
- [Microsoft: Octo Tempest operations](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/), for additional reporting. Overlapping names in industry reporting should not be treated as perfectly interchangeable groups or campaigns.

The 11 selected techniques are not an exhaustive actor profile and do not represent detection coverage. A direct MITRE relationship is a source-based attribution, not an observation from an environment I investigated.
