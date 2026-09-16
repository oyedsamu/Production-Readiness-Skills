# Event and worker readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Delivery contract
- Define event identity, producer authority, schema/version, partition/routing key, ordering scope, retention, delivery guarantees, and replay expectations.
- Kill a consumer before and after its external/database effect but before acknowledgement. Redeliver the message and verify the business invariant survives duplicates.
- Test concurrent duplicate events, deduplication expiry, idempotency key scope, and retries after partial completion. Broker guarantees alone do not prove exactly-once external effects.
- Verify atomicity between database changes and event publication through the chosen outbox/transaction/reconciliation design. Test publisher crashes and unavailable brokers.

## Failure, ordering, and replay
- Send malformed, poison, stale, and out-of-order messages. Verify retry backoff/limits, dead-letter routing, inspection, alerting, and safe replay tooling.
- Test partition rebalancing, multiple consumers, lock/lease expiration, acknowledgements/offset commits, and graceful shutdown during work.
- Replay a representative historical window with current consumers; validate schema evolution, obsolete user permissions, deleted records, and external effects.
- Scheduled jobs need explicit timezone/DST, missed-run, overlap, catch-up, and lease behavior. Long jobs should resume or restart without duplicate irreversible effects.

## Capacity and protection
- Measure sustainable throughput, oldest-message age, consumer lag, retry amplification, and recovery after an outage. Bound concurrency, payload size, and downstream pressure.
- Review broker/topic permissions, tenant identity, payload data minimization/encryption, retention/deletion, and access to replay/dead-letter tools.
- Verify alerts for stalled consumption, growing age, retry exhaustion, and producer failure. A nonempty queue alone is not necessarily unhealthy.

## Release and recovery
- Test old/new producer-consumer combinations and rollback with queued candidate-version messages. Document incompatible schema rollout order.
- Verify broker/data recovery assumptions, offset recovery, replay source availability, and operator actions under a failed deployment.
- Run a controlled event through the deployed producer, broker, consumer, persistence, and monitoring path; identify every component version in the evidence.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Kafka design](https://kafka.apache.org/documentation/#design)
- [RabbitMQ acknowledgements](https://www.rabbitmq.com/docs/confirms)
