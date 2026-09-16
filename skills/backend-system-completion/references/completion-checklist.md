# Backend System Completion Skill

Version: 1.0
Purpose: A reusable production-readiness skill to run whenever the user asks to build, finish, ship, launch, review, or complete a backend system, API, service, or platform.

---

# 1. Trigger

Run this skill whenever the user says anything equivalent to:

- "Build this backend."
- "Build the API."
- "Create this service."
- "Finish this backend."
- "Make this backend production ready."
- "Build the server."
- "Build the backend system."
- "Is this backend done?"
- "Check whether this API is ready to ship."
- "Prepare this service for production."

Do not treat a backend as complete merely because:
- it compiles;
- one happy-path request works;
- the API returns 200;
- it runs locally;
- it passes a few unit tests.

A backend system is **complete** only when:
1. required business capabilities work end-to-end;
2. failure modes are handled intentionally;
3. security and authorization are enforced server-side;
4. data integrity is protected;
5. observability and alerting exist;
6. backup/recovery procedures exist where data matters;
7. deployment and rollback are repeatable;
8. load and reliability expectations have been validated;
9. production verification has been performed where access exists.

---

# 2. Completion Gates

## GATE A — Functional Complete
The required API/business capabilities work end-to-end.

## GATE B — Quality Complete
Validation, error handling, idempotency, data integrity, concurrency behavior, and tests are acceptable.

## GATE C — Production Ready
Security, observability, monitoring, backups, deployment, scaling, resilience, documentation, and operational controls are in place.

## GATE D — Production Verified
The deployed production service, real dependencies, monitoring, alerts, migrations, backups, and critical flows have been tested after release.

Never say "complete" unless all applicable gates pass.

---

# 3. Severity System

Classify every issue:

- **P0 — Launch blocker:** auth bypass, exposed secret, destructive data bug, payment duplication, data corruption, unrecoverable migration, critical outage, broken primary flow.
- **P1 — Must fix before normal launch:** weak authorization, missing monitoring, no backups for critical data, serious performance issue, unsafe retries, unbounded resource use, policy/compliance blocker.
- **P2 — Should fix:** maintainability, minor performance, incomplete docs, edge-case handling, minor resilience issue.
- **P3 — Improvement:** polish, cost optimization, convenience, optional automation.

Final output must clearly show all open P0/P1 items.

---

# 4. Mandatory Backend Shipping Baseline

These are hard baseline checks for a normal production backend.

- [ ] Health/readiness endpoint exists where appropriate.
- [ ] Request validation exists.
- [ ] Server-side authorization exists.
- [ ] Authentication is implemented correctly where required.
- [ ] Structured error responses exist.
- [ ] Sensitive data is not exposed in errors.
- [ ] Rate limiting exists for abuse-sensitive endpoints.
- [ ] Secrets are not committed to source control.
- [ ] Production secrets are managed securely.
- [ ] TLS is required.
- [ ] Database migrations are controlled.
- [ ] Backups exist for critical persistent data.
- [ ] Restore procedure is documented.
- [ ] Logging is structured.
- [ ] Logs exclude passwords, tokens, secrets, and sensitive personal data.
- [ ] Metrics exist for availability, latency, errors, and saturation.
- [ ] Error/exception monitoring exists.
- [ ] Alerts route to a real owner/channel.
- [ ] Timeouts are configured for external dependencies.
- [ ] Retries are bounded and safe.
- [ ] Idempotency exists for retryable/high-risk operations where relevant.
- [ ] Background jobs have failure/retry visibility.
- [ ] CI runs tests/lint/build.
- [ ] Deployment is repeatable.
- [ ] Rollback strategy exists.
- [ ] API documentation exists.
- [ ] Environment separation exists.
- [ ] Debug mode is disabled in production.
- [ ] Dependency/security scanning is performed.
- [ ] Critical production flows are verified after deployment.

Every baseline item must be marked PASS, WARN, FAIL, or N/A with justification.

---

# 5. Product & Business Logic

- [ ] Business requirements are explicit.
- [ ] Core entities are defined.
- [ ] Business rules are implemented server-side where trust matters.
- [ ] Critical invariants are enforced.
- [ ] Edge cases are covered.
- [ ] Duplicate actions are handled.
- [ ] Partial failure behavior is defined.
- [ ] State transitions are explicit.
- [ ] Invalid state transitions are rejected.
- [ ] Destructive actions are protected.
- [ ] Auditability exists where business risk warrants it.
- [ ] Time/date/timezone behavior is intentional.
- [ ] Currency/precision rules are explicit where money is involved.
- [ ] External side effects occur only after intended commit points.
- [ ] No critical rule depends only on client-side enforcement.

---

# 6. API Design

For HTTP/REST APIs:

- [ ] Resource naming is consistent.
- [ ] HTTP methods are used appropriately.
- [ ] Status codes are meaningful.
- [ ] Request/response schemas are stable.
- [ ] Validation errors are structured.
- [ ] Error codes are machine-readable where useful.
- [ ] Pagination exists for unbounded collections.
- [ ] Sort/filter semantics are documented.
- [ ] Field naming is consistent.
- [ ] Nullability is intentional.
- [ ] Timestamps use an explicit standard.
- [ ] IDs are stable and non-ambiguous.
- [ ] API versioning strategy exists where needed.
- [ ] Deprecation strategy exists where needed.
- [ ] Backward compatibility is considered.
- [ ] Partial response/update semantics are clear.
- [ ] Bulk operations have limits.
- [ ] Payload limits exist.
- [ ] File upload limits exist where relevant.

For GraphQL:
- [ ] Query complexity/depth limits considered.
- [ ] N+1 query risk handled.
- [ ] Resolver authorization is enforced.
- [ ] Introspection exposure is intentional.
- [ ] Persisted queries considered where appropriate.

For gRPC:
- [ ] Deadlines/timeouts are used.
- [ ] Retry semantics are intentional.
- [ ] Streaming backpressure is handled.
- [ ] Protobuf compatibility rules are followed.

---

# 7. Authentication

If authentication exists:

- [ ] Password hashing uses a modern password-hashing function.
- [ ] Password reset flow is secure.
- [ ] Verification tokens expire.
- [ ] Session/token expiration is intentional.
- [ ] Refresh token strategy is secure.
- [ ] Token revocation strategy exists where needed.
- [ ] Session fixation is prevented where relevant.
- [ ] Brute-force protections exist.
- [ ] MFA considered for sensitive/admin accounts.
- [ ] Service-to-service authentication is secure.
- [ ] OAuth/OIDC flows follow provider best practices.
- [ ] JWT validation checks issuer, audience, expiry, signature, and algorithm.
- [ ] JWT algorithm confusion is prevented.
- [ ] API keys are scoped and revocable where used.
- [ ] Credential rotation is supported.

---

# 8. Authorization

Authorization must be enforced server-side.

- [ ] Role-based or policy-based access is explicit.
- [ ] Object-level authorization is enforced.
- [ ] Tenant isolation is enforced.
- [ ] Admin-only capabilities are protected.
- [ ] Horizontal privilege escalation attempts fail.
- [ ] Vertical privilege escalation attempts fail.
- [ ] Resource ownership checks are centralized where possible.
- [ ] Authorization is tested independently from UI assumptions.
- [ ] Sensitive fields are filtered by permission.
- [ ] Background jobs preserve authorization/tenant context correctly.
- [ ] Internal service calls do not bypass authorization accidentally.

---

# 9. Input Validation & Injection Defense

- [ ] All external input is treated as untrusted.
- [ ] SQL/NoSQL queries are parameterized.
- [ ] Command execution avoids shell injection.
- [ ] Template injection is prevented.
- [ ] Path traversal is prevented.
- [ ] SSRF risk is controlled.
- [ ] Open redirects are prevented.
- [ ] Deserialization risks are controlled.
- [ ] XML entity expansion disabled where relevant.
- [ ] Regex denial-of-service considered for untrusted patterns.
- [ ] JSON/body size is limited.
- [ ] Header size limits exist.
- [ ] Multipart/file inputs are constrained.
- [ ] URLs and callbacks are validated.
- [ ] Email/phone/usernames normalized appropriately.

---

# 10. Security Baseline

Use OWASP ASVS and OWASP API Security Top 10 as primary references.

## Transport
- [ ] TLS only.
- [ ] Weak protocols/ciphers disabled where managed directly.
- [ ] Internal service encryption considered based on threat model.
- [ ] Certificate validation is enabled for outbound calls.

## Headers / HTTP
- [ ] CORS configured narrowly.
- [ ] Security headers configured where relevant to HTTP clients/browsers.
- [ ] Content types are explicit.
- [ ] Cache headers protect sensitive responses.
- [ ] Host header handling is safe.

## Secrets
- [ ] No secrets in source code.
- [ ] No secrets in container images.
- [ ] No secrets in logs.
- [ ] Secret manager/environment injection used.
- [ ] Production credentials differ from development.
- [ ] Rotation procedure exists.
- [ ] Least privilege applied to service credentials.

## Abuse controls
- [ ] Rate limiting.
- [ ] Burst controls.
- [ ] Resource quotas.
- [ ] Enumeration controls.
- [ ] Signup/login abuse controls.
- [ ] Expensive endpoint protection.
- [ ] Bot controls where relevant.
- [ ] Request size limits.
- [ ] Concurrency limits where needed.

## Supply chain
- [ ] Lockfiles are committed.
- [ ] Dependency vulnerability scan runs.
- [ ] Base images are maintained.
- [ ] Image/package provenance is understood.
- [ ] Unused dependencies removed.
- [ ] Build dependencies are pinned where practical.
- [ ] CI credentials have least privilege.
- [ ] Third-party libraries are reviewed for maintenance/security.

---

# 11. Data Modeling & Integrity

- [ ] Data model matches business invariants.
- [ ] Primary keys are intentional.
- [ ] Foreign keys exist where appropriate.
- [ ] Unique constraints enforce uniqueness.
- [ ] NOT NULL constraints used where appropriate.
- [ ] Check constraints used where useful.
- [ ] Transactions wrap atomic business operations.
- [ ] Isolation level is appropriate.
- [ ] Race conditions are considered.
- [ ] Optimistic/pessimistic locking used where necessary.
- [ ] Money uses safe decimal/integer representation.
- [ ] Timezones stored/handled consistently.
- [ ] Soft-delete behavior is intentional.
- [ ] Referential integrity survives deletion.
- [ ] Audit/history strategy exists where required.
- [ ] Data retention rules are implementable.
- [ ] Tenant partitioning is correct.
- [ ] PII classification is understood.

---

# 12. Database Performance

- [ ] Indexes support major query patterns.
- [ ] Slow queries are identified.
- [ ] N+1 queries are avoided.
- [ ] Query plans reviewed for critical endpoints.
- [ ] Connection pooling configured.
- [ ] Pool exhaustion behavior understood.
- [ ] Long-running transactions avoided.
- [ ] Pagination avoids full scans where possible.
- [ ] Large table growth is considered.
- [ ] Archival/partitioning considered where useful.
- [ ] Database CPU/storage/IO monitored.
- [ ] Replica behavior understood if used.
- [ ] Read-after-write consistency assumptions are explicit.

---

# 13. Migrations

- [ ] Migrations are version-controlled.
- [ ] Migrations run deterministically.
- [ ] Production migration procedure is documented.
- [ ] Backward-compatible deploy strategy used where needed.
- [ ] Destructive migrations require explicit review.
- [ ] Large migrations avoid long table locks where possible.
- [ ] Data backfills are separated from schema changes where useful.
- [ ] Migration failure behavior is understood.
- [ ] Roll-forward/rollback strategy exists.
- [ ] Migration status is observable.
- [ ] Migration tested against realistic data volume where risk warrants it.

---

# 14. Transactions, Idempotency & Concurrency

- [ ] Critical multi-step operations are transactional.
- [ ] Retryable operations are idempotent where necessary.
- [ ] Idempotency keys are scoped and persisted correctly.
- [ ] Duplicate requests cannot create duplicate money/order/state.
- [ ] Race conditions are tested.
- [ ] Double-submit/double-click scenarios are safe.
- [ ] Distributed locks are avoided unless justified.
- [ ] If distributed locks are used, TTL/failure behavior is defined.
- [ ] Compare-and-swap/version checks considered.
- [ ] Exactly-once assumptions are avoided unless actually guaranteed.
- [ ] At-least-once job/message delivery is handled safely.

---

# 15. Caching

- [ ] Cache usage has a clear purpose.
- [ ] Cache keys are namespaced.
- [ ] TTLs are intentional.
- [ ] Sensitive data is not cached improperly.
- [ ] Cache invalidation strategy exists.
- [ ] Stampede/thundering-herd risk considered.
- [ ] Negative caching considered where appropriate.
- [ ] Stale data tolerance is explicit.
- [ ] Redis/memory cache failure degrades gracefully.
- [ ] Cache is not treated as source of truth unless intentionally designed.

---

# 16. Queues, Jobs & Event Processing

- [ ] Background job ownership is clear.
- [ ] Jobs are idempotent where needed.
- [ ] Retry count is bounded.
- [ ] Backoff strategy exists.
- [ ] Dead-letter handling exists.
- [ ] Failed jobs are visible.
- [ ] Poison messages cannot block entire queue.
- [ ] Job payloads are versionable.
- [ ] Large payloads avoided.
- [ ] Queue depth monitored.
- [ ] Processing latency monitored.
- [ ] Worker concurrency is bounded.
- [ ] Duplicate delivery is safe.
- [ ] Ordering assumptions are explicit.
- [ ] Scheduled jobs use correct timezone.
- [ ] Missed schedule behavior is defined.
- [ ] Long-running jobs can resume/retry safely.

---

# 17. Messaging & Event-Driven Architecture

If Kafka/PubSub/RabbitMQ/etc. are used:

- [ ] Event schema is documented.
- [ ] Event versioning strategy exists.
- [ ] Producers and consumers are loosely coupled.
- [ ] Delivery semantics understood.
- [ ] Consumer group behavior understood.
- [ ] Partitioning strategy is intentional.
- [ ] Ordering assumptions documented.
- [ ] Replay behavior is safe.
- [ ] Duplicate event handling is safe.
- [ ] Dead-letter/retry topics exist where useful.
- [ ] Schema registry/compatibility controls considered.
- [ ] Sensitive data in events is minimized.

---

# 18. External Dependencies

For every external API/service:

- [ ] Timeout configured.
- [ ] Retry policy configured.
- [ ] Retry only safe/idempotent operations automatically.
- [ ] Circuit breaker considered for unstable/critical dependencies.
- [ ] Failure fallback behavior exists.
- [ ] Dependency health/latency is monitored.
- [ ] Rate limits are understood.
- [ ] Credential rotation is possible.
- [ ] Sandbox vs production endpoints are separated.
- [ ] Webhook authenticity is verified.
- [ ] Webhook handling is idempotent.
- [ ] Dependency outage does not corrupt internal state.
- [ ] Vendor lock-in/recovery risk understood for critical services.

---

# 19. File Uploads & Object Storage

- [ ] File size limits enforced.
- [ ] MIME/content type validated.
- [ ] File extension not trusted alone.
- [ ] Untrusted uploads are not executed.
- [ ] Malware scanning considered where risk warrants.
- [ ] Object storage permissions are private by default where appropriate.
- [ ] Signed URL expiration is appropriate.
- [ ] User cannot access another user's files.
- [ ] Metadata/EXIF privacy considered.
- [ ] Orphaned uploads cleaned up.
- [ ] Retention/deletion works.
- [ ] CDN caching rules are intentional.

---

# 20. Search

If search exists:

- [ ] Search source of truth is defined.
- [ ] Index update strategy exists.
- [ ] Eventual consistency is acceptable/documented.
- [ ] Reindex procedure exists.
- [ ] Search failures degrade gracefully.
- [ ] Query injection is prevented.
- [ ] Access control is preserved in search results.
- [ ] Sensitive documents are not indexed accidentally.
- [ ] Search latency monitored.
- [ ] Index size/growth monitored.

---

# 21. Payments & Financial Systems

If money moves:

- [ ] Transaction amount is validated server-side.
- [ ] Currency is explicit.
- [ ] Decimal precision is safe.
- [ ] Idempotency is enforced.
- [ ] Duplicate charge protection exists.
- [ ] Payment state machine is explicit.
- [ ] Pending states are supported.
- [ ] Webhook signatures are verified.
- [ ] Webhook processing is idempotent.
- [ ] Reconciliation exists.
- [ ] Refund path exists where required.
- [ ] Ledger/audit trail exists where risk warrants.
- [ ] Provider status is not trusted blindly without reconciliation.
- [ ] Test credentials are absent from production.
- [ ] Secrets are protected.
- [ ] Financial events are auditable.
- [ ] Manual operations require appropriate controls.

---

# 22. Email, SMS & Notifications

- [ ] Production sender identities configured.
- [ ] Bounce/failure handling exists.
- [ ] Rate limits respected.
- [ ] Retry strategy is safe.
- [ ] Duplicate notifications prevented.
- [ ] Templates are versioned/tested.
- [ ] Unsubscribe/preferences respected.
- [ ] Transactional vs marketing distinction is clear.
- [ ] Sensitive content minimized.
- [ ] Provider outage behavior defined.
- [ ] Delivery metrics available.

---

# 23. Privacy & Compliance

Apply based on jurisdiction/domain.

- [ ] Personal data inventory exists.
- [ ] Data collection is minimized.
- [ ] Retention is defined.
- [ ] Deletion workflow exists where required.
- [ ] Export/access workflow exists where required.
- [ ] Data processors are known.
- [ ] Sensitive fields are classified.
- [ ] Encryption at rest considered/applied.
- [ ] Access to production data is controlled.
- [ ] Admin/support access is auditable where appropriate.
- [ ] Data residency requirements considered.
- [ ] Children's-data restrictions considered where relevant.
- [ ] Compliance requirements reviewed for fintech/health/etc.
- [ ] Logs do not become an uncontrolled PII store.

---

# 24. Observability

Use logs, metrics, and traces appropriately.

## Logging
- [ ] Structured logs.
- [ ] Log levels intentional.
- [ ] Request/correlation ID.
- [ ] Tenant/user context where safe.
- [ ] Secrets redacted.
- [ ] PII minimized.
- [ ] Important state transitions logged.
- [ ] Logs searchable.

## Metrics
- [ ] Request rate.
- [ ] Error rate.
- [ ] Latency.
- [ ] Saturation.
- [ ] Queue depth.
- [ ] DB pool usage.
- [ ] Dependency latency.
- [ ] Job failures.
- [ ] Business-critical metrics.

## Tracing
- [ ] Distributed tracing considered for multi-service systems.
- [ ] Trace propagation works.
- [ ] Spans include major dependencies.
- [ ] Sampling is intentional.
- [ ] Sensitive data excluded.

---

# 25. Monitoring & Alerting

- [ ] Uptime monitoring.
- [ ] Readiness/liveness monitoring.
- [ ] Error-rate alerts.
- [ ] Latency alerts.
- [ ] Saturation alerts.
- [ ] Database alerts.
- [ ] Queue backlog alerts.
- [ ] Background job failure alerts.
- [ ] External dependency alerts.
- [ ] Disk/storage alerts where applicable.
- [ ] Certificate/domain expiry monitoring where applicable.
- [ ] Backup failure alerts.
- [ ] Alert owner exists.
- [ ] Escalation path exists.
- [ ] Alert noise is controlled.
- [ ] Alerts are tested.

Suggested signals:
- p50/p95/p99 latency
- 5xx rate
- 4xx anomaly rate
- requests/sec
- CPU/memory
- DB connection saturation
- DB query latency
- queue depth
- job age
- cache hit ratio
- failed auth rate
- payment failure rate
- critical workflow success rate

---

# 26. Reliability & Resilience

- [ ] Timeouts exist everywhere.
- [ ] Retries are bounded.
- [ ] Backoff/jitter used.
- [ ] Circuit breakers considered.
- [ ] Bulkheads/concurrency limits considered.
- [ ] Single points of failure identified.
- [ ] Graceful degradation exists.
- [ ] Dependency failure does not cascade uncontrolled.
- [ ] Startup dependency behavior is intentional.
- [ ] Graceful shutdown works.
- [ ] In-flight requests/jobs handled during shutdown.
- [ ] Health checks reflect real dependency requirements.
- [ ] Load shedding considered for high-scale systems.
- [ ] Chaos/failure testing considered where risk warrants it.

---

# 27. Backups & Disaster Recovery

For important persistent data:

- [ ] Automated backups configured.
- [ ] Backup retention defined.
- [ ] Backups encrypted.
- [ ] Backup access restricted.
- [ ] Restore procedure documented.
- [ ] Restore has been tested.
- [ ] Recovery Point Objective (RPO) defined.
- [ ] Recovery Time Objective (RTO) defined.
- [ ] Regional disaster scenario considered where needed.
- [ ] Object storage backup/versioning considered.
- [ ] Infrastructure configuration is recoverable.
- [ ] Secrets recovery process exists.
- [ ] DNS/domain recovery access is documented.
- [ ] Backup failures alert.

---

# 28. Performance & Load

Measure, do not guess.

- [ ] Expected traffic documented.
- [ ] Critical endpoint latency target exists.
- [ ] Load test performed where risk warrants.
- [ ] Soak test considered for long-running systems.
- [ ] Burst traffic behavior tested.
- [ ] Database remains stable under load.
- [ ] Connection pool sizing tested.
- [ ] Queue backlog behavior tested.
- [ ] Memory growth/leaks checked.
- [ ] CPU saturation behavior understood.
- [ ] Autoscaling policy tested where used.
- [ ] Rate limiting protects system capacity.
- [ ] Expensive queries/endpoints identified.
- [ ] Caching improves actual bottlenecks, not theoretical ones.
- [ ] Capacity headroom exists.

---

# 29. Horizontal Scaling & Distributed Systems

If multiple instances/services are used:

- [ ] Service is stateless where appropriate.
- [ ] Session state is externalized where needed.
- [ ] Shared locks/state are safe.
- [ ] Leader election is correct where used.
- [ ] Clock assumptions are minimized.
- [ ] Duplicate job/event execution is safe.
- [ ] Consistency model is understood.
- [ ] Eventual consistency is acceptable where used.
- [ ] Network partitions considered.
- [ ] Split-brain scenarios considered where relevant.
- [ ] Service discovery is reliable.
- [ ] Load balancer health checks are correct.

---

# 30. Configuration Management

- [ ] Config differs safely by environment.
- [ ] Defaults are safe.
- [ ] Required config fails fast.
- [ ] Secrets are separate from non-secret config.
- [ ] Feature flags documented.
- [ ] Config changes are auditable where important.
- [ ] Dynamic config has rollback.
- [ ] Production configuration is reproducible.
- [ ] Environment variable naming is consistent.

---

# 31. Containers & Runtime

If Docker/Kubernetes/etc. are used:

- [ ] Minimal maintained base image.
- [ ] Non-root runtime user where practical.
- [ ] No secrets baked into image.
- [ ] Health checks configured.
- [ ] Resource requests/limits set.
- [ ] Graceful shutdown works.
- [ ] Signal handling works.
- [ ] Filesystem assumptions are explicit.
- [ ] Image scanning performed.
- [ ] Immutable artifact promoted across environments where possible.
- [ ] Kubernetes readiness/liveness/startup probes are correct.
- [ ] Pod disruption/rolling deployment behavior tested where applicable.

---

# 32. CI/CD

- [ ] Lint.
- [ ] Unit tests.
- [ ] Integration tests.
- [ ] Security/static analysis.
- [ ] Dependency scan.
- [ ] Build/package.
- [ ] Migration validation.
- [ ] Artifact/container creation.
- [ ] Environment promotion is controlled.
- [ ] Production deploy requires appropriate approval/control.
- [ ] Secrets injected securely.
- [ ] Rollback is possible.
- [ ] Deployment status observable.
- [ ] Failed deployment stops/rolls back safely.
- [ ] Release/version metadata captured.

---

# 33. Deployment Strategy

- [ ] Deployment procedure documented.
- [ ] Rolling/blue-green/canary strategy chosen intentionally.
- [ ] Backward compatibility supports mixed-version rollout where needed.
- [ ] Database migration order is safe.
- [ ] Health checks gate traffic.
- [ ] Rollback procedure exists.
- [ ] Rollback tested.
- [ ] Feature flags used for high-risk releases where appropriate.
- [ ] Release can be paused.
- [ ] Deployment does not drop critical background jobs.
- [ ] Post-deploy verification exists.

---

# 34. Testing

## Unit
- [ ] Business rules.
- [ ] Validation.
- [ ] Authorization policy.
- [ ] Utility logic.
- [ ] State transitions.

## Integration
- [ ] Database.
- [ ] Cache.
- [ ] Queue.
- [ ] External API adapters.
- [ ] Auth/token flow.
- [ ] Migrations.

## API/contract
- [ ] Request/response contract tests.
- [ ] Error responses.
- [ ] Pagination.
- [ ] Authorization.
- [ ] Rate limiting where practical.
- [ ] Backward compatibility where needed.

## End-to-end
- [ ] Signup/login/auth flow.
- [ ] Primary business workflow.
- [ ] Payment/transaction workflow.
- [ ] Webhook workflow.
- [ ] Background job completion.
- [ ] Failure/retry path.
- [ ] Admin workflow where applicable.

## Reliability tests
- [ ] Dependency timeout.
- [ ] Retry behavior.
- [ ] Duplicate message/request.
- [ ] Process restart.
- [ ] Queue/job failure.
- [ ] DB reconnect.
- [ ] Cache outage.
- [ ] Partial downstream outage.

---

# 35. API Documentation & Developer Experience

- [ ] OpenAPI/Swagger or equivalent exists where appropriate.
- [ ] Authentication documented.
- [ ] Error model documented.
- [ ] Pagination documented.
- [ ] Rate limits documented.
- [ ] Idempotency documented.
- [ ] Webhooks documented.
- [ ] Example requests/responses exist.
- [ ] Sandbox/test environment documented where applicable.
- [ ] Changelog/versioning documented.
- [ ] SDK/client guidance exists where useful.
- [ ] Internal architecture diagram exists for non-trivial systems.

---

# 36. Admin & Operations

- [ ] Admin access is strongly protected.
- [ ] Admin authorization is server-side.
- [ ] Sensitive admin actions are audited.
- [ ] Manual repair tools are safe.
- [ ] Support tooling can locate relevant records.
- [ ] Dangerous operations require confirmation/approval.
- [ ] Impersonation/support access is controlled and auditable.
- [ ] Operational runbooks exist.
- [ ] Incident ownership/escalation exists.
- [ ] Feature flags can be disabled quickly.
- [ ] Kill switches exist for high-risk integrations where useful.

---

# 37. Cost & Resource Controls

- [ ] Major cost drivers identified.
- [ ] Database growth monitored.
- [ ] Object storage lifecycle policies set.
- [ ] Log retention intentional.
- [ ] Queue/event retention intentional.
- [ ] Autoscaling has sane bounds.
- [ ] Expensive third-party API use is limited/cached where appropriate.
- [ ] Abuse cannot create unlimited infrastructure spend.
- [ ] Budget/cost alerts exist where appropriate.

---

# 38. Documentation & Handoff

- [ ] README explains local setup.
- [ ] Required runtime versions documented.
- [ ] Environment variables documented without secret values.
- [ ] Architecture overview exists.
- [ ] Data model documented.
- [ ] API contracts documented.
- [ ] External services documented.
- [ ] Migration process documented.
- [ ] Deployment documented.
- [ ] Rollback documented.
- [ ] Backup/restore documented.
- [ ] Monitoring/alerts documented.
- [ ] Queue/jobs documented.
- [ ] Feature flags documented.
- [ ] Known limitations documented.
- [ ] Ownership of cloud, domains, DB, secrets, observability, and vendors is clear.

---

# 39. Production Verification

Before calling the backend shipped:

1. Deploy the production artifact.
2. Verify health/readiness.
3. Verify TLS.
4. Verify critical API endpoint.
5. Verify auth.
6. Verify authorization.
7. Verify production DB connectivity.
8. Verify migrations completed.
9. Verify critical write operation.
10. Verify idempotency for high-risk operations.
11. Verify queue/background worker processing.
12. Verify webhook handling if used.
13. Verify analytics/business event if applicable.
14. Verify error monitoring with a safe controlled error.
15. Verify logs are visible and structured.
16. Verify metrics are updating.
17. Verify alerts can fire.
18. Verify backup status.
19. Verify rate limiting/abuse controls.
20. Verify no debug mode/test credentials/staging endpoints.
21. Verify deployment metadata/version.
22. Run smoke tests against production.
23. Confirm rollback path remains available.

---

# 40. Completion Report Format

Whenever this skill is run, return:

## Backend System Completion Report

**Status:** PASS / PASS WITH ISSUES / FAIL  
**Gate reached:** A / B / C / D  
**Production-ready:** Yes / No

### Scorecard
| Area | Status | Critical issue |
|---|---|---|
| Business logic | PASS/WARN/FAIL | ... |
| API design | ... | ... |
| Authentication | ... | ... |
| Authorization | ... | ... |
| Security | ... | ... |
| Data integrity | ... | ... |
| Database/migrations | ... | ... |
| Idempotency/concurrency | ... | ... |
| Queues/jobs | ... | ... |
| External dependencies | ... | ... |
| Observability | ... | ... |
| Monitoring/alerts | ... | ... |
| Reliability | ... | ... |
| Backups/DR | ... | ... |
| Performance/load | ... | ... |
| Testing | ... | ... |
| CI/CD | ... | ... |
| Deployment | ... | ... |
| Documentation | ... | ... |

### Launch Blockers
List every P0 and P1.

### Evidence
For each major category, show evidence:
- tests run;
- endpoints inspected;
- load/performance results;
- security findings;
- migration results;
- backup/restore evidence;
- log/metric/trace verification;
- alert verification;
- deployed version/smoke-test results.

### Remaining Work
List P2/P3 items.

### Verdict
Use exactly one:
- **READY TO DEPLOY**
- **READY TO DEPLOY WITH ACCEPTED RISKS**
- **NOT READY TO DEPLOY**

Never output READY TO DEPLOY with unresolved P0 issues.
Normally do not output READY TO DEPLOY with unresolved P1 issues unless the user explicitly accepts them.

---

# 41. Stack-Specific Extensions

## Node.js / NestJS / Express
- event-loop blocking
- unhandled promise rejection
- request validation pipes/schema
- async error handling
- process signal handling
- connection pooling
- dependency security
- production source maps/logging

## Python / FastAPI / Django / Flask
- ASGI/WSGI worker configuration
- sync work inside async paths
- ORM N+1
- migration correctness
- debug disabled
- secret/settings separation
- task queue handling
- dependency pinning

## Java / Kotlin / Spring Boot / Ktor
- thread pool sizing
- blocking calls on non-blocking executors
- coroutine dispatcher correctness for Ktor
- connection pools
- transaction boundaries
- actuator/health exposure
- JVM memory/GC tuning where needed
- graceful shutdown

## Go
- goroutine leaks
- context cancellation
- timeout propagation
- race detector
- connection reuse
- graceful shutdown
- pprof exposure controls

## .NET
- async/await blocking
- DI scopes
- EF query performance
- secret config
- health checks
- Kestrel/proxy config
- graceful shutdown

## PostgreSQL
- indexes
- connection pool
- transaction/isolation
- vacuum/bloat monitoring
- lock contention
- migration safety
- backup/PITR

## Redis
- eviction policy
- persistence expectations
- TTL strategy
- cache vs source-of-truth distinction
- hot keys
- memory alerts

## Kafka
- partition strategy
- consumer lag
- replay safety
- schema evolution
- DLQ/retry
- exactly-once assumptions

## Kubernetes
- readiness/liveness/startup probes
- requests/limits
- pod disruption
- rolling deploy
- secrets
- network policy
- autoscaling
- graceful termination

---

# 42. Domain-Specific Extensions

### Fintech
- double-entry ledger where appropriate
- reconciliation
- idempotent money movement
- immutable audit trail
- fraud controls
- role separation
- strong admin authentication
- provider reconciliation
- dispute/refund controls

### Healthcare
- sensitive-data access controls
- encryption
- audit logging
- consent
- retention
- break-glass/admin controls
- jurisdictional compliance

### Marketplace
- inventory consistency
- order state machine
- refund/dispute flows
- seller/buyer isolation
- payout reconciliation
- webhook idempotency

### Logistics
- job state consistency
- location event ingestion
- stale-event handling
- offline/retry behavior
- dispatch concurrency
- notification reliability

### AI/LLM backend
- prompt/input validation
- model timeout/retry
- token/cost limits
- abuse limits
- PII handling
- prompt injection boundaries
- retrieval authorization
- model fallback
- output validation
- hallucination-sensitive workflows
- evaluation suite
- tracing/token-cost observability

### Civic/public data
- provenance
- source timestamps
- correction/update history
- immutable source references
- auditability
- search indexing consistency
- editorial/admin controls

The generic checklist is the minimum, not the maximum.

---

# 43. Core Rule for the Backend Builder

When building a backend:

1. implement;
2. test;
3. inspect;
4. fix;
5. re-test;
6. run migrations safely;
7. run security checks;
8. run reliability/load checks appropriate to risk;
9. run this completion skill;
10. resolve P0/P1 issues;
11. deploy if requested and possible;
12. verify production monitoring, backups, and critical flows;
13. only then call it complete.

This skill is a production release gate, not a ceremonial checklist.
