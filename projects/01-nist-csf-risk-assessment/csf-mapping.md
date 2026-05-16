# NIST CSF Mapping

This mapping uses NIST CSF 2.0 as a public reference framework. It is a portfolio exercise, not a formal control assessment or compliance attestation.

## Function-Level Mapping

| NIST CSF function | CareBridge interpretation | Related risks | Example action |
|---|---|---|---|
| Govern | Define security accountability, policy ownership, risk decisions, and vendor oversight | R-001, R-002, R-003, R-007 | Assign owners for access reviews, vendor access, document storage, and incident response |
| Identify | Understand assets, workflows, users, vendors, and sensitive data | R-005 | Build a lightweight inventory of SaaS tools, laptops, shared folders, and business owners |
| Protect | Reduce risk through access control, MFA, training, and data safeguards | R-001, R-003, R-004, R-006, R-007 | Validate MFA coverage, apply least privilege, and publish user guidance |
| Detect | Improve visibility into suspicious activity and user reporting | R-006, R-009 | Define phishing reporting, alert sources, and review cadence |
| Respond | Prepare for incidents through roles, escalation, analysis, and communication | R-002, R-009 | Create a lightweight incident response playbook and escalation matrix |
| Recover | Restore critical workflows and learn from disruption | R-008 | Define recovery objectives and test restoration steps |

## Category Themes

| Function | Category theme | Portfolio application |
|---|---|---|
| Govern | Organizational context | Identify the workflows and sensitive data that matter most to CareBridge |
| Govern | Roles, responsibilities, and authorities | Assign owners for access reviews, vendors, incident response, and cloud storage |
| Govern | Policy | Document lightweight expectations for access, vendor support, incident reporting, and data handling |
| Govern | Cybersecurity supply chain risk management | Create a vendor access review cycle and named owner model |
| Identify | Asset management | Track laptops, SaaS tools, shared folders, and business owners |
| Identify | Risk assessment | Score risks by likelihood, impact, priority, and business area |
| Protect | Identity management, authentication, and access control | Validate MFA, remove stale accounts, and apply least privilege |
| Protect | Awareness and training | Publish phishing reporting and security awareness guidance |
| Protect | Data security | Review shared folders and sensitive document handling |
| Detect | Continuous monitoring | Define the minimum alert sources and review cadence for email and SaaS activity |
| Respond | Incident management | Create a response playbook, escalation matrix, and tabletop exercise |
| Recover | Recovery plan execution | Define restoration expectations for scheduling, billing, and document workflows |

## Key Observation

The strongest near-term value comes from governance and process improvements. CareBridge does not need an enterprise-scale security program to reduce risk; it needs clear ownership, repeatable access reviews, practical response steps, and basic visibility into the systems that support sensitive workflows.

## Practical Maturity Target

The target state is not "perfect security." The target state is a repeatable, explainable security baseline:

- Known systems and owners
- Reviewed user and vendor access
- MFA coverage validated
- Incident response steps documented
- Staff know how to report suspicious activity
- Recovery expectations are defined for critical workflows
