# Log Collection Guide

## Goal

Collect real AWS management activity logs in a way that supports cloud security investigation practice without exposing sensitive account details in a public repository.

## Primary Log Source

Use AWS CloudTrail Event History for the first version of the lab.

CloudTrail Event History provides recent management events for an AWS account and Region. These events are useful for answering questions such as:

- who signed in
- who changed an IAM policy
- who modified a security group
- who changed S3 public access settings
- who attempted a denied operation
- which source IP and user agent were involved

## Events Worth Generating

Generate safe administrative activity that creates useful logs:

| Activity | Expected CloudTrail event | Why it is useful |
|---|---|---|
| Sign in as an IAM user | `ConsoleLogin` | Teaches identity and source IP review |
| Failed sign-in attempt | `ConsoleLogin` with failure | Teaches authentication triage |
| Deploy the CloudFormation stack | `CreateStack` | Shows infrastructure deployment evidence |
| Update the CloudFormation stack | `UpdateStack` | Shows change-management evidence |
| Review or tag an S3 bucket | `PutBucketTagging` | Shows storage administration |
| Attempt blocked public bucket policy | `PutBucketPolicy` with error | Shows S3 public access control working |
| Temporarily open detached security group to `0.0.0.0/0` | `AuthorizeSecurityGroupIngress` | Shows network exposure detection |
| Immediately reverse the security group change | `RevokeSecurityGroupIngress` | Shows remediation evidence |
| Generate GuardDuty sample findings | `CreateSampleFindings` | Shows managed finding review |

Do not perform destructive activity against production accounts or resources. Do not expose a real instance to the internet for this project.

## Export From The AWS Console

1. Open the AWS CloudTrail console.
2. Choose **Event history**.
3. Select the Region used for the lab.
4. Set a time range that covers the lab activity.
5. Filter to relevant event names when needed.
6. Open individual events and read the JSON event record.
7. Download events as JSON.
8. Store the raw export outside the public repository.

## Export With AWS CLI

Use this if AWS CLI is installed and configured:

```powershell
aws cloudtrail lookup-events `
  --start-time 2026-09-01T00:00:00Z `
  --end-time 2026-09-02T00:00:00Z `
  --region us-west-2 `
  --output json > private/raw-cloudtrail-events.json
```

Then sanitize before committing anything:

```powershell
python scripts/sanitize_cloudtrail.py private/raw-cloudtrail-events.json data/sanitized-cloudtrail-events.json
python scripts/analyze_cloudtrail.py data/sanitized-cloudtrail-events.json --output-dir outputs
```

## Minimum Evidence To Capture

For a polished public writeup, capture:

- total events reviewed
- time range
- event sources reviewed
- top event names
- high-risk events found
- denied actions
- remediation steps taken
- remaining risks or follow-up actions

## What To Redact

Before publishing:

- account IDs
- ARNs
- access key IDs
- source IP addresses
- user names tied to personal accounts
- exact bucket names
- security group IDs if they identify the account
- stack IDs
- session names
- user-agent strings if they expose local system details

## Analyst Note

The point of this project is not to create dramatic alerts. The stronger story is that normal cloud administration leaves evidence. A security analyst needs to know how to read that evidence, separate routine changes from risky changes, and explain what should happen next.
