---
name: data-pipeline-completion
description: "Audit, finish, or prepare batch/streaming ETL or ELT, analytics transformations, ingestion, and scheduled data products for production release. Use for readiness reviews or shipping work, not isolated edits without a readiness request."
---

# Data pipeline readiness

Review batch/streaming ETL or ELT, analytics transformations, ingestion, and scheduled data products. Identify source/sink schemas, orchestration DAGs, transformation SQL/code, checkpoints, partitions, data contracts, and quality tests before choosing checks.

## Workflow

1. Read [review-method.md](references/review-method.md) for scope, evidence, severity, authorization, and verdict rules. Preserve audit versus remediation versus release mode.
2. Read [completion-checklist.md](references/completion-checklist.md). Evaluate its relevant sections and the method's cross-cutting checks. Add product-specific invariants and record why any section is not applicable.
3. For sensitive or specialized business behavior, read the matching section of [domain-checks.md](references/domain-checks.md).
4. Record candidate-specific evidence. Fix and retest within scope when remediation is requested. Required checks that cannot run remain `UNVERIFIED`.
5. Use [reporting.md](references/reporting.md). Give one pre-release verdict: `READY TO DEPLOY`, `READY TO DEPLOY WITH ACCEPTED RISKS`, or `NOT READY TO DEPLOY`. Report live verification separately.

An unresolved P0 or required evidence gap blocks readiness. Eligible P1 exceptions require the user's explicit acceptance. Do not claim deployment, distribution, or live verification from a local build.
