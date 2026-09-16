# ML system readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Dataset and evaluation
- Record dataset origin/rights, labels, time range, population, feature definitions, target leakage checks, and split strategy. Prevent subject/time leakage across train and evaluation sets.
- Compare candidate and baseline on held-out data and relevant slices, including rare or costly errors. Report sample sizes, uncertainty, chosen thresholds, and accepted tradeoffs.
- Test missing/out-of-range inputs, changing categories, class imbalance, calibration where probabilities drive decisions, and out-of-distribution behavior.
- Verify sensitive-data permissions and bias/fairness criteria relevant to the actual decision. Record specialist or regulatory review still needed for consequential uses.

## Training-serving consistency
- Version code, features, dependencies, random seeds where useful, data snapshots, model artifact, and preprocessing together. State reproducibility limits for nondeterministic training.
- Compare training/offline and serving transforms on identical fixtures, including default values, feature order, timezone, precision, and categorical encoding.
- Verify online feature freshness, entity/tenant keys, missing-feature fallback, and point-in-time correctness. Prevent stale or future data from producing misleading evaluations.

## Serving and artifact safety
- Validate artifact provenance and load formats; treat untrusted serialized models as potentially executable. Restrict storage/registry access and inspect dependency vulnerabilities.
- Measure warm/cold latency, batch throughput, CPU/GPU memory, concurrency, and timeout behavior with representative input sizes. Test saturation, model-load failure, and dependency outages.
- Check schema compatibility, version routing, fallback behavior, and batch retry/idempotency. Validate output ranges and business rules before consequential effects.

## Rollout and operations
- Define release criteria and stop conditions before shadow/canary/A-B evaluation. Confirm experimentation does not expose unauthorized data or perform duplicate decisions/actions.
- Monitor missing/stale features, input/output distributions, errors, latency, and delayed outcome quality. Drift alerts need an owner and investigation path; drift alone does not prove degraded accuracy.
- Verify rollback includes compatible preprocessing/features, retention/deletion, model registry recovery, and retraining triggers with evaluation before promotion.
- Run the exact packaged model through the intended inference path and record artifact hash, feature version, environment, and held-out evaluation evidence.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Google ML test score](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)
- [TensorFlow data validation](https://www.tensorflow.org/tfx/guide/tfdv)
