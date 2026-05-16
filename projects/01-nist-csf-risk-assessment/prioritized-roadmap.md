# Prioritized Roadmap

This roadmap sequences practical improvements across the first 90 days. The order reflects the sample findings: Hacking/IT incidents, network server exposure, email compromise, business associate involvement, and recovery readiness.

## 0 to 30 Days: Establish Visibility And Ownership

| Action | Primary owner | Related risks | Success measure |
|---|---|---|---|
| Build a minimum viable inventory of servers, email platforms, electronic record systems, cloud storage, endpoints, and vendor-managed systems. | IT / Security | R-001, R-005 | Inventory includes owner, data sensitivity, business function, internet exposure, and backup status. |
| Identify systems that store or process electronic protected health information. | Privacy / IT | R-005, R-008 | Sensitive data locations are documented and mapped to system owners. |
| Validate MFA coverage for remote access, email, privileged accounts, and vendor access. | IT / Identity Owner | R-002, R-004 | MFA exceptions are documented with remediation dates. |
| Create an incident contact list and escalation path for ransomware, email compromise, unauthorized access, and vendor incidents. | Security / Operations | R-003, R-006 | Playbook owners and contacts are approved by leadership. |
| Review the top externally exposed systems for known exploitable vulnerabilities and unsupported software. | IT / Security | R-001, R-009 | High-risk exposures have tickets, owners, and due dates. |

## 31 to 60 Days: Reduce Common Exposure Paths

| Action | Primary owner | Related risks | Success measure |
|---|---|---|---|
| Implement a monthly access review for privileged accounts and high-risk healthcare systems. | IT / Department Managers | R-004, R-008 | Review results show removals, approvals, and exception tracking. |
| Harden email security controls and monitor for suspicious forwarding rules or impossible-travel sign-ins. | IT / Security | R-002, R-009 | Alerting and response steps are documented and tested. |
| Create vendor access and data-sharing register for business associates and service providers. | Vendor Owner / Privacy | R-003, R-005 | Register includes access type, data handled, contract owner, and incident contact. |
| Define minimum logging sources for servers, email, identity, endpoint protection, and cloud services. | IT / Security | R-001, R-009 | Log coverage map identifies gaps and review cadence. |
| Draft ransomware and email compromise playbooks. | Security / Operations | R-002, R-006, R-007 | Playbooks include containment, evidence, communication, and recovery steps. |

## 61 to 90 Days: Test Resilience And Governance

| Action | Primary owner | Related risks | Success measure |
|---|---|---|---|
| Run a tabletop exercise for ransomware affecting a network server that stores patient-related data. | Security / Leadership | R-001, R-006, R-007, R-010 | After-action report includes decision points, gaps, and assigned remediation owners. |
| Test restoration for at least one high-priority system and verify backup isolation. | IT / Operations | R-007 | Restore test results are documented with recovery time and issues found. |
| Establish quarterly vendor access review and incident notification validation. | Vendor Owner / Privacy | R-003 | Vendor access and incident contacts are confirmed or corrected. |
| Build an executive risk dashboard using the risk register, open remediation work, and incident readiness metrics. | Security / Leadership | R-010 | Dashboard is reviewed with leadership and updated monthly. |
| Update policies and procedures based on tabletop and access review findings. | Security / Privacy / Operations | R-006, R-008 | Updated procedures are approved and communicated to relevant staff. |

## Metrics To Track

| Metric | Why it matters |
|---|---|
| Percent of high-risk systems with named owners | Ownership is required for remediation and accountability. |
| Percent of privileged and remote-access accounts covered by MFA | Identity compromise is a common path into healthcare systems. |
| Number of critical/high vulnerabilities past due on sensitive systems | Vulnerability aging shows whether risk is actually being reduced. |
| Percent of vendors with documented access type and incident contact | Third-party events require fast coordination. |
| Backup restore test success rate | Recovery confidence must be demonstrated before an incident. |
| Time from suspicious email report to triage | Email remains a frequent breach location and needs measurable response. |

## Sequencing Rationale

The first 30 days focus on knowing what exists and who owns it. The next 30 days reduce the most common compromise paths. The final 30 days test whether governance, response, and recovery actually work under pressure.
