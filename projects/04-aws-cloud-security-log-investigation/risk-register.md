# Follow-up questions from the synthetic investigation

[Project overview](README.md) · [Generated report](outputs/sample-cloudtrail-investigation-report.md)

| Observation | What remains unknown | Evidence required to decide |
| --- | --- | --- |
| Root identity activity | Approval, authentication context, scope | Sign-in result, MFA evidence, authorized reason, related activity |
| Key creation and administrator policy attachment | Business need and effective access | Target identities, before/after policies, approval, key inventory and use |
| World-CIDR ingress request | Effective reachability | Exact rules, attached resources, routes, addresses, listeners |
| Public-access-block deletion | Effective bucket access | Account and bucket settings, policy, ACL, external-access analysis |
| Denied StopLogging | Intent and overall logging health | Approval, related events, trail status, delivered logs |
| Ingress removal | Whether the relevant rule is gone | Rule IDs, current configuration, asset-level verification |

These are investigation tasks for a hypothetical environment. No owner accepted a risk and no remediation was completed.
