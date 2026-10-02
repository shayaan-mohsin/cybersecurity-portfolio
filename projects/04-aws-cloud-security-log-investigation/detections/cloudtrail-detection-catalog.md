# What the analyzer actually checks

[Project overview](../README.md) · [Code](../scripts/analyze_cloudtrail.py) · [Tests](../../../tests/test_analysis.py)

The Python code is the executable logic. The adjacent JSON is a generated **service/action index**, not a rules engine configuration. The analyzer does not load that JSON.

Error handling runs first. A known service/action pair with errorCode produces one Medium failed-action signal and stops further successful-action interpretation for that event.

| Condition after the error check | Review urgency | Limit |
| --- | --- | --- |
| Root identity | High | Intent, approval and authentication context remain unknown |
| Failed console sign-in | Medium | Failure does not establish compromise |
| Access-key creation | High | Ownership, use and business need require review |
| AdministratorAccess attachment | High | Compare effective permissions and authorization |
| Other supported policy change | Medium | Inline policy semantics are not evaluated |
| World CIDR paired with TCP 22/3389, a range containing them, or all protocols | High | Effective reachability is not established |
| Other world-CIDR ingress | Medium | Review actual service and intended exposure |
| Bucket public-access-block deletion | High | Other policy layers may still prevent public access |
| Wildcard Allow bucket policy | Medium | Conditions, actions, resources and block settings affect access |
| All four public-access-block settings true | Informational | Final effective state still needs verification |
| Missing or false block settings | Medium | Incomplete request cannot prove protection |
| Trail stop/delete without an API error | High | Other trails and history may remain available |
| Trail configuration/selectors changed | Medium | A change could improve or reduce visibility |
| Explicit GuardDuty disable/delete | High | Verify actual detector state |
| GuardDuty creation/other update | Informational | No reduction is inferred without evidence |
| Ingress removal or logging start | Informational | A follow-up request does not prove closure |

Bucket ACL analysis, data-event exfiltration detection, anomaly baselining, and automatic response are outside this implementation. Conditions above are narrow review aids, not comprehensive AWS security detection.
