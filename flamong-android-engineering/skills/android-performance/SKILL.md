---
name: android-performance
description: Investigate or measure Android startup, rendering, memory, battery or network regressions.
---
# Performance

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Identify a user-visible slow path and a baseline on a stated device and build variant. Measure release-like code rather than using debug timing as a release verdict.
2. Use traces or benchmarks to locate the cost before optimizing. Control fixture data, thermal conditions and repeated runs; compare distributions instead of one favorable sample.
3. Choose the appropriate measurement: startup/rendering benchmarks, memory profiling or work/network analysis. Evaluate Baseline Profiles when relevant and supported by the existing build.

## Verification evidence
Capture before/after measurements with build, device, scenario and variability. Confirm behavior is preserved and report inconclusive results without claiming a speedup.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) for APIs and version-sensitive details relevant to the installed toolchain.
