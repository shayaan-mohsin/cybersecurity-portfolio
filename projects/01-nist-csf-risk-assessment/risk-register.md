# Hypothetical healthcare risk register

[Project overview](README.md) · [Control mapping](csf-mapping.md)

These are discussion hypotheses for a fictional healthcare organization. Public reports do not verify any organization’s controls. Priority is an initial review order, not a calculated likelihood or loss estimate.

| ID / review order | Hypothesis and why it matters | Evidence needed | Owner to consult | Proposed response if confirmed |
| --- | --- | --- | --- | --- |
| H1 / first | Sensitive servers may have access or recovery gaps; disruption could affect care delivery | Inventory, privileged access, logging coverage, restore tests | Infrastructure and clinical service owners | Address verified access gaps and test service restoration |
| H2 / first | Mail access or account recovery may expose sensitive information | Identity logs, recovery procedure, mail audit coverage, access reviews | Identity and messaging owners | Improve verified recovery and investigate risky changes |
| H3 / next | Third-party data flows may lack clear responsibilities | Contracts, data-flow inventory, incident contacts, assurance evidence | Vendor risk and service owners | Resolve documented ownership and monitoring gaps |
| H4 / next | Data may persist outside approved storage | Data inventory, handling procedures, retention and disposal evidence | Privacy and business owners | Correct verified handling exceptions and validate disposal |
| H5 / next | Incident roles or communications may be unclear | Response plan, contact validation, exercise records | Security and operational leaders | Exercise an agreed scenario and track observed gaps |

Closing an item requires accepted evidence and an owner’s decision. Publishing this table closes none of these hypothetical risks.
