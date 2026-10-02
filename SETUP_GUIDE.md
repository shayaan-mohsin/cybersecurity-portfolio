# Reproduce the portfolio

[Portfolio home](README.md) · [Evidence boundaries](PUBLISH_STATUS.md)

Use **Python 3.10 or later**. The analysis, SVG generator, and local checks use only the standard library. No cloud account, ServiceNow instance, credentials, or paid service is required.

From the repository root:

```sh
python tools/reproduce.py
python -m unittest discover -s tests -v
python tools/check_portfolio.py
```

On Windows, use your configured Python executable or py in place of python. Regeneration writes only the tracked analysis outputs, diagrams, and generated cloud service/action index. Review the diff afterward.

## Inputs and expected results

| Project | Fixed input | Expected result |
| --- | --- | --- |
| Healthcare | 100-row May 16, 2026 CSV | 6,692,288 reported affected count; median 5,140.5 |
| KEV | 1,592-row May 16, 2026 CSV | Full ranked intake plus top 50; CVE-2024-1708 scores 116 |
| Cloud | 12 synthetic JSON events | 10 signals: 5 High, 3 Medium, 2 Informational |
| CTI | Selected ATT&CK v17.0 relationship index | 11 supported layer entries; 8 separate candidates |

The script supplies fixed analysis dates. Changing dates or input files intentionally changes results.

## Individual analysis commands

```sh
python projects/01-nist-csf-risk-assessment/scripts/analyze_hhs_breaches.py projects/01-nist-csf-risk-assessment/data/hhs-ocr-breach-sample-2026-05-16.csv --as-of 2026-05-16 --output-dir projects/01-nist-csf-risk-assessment/outputs
python projects/02-cisa-kev-vulnerability-prioritization/scripts/analyze_kev.py projects/02-cisa-kev-vulnerability-prioritization/data/known_exploited_vulnerabilities-2026-05-16.csv --as-of 2026-05-16 --output-dir projects/02-cisa-kev-vulnerability-prioritization/outputs
python projects/04-aws-cloud-security-log-investigation/scripts/analyze_cloudtrail.py projects/04-aws-cloud-security-log-investigation/data/sample-cloudtrail-events.json --output-dir projects/04-aws-cloud-security-log-investigation/outputs
python tools/generate_portfolio_visuals.py
```

## What the checks establish

Regression tests cover the corrected calculations, input rejection, overdue scoring, event outcomes, rule matching, deduplication, mapping consistency, and regenerated-output agreement. Documentation checks inspect relative links and anchors, image alternative text, SVG metadata and text bounds, and prose punctuation.

These checks do not establish live source availability, provider schema compliance, AWS deployment, ServiceNow behavior, detection accuracy on a real environment, or original-source provenance. The [status page](PUBLISH_STATUS.md) records those boundaries.
