# Offline CloudTrail-style investigation

Input records: 12; unique records: 12; duplicate copies excluded: 0.
Review signals: 10. Severity counts: {'High': 5, 'Medium': 3, 'Informational': 2}.

The repository sample is synthetic and composite; other inputs require their own provenance. No AWS deployment, live export, compromise, reachable exposure, or completed remediation is established. Event IDs are absent in the original fixture; the analyzer preserves that limitation. Management events do not establish object reads or data exfiltration.

| Urgency | Event / outcome | Interpretation | Follow-up |
| --- | --- | --- | --- |
| High | ConsoleLogin / API recorded without error; final state unverified | Root identity is recorded; approval/MFA/intent are unknown. | Verify sign-in result, MFA evidence, approval and scope. |
| High | CreateAccessKey / API recorded without error; final state unverified | Creation request recorded without error; ownership and need require review. | Check target identity, inventory, approval, use and rotation; never publish keys. |
| High | AttachUserPolicy / API recorded without error; final state unverified | AdministratorAccess attachment | Compare before/after policies and effective authorization with approval. |
| High | AuthorizeSecurityGroupIngress / API recorded without error; final state unverified | Administrative port/range/all protocols allowed to world CIDR. | Check rule IDs, attached resources, routes/listeners and approval. A detached group does not prove reachable exposure. |
| High | DeletePublicAccessBlock / API recorded without error; final state unverified | Bucket layer changed; account/organization controls and effective access remain unknown. | Check all BPA layers, bucket policy/ACL and intended access. |
| Medium | ConsoleLogin / Sign-in failure | A failed sign-in does not establish account compromise. | Correlate attempts, successes and identity context. |
| Medium | StopLogging / Denied/error | No successful change is established by this record. Error: AccessDenied | Review authorization, intent and related successful events; do not claim exposure or remediation. |
| Medium | PutBucketPolicy / Denied/error | No successful change is established by this record. Error: AccessDenied | Review authorization, intent and related successful events; do not claim exposure or remediation. |
| Informational | RevokeSecurityGroupIngress / API recorded without error; final state unverified | Recorded removal is follow-up evidence, not proof that every risky rule is gone. | Compare exact rules and verify final group/asset state. |
| Informational | CreateDetector / API recorded without error; final state unverified | Enable/setup or unclassified update; no reduction is established. | Verify detector status, enabled data sources, approval and finding delivery. |
