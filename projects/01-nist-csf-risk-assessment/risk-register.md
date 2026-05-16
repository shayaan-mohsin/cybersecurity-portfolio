# Risk Register

## Scoring Model

| Score | Likelihood meaning | Impact meaning |
|---|---|---|
| High | Likely to occur or already observed as a recurring weakness | Could affect sensitive data, patient trust, business continuity, or leadership visibility |
| Medium | Plausible given current-state assumptions | Could affect a department, workflow, or important control objective |
| Low | Less likely under current assumptions | Limited operational or security impact |

Priority is based on likelihood, impact, healthcare sensitivity, and feasibility of remediation.

## Register

| ID | Risk | Affected area | Likelihood | Impact | Priority | Recommended response | Owner | NIST CSF function |
|---|---|---|---|---|---|---|---|---|
| R-001 | Inconsistent access review process | Employee and manager accounts | Medium | High | High | Establish quarterly access reviews, define account owners, and document approvals | IT Support / Operations Manager | Govern / Protect |
| R-002 | Limited incident response documentation | Operations and leadership | Medium | High | High | Create a lightweight incident response playbook, escalation matrix, and tabletop schedule | Operations Manager / IT Support | Respond / Govern |
| R-003 | Weak vendor access governance | Scheduling, billing, and IT support vendors | Medium | High | High | Require named accounts, least privilege, vendor owner assignment, and periodic review | IT Support / Vendor Owner | Govern / Protect |
| R-004 | MFA coverage is not verified across all users | Scheduling SaaS, billing portal, email | Medium | High | High | Validate MFA coverage, prioritize privileged and remote users, and document exceptions | IT Support | Protect |
| R-005 | Asset inventory is incomplete | Laptops, SaaS tools, shared folders | Medium | Medium | Medium | Build a lightweight asset and application inventory with owner, data type, and criticality | IT Support / Office Manager | Identify |
| R-006 | Security awareness and phishing reporting are informal | Employees and managers | High | Medium | Medium | Publish phishing reporting steps and run annual security awareness training | Office Manager / Leadership | Protect / Detect |
| R-007 | Cloud document storage ownership is unclear | Intake forms and internal documents | Medium | Medium | Medium | Assign folder owners, review sharing permissions, and define retention expectations | Office Manager | Govern / Protect |
| R-008 | Backup and recovery expectations are unclear | Scheduling, billing, cloud documents | Low | High | Medium | Define recovery objectives and test restoration for one critical workflow | IT Support / Leadership | Recover |
| R-009 | Security monitoring and alert review are ad hoc | Email, SaaS login activity, privileged access | Medium | Medium | Medium | Define alert sources, review cadence, and escalation criteria | IT Support | Detect / Respond |

## Summary

The highest-priority risks are access governance, incident response readiness, vendor access, and MFA verification. These create practical risk in a healthcare services environment because they affect sensitive information, service continuity, and accountability.

## Top Three Recommendations

1. Establish quarterly access reviews for employees and vendors.
2. Create a lightweight incident response playbook and escalation matrix.
3. Validate MFA coverage for scheduling, billing, email, vendor, and privileged accounts.
