# Proposed validation work

[Project overview](README.md) · [Defensive walkthrough](detection-and-response.md)

| Work item | Reason | Completion evidence |
| --- | --- | --- |
| Define identity recovery policy | Support must know when a change is authorized | Approved method, prerequisites, failure route, and delegated roles |
| Select a test identity platform | Event fields differ by platform | Recorded version, audit settings, event examples, collection checks |
| Exercise factor changes | Distinguish legitimate, denied, and unauthorized scenarios | Scripted test inputs, observed events, expected/actual comparison |
| Correlate support and identity records | Avoid attributing events by name or IP alone | Stable identifiers, timestamp handling, missing-event tests |
| Test response and restoration | A response action may interrupt legitimate access | Authorization, observed final state, and user verification |
| Review mappings after a version upgrade | ATT&CK meaning can change | A versioned diff, updated sources, and a reviewed layer |

This is a backlog, not a record of completed control improvements.
