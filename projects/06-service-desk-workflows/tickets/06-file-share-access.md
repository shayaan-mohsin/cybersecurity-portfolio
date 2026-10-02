# Read-only access to a team file share

**LAB-REQ-002 · Core scenario · Catalog request**

> Draft exercise. All reports, observations, actions and messages below are scripted examples or expected outcomes. No ServiceNow or endpoint action has been executed. Scenario IDs are external labels, not actual ServiceNow record numbers.

[Project overview](../README.md) · [Policy](../docs/lab-service-policy.md) · [Evidence status](../docs/evidence-status.md)

## Intake record

| Field | Draft value |
| --- | --- |
| Caller / requested-for | Taylor Quinn, fictional employee |
| Service | Team document share |
| Assignment | Service Desk L1 → Identity Support |
| Classification | Catalog request |
| Impact / urgency | N/A / N/A |
| Priority / commitment | Fulfillment due date |

**User report:** “I joined the project team and need access to its reference documents. I get Access denied.”

**Classification:** Catalog request: grant a new scoped entitlement after manager and data-owner approval. A denial can be expected behavior, not a technical failure.

**Priority reasoning:** The scripted user has never had this entitlement; this is an access request. If previously approved access unexpectedly stopped working, investigate an incident instead.

## Identity, consent and authorization

Verify requested-for against the roster. Obtain manager and data-owner approval for the exact share and read-only role. Check sensitive-data restrictions and existing entitlements. No broad group, domain admin, or Everyone permission is acceptable.

## Questions that change the next step

- Did this access ever work, or is it new? Which exact resource?
- Is read-only sufficient, and for how long is access needed?
- Who owns the data and authorizes this user's business need?

## Diagnostic and fulfillment decisions

### 1. Confirm request vs broken entitlement

**Expected observation / interpretation:** Scripted roster shows new project membership without existing share approval.

**Boundary / stop rule:** Do not treat Access denied as a reason to bypass authorization.

### 2. Capture scoped approvals

**Expected observation / interpretation:** Manager confirms team need; data owner authorizes read-only access to the reference share.

**Boundary / stop rule:** Reject or pause if either approval is missing. Do not reuse another employee's approval.

### 3. Apply the narrowly delegated group change

**Expected observation / interpretation:** Add the fictional account to the appropriate read-only group in an actual directory lab.

**Boundary / stop rule:** ServiceNow is the approval record, not proof of the permission change. Effective access depends on all relevant controls.

### 4. Test permitted and forbidden actions

**Expected observation / interpretation:** Read approved test file; attempt a harmless write/delete and an unrelated share access, which must remain denied.

**Boundary / stop rule:** Use disposable files. Group membership alone is not an effective-permission test.

## Sample internal work notes

These notes show the intended documentation quality. Their statements are scripted; substitute actual results and timestamps after execution.

**Note 1:** Intake: new access needed; existing entitlement not claimed. Request-for/resource/read-only scope recorded. Manager and owner approval pending.

**Note 2:** Authorization: scripted approvals refer to the same user, share and privilege. Proposed delegated group change contains no administrative entitlement.

**Note 3:** Expected verification: approved read succeeds; write/delete and unrelated share remain denied. Record effective-access checks and an access-review/expiry reminder if the lab supports it.

## Sample customer-visible comments

**Message 1:** I’ll route the request to your manager and the share’s data owner. We need their approval for the specific access level before changing permissions.

**Message 2:** The request remains pending until the required decisions are recorded. I’ll update you by the next business day and keep the requested scope visible.

**Message 3:** Expected fulfillment message: Read-only access to the approved reference documents passed the test. Editing and unrelated shares remain restricted.

## Failure, denial or changed-condition branch

Data owner rejects the request: no membership change. Existing access still denied after an approved group change: investigate token refresh, group nesting and resource permissions within delegated scope; do not add a broader group as a shortcut.

## Required restoration / fulfillment verification

- [ ] Manager and owner approve the exact user/resource/privilege.
- [ ] Actual authorized directory change is observed if a directory lab exists.
- [ ] Approved read passes; write/delete and unrelated share tests fail as intended.
- [ ] The request outcome matches the evidence, including rejection or incomplete fulfillment.

## Expected final record treatment

Expected: submitted → approvals → scoped fulfillment → verification → required tasks complete. Retain denial outcomes and actual configured request states.

## Evidence to capture after execution

- Scoped request and both decisions
- Delegated permission-change observation
- Positive and negative effective-access tests
- Completion or rejection message

**Current limitation:** No directory/share has been provisioned. Permission and access-test outcomes are scripted.

[Return to scenario catalog](../docs/scenario-catalog.md)
