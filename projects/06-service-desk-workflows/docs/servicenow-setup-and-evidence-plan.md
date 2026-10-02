# ServiceNow setup and evidence plan

**Not executed.** These steps specify the future learning lab. They do not create an account, activate a plugin, or connect to any tenant.

## 1. Secure an appropriate learning environment

Use the [ServiceNow Developer Program PDI guide](https://developer.servicenow.com/print_page.do?category=developer-program&identifier=obtaining-a-pdi&module=guide&release=yokohama). Sign in, request an available release, and record what was actually allocated. Availability can involve a waitlist. The guide restricts PDIs to learning and experimentation and describes inactivity reclamation; export legitimate evidence as the work progresses. Do not rely on the PDI as permanent portfolio hosting.

The official documentation sampled for this draft shows the Australia release. The PDI guide link is versioned Yokohama. Neither establishes what release the learner will receive. Capture release/build, date, interface (classic or workspace), installed applications, instance timezone, and agent/caller roles before following version-specific procedures.

Confirm that Incident, Knowledge and the required Service Catalog functionality are available. Request Management workflows, workspace interfaces and optional plugins may vary. Do not promise premium ITSM, hardware asset management, HR Service Delivery or Security Incident Response licensing. The phishing case requires a documented handoff, not a licensed SIR implementation.

## 2. Create a minimal fictional roster

Create a learner administrator for setup, a scoped service-desk fulfiller, two user/caller accounts, one manager approver and one data-owner approver. Create Service Desk L1, Endpoint Support L2, Identity Support, Network Support and Security Operations groups only where supported. Use reserved example-domain identifiers; no real employees.

A learner can switch between synthetic roles to test approvals and visibility. Label that role-play explicitly. Do not leave the agent as admin simply because that makes the screenshot easy. Record the actual least-privilege roles that work; test a restricted action and a caller view.

Create fictional endpoint entries LAB-WKS-01 and LAB-WKS-02 if the CMDB feature is available. Assign each to its fictional owner. Keep CMDB records lightweight and identified as lab data. Creating a CI is not evidence of discovery, inventory accuracy, or management of a real fleet.

## 3. Configure incident records

Use the available Incident module to create a record. Populate the caller, contact channel, short description and business effect; record the service and affected CI only when known. Set category, group, assignee, impact and urgency. Check calculated priority against the lab policy.

Work the activity stream under the scoped agent. Post work notes and user comments separately. Update In Progress, use On Hold only for a legitimate dependency, then return to investigation. At resolution, choose an appropriate actual resolution code and write the restoration test. Screenshot the real state/activity and caller-visible message. Verify configured closure and reopen behavior, rather than assuming a specific menu or label.

Fields vary between interfaces. The [official incident overview guide](https://www.servicenow.com/docs/r/it-service-management/service-operations-workspace/view-update-inc-overview-tab.html) describes priority calculation and resolution information. Use it as the conceptual reference; capture the UI that is actually present.

## 4. Configure catalog requests

Create three deliberately small catalog items: Approved Software, Team Share Access and New Starter Pack. Define requested-for, business justification, scope and due date as appropriate. Do not collect secrets in variables.

Configure approval before fulfillment. Software uses the manager/license-owner decision; share access uses manager plus data owner; onboarding uses the fictional HR-authorized roster. A catalog flow must generate tasks after approval and handle rejection without provisioning. Test with distinct fictional approver and fulfiller actors.

Observe REQ → RITM → SCTASK relationships in the instance and retain actual generated numbers. A catalog item may create one or multiple tasks depending on its configured flow. [Official Request Management architecture](https://www.servicenow.com/docs/r/it-service-management/request-management/request-management-architecture.html).

For onboarding, use one starter-pack item with separate account and device tasks. Demonstrate which task is complete and which is pending; finish the request only when its requirements are met. This is a fictional catalog design, not proof of operating HR or deploying a laptop.

## 5. Establish technical lab options

A PDI alone supports record workflow. To prove technical remediation, add owned, isolated test endpoints and a licensed test directory if available. Keep account unlock, permissions and printing changes within that scope. Use test files and a disposable profile. Snapshot or record the rollback plan before fault injection.

No Microsoft 365 tenant or corporate VPN is assumed. Outlook and VPN cases may remain tabletop diagnostics until the appropriate test services exist. A note that says “web sign-in succeeded” must be marked scripted unless it was actually tested. Do not create trial billing accounts without a separate decision.

Network tests must target owned/authorized services. Example-domain names in the playbooks are placeholders: replace them with configured lab names before running. Do not run diagnostics against arbitrary public systems.

## 6. Implement and test SLAs only after the basic cases work

Create definitions in the available SLA module under the administrator role. Use the lab policy's schedule, timezone and conditions. Document actual settings; a form screenshot alone does not prove attachment.

Run a short controlled test with recorded real timestamps: attach, acknowledge, hold, resume, resolve. Check the task SLA's observed elapsed/business time against the schedule. Test a non-pause hold reason, a canceled incident and a priority change separately. Keep this outside the completion claim if not performed.

## 7. Capture evidence with provenance

Each artifact needs scenario ID, actual record number, actor role, capture time/timezone, execution type, safe filename, description and SHA-256. Execution type is one of: actual ServiceNow workflow, actual endpoint test, scripted input, or explanatory diagram.

Recommended filenames: LAB-INC-001-intake.png; LAB-INC-001-agent-notes.png; LAB-INC-001-user-verification.md. A filename is a plan, not an existing screenshot.

Sanitize instance hostname, credentials, reset/recovery links, notification addresses, tokens, real identity details and unrelated records. Use captures from fictional accounts wherever possible. Recheck the rendered image after redaction. Do not overwrite the original private evidence if you need to retain it securely.

A screenshot of a mocked record belongs under mockups/, never evidence/. The repository preview has an explicit draft banner and makes no ServiceNow execution claim.
