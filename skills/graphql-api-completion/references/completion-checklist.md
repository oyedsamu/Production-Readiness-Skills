# GraphQL API readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Schema and authorization
- Diff the candidate schema against deployed consumers. Test nullability, enum additions, deprecated fields, input defaults, and client error handling rather than assuming additive changes are harmless.
- Probe object/field/mutation authorization, nested traversal, global node IDs, aliases, batching, and tenant switching. Authorization must hold at the resolver/data boundary.
- Test pagination bounds, stable cursors/order, input validation, file uploads if supported, redacted errors, and deliberate partial-data behavior.

## Resource and data isolation
- Measure nested, wide, aliased, and batched operations; enforce appropriate cost/depth/list/concurrency limits. HTTP request counts alone do not bound query work.
- Inspect DataLoader and response cache scope across concurrent users/tenants. Verify stale permission changes and mutations invalidate or bypass sensitive cached results.
- Measure resolver N+1 and database calls on representative queries. Propagate cancellation/deadlines and cap downstream fanout.
- Treat persisted operations and introspection configuration as controls with explicit threat assumptions; disabling introspection does not secure unauthorized resolvers.

## Federation and subscriptions
- For federation, validate composition, entity ownership, key resolution, gateway authentication propagation, subgraph access, and compatibility through a rolling deployment.
- For subscriptions, test connect/refresh/revocation, per-event authorization, tenant isolation, reconnect, dropped/duplicate events, backpressure, and disconnect cleanup.
- Inspect cookie-authenticated operations for CSRF/origin issues and websocket origin validation where relevant. Separate public diagnostics from internal schema/error details.

## Release and observability
- Test consumer operations against the actual candidate, including an authorization failure, expensive query, partial downstream outage, and old-client compatibility.
- Observe operation-level error/latency/cost with safe labels; avoid logging raw queries/variables containing private data or exploding metric cardinality.
- Verify artifact/schema IDs, gateway/subgraph rollout order, rollback compatibility, production endpoint behavior, and the owner of breaking-change decisions.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [GraphQL security](https://graphql.org/learn/security/)
- [GraphQL performance](https://graphql.org/learn/performance/)
