# Kotlin Multiplatform readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Scope and target evidence
- Distinguish a published shared library from a complete application. Record declared JVM/Android/Native/JS/Wasm targets, host apps, compiler/Gradle versions, and supported consumer toolchains.
- Build and test each shipping target using its actual toolchain. Mark unavailable Apple hardware/toolchains or target runners unverified; commonTest success covers shared logic only.
- Inspect source-set dependencies and platform API leakage. Verify each expect/actual behavior through platform tests, especially secure storage, clock/locale, networking, files, and permissions.

## Interoperability and state
- Test Swift/Objective-C exports for nullability, exceptions, suspend/cancellation bridging, Flow collection cleanup, ownership, and callback threading. Verify Swift callers receive usable errors without process termination.
- Inspect coroutine scope ownership across host lifecycle boundaries, shared mutable state, cancellation, native object retention, and thread confinement assumptions for the configured runtime.
- Test serialization, timezones, numeric precision, network engines/TLS, persistence migrations, and token handling on every host. Shared interfaces do not guarantee identical platform behavior.
- For Compose Multiplatform, verify navigation/state restoration, semantics/accessibility, text input/IME, safe areas, platform back behavior, and platform-view interop on each supported target.

## Packaging and consumer compatibility
- For libraries, inspect root/target publications, Gradle metadata, API/ABI compatibility, dependency exposure, sources/licenses, and artifact coordinates. Resolve the published candidate from a clean consumer outside the repository.
- For Apple frameworks/XCFrameworks, test device and simulator slices, linkage, symbols, transitive exports, host archive/distribution builds, and minimum deployment versions.
- For JS/Wasm or JVM outputs, test supported module/runtime combinations and runtime dependencies from packaged artifacts. Do not claim support for targets that only compile but never execute.

## Host release and operations
- Android hosts need release signing, manifest/SDK/ABI review, R8 testing, upgrade/lifecycle and permission checks, and current channel policy evidence.
- Apple hosts need signing/provisioning, entitlements/privacy declarations, device/archive tests, background/link/notification checks, and current distribution requirements.
- Verify critical journeys and diagnostics across shared and native frames, measure per-target startup/memory, and preserve symbols. Record separate host readiness and library publication verdicts when both ship.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [KMP publication](https://kotlinlang.org/docs/multiplatform/multiplatform-publish-lib-setup.html)
- [Kotlin Swift interoperability](https://kotlinlang.org/docs/native-objc-interop.html)
