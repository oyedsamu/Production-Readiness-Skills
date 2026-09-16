# Native Android readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Candidate and platform matrix
- Record application ID, version code/name, min/target/compile SDK, AGP/JDK/Kotlin versions, variants, ABI support, and distribution channel. Inspect the merged release manifest and packaged resources.
- Build the intended signed release candidate; verify certificate identity and separate upload keys from distribution signing keys. Keep secrets outside source, artifacts, and logs.
- Test fresh installation and upgrade from the oldest supported installed version, including persistent data and auth. Install a device-compatible APK or store-generated split set; an AAB is not directly installable.
- Verify current target API, native library/page-size, device, developer-verification, and store policy requirements for the actual release channel. Capture current official evidence instead of hard-coding deadlines.

## Lifecycle, UI, and accessibility
- Exercise rotation, configuration changes, background/foreground, system process recreation, cold start, and back navigation during a critical task. Distinguish Activity recreation from process death and force-stop behavior.
- Preserve required navigation and draft state without repeating one-time effects or transactions. Reopen a protected deep link after login; reject malformed URIs and unauthorized resource IDs.
- Test phone/tablet/foldable layouts where supported, large font/display scaling, RTL/localization, keyboard and system insets, dark mode, and edge-to-edge behavior. Measure readability and clipping on actual target configurations.
- Complete a critical journey using TalkBack and alternative input where supported. Check semantic names, focus order, errors, contrast, touch targets, and reduced-motion expectations.
- Profile startup, frame jank, ANRs, memory growth, and battery on representative hardware using a suitable profiling build. Retest critical behavior in release; debug timings are not release evidence.

## Compose, Views, and concurrency
- For Compose, test saved state restoration, stable lazy-list identity, effect keys/cancellation, and semantics. Check recomposition with measurements before proposing stability annotations or refactors.
- For Views, inspect Fragment view-binding cleanup, lifecycle-aware observers, RecyclerView identity, and adapter/listener references after destruction.
- For coroutines/Flow, test cancellation propagation, dispatcher use for blocking work, repeated collectors, and replay of one-time events. Verify DI scopes do not retain an Activity or Fragment beyond its lifetime.

## Storage, networking, and background work
- Upgrade each supported Room/local schema with representative data. Verify constraints, transaction boundaries, disk-full/corruption handling, logout cleanup, and account separation; reject destructive fallback for irreplaceable data.
- Exercise offline writes, reconnect, conflicting edits, expired tokens, concurrent refresh, 429/5xx, malformed payloads, and request cancellation. Bound retries and preserve idempotency across process restarts.
- Inspect WorkManager constraints, unique-work policy, backoff, and exhausted retries; test interrupted work and duplicate execution. Validate foreground service behavior against supported OS requirements.
- Exercise notification permission denial, channel preferences, token refresh, cold/warm tap routing, and private lock-screen content. Verify production provider/project selection without sending to customers.

## Platform security and integrations
- Review exported components, intent validation, pending-intent configuration, URI grants, FileProvider scope, backup rules, cleartext traffic, and WebView origin/bridge access. Probe external entry points with adversarial test inputs.
- Treat values in BuildConfig, resources, assets, and native binaries as recoverable by clients. Check Keystore-backed storage and recovery/key invalidation behavior where used; obfuscation is not secret storage.
- Test permission denial, permanent denial, revocation, and limited access. For camera/files/location test scoped storage or picker behavior, MIME/content/size validation, EXIF exposure, temporary cleanup, approximate/stale location, and disabled sensors.
- For Firebase, verify release project and certificate fingerprints, rules against cross-user reads/writes, storage access, FCM refresh, and safe Remote Config defaults. App attestation does not replace authorization.

## Distribution and operations
- Test R8/resource shrinking, reflection/serialization, JNI loading, release DI graph, and production endpoints in the actual candidate. Preserve mapping/native symbols and demonstrate useful crash symbolication.
- Check app name/icons/splash, accurate screenshots, audience/rating, reviewer access, privacy/data-safety disclosures including SDK collection, account deletion, and applicable billing declarations.
- Record CI release commands, artifact identity, key recovery owner, staged rollout controls, backend compatibility with old clients, and a forward-fix path. Verify a Play-distributed test install when Play is the intended channel.
- Verify a safe diagnostic reaches the intended monitoring project with correct version and no sensitive payload. Separate store submission, store approval, rollout, and device verification as distinct evidence.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Android release preparation](https://developer.android.com/studio/publish/preparing)
- [Android app quality](https://developer.android.com/quality)
