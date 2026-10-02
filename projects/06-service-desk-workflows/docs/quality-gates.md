# Implementation quality gates

All gates below are pending. Draft-file verification is distinct from execution verification.

| Gate | Positive test | Required negative / changed-condition test |
| --- | --- | --- |
| Identity | Approved check and delegated action | Failed check leaves the account/method unchanged |
| Incident classification | Existing interruption recorded as incident | New entitlement follows request approval |
| Priority | Scope, deadline and workaround support the matrix | A second user changes scope; VIP alone does not force P1 |
| Authorization | Exact user/resource/privilege approved | Rejection produces no provisioning |
| Catalog relationships | Submission produces required item/tasks | Incomplete task prevents false fulfilled roll-up |
| Troubleshooting | Each test supports a specific inference | Working transport with failed app does not count as resolved |
| Notes / visibility | Internal note and user message serve their audiences | Caller account cannot see restricted evidence under tested access |
| Escalation | Receiving role accepts and next step is named | Pending acceptance does not count as transfer complete |
| Restoration | End-to-end test and user outcome recorded | Recurrence reopens investigation with history retained |
| SLA | Actual definition attaches and follows schedule | Non-pause hold, cancel, priority change and reopen checked |
| Evidence | Actual numbers, times, roles, hashes and limitations | Mock screenshots and scripted outputs never enter actual evidence |
| Presentation | README → case → evidence is navigable | Mobile layout and long diagram/code views remain usable |

Prioritize the first eight core scenarios. The SLA gate and extension-specific capabilities can remain outside the completion scope if honestly documented. Do not claim the whole acceptance matrix passed from a local HTML preview.
