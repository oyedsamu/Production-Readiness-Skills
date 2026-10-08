---
name: android-modularization
description: Split or review Android Gradle modules, public APIs and dependency ownership; use for module boundary changes.
---
# Modularization

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Map module dependencies, build times and ownership; identify the coupling or rebuild cost the split must address.
2. Define a minimal consumer-facing API. Keep implementation types internal where possible; check resources, manifests and dependency exposure as well as Kotlin visibility.
3. Move one vertical slice first. Check for dependency cycles and accidental API leakage through api configurations; do not impose an api/impl pair without a consumer need.

## Verification evidence
Compile a consumer against the intended API and build the affected app variant. Compare dependency reports before and after; confirm no new cycle or exposed implementation type.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/modularization) for APIs and version-sensitive details relevant to the installed toolchain.
