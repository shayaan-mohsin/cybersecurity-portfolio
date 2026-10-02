# Offline investigation playbook

[Project overview](../README.md) · [Worked examples](../walkthrough.md)

1. Establish the evidence source and scope. Here it is a synthetic fixture, with missing event IDs and mixed Regions.
2. Validate structure, preserve the input, and deduplicate without discarding distinct actor sessions.
3. Check the service/action pair and error outcome before interpreting request details.
4. Separate the observed action from intent, authorization, effective state, and business impact.
5. Identify the exact additional evidence required. For an ingress change, this includes the rule and affected resources.
6. Record findings and counter-explanations. A legitimate administrative action can match a high-urgency rule.
7. Require authorized action and final-state verification before marking a real issue resolved.

The script produces review signals, not automatic containment. It does not query AWS or verify the current state of a resource.
