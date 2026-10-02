# Proposed decisions and how to test them

[Project overview](README.md) · [Walkthrough](design-walkthrough.md)

| Design question | Proposed control or decision | What it cannot establish alone | Evidence needed |
| --- | --- | --- | --- |
| Can a customer access only their own records? | Object-level application authorization | Authentication does not prove permission for a record | Positive and cross-account negative tests |
| Can privileged changes be traced? | Separate, time-bounded administrative roles | MFA does not eliminate stolen-session risk | Approval, role grant, action logs, expiry and denial tests |
| Can a workload exceed its purpose? | Scoped service identities | A role name does not prove least privilege | Allowed and forbidden API tests, credential lifecycle evidence |
| Is stored data protected? | Defined encryption and key ownership | Encryption does not block an authorized but abusive query | Key policy, access logs, authorized/unauthorized tests |
| Does traffic filtering protect the application? | Web application firewall plus secure application controls | A WAF does not replace authentication or authorization | Rule tests and separate application security tests |
| Can the service recover? | Isolated restoration with dependency checks | A successful backup job does not prove clean restoration | Restore logs, integrity checks, application test, owner acceptance |

These are proposed acceptance criteria. The table contains no completed control tests or measured outcomes.
