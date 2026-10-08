---
name: android-static-analysis
description: Configure or diagnose Android lint and Kotlin static analysis with actionable findings and controlled suppressions.
---
# Static Analysis

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Inspect existing lint/analyzer versions, configurations and baselines. Reproduce the finding with the project task before changing rules.
2. Fix the underlying issue or add a narrow suppression with rationale; do not regenerate a baseline to hide newly introduced warnings.
3. Run checks across affected variants and source sets. Keep custom rules and generated-code exclusions scoped, and make failure severity explicit in CI.

## Verification evidence
Run the analyzer on a known offending fixture and confirm it reports the expected issue; fix it and rerun. Inspect the baseline diff for unrelated suppressed findings.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/studio/write/lint) for APIs and version-sensitive details relevant to the installed toolchain.
