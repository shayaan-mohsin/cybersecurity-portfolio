# Executive Summary

## Purpose

This project builds and documents an AWS cloud security monitoring lab focused on log investigation, baseline hardening, and Python-supported analysis.

The goal is to demonstrate how cloud activity logs can be turned into security findings, remediation steps, and leadership-facing explanations.

## Key Takeaway

Cloud security investigations often start with a simple question: who changed what?

CloudTrail helps answer that question. When paired with a clear detection catalog, hardened cloud resources, and repeatable analysis scripts, the analyst can identify risky changes such as root usage, broad IAM permissions, public security group exposure, S3 access-control changes, and attempts to modify logging.

## What Was Built

- A cost-conscious AWS lab design using CloudFormation
- Baseline hardening guidance for IAM, S3, CloudTrail, VPC security groups, Access Analyzer, and GuardDuty
- A CloudTrail field guide and investigation playbook
- A detection catalog for common cloud security risk signals
- Python scripts to sanitize and analyze CloudTrail exports
- Sanitized sample CloudTrail events for repeatable testing
- A generated investigation report and CSV outputs
- QC-checked visuals for architecture, workflow, and risk signals

## Security Value

The project emphasizes practical analyst habits:

- preserve logs before investigating
- separate successful changes from denied attempts
- focus on identity, privilege, exposure, and visibility
- look for remediation events after risky changes
- avoid publishing sensitive log details
- explain technical events in business language

## Sample Findings

The sample dataset generated 12 findings across these areas:

| Area | Example signal | Risk meaning |
|---|---|---|
| Identity | root console login | Root use should be rare and reviewed. |
| Credential | access key creation | Long-lived credentials need lifecycle control. |
| Privilege | administrator policy attachment | Broad permissions can increase blast radius. |
| Network | public SSH ingress | Internet-exposed admin access is high risk. |
| Storage | S3 public access controls changed | Public storage exposure can affect sensitive data. |
| Logging | CloudTrail logging change attempted | Reduced visibility can weaken investigations. |
| Detection | GuardDuty configuration changed | Detection coverage should be intentional. |
| Remediation | ingress rule revoked | Corrective events help close the timeline. |

## Recommended Next Steps

For a real AWS lab run:

1. Deploy the CloudFormation template in a personal AWS lab account.
2. Enable MFA and validate baseline controls.
3. Generate safe administrative activity.
4. Export CloudTrail Event History.
5. Sanitize the raw logs.
6. Run the Python analyzer.
7. Document findings, remediation, and lessons learned.
8. Clean up resources and check billing.

## Boundary Statement

This is a personal cloud security lab and portfolio project. It does not represent production security administration, a formal audit, or an incident investigation for a real organization.
