---
name: android-review-pull-request
description: Review an Android pull request for actionable correctness, security, lifecycle and test gaps; read-only by default.
---
# Review Pull Request

## Scope
Start in read-only assessment mode. Do not edit project files, install new dependencies in the target checkout, or remediate findings unless the user requests those actions. Existing safe checks and isolated reproductions are allowed. A review request does not authorize posting to external services or publication.

## Workflow
1. Read the current diff and affected callers, tests, manifests and build configuration. Evaluate new behavior against the requested change rather than redesigning the application.
2. Trace changed state transitions, lifecycle ownership, coroutine cancellation and data/security boundaries. Validate suspected defects with existing checks or an isolated reproduction without editing the checkout.
3. Report only actionable findings with severity, path/line, trigger, consequence and a concrete fix direction. Identify missing test evidence separately from proven defects; do not implement fixes unless requested.

## Verification evidence
Return prioritized findings or an explicit no-findings result with checks run and limitations. Do not post comments, request changes on GitHub, or edit the branch unless the user authorized that action.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/training/testing) for APIs and version-sensitive details relevant to the installed toolchain.
