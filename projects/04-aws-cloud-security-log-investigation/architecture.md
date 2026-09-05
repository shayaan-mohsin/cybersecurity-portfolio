# Architecture

## Design Goal

The lab creates a small AWS environment that is safe enough for a personal account and realistic enough to support cloud security investigation practice.

The environment is intentionally modest. The value comes from reading the logs, understanding the controls, and explaining the security decisions, not from deploying a large or expensive cloud footprint.

## Logical Architecture

| Layer | Component | Purpose |
|---|---|---|
| Identity | AWS account, IAM identities, MFA, least privilege | Control who can administer the environment |
| Logging | CloudTrail Event History and optional trail to S3 | Preserve management activity for review |
| Detection | GuardDuty | Surface managed cloud threat findings |
| Storage | S3 evidence bucket | Practice storage hardening and public-access review |
| Network | VPC and detached security group | Generate and investigate exposure events without running compute |
| Access review | IAM Access Analyzer | Review external and public access paths |
| Automation | Python scripts | Parse logs, flag risky events, and generate reports |

## Security Controls In The Template

The CloudFormation template includes:

- S3 Block Public Access on lab buckets
- S3 bucket versioning
- S3 server-side encryption
- CloudTrail management event logging
- CloudTrail log file validation
- a lab VPC and security group with no inbound access by default
- IAM Access Analyzer for account-level access visibility
- optional GuardDuty detector creation

## Cost-Aware Design

The lab avoids always-on compute. There is no EC2 instance created by default. The security group exists so the analyst can generate controlled configuration-change events, then immediately reverse them.

CloudTrail Event History is available by default for recent management events. A trail can be used for ongoing log delivery, but the project intentionally documents cost considerations because duplicated management-event delivery, data events, and extended services can create charges.

GuardDuty is optional in the template. AWS documents a 30-day free trial for GuardDuty when first enabled in a Region, but continuing after the trial can incur costs.

## Evidence Flow

1. A user performs AWS management actions in the console or CLI.
2. CloudTrail records management events.
3. The analyst exports Event History or retrieves trail-delivered logs.
4. Raw logs stay private.
5. The sanitizer redacts sensitive identifiers.
6. The analyzer parses events and flags risk signals.
7. The investigation report summarizes what happened and what should be remediated.

## Investigation Model

The project uses four investigation questions:

1. Who performed the action?
2. What changed?
3. Was the action expected, denied, risky, or security relevant?
4. What should be validated, reversed, or monitored next?

## Public Evidence Standard

Public artifacts should prove the work without leaking the account.

Safe to publish:

- sanitized event excerpts
- frequency summaries
- detection findings
- architecture diagrams
- investigation notes
- remediation decisions
- screenshots with account identifiers removed

Keep private:

- raw CloudTrail exports
- real account IDs
- access key IDs
- source IP addresses
- user names tied to personal accounts
- exact resource names that identify the account
- billing or account contact information
