---
name: ios-app-completion
description: "Audit, finish, or prepare native iOS and iPadOS applications using Swift, SwiftUI, or UIKit for production release. Use for readiness reviews or shipping work, not isolated edits without a readiness request."
---

# Native iOS readiness

Review native iOS and iPadOS applications using Swift, SwiftUI, or UIKit. Identify Xcode projects/workspaces, schemes, Swift packages, deployment targets, entitlements, privacy manifests, extensions, and distribution profiles before choosing checks.

## Workflow

1. Read [review-method.md](references/review-method.md) for scope, evidence, severity, authorization, and verdict rules. Preserve audit versus remediation versus release mode.
2. Read [completion-checklist.md](references/completion-checklist.md). Evaluate its relevant sections and the method's cross-cutting checks. Add product-specific invariants and record why any section is not applicable.
3. For sensitive or specialized business behavior, read the matching section of [domain-checks.md](references/domain-checks.md).
4. Record candidate-specific evidence. Fix and retest within scope when remediation is requested. Required checks that cannot run remain `UNVERIFIED`.
5. Use [reporting.md](references/reporting.md). Give one pre-release verdict: `READY TO RELEASE`, `READY TO RELEASE WITH ACCEPTED RISKS`, or `NOT READY TO RELEASE`. Report live verification separately.

An unresolved P0 or required evidence gap blocks readiness. Eligible P1 exceptions require the user's explicit acceptance. Do not claim deployment, distribution, or live verification from a local build.
