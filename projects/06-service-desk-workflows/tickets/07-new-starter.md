# New starter account and device coordination

**LAB-REQ-003 · Core scenario · Catalog request**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Alex Rivera, fictional hire; requested by fictional manager Sam Patel |
| Service | New Starter Pack |
| Assignment | Service Desk L1 / Identity and Endpoint fulfillment |
| Classification | Catalog request |
| Impact / urgency | N/A / N/A |
| Priority / commitment | Approved start-date commitment |

**User report:** “Alex starts Monday. Please prepare the standard account and laptop for the approved role.”

**Classification:** One proposed starter-pack RITM under a REQ, with separate account and device tasks. The flow must track both dependencies and roll up honestly.

**Priority reasoning:** Planned fulfillment should be managed against its start-date dependency; a future date does not automatically create a P1 incident.

## Identity, consent and authorization

Use the approved fictional HR roster and manager-confirmed role/start date. Verify requester vs requested-for. Provision only standard role entitlements with the appropriate team. Share initial access through an approved channel, never in ticket comments.

## Questions that change the next step

- Is the hire/start date approved in the authoritative lab roster?
- What standard role bundle, location and device are approved?
- Who completes identity setup, equipment and the user acceptance check?

## Diagnostic and fulfillment decisions

### 1. Validate source and scope

**Expected observation / interpretation:** Scripted roster and manager agree on the employee role and date.

**Boundary / stop rule:** An email from an unknown requester is not authority to create an account.

### 2. Generate separate fulfillment tasks

**Expected observation / interpretation:** Account task goes to Identity; device preparation task goes to Endpoint.

**Boundary / stop rule:** Record role-play actors. A single checked box must not conceal unfinished work.

### 3. Coordinate identity and endpoint prerequisites

**Expected observation / interpretation:** Standard groups, supported test image/updates, device assignment and approved enrollment are planned.

**Boundary / stop rule:** Do not imply Intune enrollment or imaging occurred unless actually observed in a licensed test lab.

### 4. Perform starter acceptance

**Expected observation / interpretation:** Test standard sign-in, required application and device readiness; verify absence of admin privilege.

**Boundary / stop rule:** HR/manager approval is not a substitute for readiness tests.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Request intake: Sam requests the approved starter pack for Alex. Fictional roster confirms role/date; request-for differs from requester.

**Note 2:** Task coordination: account task and device task have distinct owners. If the account is ready but the device is delayed, keep the item pending and communicate the blocker.

**Note 3:** Expected acceptance: standard account/device checks complete and user/manager acknowledgement captured. No password or recovery material included in the record.

## Sample customer-visible comments

**Message 1:** I’ve recorded the starter request and approved start date. We’ll track account and device preparation separately and provide a readiness update before the start date.

**Message 2:** The account task is ready in the scripted path, but device preparation is still pending. The starter request remains incomplete; I’ll communicate the revised readiness estimate.

**Message 3:** Expected fulfillment message: Both required tasks passed the readiness checks, and the approved recipient confirmed receipt through the agreed process.

## Failure, denial or changed-condition branch

HR approval absent or date/role inconsistent: hold provisioning for clarification. One task incomplete: do not close the RITM as fulfilled. A changed start date or withdrawal requires the responsible teams to review pending provisioning and revoke unnecessary test access.

## Required restoration / fulfillment verification

- [ ] Roster/manager decision identifies the same fictional hire and role.
- [ ] Actual task relationships and different assigned groups are visible when implemented.
- [ ] All required readiness tests pass and no excess privilege is present.
- [ ] A deliberately incomplete task prevents a false fulfilled outcome.

## Expected final record treatment

Expected: request approved → multiple tasks → all required tasks verified → item/parent roll-up per configured flow. Test both partial completion and cancellation.

## Evidence to capture after execution

- Authoritative fictional roster confirmation
- REQ/RITM/task relationship captures
- Identity and endpoint checks with execution labels
- Partial-completion and acceptance outcomes

**Current limitation:** This case is a coordination design; no HR integration, device imaging, shipment or Intune enrollment has occurred.

[Return to scenario catalog](../docs/scenario-catalog.md)
