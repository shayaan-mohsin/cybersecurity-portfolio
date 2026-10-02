# Data and method

[Project overview](README.md) · [Walkthrough](breach-trend-analysis.md)

The retained [CSV](data/hhs-ocr-breach-sample-2026-05-16.csv) contains 100 reports from the [HHS OCR breach portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf). Earlier collection notes describe the first 100 displayed records on May 16, 2026. The original screen capture, query, and full export were not retained, so that selection cannot be independently reconstructed.

Treat this as a convenience sample. It is not a random sample, a complete reporting-period export, or a national breach-rate estimate.

## Fields and calculations

- Submission dates run from February 9 to May 1, 2026. These are reporting dates, not necessarily incident dates.
- Sum the affected-individual field across reports. People may occur in multiple reports.
- For 100 sorted counts, the median is the mean of positions 50 and 51: 5,140.5.
- Keep all 11 exact location labels in the generated frequency table. Counts total 100.
- For mentions, split the comma-separated location labels and count each location once per report. These counts overlap.
- Two records lack a state. Keep them visible as Unknown; do not silently drop them.
- The business-associate flag is separate from the reporting entity’s type.

The script rejects empty input, missing required columns, invalid counts or dates, invalid business-associate flags, and duplicate complete rows. Missing state is retained. This validates format and internal consistency, not the accuracy of a public report.

## Interpretation limits

Public reports can be amended. Breach category does not establish the attack path, cause, control weakness, or remediation quality. A large affected count does not establish a larger financial loss. The proposed register therefore uses conditional language and identifies the evidence needed to test each hypothesis.
