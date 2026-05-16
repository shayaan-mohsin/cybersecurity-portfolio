# Data Notes

## File

`hhs-ocr-breach-sample-2026-05-16.csv`

## Source

The file is a dated sample extracted from the public HHS OCR Breach Portal on May 16, 2026.

Source page: https://ocrportal.hhs.gov/ocr/breach/

## Scope

The HHS OCR portal displayed 710 HIPAA breach records at collection time. This file preserves the first 100 displayed records after opening the public "View HIPAA Breach Reports" table.

## Fields

- `covered_entity`
- `state`
- `covered_entity_type`
- `individuals_affected`
- `breach_submission_date`
- `type_of_breach`
- `location_of_breached_information`
- `business_associate_present`

## Handling Notes

The file contains public breach report fields. The analysis uses aggregate patterns and does not assess individual organizations.
