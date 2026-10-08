---
name: android-debug-issue
description: Investigate and fix a reproducible Android bug using lifecycle, state, logs and a regression check.
---
# Debug Issue

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Capture expected/actual behavior, build, device/API, steps and frequency. Reduce the case and collect redacted logs or traces before guessing at a fix.
2. Trace the failing transition to its owning component. Form one hypothesis and choose a discriminating experiment; check lifecycle, cancellation and concurrency when symptoms are intermittent.
3. For requested remediation, change the smallest cause and add a regression assertion. For investigation-only requests, report the hypothesis and evidence without editing the app.

## Verification evidence
Rerun original reproduction and a nearby success path. Show the regression test failing before and passing after when feasible; mark an unreproduced bug unresolved rather than claiming a fix.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/studio/debug) for APIs and version-sensitive details relevant to the installed toolchain.
