# User reports a suspicious sign-in email

**LAB-INC-005 · Core scenario · Support incident / security handoff**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Drew Kim, fictional employee |
| Service | Employee security reporting |
| Assignment | Service Desk L1 → Security Operations |
| Classification | Support incident / security handoff |
| Impact / urgency | Low, provisional / High |
| Priority / commitment | P3 under support matrix; immediate security escalation |

**User report:** “I received an email saying my account will be disabled unless I sign in. I clicked the link but did not enter a password.”

**Classification:** A reported suspicious message starts a desk record and is handed into the security reporting process. A licensed ServiceNow Security Incident Response app is not assumed; a documented restricted handoff is sufficient.

**Priority reasoning:** Known scope is one user, but security urgency requires immediate SOC routing regardless of the support priority. New credential-entry or endpoint evidence may change scope and handling.

## Identity, consent and authorization

Verify reporter via an established channel. Do not browse the URL, open attachments, send the message to an unrelated account or collect passwords. Use inert sample text and reserved example-domain indicators. Preserve only the evidence the lab procedure authorizes.

## Questions that change the next step

- Did you open the message, click, enter credentials, approve an MFA prompt or download/run anything?
- What device and approximate time/timezone were involved?
- How was the message reported, and are others reporting it?

## Diagnostic and fulfillment decisions

### 1. Capture reporter actions and timing

**Expected observation / interpretation:** Scripted report says a click without credential entry or download; unknown facts stay unknown.

**Boundary / stop rule:** Do not declare safe merely because the user denies password entry.

### 2. Preserve evidence through the approved channel

**Expected observation / interpretation:** SOC packet references an inert message artifact and necessary headers/indicators in a restricted lab store.

**Boundary / stop rule:** Broad ticket comments must not contain raw sensitive mailbox data or clickable suspect links.

### 3. Route to Security Operations immediately

**Expected observation / interpretation:** The desk supplies who/what/when, affected device, reporter action, source artifact reference and outstanding questions.

**Boundary / stop rule:** SOC directs containment and identity remediation; L1 does not independently disable accounts or wipe devices.

### 4. Maintain the user update and ownership

**Expected observation / interpretation:** Expected handoff acceptance and next action are recorded; the desk remains responsible for communication until transfer is confirmed.

**Boundary / stop rule:** Assignment alone is not accepted transfer or security containment.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Intake: suspicious account-disable message reported. User states link clicked, no credentials entered/download. Facts are self-reported; scope is provisional. Immediate security escalation initiated.

**Note 2:** Handoff packet: fictional reporter/device, relative event time plus actual timezone when executed, reported interaction, inert evidence reference, checks completed and unresolved exposure questions.

**Note 3:** Ownership: receiving security role must confirm acceptance in the exercise. Desk tracks the next update; containment/outcome remains pending unless the security role supplies corroborating evidence.

## Sample customer-visible comments

**Message 1:** Thank you for reporting it. Do not interact with the message or link again. I’m escalating it through our security process now; I’ll update you within 15 minutes.

**Message 2:** The security team needs the approximate time and whether any sign-in details, MFA prompts or downloads were involved. Please do not send passwords or authentication codes.

**Message 3:** Expected handoff message: The security role has accepted the report in the lab exercise. Follow the approved instructions they provide; we’ll keep the support record linked to the follow-up.

## Failure, denial or changed-condition branch

User later admits credential entry or MFA approval: update the facts immediately and escalate the changed exposure to SOC/Identity. Do not continue the original low-exposure assumption. If security acceptance is delayed, follow the escalation chain and keep the user informed.

## Required restoration / fulfillment verification

- [ ] Handoff includes exposure details, device, time/timezone, artifact reference and pending questions.
- [ ] The receiving role explicitly accepts or the pending state/escalation remains visible.
- [ ] The desk does not claim containment, clean endpoint or harmless link without evidence.
- [ ] No live malicious URLs, secret values or unrelated mailbox content are published.

## Expected final record treatment

Expected: support record remains active through pending handoff. Closure is coordinated with the security process and the support user's needs; reassignment is not resolution.

## Evidence to capture after execution

- Inert message artifact / source reference
- Structured escalation packet
- Role-play acceptance or pending escalation
- User communication and limitations

**Current limitation:** All security evidence is inert and synthetic. No email tenant, live phishing assessment, containment action or SOC investigation has been performed.

[Return to scenario catalog](../docs/scenario-catalog.md)
