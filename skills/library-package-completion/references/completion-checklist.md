# Library and SDK readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Public contract
- Inventory exported APIs/types, compatibility promises, supported runtimes/frameworks, error/cancellation behavior, and version policy. Compare the candidate to the last published release.
- Test realistic consumers, invalid input, concurrency, disposal, and backward compatibility. Identify source-compatible changes that still alter runtime semantics or binary compatibility.
- For network SDKs, test auth configuration, redacted errors, timeouts, pagination, retry eligibility/idempotency, streaming cancellation, and endpoint overrides without contacting production by default.

## Package contents
- Inspect the exact archive before publication for required code/assets/types/licenses and accidental secrets, fixtures, private source, or build caches.
- Install/resolve the archive in a clean consumer outside the repository with no workspace dependency links. A monorepo build can hide missing exports or unpublished dependencies.
- JavaScript: verify ESM/CJS entrypoints as claimed, export maps, type resolution, peer dependencies, sideEffects/tree shaking, and browser/server boundaries.
- Python: verify wheel/sdist contents, import/package data, dependency markers, and supported interpreters. JVM/.NET/native: verify metadata, linkage/ABI, transitive dependencies, and supported toolchains. Use only applicable branches.

## Supply chain and publication
- Verify license compatibility and required notices, registry name/scope, package ownership, publication credentials, provenance/signing where supported, and scoped CI permissions.
- Check supported-version dependencies and applicable advisories; avoid claiming all dependencies are safe because one scanner passed.
- Rehearse version/tag/release-note generation and publication from the identified artifact. Never publish during an audit; registry releases may be immutable or hard to undo.

## Adoption and recovery
- Execute documented examples against the packaged candidate and verify migration guidance for breaking changes. Test optional features with and without optional dependencies.
- Measure performance/bundle size only where part of the public contract; record reproducible inputs and baseline comparison.
- Define deprecation, security reporting, compatibility support, and bad-release recovery through deprecation/yanking or a forward version according to the registry's actual rules.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [npm package specification](https://docs.npmjs.com/cli/v11/configuring-npm/package-json)
- [Python distribution formats](https://packaging.python.org/en/latest/specifications/section-distribution-formats/)
