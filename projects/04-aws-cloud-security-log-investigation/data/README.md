# Data Notes

This folder contains sanitized sample CloudTrail-style events so the Python analyzer can be run without access to a live AWS account.

## Public Data Handling Rule

Do not commit raw CloudTrail exports from a personal AWS account.

Raw AWS logs can include:

- AWS account IDs
- ARNs
- IAM user names
- source IP addresses
- access key IDs
- session names
- resource names
- request parameters
- user-agent strings

Use [`../scripts/sanitize_cloudtrail.py`](../scripts/sanitize_cloudtrail.py) before publishing any log excerpts.

## Sample Dataset

[`sample-cloudtrail-events.json`](sample-cloudtrail-events.json) is a sanitized dataset for reproducible testing. It includes representative management events related to:

- console login
- root activity
- IAM policy changes
- access key creation
- S3 public access controls
- security group exposure
- CloudTrail logging changes
- GuardDuty detector activity
- AccessDenied errors

The sample is intentionally small so the report is easy to inspect by hand.

## Real Lab Evidence

When using a live AWS account:

1. Export CloudTrail Event History as JSON.
2. Store the raw export outside the public repo.
3. Sanitize the export.
4. Run the analyzer.
5. Commit only sanitized evidence and generated summaries.
