---
name: android-navigation
description: Implement or debug Android navigation routes, back stacks, deep links and restoration using the existing navigation library.
---
# Navigation

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Define destinations and route arguments with stable identifiers rather than passing mutable objects or sensitive values in URLs.
2. Validate incoming deep links and authorization at the destination. Define back and up behavior for normal entry, external entry and nested flows.
3. Check repeated taps, logout and configuration/process restoration. Keep navigation effects tied to consumed actions so recomposition does not add duplicate destinations.

## Verification evidence
Exercise a normal route and a malformed or unauthorized deep link; press back through the flow and recreate the host. Record the resulting destination and back stack.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/guide/navigation) for APIs and version-sensitive details relevant to the installed toolchain.
