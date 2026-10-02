# Executive summary

[Project overview](README.md) · [Walkthrough](walkthrough.md)

This exercise demonstrates how I interpret cloud activity without treating every suspicious event name as a successful attack.

The offline analyzer reviews 12 synthetic records and produces 10 signals. It treats denied changes as failed actions, reviews public ingress in its actual rule context, and keeps a removal request separate from proof of restoration.

The result is a reproducible local report. A separate AWS template is a future lab design; no deployment, live collection, confirmed compromise, or measured remediation is established.
