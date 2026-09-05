# CloudTrail Detection Catalog

## Purpose

This catalog defines the risk signals used in the AWS cloud security lab. The rules are intentionally readable so a recruiter, analyst, or hiring manager can understand the reasoning without needing to reverse-engineer code.

The detections focus on common analyst questions:

- Was a privileged identity used?
- Did someone create or expand access?
- Did someone expose a resource publicly?
- Did someone try to reduce logging or detection?
- Did AWS deny an action that still deserves review?

## Detection Rules

| Rule ID | Signal | Severity | Logic | Why it matters |
|---|---|---|---|---|
| AWS-CT-001 | Root account activity | High | `userIdentity.type` equals `Root` | Root should not be used for routine administration. Any successful use deserves review. |
| AWS-CT-002 | Failed console login | Medium | `eventName` equals `ConsoleLogin` and result is failure | Failed login activity may indicate user error, password issues, or attempted access. |
| AWS-CT-003 | Access key created | High | `eventName` equals `CreateAccessKey` | Long-lived credentials can become persistence or data-access risk if unmanaged. |
| AWS-CT-004 | Broad policy attachment | High | `AttachUserPolicy`, `AttachRolePolicy`, `PutUserPolicy`, or `PutRolePolicy` | Privilege changes should be reviewed for approval, scope, and least privilege. |
| AWS-CT-005 | Public administrative ingress | Critical | `AuthorizeSecurityGroupIngress` includes `0.0.0.0/0` or `::/0` on port `22` or `3389` | Public SSH or RDP exposure is a high-risk cloud misconfiguration pattern. |
| AWS-CT-006 | S3 public access control weakened | High | `DeletePublicAccessBlock`, public `PutBucketPolicy`, or public `PutBucketAcl` | S3 exposure can create data confidentiality and compliance risk. |
| AWS-CT-007 | CloudTrail logging changed | Critical | `StopLogging`, `DeleteTrail`, `UpdateTrail`, or `PutEventSelectors` | Logging changes can reduce visibility during an investigation. |
| AWS-CT-008 | GuardDuty configuration changed | High | `DeleteDetector`, `UpdateDetector`, or `CreateDetector` | Detection coverage changes should be intentional and documented. |
| AWS-CT-009 | Access denied activity | Medium | `errorCode` includes `AccessDenied` or `UnauthorizedOperation` | Denied actions can reveal misconfiguration, probing, or attempted privilege use. |
| AWS-CT-010 | Remediation evidence | Informational | `RevokeSecurityGroupIngress` or restoration events after exposure | Remediation events help complete the investigation timeline. |

## How To Interpret Findings

A detection is not the same thing as an incident. It is a signal that an analyst should review.

For each finding:

1. Confirm whether the action succeeded.
2. Confirm whether the actor was expected.
3. Confirm whether the source IP and user agent fit the activity.
4. Review related events in the same time window.
5. Decide whether the event is benign, risky, remediated, or suspicious.
6. Document the next step.

## Triage Priority

The highest-priority events in this lab are:

- CloudTrail logging disabled or deletion attempted
- public administrative ingress
- root activity followed by configuration changes
- administrator policy attachment
- S3 public access protections removed
- access key creation for an identity that does not need long-lived credentials

## Analyst Notes

Good cloud log review is not about memorizing every AWS API name. It is about understanding the risk meaning behind actions:

- identity changes affect who can act
- network changes affect what can be reached
- storage policy changes affect who can read data
- logging changes affect whether the team can reconstruct what happened
- denied events still matter because they show intent or misconfiguration
