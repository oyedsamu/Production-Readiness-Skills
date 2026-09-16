# PWA readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Install and browser scope
- Record supported browsers/devices and which offline/install/push capabilities are actually promised. Installation eligibility and platform support must be verified against current browser behavior.
- Check manifest identity, names/icons, start URL, scope, display mode, HTTPS, and navigation outside the app. Test installation, standalone launch, uninstall, and existing-install upgrade on target platforms.
- Test login callbacks, deep links, downloads, and system back navigation inside the installed window as well as a normal browser tab.

## Service worker correctness
- Inspect registration scope, lifecycle, activation, and update ownership. Test an old worker with new pages and a new worker with old open tabs; prevent incompatible cache/API combinations.
- Interrupt asset download and installation; verify atomic precache behavior and a usable previous version or recovery path. Test worker termination and restart without relying on memory-only state.
- Review fetch routing so API errors, opaque responses, missing assets, and fallback HTML are not cached as successful content. Avoid unbounded cache growth.
- Partition or exclude authenticated content and clear sensitive caches on logout/account changes. Test private-data exposure while offline or after a different user signs in.

## Offline data and retries
- Define which reads/writes work offline, freshness indicators, conflict policy, and source of truth. Test duplicate/out-of-order writes, network flapping, cancelled operations, and multi-tab races.
- Exercise IndexedDB migrations, quota exhaustion, eviction, unavailable storage, and interrupted writes. Recover without silently deleting irreplaceable unsynced data.
- Background sync and push may be unavailable or suspended; verify fallback/manual retry and user-visible status without promising guaranteed background execution.

## Update recovery and experience
- Test update prompts, deferred reload for unsaved work, bad-release rollback/forward fix, and emergency worker replacement. Verify cleanup retains assets still needed by active clients.
- Check offline and update UI with screen readers and keyboard, denied notification permission, battery/data constraints, and mobile standalone insets.
- Measure cold/warm/offline behavior, install asset size, and cache storage under realistic use. Scope analytics/diagnostics to consent and actual worker/browser support.
- Verify the deployed worker script, cache headers, scope, manifest, release ID, and a full online-to-offline-to-update journey on the intended host.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Service worker lifecycle](https://web.dev/articles/service-worker-lifecycle)
- [Web app manifests](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest)
