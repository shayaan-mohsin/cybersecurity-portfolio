# Synthetic input

[Project overview](../README.md) · [Walkthrough](../walkthrough.md)

The JSON contains 12 fabricated CloudTrail-style management events. Account numbers, identities, resource names, documentation IP addresses, and the example key are lab values. The sequence combines Regions and lacks provider event IDs. It is not a complete provider export or a forensic record.

The denied bucket-policy example uses a composite bucketPolicy field; the analyzer checks errorCode first. Retain the fixture unchanged for reproducibility.

Supported local JSON containers are Records, Event History Events with embedded CloudTrailEvent strings, an event list, or one event object. CSV is unsupported because it commonly loses nested evidence.

Publish synthetic evidence only. The former regex sanitizer is disabled: replacing a few known strings cannot reliably remove identifiers or secrets from arbitrary real logs.
