# Executive Brief

## Situation

CareBridge Health Services is a fictional small healthcare services organization that depends on employee accounts, vendor support, SaaS tools, cloud document storage, and sensitive healthcare-related workflows. The assessment used NIST CSF 2.0 as a public reference framework to identify practical improvements in governance, access control, vendor oversight, incident readiness, and recovery.

This is a portfolio case study using fictional data. It is not a formal audit or compliance attestation.

## Key Findings

- Access review practices are inconsistent.
- Vendor access creates risk without strong ownership and periodic review.
- MFA coverage is not consistently verified across users, vendors, and privileged accounts.
- Incident response steps and escalation paths are not clearly documented.
- Asset, SaaS, and cloud folder ownership are not mature enough to support repeatable governance.
- Security monitoring and phishing reporting are informal.

## Business Impact

These gaps can affect patient trust, service continuity, accountability, and compliance readiness. The most urgent issues are not only technical; they are governance and process risks that make it harder for leadership to know who has access, who owns security decisions, and how the organization would respond during a security event.

## Recommendations

| Recommendation | Priority | Value |
|---|---|---|
| Establish quarterly employee and vendor access reviews | High | Reduces stale account, shared access, and privilege risk |
| Validate MFA coverage for email, scheduling, billing, vendor, and privileged accounts | High | Reduces account compromise risk |
| Create vendor access standards and owner assignments | High | Improves third-party accountability |
| Draft an incident response playbook and escalation matrix | High | Improves readiness during security events |
| Build a lightweight asset and SaaS inventory | Medium | Improves visibility, ownership, and prioritization |
| Publish phishing reporting and awareness guidance | Medium | Reduces preventable user-driven risk and improves early reporting |
| Test recovery for one critical workflow | Medium | Improves confidence in continuity planning |

## 30 / 60 / 90 Day Path

| Timeline | Focus |
|---|---|
| 30 days | Assign owners, build inventory, validate MFA, publish phishing reporting instructions |
| 60 days | Complete employee/vendor access reviews, create incident response playbook, review cloud sharing |
| 90 days | Run tabletop exercise, test recovery, formalize awareness guidance, define alert review cadence |

## Conclusion

CareBridge should prioritize governance basics first: ownership, access review, vendor access, MFA validation, incident response readiness, and recovery expectations. These improvements are realistic for a small organization, measurable within one quarter, and aligned with NIST CSF 2.0 functions.
