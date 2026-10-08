---
name: android-release-readiness
description: Assess an Android release candidate, packaging and rollout preparation; assessment does not authorize publication.
---
# Release Readiness

## Scope
Start in read-only assessment mode. Do not edit project files, install new dependencies in the target checkout, or remediate findings unless the user requests those actions. Existing safe checks and isolated reproductions are allowed. A review request does not authorize posting to external services or publication.

## Workflow
1. Identify the candidate commit, artifact, variant, application ID and signing configuration. Evaluate the release build rather than assuming a debug build proves release behavior.
2. Install the release-like artifact and upgrade from the previous release with existing data. Exercise minified paths, startup, core flow, permissions and offline recovery; inspect mapping/symbol artifacts.
3. Record blockers, unknown checks and conditional N/A reasons. Verify rollout ownership and a feasible recovery plan; consider data compatibility and store constraints before promising rollback.

## Verification evidence
Report candidate/environment and each required check as PASS, FAIL, UNVERIFIED or justified N/A. Missing required evidence blocks a ready verdict; do not upload, publish or change rollout during assessment.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/studio/publish/preparing) for APIs and version-sensitive details relevant to the installed toolchain.
