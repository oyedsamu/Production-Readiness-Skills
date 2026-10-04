# Flutter app readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Target and release matrix
- Record Flutter/Dart versions, target OS/device support, renderer assumptions, flavor/entrypoint/defines, native build versions, and plugin compatibility. Review each declared shipping target independently.
- Build the actual release bundle for each target using project commands. Verify production identifiers/endpoints/assets; Dart defines and bundled assets cannot hold server secrets.
- Inspect native plugin permissions, entitlements, privacy collection, ABI requirements, and release-only failures. A successful Dart analysis does not verify a platform channel implementation.

## Dart state and native boundaries
- Test widget disposal during asynchronous operations, stream/subscription cleanup, route restoration, repeated navigation, and stale callbacks. Exercise state recovery after OS process recreation.
- Verify isolate message/error handling, cancellation policy, and heavy work placement. Measure UI/raster performance and memory on representative hardware in profile mode, then smoke test release.
- Probe platform channels/FFI with missing permissions, malformed values, cancellation, and native exceptions. Validate text encoding, nullability, file/resource lifetimes, and thread expectations.
- Exercise offline cache/schema upgrades, token refresh races, deep links from cold/warm start, duplicate purchases/actions, and session/account switching.

## Platform-specific release checks
- Android: inspect merged manifest, signing certificate, SDK/ABI/native-library compatibility, R8/resource shrinking, backups/exported components, runtime permissions, app links, notification channels, and interrupted background work.
- Android: verify current Play requirements and disclosures, install a release APK or generated split set, and upgrade an existing installation without losing data. An AAB alone is not an installation test.
- iOS: verify archive/export identity, provisioning/entitlements, minimum OS/device architecture, privacy manifests/usage descriptions, Keychain behavior, universal links, APNs environment, and TestFlight/device installation when applicable.
- Web: test renderer/browser compatibility, semantics, routing/base path, browser storage, cache/update behavior, CSP, payload size, and indexability if public discovery matters.
- Desktop: verify signing/notarization where applicable, bundled native dependencies, installer/update permissions, file paths, and uninstall/data retention on supported operating systems.

## Experience and rollout
- Test Semantics with TalkBack/VoiceOver or the target's assistive technology, font scaling, focus traversal, keyboard/insets, reduced motion, locales/RTL, and platform navigation expectations.
- Run meaningful Dart unit/widget tests and integration tests through plugin-dependent critical journeys. Capture target-specific evidence; emulated plugins do not prove native integration.
- Preserve obfuscation/symbol mapping and native symbols; verify diagnostic readability and SDK consent. Document compatibility across app/backend versions and pause/forward-fix plans.

## Store packaging and first-session gate

Apply [mobile-store-readiness.md](mobile-store-readiness.md) to each shipping mobile host: inspect thumbnail icons, truthful screenshot sequences, first useful outcome, clear and correct paid offers when applicable, and the main task flow. Keep optional conversion experiments separate from release blockers. Record platform/locale/candidate evidence and justified N/A for library-only, non-mobile, non-store, or free-app sections.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Flutter Android release](https://docs.flutter.dev/deployment/android)
- [Flutter iOS release](https://docs.flutter.dev/deployment/ios)
- [Flutter performance](https://docs.flutter.dev/perf)
