---
name: android-ci-cd
description: Implement or review Android CI build/test pipelines, artifact handling and separately authorized release jobs.
---
# CI/CD

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Separate untrusted PR validation from jobs with signing or publication credentials. Use least-privilege job permissions and do not expose secrets to fork-controlled build scripts.
2. Pin the intended JDK/SDK/toolchain and run relevant lint, JVM and device checks. Cache dependencies without caching credentials; preserve reports on failures.
3. Identify artifacts by commit/variant and preserve mapping/symbol outputs. Gate publishing separately from validation; define retry behavior so a retried job cannot accidentally duplicate a release action.

## Verification evidence
Run a branch pipeline with a deliberately failing check and verify the job fails while retaining reports. Inspect fork/secret conditions and release gates without publishing or revealing secrets.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) for APIs and version-sensitive details relevant to the installed toolchain.
