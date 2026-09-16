# Infrastructure readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Change boundary and state
- Inventory environments/accounts/regions, desired resources, owners, provider/tool versions, state backend, and the exact plan/candidate. Inspect scripts for implicit apply/destroy behavior.
- Validate configuration and review a plan against the intended environment; identify replacements, deletions, drift, dependencies, and cost/quota changes. A plan is not evidence that resources exist or work.
- Verify state locking, encryption, access control, backup/recovery, and secret exposure in plans/outputs. Never publish raw state or secret-bearing plan files as evidence.
- Test modules in an isolated environment when authorized and clean up only resources created for the test. Production apply/destroy requires explicit scope authorization.

## Identity, network, and runtime
- Check least-privilege IAM/service accounts, short-lived CI credentials where supported, environment separation, public ingress, egress, private storage, encryption/key ownership, and reachable admin endpoints.
- For containers, verify maintained base image, artifact digest/provenance, non-root execution where feasible, filesystem/capabilities, resource bounds, and signal handling.
- For Kubernetes, test startup/readiness/liveness, requests/limits, disruption budgets, scheduling, rollout availability, secrets/network policy, and graceful drain of requests/jobs.
- Inspect DNS/TLS issuance/renewal, load balancer routing, health semantics, and failure isolation. Avoid probes that restart every replica during a shared dependency outage.

## Capacity and recovery
- Measure or obtain evidence for capacity, autoscaling boundaries, quota headroom, zone failures, storage growth, and cost alarms under the intended workload.
- Restore state/configuration and critical persistent volumes/data in a safe environment. Verify key/secret access and practical RTO/RPO, not merely enabled snapshots.
- Test failed rollout and recovery, including irreversible resource or schema changes. Distinguish traffic rollback from data restoration.

## Operations and delivery
- Verify logs/metrics/audit events, retention, redaction, alert routes, escalation, and ownership for infrastructure and application failures.
- Review CI plan/apply separation, reviewed artifact identity, environment protections, state migrations/imports, and emergency access procedures.
- After authorized apply, compare observed resources to the plan and test DNS/TLS, routing, permissions, workload health, and recovery access. Report provisioned and workload-verified as separate evidence.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan)
- [Kubernetes production](https://kubernetes.io/docs/setup/production-environment/)
- [Kubernetes probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
