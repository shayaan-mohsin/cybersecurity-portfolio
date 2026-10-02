# A stalled print job returns after an apparent recovery

**LAB-INC-004 · Core scenario · Incident**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Riley Brooks, fictional administrator |
| Service | Workplace printing |
| Assignment | Service Desk L1 → Endpoint Support L2 |
| Classification | Incident |
| Impact / urgency | Low / Medium |
| Priority / commitment | P4 |

**User report:** “My print job is stuck. The shared printer works for my teammate, and I need two pages for a meeting.”

**Classification:** An existing printing service is impaired. This scenario deliberately includes recurrence while the incident is Resolved, before closure.

**Priority reasoning:** One user's queue is affected and a different approved printer is a workaround. A shared spooler restart would create a larger impact than the reported symptom.

## Identity, consent and authorization

Confirm device and printer ownership. Obtain consent to cancel only the user's test job. Use a non-sensitive test document. Do not remove other users' jobs or restart a shared server from L1.

## Questions that change the next step

- Which printer/queue and document type? Can a harmless test page print?
- Can a teammate print to the same device? Is the problem local or shared?
- What driver/version and application are involved? Did it recur after a prior attempt?

## Diagnostic and fulfillment decisions

### 1. Separate device, shared queue and local-client scope

**Expected observation / interpretation:** Scripted teammate test succeeds, so start with the affected endpoint.

**Boundary / stop rule:** One successful teammate test narrows scope; it does not prove the device has no intermittent fault.

### 2. Cancel only the identified test job and retry

**Expected observation / interpretation:** A harmless test page and the original application print path both succeed in the first scripted attempt.

**Boundary / stop rule:** Remain In Progress if either check fails. After both checks and user confirmation, record temporary restoration with a defined follow-up window.

### 3. Reopen when the original symptom returns

**Expected observation / interpretation:** The scripted original application stalls again during the Resolved period.

**Boundary / stop rule:** Keep prior evidence; add the recurrence time and attempted job type. Do not conceal the reopen.

### 4. Escalate a controlled driver/application comparison

**Expected observation / interpretation:** L2 compares approved driver versions and an alternate application, then proposes a bounded driver update/rollback.

**Boundary / stop rule:** Changes occur only on the test endpoint with rollback available; no shared-server change is authorized here.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Intake: one endpoint's job is stuck; another user can print. P4. Alternate printer communicated.

**Note 2:** First attempt: scoped job cancellation followed by a harmless page and the original application print task both passed in the scripted path. Expected record temporarily Resolved after user confirmation, with follow-up pending.

**Note 3:** Recurrence: original application failed again before closure. Return to In Progress under the confirmed instance mechanism; retain first attempt and hand off driver/application comparison to L2.

## Sample customer-visible comments

**Message 1:** I’ll check your local print queue first. Please use the approved alternate printer for the meeting; we’ll avoid interrupting other users’ jobs. I’ll update you within 30 minutes.

**Message 2:** The test page and original application task both printed after we removed your stalled test job in this exercise. We will retain a follow-up window because a later recurrence still needs investigation.

**Message 3:** The issue returned, so I’ve reopened the investigation and preserved the first attempt. Endpoint Support will compare the driver and application path; I’ll keep you informed.

## Failure, denial or changed-condition branch

Shared printer tests also fail: stop the local-only path and reassess broader scope. After a recurrence, do not repeatedly clear the queue and count separate fixes. If a driver change cannot be safely reversed, escalate without changing it.

## Required restoration / fulfillment verification

- [ ] Initial recovery includes both the harmless page and original application path before Resolved; later recurrence is documented with actual times when executed.
- [ ] After an authorized L2 change, a harmless test page and the original application path both work.
- [ ] A recorded repeat-test window and user confirmation support restoration; rollback is known.

## Expected final record treatment

Expected: New → In Progress → Resolved → In Progress → Resolved → Closed after the policy window. Validate the actual reopen action. A recurrence after Closed becomes a linked new incident under this lab policy.

## Evidence to capture after execution

- Local vs shared scope test
- First restoration check and recurrence
- Reopened activity / preserved history
- L2 action, rollback and repeated verification

**Current limitation:** Printing and driver behavior are scripted. The first successful page must not be described as an executed fix.

[Return to scenario catalog](../docs/scenario-catalog.md)
