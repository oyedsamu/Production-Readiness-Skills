---
name: android-persistence
description: Implement or change Android local database schemas, transactions, queries or preferences with data compatibility checks.
---
# Persistence

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Inspect schema versions and existing installations before changing entities. Define an explicit migration; do not use destructive fallback for user data without an accepted product decision.
2. Use transactions for related writes and define uniqueness and conflict behavior. Keep blocking database work off the UI thread and observe updates from the intended source of truth.
3. Distinguish small preferences from relational data. Test logout cleanup and account separation for stored records; avoid storing secrets in ordinary preferences.

## Verification evidence
Open a fixture created with the previous schema, run the migration and compare retained records. Interrupt a multi-write operation and verify atomicity; exercise duplicate insertion and account switching.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/training/data-storage/room/migrating-db-versions) for APIs and version-sensitive details relevant to the installed toolchain.
