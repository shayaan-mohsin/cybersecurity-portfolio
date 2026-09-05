# Cleanup Guide

## Purpose

Cloud labs should be cleaned up when they are no longer needed. Cleanup reduces cost, prevents accidental exposure, and keeps the account easier to monitor.

## Before Deleting

Save only public-safe evidence:

- sanitized CloudTrail excerpts
- generated analyzer reports
- screenshots with identifiers removed
- investigation notes
- remediation decisions

Keep raw logs private or delete them if no longer needed.

## CloudFormation Cleanup

If the lab was deployed with CloudFormation:

1. Open CloudFormation.
2. Select the lab stack.
3. Review the Resources tab.
4. Empty S3 buckets created by the lab.
5. Delete the stack.
6. Confirm the stack reaches `DELETE_COMPLETE`.

If stack deletion fails, the most common cause is a non-empty S3 bucket.

## GuardDuty Cleanup

If GuardDuty was enabled only for the lab:

1. Open GuardDuty in the lab Region.
2. Export any sample finding notes you need.
3. Disable GuardDuty if you do not want it to continue running.
4. Check billing/cost explorer after cleanup.

GuardDuty can incur cost after the free-trial period or when optional protection plans are used. Review AWS pricing before leaving it enabled.

## S3 Cleanup

For each lab bucket:

- delete objects
- delete object versions if versioning was enabled
- confirm the bucket is removed

## IAM Cleanup

Remove lab-only identities, policies, and access keys:

- delete unused access keys
- remove broad policies used for testing
- delete lab IAM users or roles
- confirm root MFA remains enabled

## Network Cleanup

Confirm:

- no lab security group has public inbound access
- no lab VPC remains unless intentionally retained
- no public IP resources were created outside the template

## Final Verification

After cleanup, check:

- CloudFormation stack deleted
- S3 buckets deleted or intentionally retained
- GuardDuty state understood
- IAM lab identities removed
- billing dashboard reviewed
- repository contains only sanitized evidence
