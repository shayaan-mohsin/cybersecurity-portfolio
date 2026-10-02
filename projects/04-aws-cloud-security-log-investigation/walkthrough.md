# Walkthrough: three events, three different conclusions

[Project overview](README.md) · [Input JSON](data/sample-cloudtrail-events.json) · [Generated report](outputs/sample-cloudtrail-investigation-report.md)

All examples below come from the supplied synthetic fixture. Timestamps provide a scripted sequence, not evidence of a real incident.

## 1. A request to stop logging was denied

At 16:32:15Z on September 1, 2026, the fixture records:

```json
{
  "eventSource": "cloudtrail.amazonaws.com",
  "eventName": "StopLogging",
  "errorCode": "AccessDenied"
}
```

The actor is the fictional lab-auditor IAM user. IAM means Identity and Access Management.

The analyzer checks the error before applying the successful-action logic. It emits a Medium “Action denied or failed” signal. It does not emit a successful trail-disruption finding.

**Next checks in a real investigation:** was the request approved, why was it attempted, did related requests succeed, and are the expected trails delivering logs? This one denied event cannot answer those questions.

## 2. A rule permits SSH from a world CIDR

At 16:04:03Z, AuthorizeSecurityGroupIngress requests TCP port 22 from 0.0.0.0/0 and records no API error. A CIDR describes an address range; this one includes all IPv4 addresses. SSH is a remote administration protocol commonly using port 22.

The analyzer pairs the address range with the ports in the **same permission**, rather than combining unrelated rules. It also handles IPv6 world ranges, port ranges, and all-protocol permissions.

**Conclusion:** a High review signal for the rule request. Effective internet reachability still depends on attached resources, routes, public addresses, listeners, and other controls. The proposed lab’s group is detached.

## 3. A later removal request does not close the issue

At 16:06:59Z, RevokeSecurityGroupIngress refers to the same group. The fixture omits the specific revoked permissions. The analyzer emits an Informational follow-up signal.

It cannot prove that the earlier risky rule was removed. A real closure would require exact rule identifiers, current group state, affected asset checks, and validation of the authorized change.

## Why there are 10 signals from 12 events

The analyzer emits signals for defined review conditions, not for every row. GuardDuty sample-finding creation and CloudFormation UpdateStack have no matching signal rule. A future event could produce more than one signal, such as root activity combined with another relevant condition.

The supplied fixture has no provider event IDs and combines Regions. Identical payloads are deduplicated as a fallback; distinct events are not merged merely because actor and time match. Actor output preserves full session ARNs when supplied.

[Field guide](docs/cloudtrail-field-guide.md) · [Investigation playbook](docs/investigation-playbook.md)
