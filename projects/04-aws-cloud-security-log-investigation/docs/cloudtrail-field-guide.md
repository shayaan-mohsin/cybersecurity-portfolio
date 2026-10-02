# Field guide for this analyzer

[Project overview](../README.md) · [Signal catalog](../detections/cloudtrail-detection-catalog.md)

| Field | Use | Caution |
| --- | --- | --- |
| eventTime | Place the event in time | A timestamp alone does not prove causation |
| eventID | Deduplicate with account and Region | The supplied fixture omits it; exact-payload hashing is the fallback |
| eventSource and eventName | Identify a supported service/action pair | A matching name from another service should not trigger that action’s rule |
| userIdentity | Preserve actor and full session ARN | An account label is not proof of the person behind it |
| requestParameters | Inspect rule, policy, or setting details | A request does not by itself prove final state |
| errorCode | Identify failed or denied actions first | Its absence is not proof of authorization or maliciousness |
| responseElements.ConsoleLogin | Distinguish failed sign-in | Do not infer compromise from a failure |
| sourceIPAddress | Add network context | NAT, VPNs, and shared networks weaken attribution |

CloudTrail management events describe control-plane actions. This fixture does not establish data-plane access such as S3 object reads.
