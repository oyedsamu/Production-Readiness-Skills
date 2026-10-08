---
name: android-offline-sync
description: Implement or debug Android offline reads, queued writes, reconciliation and conflict handling.
---
# Offline Sync

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Define the local source of truth, pending-write representation and conflict policy. Persist intent before acknowledging a durable offline action.
2. Give retryable writes stable identifiers and server-supported idempotency. Define deletion/tombstone behavior and account ownership so stale work cannot recreate deleted records or cross accounts.
3. Use persistent scheduling when work must survive process death. Bound retries and distinguish conflicts or permanent rejection from transient connectivity failures.

## Verification evidence
Queue a change offline, restart the process, reconnect and redeliver the same work. Assert one server effect, correct local reconciliation, and no deleted-record resurrection or cross-account replay.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/architecture/data-layer/offline-first) for APIs and version-sensitive details relevant to the installed toolchain.
