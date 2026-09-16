---
name: backend-system-completion
description: Build, finish, audit, or deploy a backend, API, service, or platform using an evidence-backed production-readiness gate. Use when a user asks to build, complete, ship, productionize, deploy, or verify a backend system. Do not use for a narrow isolated server-side edit unless system readiness is also requested.
---

# Backend System Completion

A local server returning `200` is not completion. Apply four gates: Functional Complete, Quality Complete, Production Ready, and Production Verified.

## Workflow

1. Establish business capabilities, critical request and asynchronous flows, data classification, consistency requirements, dependencies, service-level expectations, and deployment target.
2. Build or inspect the system within the user's authorization. Preserve established contracts unless an intentional migration or breaking change is approved.
3. Before declaring completion, read [references/completion-checklist.md](references/completion-checklist.md) in full and apply every relevant section.
4. Mark checklist items `PASS`, `WARN`, `FAIL`, or `N/A`, with a reason for `N/A` and inspectable evidence for material claims.
5. Fix all issues safely within scope, then rerun affected tests, migrations, security checks, load checks, deployment checks, and failure-path exercises.
6. Classify unresolved findings as P0, P1, P2, or P3. Surface every open P0/P1 and never mask it with a percentage score.
7. Deploy and verify production when authorized and access exists. Otherwise distinguish implementation/staging evidence from production checks still requiring access.
8. Deliver the Backend System Completion Report in the reference format with one exact verdict: `READY TO DEPLOY`, `READY TO DEPLOY WITH ACCEPTED RISKS`, or `NOT READY TO DEPLOY`.

## Production integrity

- An unresolved P0 always blocks deployment.
- Unresolved P1 issues normally block an unconditional ready verdict; only the user can explicitly accept them.
- Verify authentication and object/function-level authorization, validation, structured errors, rate limits, secrets, TLS, migrations, backups and restore, observability, alerting, timeouts, and bounded safe retries.
- Exercise concurrency, transactions, idempotency, partial failure, queues, scheduled jobs, dead-letter paths, webhooks, cache behavior, dependency failure, rollback, and recovery where relevant.
- Do not claim backup readiness without a restore test, observability without useful signals and alerts, scalability without representative evidence, or deployment safety without repeatable rollback.
- Apply the reference's domain extensions when relevant, including fintech, healthcare, marketplace, logistics, AI/LLM, civic/public-data, and enterprise systems.

When infrastructure, credentials, traffic, or production access are unavailable, identify the exact unverified checks and the evidence needed to close them.
