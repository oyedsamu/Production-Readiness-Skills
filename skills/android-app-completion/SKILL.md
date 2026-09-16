---
name: android-app-completion
description: Build, finish, audit, or release an Android application using an evidence-backed production-readiness gate. Use when a user asks to build, complete, ship, publish, prepare for Play Store, or verify an Android app. Do not use for a narrow isolated Android code edit unless release completeness is also requested.
---

# Android App Completion

An app compiling or opening on one device is not completion. Apply four gates: Functional Complete, Quality Complete, Production Ready, and Release Verified.

## Workflow

1. Establish product scope, critical journeys, supported Android/API levels, device classes, distribution route, data sensitivity, and release constraints.
2. Build or inspect the app within the user's authorization. Preserve the selected architecture and stack unless changing them is necessary and within scope.
3. Before declaring completion, read [references/completion-checklist.md](references/completion-checklist.md) in full and apply every relevant section.
4. Mark checklist items `PASS`, `WARN`, `FAIL`, or `N/A`, with a reason for `N/A` and concrete evidence for each material claim.
5. Fix all issues safely within scope, rebuild the release variant, and rerun affected unit, integration, UI, device, and operational checks.
6. Classify unresolved findings as P0, P1, P2, or P3 using the reference. Never hide release blockers behind an aggregate score.
7. Distribute and verify the signed release build when authorized and possible. Otherwise separate implementation evidence from Play Console or production checks still requiring access.
8. Deliver the Android App Completion Report in the reference format with one exact verdict: `READY TO RELEASE`, `READY TO RELEASE WITH ACCEPTED RISKS`, or `NOT READY TO RELEASE`.

## Release integrity

- An unresolved P0 always blocks release.
- Unresolved P1 issues normally block an unconditional ready verdict; only the user can explicitly accept them.
- Verify the release build, signing, R8/resource shrinking behavior, production endpoints, analytics/crash delivery, permissions, deep/app links, and store configuration rather than inferring them from debug behavior.
- Exercise lifecycle recreation, process death, rotation/configuration changes, background restrictions, offline and degraded networks, retries, migrations, upgrades, and accessibility where relevant.
- Treat server-side authorization, secure storage, sensitive logging, network security, backup behavior, exported components, WebViews, file handling, and dependency risk as release concerns.
- Apply the reference's stack and domain extensions when relevant, including Compose, Views, Retrofit/OkHttp, Room, dependency injection, WorkManager, Firebase, fintech, healthcare, marketplace, logistics, civic/public-data, and enterprise apps.

When devices, Play Console, credentials, or production access are unavailable, report the exact unverified checks. Do not substitute a debug APK result for signed-release evidence.
