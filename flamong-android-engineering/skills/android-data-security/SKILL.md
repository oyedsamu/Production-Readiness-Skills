---
name: android-data-security
description: Review or harden Android handling of sensitive local data, credentials, backups, logs and cryptographic keys.
---
# Data Security

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Inventory sensitive values and every persistence/export path, including database, preferences, cache, screenshots, backups and telemetry. Tie controls to the threat model.
2. Use private storage for private data and platform key management where encryption is required. Do not embed reusable secrets in the APK or implement custom cryptography.
3. Inspect backup inclusion, logout cleanup and account isolation. Redact credentials and personal values from logs; plan key invalidation and recovery rather than silently losing encrypted records.

## Verification evidence
Using synthetic secrets, inspect app-created files and captured logs, exercise logout/account switch, and review backup rules. Test key-unavailable recovery if encryption is used; record residual exposure.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/privacy-and-security/security-best-practices) for APIs and version-sensitive details relevant to the installed toolchain.
