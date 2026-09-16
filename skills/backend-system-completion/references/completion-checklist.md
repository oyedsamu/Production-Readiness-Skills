# Backend API readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Contracts and business rules
- Trace critical read/write workflows through persistence and external effects. Test invalid transitions, precision/currency, nullability, timezone boundaries, bulk limits, and partial failure.
- Check HTTP methods/statuses, structured redacted errors, pagination/order, filters, versioning, and backward compatibility with deployed clients. Compare the generated API schema with observed responses.
- For gRPC, verify protobuf compatibility, field-number retention, deadlines/cancellation propagation, streaming backpressure, and retry eligibility; test old/new client combinations.

## Trust boundaries
- Test authentication expiry/revocation, password reset or identity-provider callbacks, refresh races, scoped API keys, and service credentials. Validate token issuer/audience/signature/algorithm where applicable.
- Probe object, field, function, and tenant authorization with multiple roles/users, including administrative actions, batch endpoints, exports, and jobs. Verify changes to roles take effect at the intended time.
- Test parameterized queries, unsafe deserialization, shell/path/template injection, SSRF destinations/redirects, request size limits, and abuse-sensitive endpoints. Check proxy trust, host headers, TLS, CORS, and browser CSRF where relevant.
- Inspect configuration failure behavior, secrets/log redaction, least-privilege data/service access, and reachable dependency vulnerabilities. Do not add arbitrary security headers to non-browser protocols.

## Persistence and concurrency
- Reproduce conflicting writes and duplicate requests. Verify database constraints, transaction isolation, lost-update prevention, durable scoped idempotency, and consistent external effects after commit.
- Apply migrations to a representative prior schema and realistic data volume. Measure locks/backfills and prove mixed-version deploy compatibility; define roll-forward when reversal loses data.
- Test cache miss/outage/stampede and user/tenant key separation. Measure critical query plans, index use, N+1 behavior, pool exhaustion, replica lag, and read-after-write expectations.
- Restore important data into an isolated environment, validate application reads and integrity, and compare elapsed recovery/data loss to RTO/RPO. Include object storage and encryption/key dependencies.

## Dependencies and background work
- Bound connection/request timeouts, retry counts/backoff/jitter, and concurrency across the whole call chain. Cancel downstream work when callers leave; test dependency outage and ambiguous timeout results.
- Verify webhook signatures over the expected raw payload, replay/duplicate safety, event ordering assumptions, queue retry/dead-letter visibility, and scheduled-job timezone/overlap behavior.
- Check file content/size validation, private storage and signed-link access, retention/orphan cleanup, and malicious inputs. Verify search indexes enforce authorization and can be rebuilt after deletion or schema changes.
- For email/SMS, verify sender identity, preferences, controlled delivery, duplicate suppression, provider throttling, and failures without sending test messages to real users.

## Runtime and operations
- Measure representative load and bursts, latency/error distribution, resource/pool saturation, memory growth, queue backlog, and cost bounds. State achieved load and limits; do not infer capacity from one successful request.
- Test startup, readiness, liveness, graceful shutdown, connection drain, and in-flight jobs. Dependency outages must not create uncontrolled restart loops or corruption.
- Verify structured logs, correlation, actionable metrics/traces where useful, redaction, and safe alert delivery to an owner. Protect admin/debug/profiler endpoints.
- Promote an identified artifact with controlled config/migrations. Rehearse pause/rollback or roll-forward, verify production smoke checks and dependency connectivity, and retain operational access/runbooks.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [OWASP API Security](https://api-security.owasp.org/)
- [gRPC deadlines](https://grpc.io/docs/guides/deadlines/)
- [PostgreSQL backup](https://www.postgresql.org/docs/current/backup.html)
