# Walkthrough: from a count to a useful question

[Project overview](README.md) · [Source and method](data-methodology.md)

## 1. Check the unit of analysis

A row is a reported breach, not a patient, hospital, or unique incident victim. The 100 rows sum to 6,692,288 reported affected individuals. The largest report contains 3,117,874, or 46.6% of the total.

The median of 5,140.5 is a useful companion to the sum because one large report dominates the latter. Neither describes a typical organization’s annual risk.

## 2. Resolve an ambiguous category

The exact label “Network Server” occurs 60 times. Seven additional reports include it with another location, giving 67 mentions. “Email” has 21 exact-label records and 24 mentions.

Those are different calculations. An exact-label distribution partitions the 100 rows; a mention distribution allows overlaps. The [generated location table](outputs/hhs-breach-summary-2026-05-16.md#location-frequency) retains all 11 exact categories.

The breach-type labels are Hacking/IT Incident (88), Unauthorized Access/Disclosure (11), and Theft (1). These broad labels do not identify specific technical causes.

## 3. Connect the evidence to a control question

**Observation:** server and email labels are common in this retained sample.

**Question:** for a hypothetical healthcare organization, can the owners identify sensitive-data systems, explain access decisions, and show monitored recovery procedures?

**Evidence I would request:** an asset inventory, access-review results, relevant identity and mail logs, exception records, and a restore-test record.

**Decision boundary:** public counts alone are insufficient to mark a control failed or assign an organization-specific risk rating.

## 4. Make the next action reviewable

The [risk register](risk-register.md) gives each hypothesis an owner to consult and a test to perform. The [roadmap](prioritized-roadmap.md) begins with validation before making larger control investments.

For exact figures, use the [generated summary](outputs/hhs-breach-summary-2026-05-16.md). The [script](scripts/analyze_hhs_breaches.py) and [repository checks](../../SETUP_GUIDE.md) make recalculation possible.
