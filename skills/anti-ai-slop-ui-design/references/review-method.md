# Review method

## Establish the release boundary

Read the repository instructions, manifests, lockfiles, build configuration, CI, and deployment documentation. Identify the actual runtime and framework versions, deployable units, supported platforms, critical journeys, external dependencies, and data owners. A directory name alone is not evidence of a stack.

Record the requested mode:

- Audit: inspect and test; report findings without changing product code.
- Remediation: fix issues within the requested scope, then verify the changed behavior.
- Release: prepare and, where authorized, publish or deploy the artifact and verify it.

Use existing authorization. A readiness request does not itself authorize production data changes, paid load tests, real charges, customer messages, or publication. Prepare locally and use isolated fixtures where possible. Inspect repository scripts before executing them; tests and package hooks can contact live services. Never print credentials or include personal records in evidence.

Define the candidate commit and dirty-tree state, artifact/version, environment, audience, expected workload, and acceptance criteria. Identify which checks must pass before release and which can only happen after rollout. Ask only for missing decisions that affect the verdict or prevent safe progress; continue independent checks. Mark assumptions explicitly.

## Build an evidence ledger

Read the stack checklist and choose the applicable conditional sections. Add checks for the product's business invariants and supported integrations. Include at least one failure or recovery case for each critical journey. Assign stable local check IDs and record:

| Check | Phase | Required? | Status | Evidence | Gap or finding |
| --- | --- | --- | --- | --- | --- |
| AUTH-01 | Before release | Yes | UNVERIFIED | No runnable environment | Test access across two tenants |

Use these statuses consistently:

- `PASS`: observed behavior meets the stated criterion for this candidate and environment.
- `FAIL`: observed behavior violates the criterion. Record severity separately.
- `WARN`: a measured limitation or concern that does not fail a required criterion. Never use this for missing evidence.
- `UNVERIFIED`: unavailable access, a skipped test, inconclusive results, or evidence that cannot be tied to this candidate. State what would close the gap.
- `N/A`: not applicable, with a specific reason. Lack of access is never an N/A reason.

Record command, working directory, relevant tool version, exit result, date, environment, and an artifact/log/test location. For manual checks include steps, expected and observed outcomes, device/browser/runtime, and test data class. Config inspection proves configuration; it does not prove runtime delivery, recovery, or performance. User-provided evidence can be used when its provenance and scope are clear; label it as supplied evidence.

Prefer focused tests over arbitrary coverage percentages. Derive commands from project scripts and CI; examples in references are starting points, not commands to run blindly. A passing scanner does not establish security, and a successful build does not establish a working release. Document unavailable tools; do not install or replace the stack simply to satisfy a checklist.

## Assess consequences and fix within scope

Severity describes impact and exposure, not the name of the missing feature:

| Severity | Decision | Typical consequence |
| --- | --- | --- |
| P0 | Always blocks release | Credible auth bypass, exposed production credential, irreversible loss, duplicate money movement, or unusable primary journey |
| P1 | Blocks unless explicitly accepted | Material reliability, access, accessibility, recovery, or compatibility failure affecting intended users |
| P2 | Track with owner | Bounded defect with a usable workaround and limited impact |
| P3 | Optional improvement | Polish or maintainability with no demonstrated release impact |

Explain reachability, affected users/data, and reproduction before assigning severity. Do not label every scanner alert P0 or every missing tool P1. A policy or contractual release prohibition remains a blocker when applicable; informal risk acceptance does not override it.

When remediation is requested, fix the highest-impact issues within scope and add a regression check when it protects meaningful behavior. Retest affected boundaries and rebuild if the artifact changes. Mark stale evidence and rerun dependent checks. Preserve unrelated changes. Do not introduce broad refactors to pass a readiness review.

For any accepted risk, record the specific finding, the user's explicit acceptance, affected release/environment, mitigation, owner, and expiry or revisit condition. Proposed acceptance is not acceptance. Missing evidence cannot be accepted as a passing test. A required unverified check continues to block readiness; the user can explicitly change scope, and that scope change must remain visible.

## Decide readiness separately from rollout

Report each gate independently; a later check does not erase an earlier failure:

- A, Functionality: critical product journeys and business rules.
- B, Quality: failure handling, compatibility, accessibility, performance, and tests appropriate to the product.
- C, Release preparation: security, data recovery where needed, packaging, configuration, operational ownership, and rollout controls.
- D, Live verification: the distributed/deployed candidate and critical dependencies, monitoring, and smoke checks in the intended environment.

The pre-release verdict uses gates A through C and required pre-release checks. A required `FAIL` or `UNVERIFIED` blocks it, except explicitly accepted P1 findings that are eligible for acceptance. Every P0 blocks. Use the skill's exact verdict wording:

- `READY TO …`: required pre-release checks pass; no open P0/P1 and no accepted material exception. List remaining P2/P3 concerns.
- `READY TO … WITH ACCEPTED RISKS`: required evidence is present, no P0 or mandatory external prohibition remains, and every open P1 has explicit acceptance. Also use this when an accepted material exception qualifies the release despite lower severity.
- `NOT READY TO …`: a blocker or required evidence gap remains.

Report live verification separately as `VERIFIED`, `PARTIAL`, `NOT VERIFIED`, or `N/A` with reason. A release candidate can be ready before publication; it cannot be called shipped or production-verified until gate D passes. A failing post-release check means live verification failed even if the candidate previously passed. Reassess the current readiness verdict when that failure reveals a pre-release defect. Never infer readiness from an aggregate percentage.

## Cross-cutting checks

Apply these to each deployable unit, with proportional depth and an explicit reason for exclusions:

- Trace at least one critical user action through its real persistence and external effects, including cancellation, duplicate submission, denied access, and dependency failure where applicable.
- Test authentication and authorization across users/tenants; inspect secrets, untrusted inputs, logging, dependencies, and least-privilege runtime/CI access. Examine scanner findings for applicability and remediation availability.
- Inventory sensitive data in caches, exports, telemetry, backups, and vendors. Exercise applicable deletion and retention behavior. Review current official requirements for the target market; do not certify legal compliance from code alone.
- Measure critical performance against agreed budgets on representative devices/data/load. State sample size, duration, warm/cold state, and limitations. Do not invent universal latency, coverage, or scale targets.
- For persistent data, test upgrades/migrations on a representative copy and demonstrate restore or recovery against the agreed RPO/RTO. Keep destructive recovery exercises away from production unless explicitly authorized.
- Verify release artifact identity, locked/resolved dependencies, production configuration, and the minimum runtime permissions. Keep diagnostic symbols available to owners without exposing secrets.
- Show how operators detect a failed critical journey, who receives the signal, and how they recover. Use a safe test event or existing delivery evidence; never deliberately crash customer workloads to prove monitoring.
- Separate optional product analytics from operational failure detection. Validate event payloads, consent and duplicates when analytics is required; do not install tracking by default.
- Document deployment/update steps, rollback or roll-forward limits, ownership, and support actions. Mobile/store updates and schema migrations may require forward fixes rather than literal rollback.
- Verify version-sensitive framework behavior, store policies, platform requirements, and security advisories against official documentation for the detected version. Record URL and access date; if unavailable, mark that check unverified instead of guessing a deadline or minimum version.

For applicable business domains, read [domain-checks.md](domain-checks.md). Write the result using [reporting.md](reporting.md).
