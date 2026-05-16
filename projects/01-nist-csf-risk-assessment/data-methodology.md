# Data Methodology

## Research Question

Which cybersecurity risks should a small or modest-maturity healthcare organization prioritize based on recent public healthcare breach reporting patterns?

## Data Sources

| Source | Use in this report |
|---|---|
| HHS OCR Breach Portal | Primary public breach record source for reported breaches affecting 500 or more individuals. |
| HHS HC3 healthcare threat guidance | Sector context for healthcare threats, ransomware, phishing, cloud risk, and security response practices. |
| HHS Ransomware and HIPAA Fact Sheet | Healthcare-specific context for malware prevention, incident response, backups, and breach risk assessment. |
| NIST CSF 2.0 | Framework for organizing governance, identification, protection, detection, response, and recovery recommendations. |
| NIST SP 1300 | Practical CSF 2.0 quick-start guidance for small and medium-sized organizations. |

## Collection Method

Collection date: May 16, 2026.

The HHS OCR Breach Portal was opened through the public "View HIPAA Breach Reports" workflow. The portal displayed 710 HIPAA breach records at the time of collection. The first page of results was configured to display 100 records and was saved as a dated sample extract.

The resulting sample is stored at:

[`data/hhs-ocr-breach-sample-2026-05-16.csv`](data/hhs-ocr-breach-sample-2026-05-16.csv)

## Fields Used

| Field | Analytical use |
|---|---|
| covered_entity | Preserved for source traceability; not used to single out organizations in the findings. |
| state | Used to understand geographic spread at a high level. |
| covered_entity_type | Used to compare healthcare provider, health plan, and business associate patterns. |
| individuals_affected | Used to understand impact scale. |
| breach_submission_date | Used to define the collection window. |
| type_of_breach | Used to identify recurring incident categories. |
| location_of_breached_information | Used to infer common technology and workflow exposure points. |
| business_associate_present | Used to evaluate third-party risk relevance. |

## Sample Summary

| Metric | Value |
|---|---:|
| Public records displayed by portal at collection | 710 |
| Records included in dated sample | 100 |
| Sample date range | February 9, 2026 to May 1, 2026 |
| Total affected individuals in sampled records | 6,692,288 |
| Largest single sampled record by affected individuals | 3,117,874 |
| Median affected individuals in sampled records | 5,073 |

## Limitations

The sample is a point-in-time extract of the first 100 records displayed by the public portal, not a longitudinal study of every reported healthcare breach. The portal fields provide useful indicators, but they do not describe root cause, control maturity, incident timeline, or full investigative detail.

The recommendations in this report are analyst interpretations based on public breach patterns and public frameworks. They should be validated against an organization's own assets, workflows, threat model, budget, and regulatory obligations before implementation.
