# Browser extension readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Permissions and trust
- Record supported browser/manifest versions, extension identity, distribution channel, declared permissions, and host access. Justify requested privileges against actual features.
- Validate messages by sender/origin and payload at privileged handlers. Test hostile web pages/content scripts trying to trigger downloads, read tabs, access cookies, or execute privileged actions.
- Inspect content-script isolation, DOM injection, CSP, external connections, remote code, web-accessible resources, and unsafe evaluation. Verify current store/browser restrictions.
- Test optional permission denial/revocation and restricted pages. Explain unavailable features without requesting broader permissions than needed.

## Lifecycle and data
- Terminate/restart the extension background worker/page during critical work. Persist necessary state; do not rely on long-lived globals or timers where the runtime can suspend them.
- Test tab/window closure, navigation, browser restart, alarms, duplicate events, and concurrent messages. Bound retries and avoid repeating irreversible side effects.
- Exercise local/sync storage quotas, schema migration, account changes, uninstall/reinstall behavior, and deletion/retention. Never store secret credentials in page-accessible DOM or logs.

## UI and compatibility
- Test popup/options/content UI with keyboard and assistive technology, zoom, narrow layouts, dark themes, localization, and pages with conflicting CSS.
- Run actual packaged candidates across supported browsers and manifest implementations. Verify API capability fallbacks rather than assuming Chromium/Firefox parity.
- Measure injection overhead, memory, CPU, and large-page behavior; ensure listeners/scripts do not accumulate after navigation.

## Publication and updates
- Inspect packaged files for secrets/debug artifacts, correct identity/version, permissions changes, privacy disclosures, and required store metadata.
- Test update migrations, failed update/restart, and compatibility between content scripts already injected and a newly updated background context.
- Verify signing/store installation where available, safe diagnostic delivery, release stop/forward-fix procedure, and current review rules for remote behavior and data collection.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Chrome extension security](https://developer.chrome.com/docs/extensions/develop/security-privacy/stay-secure)
- [Extension worker lifecycle](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle)
- [Firefox publishing](https://extensionworkshop.com/documentation/publish/)
