---
name: android-legacy-migration
description: Migrate an Android implementation incrementally while preserving existing behavior and a rollback path.
---
# Legacy Migration

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Capture current behavior and callers with characterization tests before replacing a framework, state model or module boundary.
2. Choose one migration seam and a reversible slice. Keep old and new callers interoperable during rollout; avoid coupling unrelated dependency upgrades to the migration.
3. Compare persisted data, navigation state and lifecycle behavior across old and new implementations. Remove the old path only after callers and compatibility checks are accounted for.

## Verification evidence
Run characterization tests on both paths, test upgrade from existing app data, and document how to revert the slice without losing user data.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/architecture) for APIs and version-sensitive details relevant to the installed toolchain.
