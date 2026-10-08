---
name: android-create-feature
description: Implement a requested Android feature as a vertical slice following existing modules, state and data conventions.
---
# Create Feature

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Trace a neighboring feature and map the requested acceptance criteria to screen actions, state, data contracts and authorization boundaries.
2. Implement a minimal complete slice with explicit loading, empty, error and recovery behavior; keep unrelated architecture changes out of the task.
3. Connect navigation, persistence and background work only when the feature needs them. Add focused tests at the boundary owning each acceptance criterion and exercise the core user flow.

## Verification evidence
Report which acceptance criteria were exercised, affected variants and failure cases. Separate passing local tests from device checks that were unavailable; do not call the feature complete on compilation alone.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/architecture) for APIs and version-sensitive details relevant to the installed toolchain.
