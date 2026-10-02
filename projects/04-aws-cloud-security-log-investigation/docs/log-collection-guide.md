# Future collection and evidence plan

[Project overview](../README.md) · [Lab design](../architecture.md)

This is a plan for a future authorized lab. The current project uses synthetic JSON only.

For a future run, record the account boundary, Region, trail settings, collection time, event types, file hash, and authorized collector. Verify log delivery and distinguish Event History management events from delivered trail files and data-event coverage.

Keep raw exports outside the repository in restricted storage. Review every field before any sharing; user agents, ARNs, nested policies, tags, names, and error messages can contain sensitive information. The disabled sanitizer must not be used as a publication control.

Create a deliberately synthetic public fixture to illustrate findings. Do not relabel real logs as synthetic. Document what was actually executed and attach separately reviewed evidence before claiming live collection.
