# Workflow illustrations

[Project overview](../README.md)

These illustrations describe proposed decisions, not platform execution.

## Resolution requires verification

![Proposed incident flow; no ServiceNow execution. Intake and investigation: Record scope, priority, owner, observations and next action. Work or accepted handoff: Keep ownership and user updates. Reassignment is not resolution. Verify the original task: Check the technical result and obtain user confirmation. Resolve, then close under policy: If it recurs before closure, return to investigation. After closure, link a new incident.](incident-lifecycle.svg)

Proposed incident flow; no ServiceNow execution. Intake and investigation: Record scope, priority, owner, observations and next action. Work or accepted handoff: Keep ownership and user updates. Reassignment is not resolution. Verify the original task: Check the technical result and obtain user confirmation. Resolve, then close under policy: If it recurs before closure, return to investigation. After closure, link a new incident. [Open full-size](incident-lifecycle.svg).

## Approval before fulfillment

![Proposed catalog flow; actual record links untested. Request and requested item: Record requested-for, scope, justification and due date. Authorized approval: Reject or request clarification if approval is missing. Scoped fulfillment task: Implement only approved access or software. Verify all required tasks: Test allowed and prohibited actions before completion.](request-fulfillment.svg)

Proposed catalog flow; actual record links untested. Request and requested item: Record requested-for, scope, justification and due date. Authorized approval: Reject or request clarification if approval is missing. Scoped fulfillment task: Implement only approved access or software. Verify all required tasks: Test allowed and prohibited actions before completion. [Open full-size](request-fulfillment.svg).

## Record workflow and real repair differ

![All systems below are planned, not configured. ServiceNow learning instance: Ticket state, notes, approval and assignment evidence. Owned endpoint or directory lab: Separate evidence is needed for an actual technical action. Public portfolio: Only reviewed artifacts; scripted notes remain labeled.](lab-boundaries.svg)

All systems below are planned, not configured. ServiceNow learning instance: Ticket state, notes, approval and assignment evidence. Owned endpoint or directory lab: Separate evidence is needed for an actual technical action. Public portfolio: Only reviewed artifacts; scripted notes remain labeled. [Open full-size](lab-boundaries.svg).

## VPN connected: what to check next

![Scripted diagnostic decisions; no live VPN test. Check name resolution: If the internal name fails, compare the approved DNS/profile settings. If DNS succeeds, check transport: If the approved port fails, inspect the authorized network path. If transport succeeds, check the app: Authentication and the user’s original task still need testing. Route with evidence; verify recovery: Hand off the failed layer, observations and next action.](vpn-decision-tree.svg)

Scripted diagnostic decisions; no live VPN test. Check name resolution: If the internal name fails, compare the approved DNS/profile settings. If DNS succeeds, check transport: If the approved port fails, inspect the authorized network path. If transport succeeds, check the app: Authentication and the user’s original task still need testing. Route with evidence; verify recovery: Hand off the failed layer, observations and next action. [Open full-size](vpn-decision-tree.svg).
