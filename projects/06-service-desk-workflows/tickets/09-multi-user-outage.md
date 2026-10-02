# Multiple callers report a critical application outage

**LAB-INC-006 · Optional extension · Incident / outage coordination**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Several fictional users across two teams |
| Service | Critical scheduling application |
| Assignment | Service Desk L1 → Network/Application support and incident lead |
| Classification | Incident / outage coordination |
| Impact / urgency | High / High |
| Priority / commitment | P1 |

**User report:** “The scheduling application is unavailable for two teams. There is no approved workaround and a time-critical scheduling window is open.”

**Classification:** An outage incident coordinates multiple affected-user reports. Parent/related incident linkage and major-incident capabilities must be verified in the actual instance.

**Priority reasoning:** The scripted impact is a widespread critical business service with an immediate deadline and no viable workaround. Validate facts before raising priority.

## Identity, consent and authorization

Correlate symptoms, service and timing without assuming every complaint has the same cause. Use the designated incident lead for a major-incident decision. L1 cannot claim authority to declare one merely because priority is P1.

## Questions that change the next step

- Which service, locations and user groups are affected?
- Is there an approved workaround or critical deadline?
- Do the symptom and start time align across reports?

## Diagnostic and fulfillment decisions

### 1. Confirm broad service effect

**Expected observation / interpretation:** Two teams report matching symptoms and a controlled service check fails in the script.

**Boundary / stop rule:** One slow workstation is insufficient for an outage declaration.

### 2. Link reports to a coordinating incident

**Expected observation / interpretation:** Retain each caller's information and associate related records when supported.

**Boundary / stop rule:** Do not cancel every related ticket as a duplicate without preserving communication needs.

### 3. Escalate and issue consistent updates

**Expected observation / interpretation:** Incident lead receives business effect, timing, scope, checks and next action.

**Boundary / stop rule:** Avoid unverified root-cause statements or speculative recovery promises.

### 4. Verify recovery with representatives

**Expected observation / interpretation:** Check the critical workflow with users from both teams after the responsible group acts.

**Boundary / stop rule:** A green status page alone is not proof of user recovery.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Scope confirmed in scripted reports: critical application inaccessible for two teams during a time-sensitive window, no workaround. High impact/High urgency/P1.

**Note 2:** Coordinating incident retains related report references. Lead escalation and next status update recorded; root cause remains unknown.

**Note 3:** Expected recovery: responsible team action documented; representative users complete a controlled scheduling task. Related records receive the same verified status.

## Sample customer-visible comments

**Message 1:** We’re coordinating reports affecting the scheduling application and have escalated the business impact. The cause is still under investigation. The next update is in 15 minutes.

**Message 2:** The incident lead is coordinating the responsible teams. We’ll share verified progress and any approved workaround rather than guessing a recovery time.

**Message 3:** Expected recovery message: Representative users from both affected teams completed the scheduling check. Please report remaining issues against the incident reference.

## Failure, denial or changed-condition branch

One caller's symptom differs: investigate separately rather than linking by time alone. Restoration only works for one team: keep the broader incident active. An unresolved dependency must remain visible after a workaround.

## Required restoration / fulfillment verification

- [ ] Priority is supported by recorded scope and business effect.
- [ ] Related records preserve caller context and communication.
- [ ] Both teams pass the end-to-end recovery check.
- [ ] Major-incident designation, if used, is made by the authorized role and supported feature.

## Expected final record treatment

Expected: coordinating incident and related reports remain active through restoration and confirmation. Resolve related records according to their individual verified outcomes.

## Evidence to capture after execution

- Scope and impact decision
- Actual relationship fields if supported
- Incident-lead handoff and update sequence
- Representative recovery checks

**Current limitation:** An extension scenario only; no outage, major-incident plugin or multi-team operation has been executed.

[Return to scenario catalog](../docs/scenario-catalog.md)
