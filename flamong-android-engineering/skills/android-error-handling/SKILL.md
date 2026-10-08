---
name: android-error-handling
description: Define Android failure classification, user recovery, cancellation and safe diagnostic reporting.
---
# Error Handling

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Separate validation, authentication, transient transport and permanent failures at the owning boundary. Preserve cancellation instead of presenting it as an error.
2. Give recoverable failures an explicit action. Bound automatic retries and require idempotency for operations that may already have succeeded.
3. Keep user messages free of stack traces and sensitive server payloads; retain a safe diagnostic identifier. Preserve valid content when a refresh fails where the product permits it.

## Verification evidence
Inject each supported failure and retry it. Assert the UI state, retry count and retained data; verify logs omit sensitive values and cancellation creates no error banner.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/architecture/ui-layer) for APIs and version-sensitive details relevant to the installed toolchain.
