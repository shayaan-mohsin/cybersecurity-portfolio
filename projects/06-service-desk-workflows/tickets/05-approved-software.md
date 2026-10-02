# Request for an approved PDF application

**LAB-REQ-001 · Core scenario · Catalog request**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Casey Lane, fictional employee |
| Service | Approved software catalog |
| Assignment | Service Desk L1 / Software Fulfillment |
| Classification | Catalog request |
| Impact / urgency | N/A / N/A |
| Priority / commitment | Fulfillment due date |

**User report:** “I need the approved PDF editor for a new assignment. Can someone install it by Friday?”

**Classification:** Catalog request: a functioning device needs an additional authorized application. Proposed hierarchy: REQ → one software RITM → fulfillment task after approval.

**Priority reasoning:** A new capability is requested; use approvals and an agreed fulfillment date rather than an incident restoration SLA.

## Identity, consent and authorization

Confirm requested-for, business need, approved package, supported endpoint and license availability. Use separate fictional manager/license-owner approval. The user's request does not authorize local admin rights or an unapproved download.

## Questions that change the next step

- What capability and deadline are needed? Is the approved viewer enough?
- Which lab device will receive the application? Is it supported?
- Who approves cost/license allocation, and is a seat available?

## Diagnostic and fulfillment decisions

### 1. Select the approved catalog item

**Expected observation / interpretation:** Scripted need requires the editor, not merely a viewer; due date is recorded.

**Boundary / stop rule:** Do not turn the request into an incident to jump the queue.

### 2. Request and record authorization

**Expected observation / interpretation:** Manager and license-owner decisions must precede fulfillment under this lab design.

**Boundary / stop rule:** Approvals are recorded decisions from separate role-play accounts; no approval is assumed.

### 3. Deploy an approved test package if available

**Expected observation / interpretation:** A managed, licensed lab package is installed under the delegated fulfillment method.

**Boundary / stop rule:** No ad hoc local admin membership, cracked software, or real purchasing.

### 4. Verify entitlement and function

**Expected observation / interpretation:** Check approved version, assigned license and a harmless open/edit/save workflow.

**Boundary / stop rule:** A completed task is insufficient if the application or entitlement does not work.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Request intake: PDF editing needed for an assignment; requested-for and device identified. Proposed catalog item selected, due date recorded; approval pending.

**Note 2:** Approval path: manager/license-owner decision must be captured before a fulfillment task can proceed. If unavailable, communicate the dependency and new estimate.

**Note 3:** Expected fulfillment: approved package and entitlement checked on the lab endpoint; functional test and user confirmation recorded before required tasks are Closed Complete.

## Sample customer-visible comments

**Message 1:** I’ve recorded the PDF editor request and Friday deadline. We’ll confirm approval and a license before installation; I’ll provide an estimate after those checks.

**Message 2:** The request is awaiting the required approval/license decision. I’ll update you by the next business day even if that dependency is still pending.

**Message 3:** Expected fulfillment message: The approved application and license passed the controlled edit/save test. Please confirm that it meets the requested need.

## Failure, denial or changed-condition branch

Approval rejected or no licensed seat available: do not install. Record rejection or a pending dependency with a user update. Any alternative package must follow the same catalog authorization. A withdrawn request must not report fulfilled.

## Required restoration / fulfillment verification

- [ ] Catalog submission generates actual related records when implemented.
- [ ] A rejected test produces no provisioning action; approval identity and scope are captured.
- [ ] Approved package/version, entitlement and functional test pass; unrelated admin privileges remain absent.

## Expected final record treatment

Expected: request submitted → approval → fulfillment task → verified completion. Use actual catalog states/flow roll-up; do not label a rejected request Resolved.

## Evidence to capture after execution

- Catalog variables and actual related record numbers
- Manager/license-owner decision
- Package/version/entitlement check
- Functional verification and request outcome

**Current limitation:** No license, software purchase or installation has occurred. The flow and package outcome are proposed.

[Return to scenario catalog](../docs/scenario-catalog.md)
