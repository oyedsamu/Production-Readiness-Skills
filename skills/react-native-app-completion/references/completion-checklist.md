# React Native readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Build identity and native compatibility
- Record React Native/Expo versions, Hermes or other JS engine, architecture configuration, native dependency support, OS targets, and the intended store/update channel.
- Build Android and iOS release candidates independently. Check generated/prebuilt native configuration against app config and config plugins; identify manual changes that regeneration would erase.
- Verify native module/codegen compatibility and production bundle loading with the development server absent. Debug mode cannot establish release behavior.

## Runtime and experience
- Exercise AppState changes, process recreation, permission denial/revocation, linking from cold/warm start, keyboard/insets, platform back behavior, and local notification routing.
- Test async effect/subscription cleanup, stale responses after navigation, unhandled promises, JS/native exceptions, and native module argument validation.
- Measure JS/UI thread responsiveness, startup, large-list behavior, image memory, bridge/JSI work where applicable, and long-session leaks on target hardware.
- Test screen-reader roles/names, focus, large text, reduced motion, RTL/localization, and platform UI differences. JavaScript component snapshots do not prove accessibility.
- Exercise secure credential storage, account switching/cache cleanup, offline persistence upgrades, reconnect/conflicts, refresh races, and idempotent retries.

## Over-the-air updates when used
- Verify runtime/native compatibility rules, channel/branch targeting, update authenticity where supported, and access controls. A JS update must not assume native APIs absent from installed binaries.
- Test interrupted download, failed startup, rollback/fallback to the embedded bundle, offline launch, and database compatibility after an update. Keep update cohorts and artifact identities observable.
- Review current store rules for downloaded functionality and define an authorized rollout/rollback procedure. Mark OTA N/A if not used; do not introduce it to pass the review.

## Native distribution
- Android: inspect release manifest, signing, min/target SDK, ABI/native-library policy, R8, exported components, backups, app links, and notification/background behavior; verify current Play declarations and device upgrade.
- iOS: inspect signing/provisioning, entitlements, privacy/usage declarations, Keychain, universal links, APNs environment, archive/device installation, and current App Store requirements.
- Keep Metro source maps tied to the exact JS bundle and release/update ID plus native symbols. Verify symbolicated diagnostics without sensitive payloads.
- Run critical integration/E2E journeys against the packaged release with native dependencies. For Expo, distinguish Expo Go results from the actual development/release binary.

## Store packaging and first-session gate

Apply [mobile-store-readiness.md](mobile-store-readiness.md) to each shipping mobile host: inspect thumbnail icons, truthful screenshot sequences, first useful outcome, clear and correct paid offers when applicable, and the main task flow. Keep optional conversion experiments separate from release blockers. Record platform/locale/candidate evidence and justified N/A for library-only, non-mobile, non-store, or free-app sections.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [React Native Android release](https://reactnative.dev/docs/signed-apk-android)
- [React Native iOS release](https://reactnative.dev/docs/publishing-to-app-store)
- [Expo runtime versions](https://docs.expo.dev/eas-update/runtime-versions/)
