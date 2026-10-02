# Account locked before a scheduled meeting

**LAB-INC-001 · Core scenario · Incident**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Avery Chen, fictional coordinator |
| Service | Workforce sign-in |
| Assignment | Service Desk L1 → Identity Support when required |
| Classification | Incident |
| Impact / urgency | Low / High |
| Priority / commitment | P3 |

**User report:** “I cannot sign in to my work laptop. It says my account is locked. I have a meeting in 40 minutes.”

**Classification:** An existing account unexpectedly stopped working; restoration is an incident under the lab policy. A routine reset requested while access works would follow the catalog process.

**Priority reasoning:** One user cannot use an existing service and has a time-sensitive meeting without a confirmed workaround. No evidence of a wider outage.

## Identity, consent and authorization

Use the lab's approved callback to a pre-enrolled directory number plus an approved second verification step. If this cannot be completed, keep the account unchanged and route to Identity Support. Never request the password, an OTP, or a recovery code in the ticket.

## Questions that change the next step

- What exact sign-in message appears, and when did it start?
- Does web sign-in fail too? Did the password recently change?
- Are repeated MFA prompts, unfamiliar sign-ins or another affected user present?

## Diagnostic and fulfillment decisions

### 1. Confirm service health and scope

**Expected observation / interpretation:** No widespread failure in the scripted input; continue with a single account hypothesis.

**Boundary / stop rule:** A security signal routes to the security procedure before normal unlock.

### 2. Review authorized account status and recent lockout metadata

**Expected observation / interpretation:** The scripted account is locked; unlock authority must be delegated to the acting role.

**Boundary / stop rule:** A ServiceNow ticket does not prove directory access. If a directory lab is absent, label the account result simulated.

### 3. Correlate recurrence with a controlled test endpoint

**Expected observation / interpretation:** Scripted evidence points to a stale credential in an approved application on LAB-WKS-01.

**Boundary / stop rule:** Do not delete all stored credentials or infer compromise from a lockout alone. Obtain permission for the specific saved entry.

### 4. Apply the narrowly authorized correction and unlock

**Expected observation / interpretation:** Remove/update only the identified lab credential, then unlock under the delegated role.

**Boundary / stop rule:** Do not reset the password unless the policy and findings require it; suspected compromise requires Identity/SOC direction.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Intake: user unable to sign in; one device/account affected. Impact Low, urgency High, computed P3. Identity check pending; no account action taken.

**Note 2:** Investigation: approved identity check completed in the script. Lab account lockout and repeat attempts from LAB-WKS-01 support a stale-credential hypothesis; broad outage not observed.

**Note 3:** Restoration: scoped stale credential corrected and delegated unlock performed in the expected path. User sign-in and normal application access must be verified before Resolved.

## Sample customer-visible comments

**Message 1:** I’ve recorded the sign-in issue and the meeting deadline. I’ll complete our approved identity check before changing the account. I’ll update you within 15 minutes.

**Message 2:** The account appears to be locking again from a saved sign-in on your test laptop. With your permission, we’ll correct that specific entry and test access.

**Message 3:** Expected closure message: Sign-in and the required application now work in the lab check. Please report any repeat lockout; I’ll include the incident reference for follow-up.

## Failure, denial or changed-condition branch

Identity verification fails: do not unlock, do not enroll a new factor, and do not change the verified contact route based on this caller's request. Record the failed verification method without its secret answers; escalate. A recurrence after correction remains In Progress and needs further event correlation.

## Required restoration / fulfillment verification

- [ ] Actual lab sign-in succeeds using the user's own input, without disclosing secrets to the agent.
- [ ] The required application opens and the lockout does not recur during an explicitly recorded observation window.
- [ ] Before/after account state and the acting role are captured; user confirmation is separate from the agent's test.

## Expected final record treatment

Expected: New → In Progress → Resolved after restoration proof; Closed only under the confirmed lab closure rule. An escalation stays open with a named receiving group and next update time.

## Evidence to capture after execution

- Sanitized intake and priority rationale
- Approved identity-check outcome, without answers
- Actual delegated action / directory observation if performed
- Sign-in verification and observation window

**Current limitation:** Directory state and unlock are scripted until an authorized test directory and endpoint exist; a PDI alone cannot substantiate them.

[Return to scenario catalog](../docs/scenario-catalog.md)
