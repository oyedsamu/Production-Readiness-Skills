# Native iOS readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Archive and distribution
- Record supported OS/devices, Xcode/Swift versions, scheme/configuration, bundle identifiers, extension targets, signing team, entitlements, and distribution channel.
- Create and inspect the intended release archive/export. Verify profiles/certificates, embedded frameworks, device architectures, minimum OS, and install through the intended test channel when accessible.
- Review current App Store requirements, SDK privacy manifests/signatures where required, usage descriptions, collection disclosures, account deletion, reviewer access, and purchasing rules against real behavior.

## Lifecycle and concurrency
- Exercise cold launch, scene recreation, background/foreground, memory pressure, interrupted authentication, multiple windows where supported, and restoration of drafts/navigation.
- For SwiftUI, test state ownership, task identity/cancellation, repeated appearance, observation updates, and navigation restoration. For UIKit, inspect view-controller containment, observers, delegates, and retain cycles.
- Test actor/main-thread boundaries, callback cancellation, races, retained tasks, and errors crossing async boundaries. Measure rather than infer responsiveness from compiler concurrency checks.

## Platform and storage boundaries
- Test Keychain access groups/accessibility, device lock, logout, backup/restore and reinstall behavior. Verify Core Data/SwiftData or other store migration from supported prior versions and disk-pressure recovery.
- Exercise denied/limited/revoked permissions, photo/file access, approximate/stale location, universal links, extension/app-group isolation, and untrusted URL or web-view inputs.
- Test notification authorization/token changes, APNs environment, foreground/background delivery behavior, and private content. Check background-task expiration and idempotent retry without assuming continuous execution.
- Verify network timeout/cancellation, offline state, refresh races, TLS/ATS exceptions, and production endpoint selection. Inspect bundled config and logs for secrets.

## User experience and rollout
- Complete a critical journey with VoiceOver; test Dynamic Type, contrast, Reduce Motion, keyboard, safe areas, rotation, iPad multitasking, and supported locales/RTL.
- Profile launch, hangs, frame responsiveness, memory, and battery on representative devices. Test the release candidate independently of previews/simulators.
- For purchases, exercise pending, restored, refunded/revoked, and server-verified entitlements with authorized test accounts.
- Match dSYMs to the archive and verify symbolicated diagnostics. Test clean install and upgrade, record phased rollout/stop criteria, backend compatibility, and a forward-fix owner.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Apple distribution](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases)
- [Apple privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files)
