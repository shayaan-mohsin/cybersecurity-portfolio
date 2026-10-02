# Servicing a ticket in ServiceNow : proposed click-through

**Status:** future lab walkthrough, not an executed run. Use [LAB-INC-001](../tickets/01-account-lockout.md) as the example. The actual interface, field names, permissions and generated record number must be captured from the allocated instance.

## 1. Open the work queue under the agent role

Sign in as the scoped fictional service-desk agent, not the setup administrator. Open the available incident work list and filter to the L1 assignment group / active work. Review priority, age, service effect and next-update obligations; do not sort only by who complained most recently.

**Evidence:** agent identity/role and the queue filter. **Check:** the agent cannot perform an administrator-only setup action.

## 2. Create or accept the intake record

If no record exists, use the available New incident action. Set the fictional caller Avery Chen, channel Phone, short description “Existing account locked before scheduled meeting,” and the reported error/business effect. Retain the actual system-generated number and creation time.

Link LAB-INC-001 in an allowed description/reference field or evidence manifest; do not overwrite the native number. Record service Workforce sign-in and the device only after its identity is confirmed.

**Evidence:** intake record with source of each important fact. **Check:** requester identity and actual affected user are not confused.

## 3. Classify, prioritize and take ownership

This is an incident under the fictional policy. Select the appropriate actual category/subcategory; do not invent a category that the instance does not support. Choose Service Desk L1 and an accountable agent. Set impact Low and urgency High, then save and observe the calculated priority. The proposed matrix yields P3; investigate a mismatch before proceeding.

Transition to In Progress when the assigned investigation starts. Record why one user and a meeting deadline support these values.

**Evidence:** calculated priority, assignment, state and rationale. **Check:** VIP status or urgency alone did not create P1.

## 4. Acknowledge the user

Post the sample first customer message from the case in the user-visible comments field: describe the issue, explain the verification step, and state the next update interval. Inspect the caller view using the fictional user account to verify that it is visible.

If implementing the optional response SLA, configure a lab-only Boolean **u_acknowledged**, default false, under the setup administrator. The agent sets it true only after a substantive customer acknowledgement exists. Use this as an explicitly manual stop checkpoint, with audited role/time and a check of the attached task SLA. It is a proposed custom field, not a ServiceNow default or automatic proof of response quality. If that field or rule is not implemented, omit the response SLA claim and retain the actual dated message instead.

**Evidence:** actual user-visible acknowledgement and caller-view check. **Check:** an empty/internal-only note does not count as acknowledging the user.

## 5. Verify identity before a privileged action

Follow the lab's approved verification procedure through the established pre-enrolled route. Record the method/result without answers or codes. If verification fails, document that no account action occurred, route to Identity Support, and keep the next update owned.

**Evidence:** verification outcome and delegated-role decision. **Check:** the caller cannot replace the trusted callback detail merely by supplying a new number.

## 6. Investigate and document decisions

Use internal work notes to distinguish report, observation, hypothesis and action. For this scenario, inspect account state and recurrence metadata only if an authorized test directory exists. Otherwise, mark those conditions scripted and record the platform-workflow limitation.

Perform the narrow authorized action in the endpoint/directory lab if available. Document result and next hypothesis. No password belongs in the record.

**Evidence:** relevant before/after observation, actual action and role if performed. **Check:** a sentence typed into ServiceNow is not treated as proof that the endpoint action happened.

## 7. Handle a legitimate dependency or escalation

For missing caller information, select On Hold and the actual supported hold reason, include the requested information and next update. Under the proposed policy, only Awaiting Caller pauses the restoration SLA; verify the actual attached definition.

For a transfer, record the receiving group, concise diagnostic packet, remaining question, acceptance or pending acceptance, and next user update. Reassignment alone must not move the record to Resolved.

**Evidence:** dependency reason or handoff packet and acceptance state. **Check:** the case cannot disappear into an unowned queue.

## 8. Verify recovery, then resolve

Have the fictional user enter their own credentials and test the intended sign-in/application path. Record actual times, the recurrence observation window and user confirmation. If the technical service is only simulated, label the result accordingly and claim only a completed record workflow.

Use the actual resolution action, appropriate available resolution code and a specific resolution note: what changed, why, test outcome and any remaining risk. Post the user-facing restoration message. A workaround may justify restored service; record the unresolved cause separately.

**Evidence:** real state/activity and test result with its execution type. **Check:** the resolution note cannot be “fixed” without supporting detail.

## 9. Follow up, close or reopen

Check the configured closure property/policy against the fictional two-business-day proposal. For this lab, a recurrence while Resolved reopens the investigation through the supported action. Preserve history and reassess the hypothesis. A recurrence after Closed gets a linked new incident under the lab policy.

**Evidence:** closure or reopen behavior with actual timestamps. **Check:** failed recovery is not hidden as a new successful ticket count.

[Incident overview reference](https://www.servicenow.com/docs/r/it-service-management/service-operations-workspace/view-update-inc-overview-tab.html) · [Incident lifecycle reference](https://www.servicenow.com/docs/r/it-service-management/incident-management/c_IncidentManagementStateModel.html) · [Setup plan](servicenow-setup-and-evidence-plan.md)
