# Fictional lab service policy

This is a proposed Northstar Learning Services policy for the exercise. It is not a universal ITIL rule, a ServiceNow default, or an employer commitment.

## Classification and intake

An incident restores an existing service that is interrupted or degraded. A service request delivers something authorized: software, new access, onboarding, or recovery fulfillment under this lab policy. Classify from the service effect, not from a word such as “password.” An ordinary reset may be a request at another employer; an existing account unexpectedly locked out is an incident in this exercise.

Use fictional caller and requested-for identities separately. A manager requesting something for an employee is not the affected employee. Validate against the lab directory/roster; a message display name is not proof. Record the approved verification method and its result, without storing answers, authentication secrets, or identity-document images.

## Identity verification implementation prerequisite

The “approved second verification step” in the lockout and MFA cases is currently undefined. No account unlock or factor recovery may run until a specific approved method, eligibility rules, failure route and delegated role are documented and tested. A callback and manager approval are not automatically sufficient identity proofing. For the first PDI-only run, use explicitly scripted verification results and claim only the ticket workflow. Do not improvise security questions or collect identity documents to fill this gap.

## Proposed impact / urgency matrix

Impact: High = widespread critical service effect; Medium = multiple users or a business team; Low = one user or a narrow task. Urgency: High = time-critical with no viable workaround; Medium = work impaired but a workaround exists or delay is tolerable; Low = planned or low time sensitivity.

| Impact ↓ / Urgency → | High | Medium | Low |
| --- | --- | --- | --- |
| High | P1 | P2 | P3 |
| Medium | P2 | P3 | P4 |
| Low | P3 | P4 | P5 |

Validate the actual instance calculation. Do not override it silently. Request target dates are fulfillment commitments; incident SLAs should not be applied indiscriminately to requests.

## Proposed incident targets

| Priority | Acknowledge target | Restoration target | Proposed schedule |
| --- | --- | --- | --- |
| P1 | 15 minutes | 4 hours | 24 × 7 for the exercise |
| P2 | 30 minutes | 8 hours | 24 × 7 for the exercise |
| P3 | 1 business hour | 8 business hours | Mon–Fri 09:00–17:00 America/Los_Angeles |
| P4 | 4 business hours | 16 business hours | Same business schedule |
| P5 | 8 business hours | 40 business hours | Same business schedule |

These numbers are chosen for the lab, not extracted from the job postings. No SLA performance has been measured. Define holidays explicitly when implementing; never treat a business hour as an elapsed hour by default.

Proposed response SLA: start at incident creation, stop at the explicitly manual, audited u_acknowledged checkpoint after the first substantive user-visible acknowledgement; no pause. See the [ticket click-through](servicenow-ticket-walkthrough.md) for this proposed custom field and its limitations. Proposed restoration SLA: start at creation, stop at Resolved; pause only at On Hold / Awaiting Caller with a documented information request. Other wait reasons continue under this policy. Cancellation and priority-change behavior must be explicitly configured and tested before any metric is reported. Reopened incidents must be checked for expected reattachment/reset behavior; do not assume the old SLA restarts.

ServiceNow supports configurable start, pause, stop and reset conditions; actual outcomes depend on the configured definition. [Official SLA definition documentation](https://www.servicenow.com/docs/r/it-service-management/service-level-management/t_CreateAnSLADefinition.html).

## Ownership and communication

Every active record has an assignment group, an accountable agent or queue owner, the next step and a next update time. For core cases, choose an explicit update interval at intake; the messages in the playbooks use relative exercise times, not historical response claims.

Work notes carry technical context for authorized fulfillers. Additional comments carry user updates. Verify the actual instance access and notification behavior from a caller account; labels alone do not prove privacy. Keep sensitive security evidence in the approved restricted store and reference it in the support ticket. [Incident properties and note visibility labels](https://www.servicenow.com/docs/r/it-service-management/incident-management/incident-management-properties.html).

Escalate when the required role is unavailable, identity/approval cannot be established, a security concern exists, the tested diagnostics exceed L1 scope, the incident becomes wider than initially believed, or the service target is at risk. Do not mark Resolved just to stop a clock.

## Resolution and closure

For incidents, record what restored service, the test result, any remaining risk, and user confirmation or the defined follow-up path. A workaround can restore service while a problem remains open; distinguish it from a permanent fix. The planned closure policy is two business days after Resolved with a final notification, subject to actual instance capability and confirmation checks. A closed incident that recurs gets a linked new incident under this lab policy; the printer exercise reopens during the Resolved period.

For requests, complete required approvals and all required tasks before reporting fulfillment. Rejected, withdrawn and incomplete requests retain their outcome. A rejection is not a resolved incident. Verify the actual task/request state names and roll-up logic.

Official incident states include New, In Progress, On Hold, Resolved, Closed and Canceled; configuration and closure properties must be checked on the instance. [Incident lifecycle](https://www.servicenow.com/docs/r/it-service-management/incident-management/c_IncidentManagementStateModel.html).
