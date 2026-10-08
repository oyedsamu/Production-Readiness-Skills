---
name: android-gradle-build-logic
description: Change or diagnose Android Gradle configuration, convention plugins, variants and reproducible build behavior.
---
# Gradle Build Logic

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Reproduce the affected task and inspect plugin/toolchain compatibility and variant wiring. Put reusable configuration in existing convention mechanisms rather than adding ad hoc cross-project mutation.
2. Keep secrets and machine-specific paths out of configuration. Declare task inputs/outputs correctly and avoid eager work that runs during unrelated task configuration.
3. Check dependency resolution and generated artifacts for the affected flavors/build types. Use configuration-cache checks only where the project supports them; explain incompatibilities rather than hiding failures.

## Verification evidence
Build the target variant from clean state, rerun to inspect incremental behavior, and verify another consumer of shared build logic. Record task outputs and any toolchain constraint.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/build) for APIs and version-sensitive details relevant to the installed toolchain.
