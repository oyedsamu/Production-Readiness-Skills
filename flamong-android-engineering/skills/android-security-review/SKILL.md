---
name: android-security-review
description: Audit Android attack surfaces and security controls against a scoped threat model; review is read-only by default.
---
# Security Review

## Scope
Start in read-only assessment mode. Do not edit project files, install new dependencies in the target checkout, or remediate findings unless the user requests those actions. Existing safe checks and isolated reproductions are allowed. A review request does not authorize posting to external services or publication.

## Workflow
1. Identify assets, trust boundaries and attacker capabilities; map relevant MASVS controls to manifest, IPC, links, WebViews, storage, transport and backend authorization.
2. Inspect exported components and URI/input validation. Exercise safe malformed inputs in an isolated app or fixture; avoid real credentials or production exploitation.
3. Separate observed vulnerabilities from missing evidence. Client-side gates do not prove server authorization; report exact preconditions, impact and a proportionate remediation.

## Verification evidence
Produce findings with path/line, reproducible input, observed result and expected control. Mark inaccessible server/device checks unverified; do not certify security from a checklist.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://mas.owasp.org/MASVS/) for APIs and version-sensitive details relevant to the installed toolchain.
