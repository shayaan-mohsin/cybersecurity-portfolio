# NIST CSF 2.0 Mapping

This mapping uses NIST CSF 2.0 to translate the breach trend findings into security outcomes and implementation priorities. Category themes are selected at a practical level for a small or modest-maturity healthcare organization.

| NIST CSF 2.0 function | Relevant category themes | Related risks | Assessment implication |
|---|---|---|---|
| Govern | Organizational context; risk management strategy; roles and responsibilities; cybersecurity supply chain risk management | R-003, R-005, R-010 | Leadership needs clear ownership for systems, vendors, sensitive data, and risk decisions. |
| Identify | Asset management; risk assessment; improvement | R-001, R-005, R-008 | Inventory and data-location visibility are prerequisites for prioritizing network server, email, and electronic record risk. |
| Protect | Identity management, authentication, and access control; awareness and training; data security; platform security; infrastructure resilience | R-001, R-002, R-004, R-007, R-008 | Access control, MFA, secure configuration, user reporting, and resilient backups reduce the most common observed exposure paths. |
| Detect | Continuous monitoring; adverse event analysis | R-002, R-004, R-009 | Monitoring should cover email, privileged access, server activity, endpoint alerts, and vendor access anomalies. |
| Respond | Incident management; incident analysis; incident reporting and communication; incident mitigation | R-002, R-003, R-006, R-009 | Playbooks should define containment, evidence handling, escalation, vendor coordination, and breach decision support. |
| Recover | Incident recovery plan execution; recovery communication | R-006, R-007, R-010 | Recovery priorities should be tied to clinical, operational, and patient communication needs. |

## Mapping By Finding

| Finding | CSF interpretation | Control direction |
|---|---|---|
| Hacking/IT incidents dominate the sample | Treat compromise prevention and detection as board-level risk topics, not only technical backlog items. | Prioritize identity, patching, secure configuration, logging, and response readiness. |
| Network servers appear most often as breached information locations | Server inventory and hardening are core risk management tasks. | Maintain system owners, exposure review, vulnerability prioritization, backup validation, and alert coverage. |
| Email appears frequently | Workforce-facing controls remain critical in healthcare operations. | Enforce MFA, phishing reporting, mailbox monitoring, and account compromise playbooks. |
| Business associates are present in a meaningful share of records | Supply chain risk should be integrated into governance and response. | Track vendors, data access, security expectations, incident contacts, and review cadence. |
| Affected-individual totals vary widely | Risk cannot be ranked by incident count alone. | Combine likelihood, impact, data sensitivity, system criticality, and affected-population scale. |

## Target State

The target state is a repeatable healthcare security baseline:

1. Leadership can name the systems, vendors, and data flows that matter most.
2. Technical teams can prioritize vulnerabilities and misconfigurations by patient and operational impact.
3. Workforce users know how to report suspicious email, account issues, and disclosure concerns.
4. Incident responders can contain, analyze, communicate, and recover without inventing the process during the incident.
5. Vendors with sensitive data access are reviewed as part of routine governance.
