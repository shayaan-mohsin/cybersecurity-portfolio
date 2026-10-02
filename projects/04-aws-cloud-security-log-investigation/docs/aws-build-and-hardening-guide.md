# Proposed lab build and validation plan

[Project overview](../README.md) · [Architecture](../architecture.md) · [Cleanup plan](cleanup-guide.md)

The CloudFormation template has not been deployed. The following are acceptance criteria for a future run, not completed steps.

## Before deployment

Use an authorized isolated AWS account, temporary role credentials, an agreed Region, and a cost budget. Review existing trails, analyzers, and GuardDuty configuration to avoid conflicts. Check current AWS service requirements and pricing before provisioning.

Review the template’s change set and permissions. GuardDuty is optional and false by default. The network resources have no attached workloads or internet gateway.

## Evidence to collect

- AWS template validation and change-set results
- Stack events and outputs, with sensitive values kept private
- Actual public-access-block settings, encryption, and versioning on both buckets
- Trail status, selected event coverage, new delivered files, and integrity validation
- SourceArn restrictions on both CloudTrail bucket-policy statements
- Account access-analyzer state, and detector state if GuardDuty is enabled
- Proof that test resources are isolated and the security group is detached

Do not manufacture unsafe exposure merely to populate a screenshot. Use denied operations or controlled changes to isolated resources, with a reviewed rollback plan.

## Completion criteria

Record the exact actions, event IDs, expected and observed outcomes, final state, and cleanup results. If a deployment or validation fails, retain the failure as evidence instead of describing the lab as complete.
