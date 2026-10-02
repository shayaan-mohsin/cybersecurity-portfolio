# Findings narrative

[Project overview](README.md) · [Worked examples](walkthrough.md) · [Generated details](outputs/sample-cloudtrail-investigation-report.md)

The fixture produces five High signals: root identity activity, access-key creation, AdministratorAccess attachment, world-CIDR administrative ingress, and deletion of a bucket public-access block.

Three Medium signals cover a failed console sign-in and two denied actions: stopping a trail and setting a bucket policy. Those denied records do not demonstrate successful configuration changes.

The two Informational signals record an ingress-removal request and GuardDuty creation with enable set to true. They are follow-up or configuration context, not verified remediation.

No signal establishes malicious intent. Approval, effective permissions, asset state, and final service health would require additional evidence. The [risk register](risk-register.md) describes those follow-up questions.
