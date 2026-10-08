---
name: android-coroutines-flow
description: Implement or diagnose Kotlin coroutines and Flow cancellation, collection lifetime, dispatchers and concurrency in Android.
---
# Coroutines Flow

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Identify the scope owning each job and the lifecycle owning each collector. Use structured concurrency; avoid creating detached jobs to bypass cancellation.
2. Keep blocking work off the main thread. Preserve cancellation when translating exceptions; choose buffering, conflation and sharing based on whether intermediate values may be lost.
3. Check retry bounds and duplicate collectors. Use lifecycle-aware UI collection and an explicit strategy for concurrent writes or latest-request-wins behavior.

## Verification evidence
With controlled dispatchers, cancel during suspended work and verify cleanup; restart collection and test concurrent emissions. Confirm no stale update or duplicate side effect after the screen stops.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/libraries/architecture/coroutines) for APIs and version-sensitive details relevant to the installed toolchain.
