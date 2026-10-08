---
name: android-compose-testing
description: Write or debug Compose UI tests involving semantics, user actions, synchronization, clocks and state transitions.
---
# Compose Testing

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Choose the smallest suitable Compose test rule and provide controlled screen state or test dependencies. Locate controls through semantics; inspect merged/unmerged trees when selectors fail.
2. Perform a user action and assert a visible state or callback. Use the Compose test clock for Compose-driven timing and explicit bounded waits for external async work; do not stabilize tests with arbitrary sleeps.
3. Cover loading/error/retry plus the affected interaction. Assert accessible labels and control state, and isolate navigation or repository integration when a screen-only test is sufficient.

## Verification evidence
Run the relevant UI test on an available device/emulator. Demonstrate that a broken action or missing semantic label fails the assertion; record device/API and any external work synchronization.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/develop/ui/compose/testing) for APIs and version-sensitive details relevant to the installed toolchain.
