# CloudTrail Field Guide

## Purpose

CloudTrail events can look dense at first. This guide explains the fields that matter most during a basic security investigation.

## Core Fields

| Field | Plain-English meaning | Investigation use |
|---|---|---|
| `eventTime` | When the action happened | Build the timeline |
| `eventSource` | Which AWS service received the request | Identify the service involved |
| `eventName` | The API action | Understand what changed |
| `awsRegion` | Region where the event was recorded | Scope the investigation |
| `sourceIPAddress` | Network source of the request | Spot unexpected locations |
| `userAgent` | Tool or browser used | Distinguish console, CLI, SDK, or service activity |
| `userIdentity.type` | Identity type, such as Root, IAMUser, AssumedRole | Understand who or what acted |
| `userIdentity.userName` | IAM user name when present | Attribute the action |
| `userIdentity.arn` | Full AWS identity ARN | Tie activity to a principal |
| `requestParameters` | Inputs sent with the request | Inspect what the action tried to change |
| `responseElements` | AWS response details | Confirm success or returned values |
| `errorCode` | AWS error code | Identify denied or failed activity |
| `errorMessage` | Human-readable failure reason | Understand why the request failed |

## Triage Questions

For each event, ask:

1. Is this a read action or a write/change action?
2. Did the action succeed or fail?
3. Which identity performed it?
4. Was the source IP expected?
5. Was the action part of a planned lab step?
6. Did the action create exposure, privilege, persistence, or logging risk?
7. Is there a matching remediation event?

## Common Events And Why They Matter

| Event | Why it matters |
|---|---|
| `ConsoleLogin` | Shows interactive sign-in activity |
| `CreateAccessKey` | Creates long-lived credentials that need protection and rotation |
| `AttachUserPolicy` | Can grant broad privilege |
| `AuthorizeSecurityGroupIngress` | Can expose services to the internet |
| `RevokeSecurityGroupIngress` | Shows remediation of network exposure |
| `PutBucketPolicy` | Can change who can access S3 data |
| `DeletePublicAccessBlock` | Can remove protection against public S3 exposure |
| `StopLogging` | Can reduce visibility into account activity |
| `DeleteTrail` | Can remove ongoing log delivery |
| `CreateDetector` | Shows GuardDuty enablement |
| `CreateSampleFindings` | Generates GuardDuty sample findings for analyst practice |

## What Counts As A Risk Signal

Risk signals are not automatic proof of compromise. They are events that deserve review because they can increase exposure or reduce visibility.

Examples:

- root account used successfully
- failed console login
- public inbound rule on port `22` or `3389`
- administrator policy attached to a user
- access key created
- public S3 policy attempted or applied
- public access block removed
- CloudTrail logging stopped or deletion attempted
- GuardDuty disabled
- repeated AccessDenied events from the same actor

## How To Write An Investigation Note

A clear note should include:

- what happened
- why it matters
- what evidence supports it
- whether the action succeeded or failed
- what was done to remediate it
- what should be monitored next

Example:

> `AuthorizeSecurityGroupIngress` was observed for a detached lab security group with `0.0.0.0/0` on port `22`. Even though no EC2 instance was attached, the event demonstrates a public administrative exposure pattern. The rule was reversed with `RevokeSecurityGroupIngress`, and future monitoring should alert on public admin ports.
