# Serverless and edge readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Provider execution model
- Record provider/runtime versions, regions, trigger types, limits, and deployment identity. Verify current official limits rather than copying numbers from another provider.
- Test cold start, warm reuse, concurrent invocations, deadline termination, and ephemeral filesystem behavior. Do not rely on process memory for durable state or user isolation.
- Confirm awaited/background work fits the provider lifecycle. Test cancellation and partial completion when an invocation times out.

## Trigger and permission boundaries
- Verify HTTP auth, event-source permissions, binding scopes, secret separation, and least-privilege deployment/runtime roles. Inspect public routes and staging bindings in the deployed config.
- Exercise duplicate/retried events, partial batch failure, poison messages, dead-letter destinations, and scheduler overlap for actual trigger semantics.
- Test provider-specific runtime APIs, native module support, request streaming, body limits, and regional data placement where relevant.

## Capacity and dependency behavior
- Load a bounded representative workload within authorized cost limits; measure cold/warm latency, throttles, concurrency, downstream pool use, and retry storms.
- Verify database pooling/proxy strategy, connection lifecycle, dependency timeouts, and backpressure so scaling functions cannot overwhelm shared services.
- Check quotas, abuse controls, budget alarms, fanout limits, and log retention. Confirm a client request cannot create unbounded billable work.

## Deployment and recovery
- Inspect packaged artifact and provider-resolved configuration, aliases/versions, environment separation, and managed resource changes before deployment.
- Rehearse traffic shift/rollback and compatibility with durable state or migrations. Edge routing rollback does not automatically reverse storage changes.
- Verify deployed routes/triggers with controlled inputs, dependency access, useful logs/traces, and alert delivery. Record which provider-managed guarantees were documented versus directly tested.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [AWS Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Cloudflare Workers limits](https://developers.cloudflare.com/workers/platform/limits/)
- [Azure Functions reliability](https://learn.microsoft.com/en-us/azure/azure-functions/performance-reliability)
