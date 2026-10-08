---
name: android-state-management
description: Design or debug Android screen state, action handling, state restoration and transient UI effects.
---
# State Management

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. List user actions and model the allowed loading, content and failure transitions. Choose a single authoritative state owner rather than competing mutable copies.
2. Expose immutable state and handle actions through a defined entry point. Decide explicitly whether each effect may be lost, replayed or acknowledged across lifecycle changes.
3. Keep persisted domain data separate from saved UI selection. Cancel or supersede stale requests so an older response cannot overwrite a newer user choice.

## Verification evidence
Test rapid successive actions, failure followed by retry, rotation and returning from background. Assert final state and effect delivery counts, including the agreed restoration behavior.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/architecture/ui-layer/state-production) for APIs and version-sensitive details relevant to the installed toolchain.
