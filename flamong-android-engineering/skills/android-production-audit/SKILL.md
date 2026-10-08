---
name: android-production-audit
description: Audit a native Android candidate for release blockers and missing evidence; use android-app-completion for the broader readiness track when available.
---
# Production Audit

## Scope
Start in read-only assessment mode. Do not edit project files, install new dependencies in the target checkout, or remediate findings unless the user requests those actions. Existing safe checks and isolated reproductions are allowed. A review request does not authorize posting to external services or publication.

## Workflow
1. Identify the candidate commit/artifact and inventory core flows, stored data, permissions, background work and release configuration. Keep the audit read-only unless remediation is requested.
2. Exercise the main flow and recovery from network failure, process recreation and denied permissions in an isolated environment. Inspect release signing/minification, accessibility and relevant security boundaries.
3. Classify observed issues by impact and distinguish missing evidence. Route to existing readiness guidance when available, but keep a usable findings report when installed independently.

## Verification evidence
Report per-check PASS, FAIL, UNVERIFIED or justified N/A with candidate, command/procedure and observed result. Required failures or unverified release checks prevent a ready verdict. Return findings and proposed remediation without implementing, uploading or publishing.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/studio/publish/preparing) for APIs and version-sensitive details relevant to the installed toolchain.
