# MITRE ATT&CK Mapping

| ATT&CK area | Example behavior | Defensive takeaway |
|---|---|---|
| Initial Access | Phishing attempts against employees | Improve awareness, reporting, and email security controls |
| Credential Access | Credential harvesting or password reuse | Require MFA and monitor suspicious authentication events |
| Persistence | Continued access through valid accounts | Review sessions, account changes, and unusual access patterns |
| Discovery | Actor explores accessible applications or files | Monitor abnormal access to sensitive repositories or directories |
| Collection | Sensitive files or email content gathered | Limit access and monitor unusual downloads or mailbox activity |
| Exfiltration | Data copied out through cloud or email channels | Review egress controls and alerting for large exports |

## Notes

This mapping is intentionally high-level and portfolio-safe. A production CTI report would include more precise techniques, evidence, telemetry, and confidence levels.
