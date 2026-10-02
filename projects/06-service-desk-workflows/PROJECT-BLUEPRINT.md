# Service desk lab blueprint

[Project overview](README.md) · [Setup plan](docs/servicenow-setup-and-evidence-plan.md)

The fictional Northstar Learning Services lab asks whether a technician can classify a report, prioritize its business effect, work within their authority, communicate clearly, and either verify restoration or transfer ownership with useful evidence.

## Scope

Eight core cases cover account lockout, Outlook sign-in, VPN/DNS, printing recurrence, software requests, file-share access, onboarding, and phishing reporting. Two extensions cover a wider outage and MFA recovery. Six are incidents; four are request scenarios under the fictional policy.

The ServiceNow record system is separate from endpoint, directory, mail, and network systems. The latter need their own authorized test environments before technical outcomes can be claimed.

## Implementation sequence

1. Record the actual instance release, interface, applications, timezone, and roles.
2. Configure fictional callers, an agent, approvers, and queues. Use a scoped agent to test tickets.
3. Execute one incident lifecycle, including user-visible comments, work notes, a handoff, and restoration evidence.
4. Configure an approved catalog flow and verify actual request/item/task relationships and rejected-request behavior.
5. Add endpoint testing only where an isolated, authorized environment exists.
6. Test the fictional priority and SLA policy against actual observed behavior.
7. Capture evidence with provenance and update status one case at a time.

Identity recovery is blocked until the approved verification procedure and agent authority are specified. Scripted verification outcomes can illustrate a tabletop decision but cannot justify a real unlock.

## Definition of completion

A case needs its actual record number, actor role, executed actions, observed result, failure branch, user verification, and outstanding limitations. Platform workflow and technical remediation are recorded separately. No part of this blueprint is marked executed.
