# Outlook desktop keeps asking for sign-in

**LAB-INC-002 · Core scenario · Incident**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Morgan Reed, fictional analyst |
| Service | Employee email |
| Assignment | Service Desk L1 → Messaging Support role-play |
| Classification | Incident |
| Impact / urgency | Low / Medium |
| Priority / commitment | P4 |

**User report:** “Outlook keeps asking me to log in. I can use email in the browser, but the desktop app will not sync.”

**Classification:** Existing mail functionality is degraded. The browser workaround restores some productivity but does not by itself fix desktop synchronization.

**Priority reasoning:** One desktop client is impaired and browser email is a viable workaround. The symptom does not establish a tenant outage.

## Identity, consent and authorization

Verify the user through the established support channel and obtain consent before viewing their screen. Keep mailbox content out of attachments. Ask the user to enter credentials themselves in the official sign-in flow.

## Questions that change the next step

- What client/version and error are shown? When did it last work?
- Does a controlled browser sign-in and test send/receive work?
- Did the password, device, network or app configuration change? Are others affected?

## Diagnostic and fulfillment decisions

### 1. Check scope and official service health if authorized

**Expected observation / interpretation:** Browser send/receive succeeds in the scripted input; no wider issue is given.

**Boundary / stop rule:** Access to tenant health requires the proper role. Lack of visibility is a limitation, not a healthy-service finding.

### 2. Check client clock, network and supported updates

**Expected observation / interpretation:** The scripted device has a supported client and normal clock; the error is limited to desktop sign-in.

**Boundary / stop rule:** Record the actual build when testing. Windows 10 mentions in postings do not make an unsupported installation acceptable.

### 3. Use the approved client sign-out / sign-in procedure

**Expected observation / interpretation:** A stale desktop session is the scripted hypothesis; a bounded re-authentication restores the client in the expected path.

**Boundary / stop rule:** Follow the applicable client version. Do not erase an Outlook profile, PST, cached mailbox or all Windows credentials as a first step.

### 4. Validate end-to-end mail behavior

**Expected observation / interpretation:** A controlled test message sends and arrives; restart the app and check synchronization again.

**Boundary / stop rule:** TCP connectivity or a dismissed prompt is not proof of mail flow. Avoid sending test email to unrelated people.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Intake: desktop Outlook cannot sync; webmail workaround reported. One user, Low impact / Medium urgency / P4. Captured client error with mailbox content excluded.

**Note 2:** Investigation: scripted browser send/receive succeeds. Desktop session hypothesis remains provisional; service health and actual build require authorized lab checks.

**Note 3:** Expected action: approved re-authentication, then controlled send/receive and application restart. Profile deletion is outside the first-line path.

## Sample customer-visible comments

**Message 1:** Please use browser email while I check the desktop app. I’ll avoid changes that could remove your local mail data and update you within 30 minutes.

**Message 2:** The symptom appears specific to the desktop sign-in session in this exercise. You’ll enter your credentials yourself during the approved sign-in step.

**Message 3:** Expected closure message: The desktop client sent and received the controlled test and stayed connected after restart. If the prompt returns, we’ll continue the investigation.

## Failure, denial or changed-condition branch

Browser sign-in also fails or additional users report the same issue: reassess scope and priority; do not keep treating it as one desktop profile. If the first attempt fails, retain the error/build evidence and escalate rather than repeating destructive resets.

## Required restoration / fulfillment verification

- [ ] Record an actual supported client build and the precise error if a licensed test tenant is available.
- [ ] Controlled send and receive both succeed, with no unrelated mailbox content captured.
- [ ] Client restart and user confirmation show the symptom has cleared; note any remaining limitation.

## Expected final record treatment

Expected: New → In Progress → Resolved after client verification. Use a legitimate On Hold / Awaiting Caller path only when necessary information is requested.

## Evidence to capture after execution

- Error without mailbox content
- Client version and scoped diagnostic notes
- Controlled test result
- User-visible workaround and verification message

**Current limitation:** No Microsoft 365 tenant or Outlook license is provisioned; all client/service outcomes currently remain scripted.

[Return to scenario catalog](../docs/scenario-catalog.md)
