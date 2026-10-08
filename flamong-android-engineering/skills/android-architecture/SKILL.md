---
name: android-architecture
description: Choose or review Android layer boundaries and dependency direction for a feature or architectural change.
---
# Architecture

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Identify the feature entry points and trace one operation through UI, state holder, business logic and data sources. Draw the actual dependency direction before adding layers.
2. Keep domain contracts independent of Android types when a pure domain boundary is useful. Put implementations behind the owning contract; avoid adding use cases that only forward calls.
3. Inspect module dependencies for cycles and implementation leakage; preserve the existing architecture unless the requested change requires a documented deviation.

## Verification evidence
Compile the affected modules and test a business operation without starting the UI. Record the dependency edges checked and any framework dependency that remains intentional.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/architecture) for APIs and version-sensitive details relevant to the installed toolchain.
