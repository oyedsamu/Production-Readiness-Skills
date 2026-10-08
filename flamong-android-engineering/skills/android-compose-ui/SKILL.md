---
name: android-compose-ui
description: Use when working on Android compose ui, implementing or reviewing related Kotlin, Compose, Gradle, or Android application behavior.
---
# Compose Ui

## Goal
Deliver correct, maintainable Android changes with evidence, not unsupported completion claims.

## Workflow
1. Inspect the existing repository, its modules, build configuration, conventions and relevant tests before proposing changes.
2. Identify the user-visible requirement, constraints, affected layers, compatibility needs and security implications.
3. Prefer the smallest coherent implementation that follows existing project conventions. Document deviations and trade-offs.
4. Implement explicit error, loading, empty, cancellation and recovery behavior where relevant. Avoid silently swallowing failures.
5. Add focused automated tests for new behavior, failure modes and regressions. Do not claim tests passed without running them.
6. Run the applicable Gradle, lint, test and device checks available in the environment. Report exact commands and results.
7. Summarize changed files, behavior, risks, evidence, and any checks that could not be run.

## Domain-specific checks
- Use the official Android/Kotlin API contracts and the repository’s established patterns.
- Verify edge cases, lifecycle correctness, cancellation, accessibility and testability where applicable. 

## Verification evidence
- Changed paths and rationale.
- Commands run with pass/fail/not-run status.
- Tests added or updated, with uncovered risks.
- No fabricated benchmark, security, device or release results.

## References
- https://developer.android.com/
- https://developer.android.com/topic/architecture
- https://developer.android.com/training/testing
