# Conditional backend runtime checks

Read only the runtime and storage sections found in the project. Derive commands from its CI and pinned toolchain. These checks supplement [completion-checklist.md](completion-checklist.md); they do not require replacing the current architecture.

## Node.js, Express, and NestJS

- Exercise blocking CPU/synchronous I/O on busy request paths and measure event-loop delay under load. Offload expensive work only when measurements and workload warrant it.
- Verify rejected promises reach the intended error boundary; test streaming disconnects and aborted requests. Ensure unexpected process failures produce diagnostics and a safe restart.
- Check middleware order, validation/coercion, proxy trust, raw-body webhook handling, request size limits, and authentication coverage on every route.
- Test SIGTERM drain, connection reuse/pool closure, and job cancellation. Inspect production source maps and runtime environment flags without exposing secrets.

## Python, Django, Flask, and FastAPI

- Verify ASGI/WSGI server choice, worker/thread counts, startup hooks, and per-worker memory/connection pools. Avoid multiplying a database pool beyond capacity as workers scale.
- Exercise blocking operations inside async handlers and cancellation of disconnected requests. Inspect ORM lazy evaluation and N+1 behavior with actual query counts.
- For Django/Flask, verify production settings, trusted hosts/proxies, CSRF/session configuration, admin access, migration order, and debug exposure. For FastAPI, inspect dependency lifetime and background task durability assumptions.
- Test task queue retries, graceful worker shutdown, and shared database transaction boundaries. Verify the packaged environment resolves the locked or constrained dependencies.

## JVM, Spring Boot, and Ktor

- Measure heap/native memory, GC pauses, thread pools and database pools under representative load. Inspect container memory behavior and avoid tuning without evidence.
- For Spring, verify transaction propagation/proxy boundaries, async work outside transactions, validation, and secured management endpoints.
- For Ktor/coroutines or reactive stacks, verify dispatcher/executor placement, cancellation, blocking libraries, and backpressure. A non-blocking API can still invoke blocking dependencies.
- Exercise graceful termination, in-flight requests, serialization/reflection in optimized packaging, and mixed-version API/schema compatibility.

## Go

- Run relevant tests with the race detector where supported; exercise concurrent business invariants, not just serial happy paths.
- Verify context/deadline propagation, HTTP client/server timeouts, response-body closure, goroutine lifetime, bounded channels, and cancellation under dependency stalls.
- Inspect connection reuse, shared client state, signal handling, server drain, and protected profiling endpoints. Use runtime profiles when investigating leaks or contention.

## .NET

- Exercise async cancellation, thread-pool starvation from blocking calls, scoped service lifetime, and background service shutdown.
- Inspect EF query counts/tracking, transaction boundaries, migrations, and pool behavior. Test concurrent writes against real database constraints.
- Verify forwarded headers/proxy trust, Kestrel/request limits, authentication policy coverage, secret configuration, and health endpoint exposure.

## PostgreSQL and relational storage

- Inspect critical query plans with representative data; avoid executing destructive or expensive production analysis without authorization. Check indexes, lock contention, long transactions, pool limits, and replica consistency.
- Verify maintenance/vacuum and storage growth, migration lock behavior, uniqueness/isolation under concurrency, and recovery from lost connections.
- Validate a restore or point-in-time recovery into a separate environment, including roles, extensions, schema, encrypted-key access, and application reads.

## Redis and other caches

- State whether the service is a cache or an authoritative store. Review eviction policy, memory ceilings, persistence/recovery where required, TTLs, hot keys, and key/tenant scope.
- Test unavailable cache, stampede, stale values, and deletion/invalidation. A cache eviction must not silently remove an authoritative idempotency or financial record.
- If locks are used, test expiry and stale lock holders; validate fencing or equivalent protection where late writers can violate invariants.

## Container and orchestrated deployments

- Verify signal propagation, PID 1 behavior, non-root permissions, writable paths, resource requests/limits, and the artifact actually deployed.
- For Kubernetes, test startup/readiness/liveness separately, disruption/rolling-update capacity, secret/network policy, and request/job drain before termination.
- Do not make a shared dependency outage trigger endless liveness restarts. Observe service behavior during a controlled failure.

## Documentation

Use official documentation for the installed runtime before choosing commands or version-dependent behavior: [Node.js](https://nodejs.org/api/), [Django deployment](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/), [Spring Boot](https://docs.spring.io/spring-boot/reference/), [Go race detector](https://go.dev/doc/articles/race_detector), [.NET performance](https://learn.microsoft.com/en-us/aspnet/core/performance/performance-best-practices), [PostgreSQL](https://www.postgresql.org/docs/current/), and [Redis](https://redis.io/docs/latest/).
