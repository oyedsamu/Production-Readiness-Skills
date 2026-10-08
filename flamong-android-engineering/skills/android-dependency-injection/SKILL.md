---
name: android-dependency-injection
description: Implement or diagnose Android dependency injection bindings, scopes and test replacement using the existing DI framework.
---
# Dependency Injection

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Trace the failing or proposed binding from its consumer to its provider. Identify the owning component and required lifetime before changing scopes.
2. Keep Activity or View references out of longer-lived objects. Check qualifiers where multiple instances of one type exist; avoid making every dependency a singleton.
3. Provide test replacements at the same boundary used by production. Verify worker and ViewModel construction through the framework instead of only manual constructors.

## Verification evidence
Build the generated DI code and exercise recreation or a second consumer. Verify the intended shared instance and that shorter-lived contexts are not retained.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/training/dependency-injection) for APIs and version-sensitive details relevant to the installed toolchain.
