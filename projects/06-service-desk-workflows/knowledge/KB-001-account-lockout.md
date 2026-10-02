# KB-001 : Account lockout triage and safe escalation

**Status:** untested draft. **Audience:** delegated L1/Identity lab agents. **Owner:** learner role-play. **Version:** 0.1. **Last tested:** not tested. **Review trigger:** identity policy, directory platform or delegated-role change.

## Applies when

An existing fictional user reports an account-locked message. The affected platform and actual error must be confirmed. This article does not authorize authentication-method recovery or a compromised-account response.

## Before any account action

Complete the established identity check through a trusted pre-enrolled route. Document method/result without secret answers. Confirm the agent's delegated role permits the proposed action. If either check fails, stop account changes and route to Identity Support.

Ask whether there are unfamiliar sign-ins, unsolicited MFA prompts, a lost device or a suspicious message. A positive security signal triggers the security escalation procedure. Do not ask for passwords, OTPs or recovery codes.

## Procedure

1. Record exact error, onset, device, business effect and whether other users/services are affected.
2. Check authorized service-health and account-state information where available. Lack of access is a limitation; never fabricate a healthy-service conclusion.
3. If the account is locked, examine authorized lockout metadata and recent change history. A recent password change may support a stale saved-credential hypothesis, but is not proof.
4. Identify one controlled test endpoint/application if the evidence supports it. Ask permission before changing a specific stored entry. Preserve the scope and rollback approach.
5. Have the authorized role perform the narrow action. L1 can hand off the evidence without performing the unlock.
6. The user enters their own credentials. Test normal sign-in and the required application. Record the observation window and any recurrence.

## Stop / escalation conditions

Failed verification; insufficient delegated privilege; suspected compromise; broader service interruption; unknown source of recurrent lockouts; unsafe endpoint change; or repeated lockout after a bounded correction.

A useful handoff includes identity-check result, exact error and timing, affected account/device, service scope, observations, attempted actions and results, remaining question, and requested next action. Exclude secret values.

## Resolution documentation

State whether restoration was a workaround or a durable correction. Record actual before/after checks, the acting role, user confirmation and recurrence behavior. Keep the ticket active if restoration is unconfirmed. Do not close merely because the account is temporarily unlocked.

## Validation required before publication

- [ ] Failed identity verification produces no account change.
- [ ] Authorized action is performed by the delegated role.
- [ ] The intended sign-in path works afterward.
- [ ] A recurrence stays open and preserves earlier actions.
- [ ] Notes and screenshots contain no authentication secrets.

Related exercise: [LAB-INC-001](../tickets/01-account-lockout.md).
