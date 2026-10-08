---
name: android-play-store
description: Prepare or review Android Play submission artifacts, declarations and store-specific requirements without publishing by default.
---
# Play Store

## Scope
Start in read-only assessment mode. Do not edit project files, install new dependencies in the target checkout, or remediate findings unless the user requests those actions. Existing safe checks and isolated reproductions are allowed. A review request does not authorize posting to external services or publication.

## Workflow
1. Identify the intended track and artifact, then verify current official requirements for that submission rather than freezing SDK deadlines in the skill.
2. Compare permissions, SDK data collection and actual behavior with Data safety and other applicable declarations. Check signing, version code and package identity against the intended app.
3. Review listing assets and user journey for accuracy; document any unavailable Console checks. Keep upload, submission and rollout distinct from local packaging and require user authorization for those actions.

## Verification evidence
Record requirement sources and inspection date, artifact identity and declaration gaps. Confirm Console state only with access; return unresolved submission blockers without claiming publication.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://support.google.com/googleplay/android-developer/answer/9859152) for APIs and version-sensitive details relevant to the installed toolchain.
