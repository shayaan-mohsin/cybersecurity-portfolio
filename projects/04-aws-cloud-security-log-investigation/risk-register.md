# Cloud Security Lab Risk Register

## Purpose

This risk register translates CloudTrail investigation signals into practical cloud security priorities. It is written for a small AWS environment where the analyst needs to understand identity, logging, public exposure, and evidence handling.

## Risk Register

| ID | Risk | Evidence signal | Likelihood | Impact | Priority | Owner | Recommended response |
|---|---|---|---|---|---|---|---|
| AWS-RISK-01 | Root account used for routine administration | `ConsoleLogin` by `Root` | Medium | High | High | Account owner | Enforce MFA, avoid root use, document break-glass use cases, and review follow-on events. |
| AWS-RISK-02 | Long-lived credentials created without lifecycle control | `CreateAccessKey` | Medium | High | High | IAM owner | Validate need, delete unused keys, rotate keys, and prefer temporary credentials. |
| AWS-RISK-03 | Broad IAM permissions granted without least-privilege review | `AttachUserPolicy` or inline policy changes | Medium | High | High | IAM owner | Review approvals, remove unnecessary administrator access, and scope permissions to job function. |
| AWS-RISK-04 | Public administrative network exposure | `AuthorizeSecurityGroupIngress` to `0.0.0.0/0` on port `22` or `3389` | Medium | Critical | Critical | Cloud/network owner | Revoke public admin ingress, restrict source ranges, and monitor high-risk ports. |
| AWS-RISK-05 | S3 public access controls weakened | `DeletePublicAccessBlock`, public policy, or ACL changes | Medium | High | High | Storage owner | Keep Block Public Access enabled and review bucket policies with Access Analyzer. |
| AWS-RISK-06 | Logging visibility reduced | `StopLogging`, `DeleteTrail`, or event selector changes | Low | Critical | Critical | Security owner | Alert on CloudTrail changes, restrict permissions, and validate logging status. |
| AWS-RISK-07 | Detection coverage changed without review | GuardDuty detector creation, update, or deletion | Low | High | Medium | Security owner | Document detector state, monitor findings, and validate billing impact. |
| AWS-RISK-08 | Repeated denied activity ignored | `AccessDenied` or `UnauthorizedOperation` | Medium | Medium | Medium | Security analyst | Review denied actions by actor, source IP, and time window to identify misconfiguration or suspicious behavior. |
| AWS-RISK-09 | Public evidence leaks sensitive account details | raw CloudTrail logs committed to GitHub | Medium | High | High | Project owner | Sanitize account IDs, ARNs, IPs, key IDs, resource names, and user-agent strings before publishing. |

## How To Use This Register

The risk register is not meant to prove an incident occurred. It organizes the investigation into decisions:

- Which events are normal but still worth documenting?
- Which events increase exposure?
- Which events reduce visibility?
- Which events show remediation?
- Which risks need prevention, detection, or governance controls?

## Prioritized Control Themes

1. Protect identity first: root, MFA, access keys, and IAM permissions.
2. Preserve visibility: CloudTrail and GuardDuty changes should be rare and reviewed.
3. Reduce public exposure: security groups and S3 policies need strong defaults.
4. Use evidence carefully: raw logs should remain private and sanitized before publication.
5. Document remediation: show not only what happened, but what was fixed.
