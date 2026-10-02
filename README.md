# Shayaan Mohsin | Cybersecurity portfolio

I’m an early-career cybersecurity analyst with an M.S. in Cybersecurity Operations and Leadership from the University of San Diego (June 2026) and a background in public policy and customer-facing operations.

I’m interested in work that connects technical evidence to a clear decision: which risk to investigate, what to prioritize, and what to tell the people affected.

[LinkedIn](https://www.linkedin.com/in/shayaanm/) · [Reproduce the analysis](SETUP_GUIDE.md) · [Scope and contributions](CONTRIBUTIONS.md)

## Start here

**Have two minutes?** Open the [cloud log investigation](projects/04-aws-cloud-security-log-investigation/README.md). The worked example shows how I distinguish an attempted change from a successful one, explain the uncertainty, and identify the next check.

**Looking for a particular skill?** Pick the question closest to the role:

- **[Healthcare risk analysis](projects/01-nist-csf-risk-assessment/README.md)**: turn 100 public breach reports into control questions. Inspect the calculations, hypothetical risk register, and proposed roadmap. **Public-data analysis.**
- **[Vulnerability intake](projects/02-cisa-kev-vulnerability-prioritization/README.md)**: explain which known-exploited vulnerabilities to research first. Inspect the Python model, full ranking, and one worked decision. **Public-data analysis.**
- **[Identity threat brief](projects/03-mitre-attack-cti-brief/README.md)**: connect reported identity abuse to useful investigation questions. Inspect 11 supported ATT&CK mappings and their sources. **Research and defensive design.**
- **[Cloud log investigation](projects/04-aws-cloud-security-log-investigation/README.md)**: distinguish a requested action from its result. Inspect synthetic events, Python logic, and an investigation walkthrough. **Offline simulation.**

## Explore by role

- **Governance, risk, and compliance (GRC):** [healthcare executive brief](projects/01-nist-csf-risk-assessment/executive-brief.md) → [risk assumptions and evidence needed](projects/01-nist-csf-risk-assessment/risk-register.md).
- **Security operations center (SOC) and cloud:** [one event, step by step](projects/04-aws-cloud-security-log-investigation/walkthrough.md) → [analysis code](projects/04-aws-cloud-security-log-investigation/scripts/analyze_cloudtrail.py) → [regression tests](tests/test_analysis.py).
- **Vulnerability management:** [intake model](projects/02-cisa-kev-vulnerability-prioritization/triage-model.md) → [prioritized research list](projects/02-cisa-kev-vulnerability-prioritization/outputs/kev-prioritized-watchlist-2026-05-16.csv).
- **Identity and support:** [threat-to-evidence mapping](projects/03-mitre-attack-cti-brief/detection-and-response.md) → [service desk scenario](projects/06-service-desk-workflows/tickets/03-vpn-dns.md).

## Designs I’m developing

These documents show planning and reasoning. They do not represent systems I have deployed.

- [Serenity Bank capstone](projects/05-serenity-bank-capstone/README.md): an academic security design for a fictional bank, separating customer, employee, administrator, and workload identities.
- [Service desk workflows](projects/06-service-desk-workflows/README.md): ten scripted ticket scenarios covering troubleshooting, access requests, escalation, and confirmation of restoration. ServiceNow execution and screenshots are still pending.

## What this work demonstrates

The analysis uses Python’s standard library to validate and summarize CSV tables and JSON activity records. The written deliverables connect observations to investigation steps, control questions, or prioritization decisions. The projects also show where I would stop and ask for more evidence.

The dated datasets remain fixed so a reviewer can reproduce the results. This repository contains no production incident response, deployed bank environment, completed ServiceNow tickets, or verified patching outcomes.

[Interview discussion guide](INTERVIEW-GUIDE.md) · [Reproduction and checks](SETUP_GUIDE.md) · [Current evidence boundaries](PUBLISH_STATUS.md)
