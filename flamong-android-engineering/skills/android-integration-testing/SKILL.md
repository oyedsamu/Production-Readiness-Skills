---
name: android-integration-testing
description: Test Android interactions across real component boundaries such as database, HTTP client, repository and background worker.
---
# Integration Testing

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Select the integration seam and keep the components under test real while substituting only external services. Use isolated database/files and controlled server responses.
2. Exercise a complete operation across the boundary, including failure after partial progress. Assert committed data and externally visible effects rather than only mocked calls.
3. Reset persistent work and test state between cases. Include upgrade, retry or duplicate execution where the integration owns those contracts; avoid live production endpoints.

## Verification evidence
Run the test twice from clean state and inject a boundary failure. Record final persisted state, request counts and cleanup; distinguish JVM coverage from device-only behavior.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/training/testing) for APIs and version-sensitive details relevant to the installed toolchain.
