# MFA access recovery after a phone replacement

**LAB-REQ-004 · Optional extension · Catalog request / restricted identity recovery**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Jamie Park, fictional employee |
| Service | Workforce authentication recovery |
| Assignment | Service Desk L1 → Identity Support |
| Classification | Catalog request / restricted identity recovery |
| Impact / urgency | N/A / N/A |
| Priority / commitment | Identity recovery routing; reassess service impact |

**User report:** “I replaced my phone and cannot use my normal MFA method. Please change my number so I can sign in.”

**Classification:** A recovery request manages the approved identity procedure. It is distinct from simply enrolling a factor while authenticated. New-factor enrollment is a sensitive change.

**Priority reasoning:** The recovery workflow uses restricted verification and authorization under this lab policy. If the underlying sign-in interruption requires an incident, link that incident rather than bypass recovery controls.

## Identity, consent and authorization

Use the established recovery policy and pre-enrolled verification routes. A caller-provided phone number or manager email alone is insufficient under this exercise. Identity Support performs recovery within its delegated role. Never disclose codes in ticket notes or disable MFA to make the case easy.

## Questions that change the next step

- Is an approved alternate enrolled method available?
- Can the established recovery verification be completed?
- Was the old device lost/stolen, or are unexpected authentication prompts occurring?

## Diagnostic and fulfillment decisions

### 1. Check an approved alternate method

**Expected observation / interpretation:** If available, the user follows the official recovery/enrollment path themselves.

**Boundary / stop rule:** Do not solicit an OTP from the user.

### 2. Verify identity independently of the new contact detail

**Expected observation / interpretation:** Scripted approved verification must pass before Identity Support changes any method.

**Boundary / stop rule:** If verification fails, leave authentication methods unchanged.

### 3. Hand off scoped authorized recovery

**Expected observation / interpretation:** Identity Support follows the lab's documented procedure and records only the action/result.

**Boundary / stop rule:** Temporary access methods, if ever used, require actual tenant support and authorized policy; none is assumed here.

### 4. Confirm normal sign-in and method cleanup

**Expected observation / interpretation:** User verifies new enrollment; the old method is reviewed/revoked by the authorized role as appropriate.

**Boundary / stop rule:** A ticket marked complete is not proof of safe recovery or removal of a lost method.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Intake: phone replacement prevents normal factor use. New phone detail is unverified; no method changes performed by L1.

**Note 2:** Recovery handoff: approved verification outcome and scope provided to Identity Support without secrets. If device was lost or suspicious prompts exist, security exposure is escalated.

**Note 3:** Expected verification: authorized method change, successful user authentication and appropriate old-method disposition; no MFA bypass or broad admin assignment.

## Sample customer-visible comments

**Message 1:** I’ll help route the recovery request. We must complete the established identity checks before changing authentication methods; please do not send codes or recovery secrets.

**Message 2:** The request is with Identity Support for the approved recovery process. I’ll update you within 30 minutes; the new contact detail is not being treated as proof of identity.

**Message 3:** Expected completion message: The approved identity role completed recovery and you verified normal sign-in. The previous method was reviewed under the recovery policy.

## Failure, denial or changed-condition branch

Verification cannot be completed: no factor reset, new method, temporary access or MFA disablement. Route to the approved exception process. Evidence of theft or suspicious prompts triggers security escalation and an updated exposure assessment.

## Required restoration / fulfillment verification

- [ ] Independent approved verification passes without relying solely on new contact details.
- [ ] Only the authorized identity role performs the scoped recovery.
- [ ] User authenticates normally and previous-method disposition is documented.
- [ ] Failed verification results in zero authentication-method changes.

## Expected final record treatment

Expected: restricted recovery request remains pending until verified/authorized; fulfill only after the normal sign-in check. Link any associated interruption/security record under the actual process.

## Evidence to capture after execution

- Restricted verification outcome
- Identity-role action with no secret material
- User sign-in and old-method disposition
- Failed-verification negative test

**Current limitation:** No Microsoft Entra tenant, MFA change or recovery action has been performed. This extension is a procedure design.

[Return to scenario catalog](../docs/scenario-catalog.md)
