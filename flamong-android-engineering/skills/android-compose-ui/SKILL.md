---
name: android-compose-ui
description: Implement or revise Jetpack Compose UI, including state ownership, effects, semantics and adaptive layout.
---
# Compose UI

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Separate screen state ownership from reusable composables; expose values and callbacks instead of giving every child a ViewModel.
2. Key remembered state and effects to their actual lifetime. Keep side effects out of composition; use saveable state only for restorable UI values rather than credentials or whole repositories.
3. Exercise loading, empty, error and populated states with long content, larger fonts and different widths. Give actionable controls meaningful semantics and avoid duplicate event handling during recomposition.

## Verification evidence
Recompose and recreate the screen; verify callbacks fire once per action and intended state survives recreation. Capture layout and accessibility observations for the affected states.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/develop/ui/compose/state) for APIs and version-sensitive details relevant to the installed toolchain.
