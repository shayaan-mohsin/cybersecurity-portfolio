# Organization Profile

## Fictional Organization

**CareBridge Health Services** is a fictional small healthcare services organization used for portfolio analysis. It provides non-emergency patient scheduling, benefits coordination support, billing support, and document intake for regional care providers.

This profile is fictional. It does not describe a real organization, patient population, employer, or client.

## Business Context

| Area | Portfolio scenario |
|---|---|
| Approximate size | 45 employees |
| Operating model | Hybrid administrative workforce with one small office and remote staff |
| Primary users | Scheduling coordinators, billing support staff, intake specialists, managers, IT support, vendor support |
| Sensitive data | Patient contact details, appointment information, insurance details, billing support documentation, employee account data |
| Business priorities | Patient trust, service continuity, accurate documentation, vendor accountability, basic compliance readiness |
| Security maturity | Developing; informal practices exist, but governance and documentation are inconsistent |

## Core Workflows

| Workflow | Description | Security relevance |
|---|---|---|
| Patient scheduling | Staff coordinate appointments and update patient contact information | Requires access control, data handling expectations, and account monitoring |
| Billing support | Staff process billing-related documentation and insurance support information | Involves sensitive financial and healthcare-related data |
| Document intake | Staff receive, upload, and route documents through cloud storage | Requires storage ownership, sharing rules, and retention expectations |
| Vendor support | Third-party vendors help with scheduling, billing, and IT tools | Requires vendor access review and least-privilege expectations |
| Incident escalation | Managers handle disruptions, suspicious emails, and account issues | Requires clear reporting paths and response documentation |

## Sample Asset Inventory

| Asset / system | Business owner | Data handled | Current-state assumption |
|---|---|---|---|
| Scheduling SaaS | Operations Manager | Patient contact and appointment information | MFA enabled for managers, inconsistent for staff |
| Billing support portal | Billing Lead | Billing support and insurance documentation | Vendor support accounts reviewed informally |
| Cloud document storage | Office Manager | Intake forms and internal documentation | Shared folders exist, but ownership is unclear |
| Email and collaboration suite | IT Support / Office Manager | Internal communications and attachments | Phishing reporting process is informal |
| Employee laptops | IT Support | Local work files and browser sessions | Asset inventory is incomplete |
| Vendor remote support | IT Support | Administrative access to selected systems | No formal quarterly access review |

## Security Assumptions

- The organization has basic security controls, but they are not consistently documented.
- MFA exists for some accounts but has not been verified across all users and vendors.
- Asset ownership is known informally by managers but not tracked in a central inventory.
- Incident response depends on ad hoc escalation rather than a written playbook.
- Vendor access is business-critical but not governed through a formal review cycle.

## Why This Scenario Fits The Portfolio

CareBridge creates a realistic GRC/risk scenario without exposing private data. It allows the assessment to show governance, risk prioritization, privacy awareness, third-party risk thinking, and executive communication.
