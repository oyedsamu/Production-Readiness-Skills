---
name: production-readiness-review
description: Assess release readiness across mixed-stack repositories, monorepos, or projects whose architecture is not yet known. Use to choose relevant readiness tracks and combine evidence into one release decision. For a single known stack, prefer its specific completion skill.
---

# Production readiness review

Use this entrypoint when the release spans multiple components or the project type is unclear.

1. Read [review-method.md](references/review-method.md) and establish the requested audit, remediation, or release scope.
2. Read [project-routing.md](references/project-routing.md). Inspect manifests and deployment boundaries, then select only the relevant tracks. Use installed specialist skills when available; never assume a sibling skill is installed. If a specialist is unavailable, use this package's cross-cutting method and integration checks, derive stack checks from the detected project's official documentation, and state the coverage limit.
3. Read [completion-checklist.md](references/completion-checklist.md) for boundaries between components. Keep one evidence ledger with component-qualified IDs and reuse shared evidence only when it proves the same candidate, environment, and criterion.
4. Add applicable checks from [domain-checks.md](references/domain-checks.md). Fix and retest within scope when requested; preserve audit-only mode.
5. Follow [reporting.md](references/reporting.md). Give each component its own verdict and an overall `READY TO RELEASE`, `READY TO RELEASE WITH ACCEPTED RISKS`, or `NOT READY TO RELEASE`. State live verification separately.

An unresolved P0 or required evidence gap on a critical release path blocks the overall decision. Explicitly accepted eligible P1 risks remain visible. A successful shared library or frontend build cannot prove its host, service, or infrastructure is ready.
