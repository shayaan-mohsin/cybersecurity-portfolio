# VPN connects but a team application will not open

**LAB-INC-003 · Core scenario · Incident**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Jordan Ellis, fictional remote employee |
| Service | Remote access to team application |
| Assignment | Service Desk L1 → Network Support |
| Classification | Incident |
| Impact / urgency | Low / Medium |
| Priority / commitment | P4 |

**User report:** “The VPN says connected, but the team app does not load. Normal websites work.”

**Classification:** Access to an existing application is degraded. VPN tunnel establishment alone does not prove DNS, routing, transport or application availability.

**Priority reasoning:** One user is currently known to be affected and an approved browser-based alternate workflow is available in the scenario. Reassess if another user reports the same symptom.

## Identity, consent and authorization

Confirm the caller/device and approved VPN profile. Obtain consent for remote diagnostics. Use only owned or authorized lab hosts. Do not disable the firewall, antivirus, MFA or certificate validation.

## Questions that change the next step

- What application name and exact error? Does another internal service work?
- What changed: location, Wi-Fi, client version or VPN profile?
- Are others affected, and is an approved workaround available?

## Diagnostic and fulfillment decisions

### 1. Check tunnel and local network configuration

**Expected observation / interpretation:** Scripted tunnel is connected; local internet works. Record the actual interface/DNS configuration if testing.

**Boundary / stop rule:** Public browsing is not proof of internal reachability.

### 2. Resolve the owned internal app name

**Expected observation / interpretation:** Resolve-DnsName against the configured lab host fails on the affected profile but succeeds on the known-good profile in the script.

**Boundary / stop rule:** An example-domain placeholder is not a runnable host; do not invent terminal output.

### 3. Test transport only after DNS succeeds

**Expected observation / interpretation:** Test-NetConnection to the owned app on its approved port can narrow transport failure.

**Boundary / stop rule:** TCP success is not authentication or application success; ICMP failure alone does not prove an outage.

### 4. Compare approved profile settings and route to Network Support

**Expected observation / interpretation:** A missing DNS suffix/server in the scripted profile is the candidate cause; request correction through the responsible team.

**Boundary / stop rule:** Do not switch to public DNS for internal names or edit global routes outside L1 authority.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Intake: tunnel reports connected, public web works, one internal application fails. P4 based on known scope and workaround. User update due within 30 minutes.

**Note 2:** Investigation: DNS failure is the scripted discriminating observation; the known-good comparison supports a profile-specific configuration issue. No live diagnostic output exists.

**Note 3:** Handoff: Network Support receives exact symptom, scope, approved profile/version, DNS comparison, checks already attempted and requested next action. Service restoration remains unconfirmed.

## Sample customer-visible comments

**Message 1:** I’ve recorded that the VPN connects but the application does not. Please use the approved alternate workflow while we check the connection path. I’ll update you within 30 minutes.

**Message 2:** The exercise points to an internal name-resolution setting. I’m sending the relevant checks to Network Support; the ticket remains open until application access is verified.

**Message 3:** Expected final message after the receiving team acts: The application opened and its controlled task completed after reconnect. We’ve recorded the corrected profile and your confirmation.

## Failure, denial or changed-condition branch

A second affected user reports the same profile failure: update scope, reconsider impact and coordinate a wider incident. If DNS works but TCP fails, follow the transport branch. If TCP works but app sign-in fails, route to the application/identity owner with that distinction.

## Required restoration / fulfillment verification

- [ ] Actual owned-host DNS resolution succeeds after an authorized correction.
- [ ] Approved-port connectivity succeeds; application authentication and a harmless task are independently tested.
- [ ] User reconnects and confirms access; receiving team's action and actual role are recorded.

## Expected final record treatment

Expected: In Progress during network handoff; do not mark Resolved merely because the ticket was reassigned. Resolve only after end-to-end restoration evidence.

## Evidence to capture after execution

- Sanitized device/profile context
- Actual DNS and transport observations if run
- Structured escalation packet and ownership
- Application-level confirmation

**Current limitation:** No real VPN or internal application has been created. All network findings are hypothetical until tested in owned infrastructure.

[Return to scenario catalog](../docs/scenario-catalog.md)
