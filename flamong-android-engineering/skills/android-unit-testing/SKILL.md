---
name: android-unit-testing
description: Write or improve Android JVM unit tests for business logic, state holders and coroutine behavior.
---
# Unit Testing

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Choose a behavior boundary with observable inputs and outputs. Use fakes for owned dependencies instead of asserting incidental internal call order.
2. Control time and dispatchers for coroutine tests; avoid sleeps and real network dependencies. Cover success, failure, cancellation and a relevant boundary value.
3. Keep framework-dependent tests separate from pure JVM tests. Ensure the test can fail for the targeted regression rather than only exercising constructor wiring.

## Verification evidence
Run the specific JVM test task and show an assertion that fails when the targeted behavior is broken. Record any Android runtime behavior the JVM test cannot establish.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/training/testing/local-tests) for APIs and version-sensitive details relevant to the installed toolchain.
