# Desktop app readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Installation and OS matrix
- Record supported OS versions/architectures, installer formats, runtime/native dependencies, privileges, and distribution channel. Build and install the actual package on each supported platform.
- Test fresh install, upgrade from supported versions, interrupted install/update, uninstall, and retained user data. Exercise paths containing spaces/non-ASCII characters and restricted user accounts.
- Verify signing/notarization or platform trust requirements where applicable, package identity, entitlements, quarantined/downloaded behavior, and current distribution policies.

## Process and OS security
- For Electron, inspect sandbox/context isolation, Node access, preload exposure, IPC sender/argument validation, navigation/window opening, and remote-content privileges.
- For Tauri, inspect capability/permission scopes, commands, filesystem/network access, remote origins, and frontend-to-native argument validation.
- For native apps, inspect IPC, custom URL handlers, file associations, shell invocation, plugin loading, and privilege boundaries. Test untrusted files/URLs from outside the app.
- Protect credentials in platform storage, redact diagnostics, review bundled secrets, and constrain unsafe file traversal/symlink behavior.

## Updates and data safety
- Verify update origin, integrity/authenticity, platform/architecture selection, version ordering, and recovery from interrupted or invalid downloads. Test rollback/forward fixes against migrated user data.
- Exercise local schema/config upgrades, concurrent instances, crashes during writes, disk full, read-only paths, file locking, and recoverable backups for valuable local data.
- Check offline behavior, proxy/certificate environments, session expiry, and cancellation of long-running work. Define ownership of background/tray processes at exit.

## Experience and support
- Test keyboard and assistive technology, high DPI/scaling, multiple displays, window restoration, focus, locale, sleep/wake, and OS theme changes as supported.
- Measure startup, idle CPU/memory, long-session leaks, large file handling, and battery use on representative hardware.
- Verify crash symbols, opt-in diagnostics where applicable, update/support channels, controlled release smoke tests, and ownership of platform-specific failures.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Electron security](https://www.electronjs.org/docs/latest/tutorial/security)
- [Tauri security](https://v2.tauri.app/security/)
