# Data pipeline readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Data contract and correctness
- Define source ownership, grain, keys, units, timezones, freshness, completeness, and destination consumers. Establish acceptable late/missing data and correction behavior.
- Validate missingness, duplicate keys, join cardinality, referential integrity, schema drift, precision, and reconciliation against independent source totals on representative data.
- Test nulls, malformed rows, timezone/DST boundaries, deletions, source corrections, and empty input. Distinguish a valid zero-row result from a failed or stale extraction.
- Protect restricted rows/columns through staging tables, transformations, exports, and downstream access; masking at the dashboard does not protect intermediate data.

## Incremental and streaming behavior
- Verify watermarks/checkpoints, late arrivals, update/delete propagation, deduplication windows, and partition boundaries. Compare incremental output with a full recomputation on a bounded fixture.
- Interrupt between read, transform, write, and checkpoint commit; restart and confirm no missing or double-counted records. Test partial batches and transactional sink behavior.
- For streaming, exercise out-of-order events, backpressure, poison messages, event versus processing time, and retention gaps.

## Backfills and orchestration
- Run a bounded backfill with isolated destinations or safeguards; prove reruns are idempotent and do not resend external notifications or rewrite unrelated partitions.
- Test dependency failure, task retries, overlap, missed schedules, cancellation, and partial DAG success. Bound retry costs and make manual replay traceable.
- Validate schema/transform deployment compatibility with readers and concurrent jobs. Define atomic publication or visibility rules so consumers do not see incomplete snapshots.

## Operations and recovery
- Measure representative volume/runtime/cost and catch-up capacity. Verify source rate limits, query plans, skewed partitions, storage growth, and compute/concurrency limits.
- Monitor freshness, volume anomalies, quality failures, rejected rows, lag, and lineage by run/version. A green scheduler run is insufficient when data is stale or wrong.
- Verify source replay availability, backup/restore or recomputation, retention, credentials, and the owner of quality incidents. Record evidence of a complete candidate run into its intended destination.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Apache Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests)
