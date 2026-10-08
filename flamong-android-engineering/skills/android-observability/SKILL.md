---
name: android-observability
description: Implement or review Android crash, ANR, error and performance diagnostics with useful context and redaction.
---
# Observability

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Define the failure or latency question to answer and select a minimal event/metric. Include build/version and safe correlation context without user payloads or credentials.
2. Verify release mapping/symbol artifacts reach the chosen crash service. Distinguish crashes, nonfatal failures and expected cancellation to avoid noisy alerts.
3. Exercise offline delivery, sampling and telemetry-disabled behavior. Keep reporting bounded so a failing collector cannot block the main user flow.

## Verification evidence
Trigger a synthetic failure in an isolated build, inspect its decoded report and redacted fields, and confirm the app still works when telemetry is unavailable. Record vendor access gaps.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/performance/vitals) for APIs and version-sensitive details relevant to the installed toolchain.
