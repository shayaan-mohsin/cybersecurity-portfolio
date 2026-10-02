# A discussion guide for the portfolio

[Portfolio home](README.md) · [Scope and contributions](CONTRIBUTIONS.md)

Use these as prompts, not a script to memorize. Open the linked artifact while explaining it. State what you personally understand and can reproduce; be candid about AI assistance and work that remains a design.

## Healthcare analysis

**Opening:** “I used 100 public healthcare breach reports to practice turning data into risk questions without pretending the reports revealed an organization’s controls.”

**Show:** [calculation walkthrough](projects/01-nist-csf-risk-assessment/breach-trend-analysis.md) and [risk register](projects/01-nist-csf-risk-assessment/risk-register.md).

**Explain:** Python reads and validates the CSV, counts exact categories, and sums reported affected counts. Contrast 60 Network Server-only reports with 67 mentions. Explain why the median is useful when one report contributes 46.6% of the sum.

**Decision and learning:** ask for inventory, access, monitoring, and restore evidence before confirming a risk. The sample is not representative and the original portal capture is missing.

## Vulnerability intake

**Opening:** “I built a transparent research queue from a fixed CISA KEV snapshot. I wanted another analyst to see why each item ranked where it did.”

**Show:** [116-point example](projects/02-cisa-kev-vulnerability-prioritization/kev-catalog-analysis.md) and [model](projects/02-cisa-kev-vulnerability-prioritization/triage-model.md).

**Explain:** CSV validation, dates, keyword branches, scoring, and deterministic sorting use Python’s standard library. A product keyword is a research hint, not evidence of ownership or exposure. The due-date bonus no longer decays after a date passes.

**Decision and learning:** validate product/version and asset context before opening a remediation task. No scanning, patching, or risk reduction was performed.

## Identity threat research

**Opening:** “I studied how support and identity-recovery processes appear in public threat reporting, then translated that into questions a defender could investigate.”

**Show:** [supported mappings](projects/03-mitre-attack-cti-brief/attack-mapping.md) and [factor-change walkthrough](projects/03-mitre-attack-cti-brief/detection-and-response.md).

**Explain:** ATT&CK v17.0, direct group-to-technique relationships, STIX source identifiers, and the JSON layer. Eleven selected mappings have direct support; eight candidates remain separate. A valid ID alone is insufficient attribution.

**Decision and learning:** correlate the support ticket, authorizer, identity event, and subsequent access, while checking legitimate recovery as an explanation. Detection performance is untested.

## Cloud investigation

**Opening:** “I wrote an offline analyzer for synthetic CloudTrail-style JSON. The main lesson was to separate an attempted action from its outcome and from the resource’s final state.”

**Show:** [three-event walkthrough](projects/04-aws-cloud-security-log-investigation/walkthrough.md), [code](projects/04-aws-cloud-security-log-investigation/scripts/analyze_cloudtrail.py), and [tests](tests/test_analysis.py).

**Explain:** JSON normalization, deduplication, full actor identifiers, service/action validation, error-first logic, and per-rule port/CIDR matching. A denied StopLogging request does not prove logging stopped.

**Decision and learning:** ask for state and delivery evidence before claiming exposure or restoration. The 12 records produce 10 signals, not 10 confirmed incidents. AWS deployment remains planned.

## Serenity Bank capstone

**Opening:** “For my individual academic capstone, I proposed security controls for a fictional bank. This portfolio version makes the identity boundaries and required tests explicit.”

**Show:** [customer and administrator paths](projects/05-serenity-bank-capstone/design-walkthrough.md).

**Explain:** authentication versus authorization, workload versus human identity, key administration, logging, and recovery dependencies. A customer session does not grant cloud administrative privileges.

**Decision and learning:** define an acceptance test for each control. Encryption and a firewall do not replace record-level authorization. The capstone is my individual academic design; no implementation or recovery metric is claimed.

## Service desk design

**Opening:** “I designed ten scripted support scenarios to practice the decisions and documentation behind a good ticket. ServiceNow and endpoint execution are still pending.”

**Show:** [VPN case](projects/06-service-desk-workflows/tickets/03-vpn-dns.md), [printer recurrence](projects/06-service-desk-workflows/tickets/04-printer-reopen.md), or [access request](projects/06-service-desk-workflows/tickets/06-file-share-access.md).

**Explain:** incident versus request, impact and urgency, work notes versus user comments, accepted handoff, approval, verification, and closure. A connected VPN does not prove application access.

**Decision and learning:** stop identity recovery if the approved verification method or agent authority is missing. Do not convert scripted notes into an experience claim.

## Questions to be ready for

- Which part of this did you execute, and where is the artifact?
- What observation could change your conclusion?
- What did the earlier version get wrong, and how does a test protect the correction?
- What would you do differently with real users, an inventory, and authorized access?
- What remains untested, and what evidence would close that gap?
