# Findings Narrative

## Overview

The sample CloudTrail analysis shows how a cloud security analyst can move from individual AWS events to a defensible investigation narrative.

The events are not treated as automatic proof of compromise. They are treated as signals that deserve context, validation, and clear follow-up.

## What The Logs Show

The sample dataset includes 12 AWS management events across sign-in, IAM, EC2, S3, CloudTrail, GuardDuty, and CloudFormation activity.

The analyzer generated 12 findings:

- 2 Critical
- 6 High
- 3 Medium
- 1 Informational

The highest priority findings involved:

- public administrative network exposure
- CloudTrail logging change activity
- root account activity
- long-lived credential creation
- privilege policy changes
- S3 public access control changes

## Why The Critical Findings Matter

### Public Administrative Ingress

Opening SSH or RDP to the public internet is a common cloud exposure pattern. Even when no compute resource is attached, the configuration change is important because it shows the kind of event an analyst should catch quickly.

The remediation event matters too. Seeing `RevokeSecurityGroupIngress` after `AuthorizeSecurityGroupIngress` helps complete the timeline and shows that the risky rule was reversed.

### CloudTrail Logging Change

CloudTrail is one of the main sources used to reconstruct AWS account activity. Any attempt to stop, delete, or materially change logging deserves high attention.

In the sample evidence, the `StopLogging` action was denied. That is still useful: a blocked action can show that least privilege worked, while also giving the analyst a reason to review who attempted the action and why.

## Why The High Findings Matter

Root activity, IAM policy changes, access key creation, S3 public access changes, and GuardDuty configuration changes all affect the security posture of the account.

These events are not automatically malicious. An administrator may perform them during normal setup. The analyst's job is to determine whether the activity was expected, approved, properly scoped, and followed by remediation if needed.

## Analyst Conclusion

The project shows that cloud log investigation is partly technical and partly judgment-based.

The technical side is knowing which fields to read: `eventName`, `eventSource`, `userIdentity`, `sourceIPAddress`, `requestParameters`, `responseElements`, and `errorCode`.

The judgment side is knowing what the event means:

- Did it create public exposure?
- Did it grant privilege?
- Did it create long-lived access?
- Did it reduce visibility?
- Did AWS block it?
- Was it remediated?

That combination is the core skill this project is designed to practice.
