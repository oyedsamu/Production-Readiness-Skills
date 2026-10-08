---
name: android-dependency-upgrades
description: Upgrade Android libraries or build plugins with compatibility, migration and regression evidence.
---
# Dependency Upgrades

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Record the current dependency graph, proposed versions and official release notes. Check Kotlin, AGP, Gradle, JDK and Android API compatibility as a connected toolchain.
2. Change the smallest compatible set and explain transitive changes. Apply documented migrations instead of suppressing compile or runtime warnings blindly.
3. Exercise the features using the upgraded APIs in relevant build variants, including minified code when reflection or serialization is involved. Keep a revert path and avoid unrelated bulk upgrades.

## Verification evidence
Compare resolved dependency graphs and run affected compile/lint/tests plus a release-like smoke test where needed. Report behavioral migrations and any device/API coverage gap.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/build/releases/gradle-plugin) for APIs and version-sensitive details relevant to the installed toolchain.
