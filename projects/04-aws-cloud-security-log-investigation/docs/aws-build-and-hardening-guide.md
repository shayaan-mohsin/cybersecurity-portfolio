# AWS Build And Hardening Guide

## Purpose

This guide walks through a cost-conscious AWS lab build for cloud security monitoring and log investigation practice.

The goal is not to build a large production environment. The goal is to create a small, controlled environment where security-relevant actions generate real AWS management logs that can be reviewed, sanitized, and analyzed.

## Pre-Build Safety Checklist

Before deploying anything:

- Use a personal AWS lab account, not an employer or school production account.
- Enable MFA on the root account.
- Create a budget alert in AWS Billing.
- Confirm the target Region.
- Keep raw logs private.
- Plan to delete lab resources when finished.
- Review GuardDuty pricing before enabling GuardDuty beyond the initial free trial.

## Recommended Region

Use one primary Region, such as `us-west-2` or `us-east-1`.

Keeping the lab in one Region makes the investigation easier because the analyst can connect events, resources, and timestamps without hopping across unnecessary Regions.

## Deployment Options

### Console Deployment

1. Sign in to the AWS Management Console.
2. Open CloudFormation.
3. Choose **Create stack**.
4. Upload [`../cloudformation/aws-cloud-security-lab.yaml`](../cloudformation/aws-cloud-security-lab.yaml).
5. Use the default `LabName`, or choose a short name.
6. Leave `EnableGuardDuty` as `false` unless you are ready to monitor GuardDuty usage and cost.
7. Create the stack.
8. Save the stack outputs for the investigation notes.

### CLI Deployment

Use this only if AWS CLI is installed and configured:

```powershell
aws cloudformation deploy `
  --template-file cloudformation/aws-cloud-security-lab.yaml `
  --stack-name shayaan-cloud-security-lab `
  --capabilities CAPABILITY_NAMED_IAM `
  --parameter-overrides EnableGuardDuty=false
```

The template does not create named IAM roles, but `CAPABILITY_NAMED_IAM` is included in the example so the deployment pattern is explicit if the template is extended later.

## Baseline Controls To Validate

After deployment, validate the following:

| Control | Why it matters | How to validate |
|---|---|---|
| Root MFA enabled | Root account compromise is high impact | IAM or account security settings |
| CloudTrail logging active | Management activity should be recorded | CloudTrail trail status |
| CloudTrail log file validation enabled | Supports log integrity assurance | Trail settings |
| S3 Block Public Access enabled | Reduces accidental public exposure | S3 bucket permissions |
| S3 encryption enabled | Protects stored evidence and logs | S3 bucket properties |
| S3 versioning enabled | Preserves object history | S3 bucket properties |
| Security group has no inbound rules | Avoids unnecessary exposure | EC2 security group inbound rules |
| IAM Access Analyzer active | Supports review of external access | IAM Access Analyzer dashboard |
| GuardDuty enabled only by decision | Avoids surprise cost | GuardDuty settings and billing |

## Hardening Notes

### Identity

- Do not use the root account for routine lab work.
- Use MFA on human users.
- Keep IAM permissions narrow.
- Remove unused access keys.
- Prefer temporary credentials where possible.

### Logging

- Keep CloudTrail enabled.
- Do not disable log validation.
- Treat `StopLogging`, `DeleteTrail`, and `PutEventSelectors` as high-risk events.
- Keep raw log exports private.

### S3

- Keep all four Block Public Access settings enabled.
- Use encryption and versioning.
- Avoid public bucket policies.
- Review Access Analyzer findings if any bucket is shared externally.

### Network

- Avoid attaching compute to a public security group for this project.
- If you generate an exposure event, use a detached security group and reverse the change immediately.
- Treat `0.0.0.0/0` or `::/0` on administrative ports such as `22` or `3389` as high risk.

## Completion Criteria

The build is complete when:

- the stack deploys successfully
- CloudTrail records management events
- S3 public access controls are enabled
- the detached security group has no inbound rules after testing
- raw logs are stored privately
- sanitized logs can be analyzed by the Python script
- the generated report explains findings and remediation
