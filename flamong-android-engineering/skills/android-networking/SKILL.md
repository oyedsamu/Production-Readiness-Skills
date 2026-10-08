---
name: android-networking
description: Implement or review Android HTTP requests, authentication refresh, timeout behavior and network failure recovery.
---
# Networking

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Inspect client configuration, authentication ownership and request semantics. Configure timeouts deliberately and use HTTPS without weakening certificate verification.
2. Coalesce concurrent credential refresh where needed. Bound retries; retry mutations only with a documented server idempotency contract and distinguish an unknown result from a definite rejection.
3. Map transport, HTTP and decoding failures separately. Avoid leaking credentials in logs, redirects or query parameters; cancel obsolete requests with their owning work.

## Verification evidence
Use a local fake server to simulate timeout, malformed data, concurrent unauthorized responses and a dropped mutation response. Assert refresh/retry counts and that user actions are not duplicated.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/training/basics/network-ops) for APIs and version-sensitive details relevant to the installed toolchain.
