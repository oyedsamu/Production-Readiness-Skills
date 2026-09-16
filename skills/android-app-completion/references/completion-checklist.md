# Android App Completion Skill

Version: 1.0
Purpose: A reusable production-readiness skill to run whenever the user asks to build, finish, ship, launch, redesign, or complete an Android application.

---

# 1. Trigger

Run this skill whenever the user says anything equivalent to:

- "Build this Android app."
- "Create this app."
- "Finish this Android app."
- "Make this app production ready."
- "Prepare this app for Play Store."
- "Ship this Android app."
- "Is this Android app done?"
- "Check whether this Android app is complete."

Do not treat an Android app as complete merely because it builds or launches on one emulator/device.

An Android app is **complete** only when:
1. requested functionality works end-to-end;
2. critical user journeys pass;
3. production-readiness checks pass;
4. unresolved failures and risks are explicitly reported;
5. release-build verification has been performed;
6. Play Store / production-distribution requirements are satisfied where applicable.

---

# 2. Completion Gates

## GATE A — Functional Complete
The requested product works end-to-end.

## GATE B — Quality Complete
UI, UX, accessibility, responsiveness/adaptive layouts, performance, offline/error states, and device compatibility are acceptable.

## GATE C — Production Ready
Security, privacy, analytics, crash monitoring, observability, signing, CI/CD, release configuration, data safety, and operational readiness are in place.

## GATE D — Release Verified
The signed release build has been installed/tested, production services work, crash/analytics events are received, app links/deep links work, store metadata is ready, and critical journeys pass in the release variant.

Never say "complete" unless all applicable gates pass.

---

# 3. Severity System

Classify failures:

- **P0 — Release blocker:** crash on startup, broken primary flow, auth/payment/data-loss issue, exposed secret, insecure sensitive-data handling, signing/release failure.
- **P1 — Must fix before normal release:** major UX/accessibility issue, serious performance issue, analytics/crash monitoring unavailable, Play policy blocker, major device/API incompatibility.
- **P2 — Should fix:** non-critical UX, test coverage, maintainability, minor performance/accessibility issue.
- **P3 — Improvement:** polish, experimentation, optional optimization.

Final output must surface every open P0/P1 item clearly.

---

# 4. Mandatory Android Shipping Baseline

These are hard baseline checks for a normal production Android app.

- [ ] Production app name, icon, and adaptive icon are set.
- [ ] Splash screen is implemented correctly.
- [ ] Correct application ID / package name is used.
- [ ] Version code and version name are set correctly.
- [ ] Release build installs and launches successfully.
- [ ] Custom loading states exist.
- [ ] Empty states exist.
- [ ] Error states exist.
- [ ] Retry states exist.
- [ ] Offline/no-network behavior is handled.
- [ ] Form validation/error states exist where forms are present.
- [ ] Success/confirmation states exist after important actions.
- [ ] Back navigation behaves correctly.
- [ ] Deep links / app links are handled where relevant.
- [ ] Runtime permissions are requested only when needed.
- [ ] Denied-permission states are handled.
- [ ] Accessibility labels/content descriptions exist.
- [ ] Analytics installed and verified.
- [ ] Crash/error monitoring installed and verified.
- [ ] Privacy policy is available where required.
- [ ] Play Store Data Safety inputs are prepared accurately.
- [ ] Sensitive data is not logged.
- [ ] Release signing is configured securely.
- [ ] Min/target/compile SDK configuration is intentional.
- [ ] App tested on multiple screen sizes and at least one physical Android device.
- [ ] Network/API failures do not leave the app in a broken state.
- [ ] No debug UI, test endpoints, mock data, or staging secrets remain in production.
- [ ] Images/assets are optimized.
- [ ] Important screens work in dark/light mode where both are supported.
- [ ] Critical flows work in the release build, not only debug.

Every baseline item must be marked PASS, WARN, FAIL, or N/A with justification.

---

# 5. Product & Functional Completeness

- [ ] Primary app objective is clear.
- [ ] Target user is clear.
- [ ] Main user journeys are documented.
- [ ] All requested screens exist.
- [ ] Navigation is complete.
- [ ] Primary actions work.
- [ ] Business logic matches requirements.
- [ ] Required user roles are implemented.
- [ ] Required states and workflows exist.
- [ ] Empty states exist.
- [ ] Loading states exist.
- [ ] Error states exist.
- [ ] Success states exist.
- [ ] Permission-denied states exist.
- [ ] Offline states exist where applicable.
- [ ] Retry behavior exists.
- [ ] Destructive actions require confirmation where appropriate.
- [ ] User gets feedback after important actions.
- [ ] No dead buttons.
- [ ] No placeholder screens.
- [ ] No unfinished TODO/FIXME affecting release-critical behavior.
- [ ] No accidental test/demo content.

---

# 6. Android UI / UX Quality

Check all important screens on multiple device sizes.

- [ ] UI follows Material / intended design system consistently.
- [ ] Typography is consistent.
- [ ] Spacing is consistent.
- [ ] Color system is consistent.
- [ ] Icons are consistent.
- [ ] Components have clear enabled/disabled/loading/error states.
- [ ] Status bar behavior is correct.
- [ ] Navigation bar / gesture insets are handled.
- [ ] Edge-to-edge layout works intentionally.
- [ ] Keyboard/IME does not cover inputs.
- [ ] Insets are handled correctly.
- [ ] Dialogs fit on small screens.
- [ ] Bottom sheets fit and scroll correctly.
- [ ] Long content scrolls without clipping.
- [ ] Lists recycle/render efficiently.
- [ ] Images do not stretch or pixelate.
- [ ] Text does not overflow unexpectedly.
- [ ] Dynamic text/font scaling is supported.
- [ ] Large fonts do not break critical layouts.
- [ ] Landscape orientation is supported or intentionally locked.
- [ ] Foldables/tablets are handled where relevant.
- [ ] RTL is considered if target audience requires it.
- [ ] Dark mode works where supported.
- [ ] Touch targets are adequately sized.
- [ ] Gesture conflicts are avoided.
- [ ] Back behavior is predictable.

---

# 7. Adaptive Layout / Device Coverage

At minimum test representative categories:

- small phone
- standard phone
- large phone
- tablet where applicable
- foldable where target audience warrants it

Also test:
- low-density / high-density screens
- portrait
- landscape if supported
- gesture navigation
- three-button navigation where relevant

- [ ] No clipped content.
- [ ] No accidental horizontal scrolling.
- [ ] Controls remain reachable.
- [ ] Dialogs/bottom sheets remain usable.
- [ ] Keyboard does not obscure primary actions.
- [ ] Navigation remains understandable.

---

# 8. Navigation & Lifecycle

- [ ] System Back works correctly.
- [ ] Up navigation works correctly.
- [ ] Deep links open the intended destination.
- [ ] App links are verified where applicable.
- [ ] Navigation state restores after process recreation where needed.
- [ ] Rotation/configuration changes do not corrupt state.
- [ ] Background/foreground transitions behave correctly.
- [ ] App survives process death where critical.
- [ ] Saved state is used appropriately.
- [ ] Duplicate navigation is prevented.
- [ ] Multiple taps do not create duplicate screens/actions.
- [ ] External intents fail gracefully if no handler exists.

---

# 9. Forms & User Input

For every form/input flow:

- [ ] Labels/hints are clear.
- [ ] Required fields are identified.
- [ ] Input types are appropriate.
- [ ] Keyboard actions are appropriate.
- [ ] Client validation exists.
- [ ] Server validation exists.
- [ ] Error messages are clear.
- [ ] Invalid input cannot bypass validation.
- [ ] Submit prevents accidental double-taps.
- [ ] Progress/loading state shown.
- [ ] Error recovery works.
- [ ] User input is preserved after recoverable failures.
- [ ] Autofill considered where appropriate.
- [ ] Password fields use appropriate secure input behavior.
- [ ] Sensitive text is not exposed in screenshots/logs where risk warrants protection.
- [ ] File/image selection constraints are enforced.

---

# 10. Authentication & Authorization

If accounts exist:

- [ ] Signup works.
- [ ] Login works.
- [ ] Logout works.
- [ ] Password reset works.
- [ ] Account verification works where required.
- [ ] Session expiration is handled.
- [ ] Expired tokens refresh or fail correctly.
- [ ] Invalid refresh tokens result in clean logout.
- [ ] Auth state survives process death as intended.
- [ ] Secure storage is used for sensitive tokens.
- [ ] Server-side authorization is enforced.
- [ ] Object-level authorization is enforced.
- [ ] Users cannot access another user's data by changing IDs.
- [ ] Admin-only behavior is server protected.
- [ ] MFA considered for sensitive apps.
- [ ] Biometric authentication used only as a local convenience/control where appropriate.
- [ ] Re-authentication required for sensitive actions where appropriate.

---

# 11. Android Security

Use OWASP MASVS / MASTG as the primary mobile-security baseline.

## Secrets & build configuration
- [ ] No private API keys/secrets embedded in APK/AAB.
- [ ] No credentials committed to source control.
- [ ] Production secrets managed through secure backend/build infrastructure.
- [ ] Debug flags disabled in release.
- [ ] `android:debuggable` false in release.
- [ ] Backup behavior reviewed.
- [ ] Cleartext traffic disabled unless explicitly required.
- [ ] Network Security Config reviewed.
- [ ] Certificate pinning considered for genuinely high-risk use cases, with operational tradeoffs understood.
- [ ] ProGuard/R8 configured where appropriate.
- [ ] Obfuscation/minification tested in release.

## Data at rest
- [ ] Sensitive values are not stored in plain SharedPreferences/DataStore.
- [ ] Keystore-backed encryption used where appropriate.
- [ ] Sensitive database fields encrypted where appropriate.
- [ ] Secrets/tokens are not written to logs.
- [ ] Clipboard exposure is considered.
- [ ] Screenshots/recent-app preview restrictions considered for sensitive screens.
- [ ] Cache/temp files do not expose sensitive content.

## Network
- [ ] TLS is required.
- [ ] Cleartext HTTP blocked unless justified.
- [ ] API certificate validation is intact.
- [ ] CORS assumptions are not treated as Android security.
- [ ] API authorization occurs server-side.
- [ ] API rate limiting exists server-side.
- [ ] Request/response logging excludes secrets.
- [ ] WebSocket security reviewed where applicable.

## Components / intents
- [ ] Exported activities/services/receivers/providers are intentional.
- [ ] Unnecessary exported components are disabled.
- [ ] Intent inputs are validated.
- [ ] PendingIntent flags are correct.
- [ ] Deep link parameters are validated.
- [ ] WebView JavaScript/interfaces are reviewed.
- [ ] WebView URL loading is restricted as appropriate.
- [ ] FileProvider is configured safely.
- [ ] ContentProvider permissions are reviewed.
- [ ] Broadcast receiver exposure is reviewed.

## Reverse engineering / tampering
- [ ] Sensitive business rules are not trusted solely on-device.
- [ ] Root/emulator/tamper checks used only where risk justifies them.
- [ ] Play Integrity API considered where abuse prevention requires it.
- [ ] Anti-tamper measures do not become the sole security boundary.

---

# 12. Permissions & Privacy

- [ ] Every permission is necessary.
- [ ] Dangerous permissions requested at runtime.
- [ ] Permission requested at the moment of need.
- [ ] Rationale shown where useful.
- [ ] Denial is handled gracefully.
- [ ] "Don't ask again" behavior handled.
- [ ] Background location avoided unless truly required.
- [ ] Contacts/SMS/call logs used only when necessary and policy-compliant.
- [ ] Media/photo access uses modern scoped APIs.
- [ ] Notifications permission handled on supported Android versions.
- [ ] Privacy policy reflects actual data handling.
- [ ] Data collection minimized.
- [ ] Retention/deletion policy considered.
- [ ] Third-party SDK data collection reviewed.
- [ ] Play Data Safety form matches actual behavior.
- [ ] Account deletion flow exists if required by policy/product.
- [ ] Consent flows exist where legally required.

---

# 13. Accessibility

Target Android accessibility best practices and WCAG principles where applicable.

- [ ] TalkBack works on critical flows.
- [ ] Interactive controls have meaningful accessible names.
- [ ] Decorative images are ignored appropriately.
- [ ] Content descriptions are not redundant.
- [ ] Reading/focus order is logical.
- [ ] Touch target sizes are adequate.
- [ ] Color is not the only way to convey meaning.
- [ ] Contrast is sufficient.
- [ ] Dynamic font scaling is supported.
- [ ] Large text does not break layouts.
- [ ] Custom components expose correct semantics.
- [ ] Error messages are announced appropriately.
- [ ] Motion/animation respects accessibility needs where appropriate.
- [ ] Switch Access / keyboard navigation considered where relevant.
- [ ] Accessibility Scanner or equivalent checks run.
- [ ] Manual TalkBack spot check performed on critical flows.

---

# 14. Performance

Measure on release builds and realistic hardware.

- [ ] Cold startup measured.
- [ ] Warm startup measured.
- [ ] No obvious main-thread I/O.
- [ ] No network/database work blocks UI thread.
- [ ] StrictMode or equivalent checks considered during development.
- [ ] ANR risk reviewed.
- [ ] Jank monitored on critical screens.
- [ ] Compose recomposition behavior reviewed where applicable.
- [ ] RecyclerView/list rendering is efficient.
- [ ] Images are appropriately resized/cached.
- [ ] Large bitmaps are avoided.
- [ ] Memory usage is reasonable.
- [ ] Memory leaks checked.
- [ ] Background work uses correct APIs.
- [ ] WorkManager used where appropriate for deferrable guaranteed work.
- [ ] Battery impact considered.
- [ ] Network calls are cached/deduplicated where sensible.
- [ ] Database queries are efficient.
- [ ] App size reviewed.
- [ ] Unused resources removed where appropriate.
- [ ] Baseline Profiles considered for performance-sensitive apps.
- [ ] Startup profile/performance improvements considered.
- [ ] App tested on a lower-end device/emulator profile, not only flagship hardware.

---

# 15. Networking / API Reliability

- [ ] Connection timeouts configured.
- [ ] Read/write timeouts configured.
- [ ] Retry behavior is safe.
- [ ] Non-idempotent actions are not blindly retried.
- [ ] Offline behavior is intentional.
- [ ] User can retry failed requests.
- [ ] API errors map to useful UI messages.
- [ ] 401/403 handling is correct.
- [ ] 429 handling is correct.
- [ ] 5xx handling is correct.
- [ ] Malformed responses do not crash app.
- [ ] API schema changes fail safely.
- [ ] Pagination works correctly.
- [ ] Duplicate requests avoided.
- [ ] Request cancellation works when UI disappears where appropriate.
- [ ] Background sync respects lifecycle/network constraints.

---

# 16. Local Data / Database

- [ ] Local persistence has clear ownership.
- [ ] Room/schema migrations are implemented.
- [ ] Migration tests exist where important.
- [ ] Destructive migration is not accidentally enabled for production-critical data.
- [ ] Encryption considered for sensitive local data.
- [ ] Cache invalidation strategy exists.
- [ ] Offline-first conflict behavior is defined where relevant.
- [ ] Corrupt database handling considered.
- [ ] User logout clears appropriate local data.
- [ ] Multi-user data isolation works on shared devices.
- [ ] Timezones/date persistence is intentional.

---

# 17. Notifications

If push/local notifications exist:

- [ ] Notification permission flow handled.
- [ ] Notification channels configured.
- [ ] Channel importance is appropriate.
- [ ] Notification tap opens correct screen.
- [ ] Deep-link payload is validated.
- [ ] Duplicate notifications prevented.
- [ ] Notification IDs/grouping behave correctly.
- [ ] Sensitive content is not exposed on lock screen unless intended.
- [ ] Token refresh is handled.
- [ ] Invalid/expired device tokens cleaned up server-side.
- [ ] User preferences are respected.
- [ ] Marketing opt-in requirements handled.

---

# 18. Background Work

- [ ] Correct Android background API selected.
- [ ] WorkManager used for deferrable guaranteed work where appropriate.
- [ ] Foreground services used only when justified.
- [ ] Foreground service types/permissions are correct.
- [ ] Doze/App Standby behavior considered.
- [ ] Background restrictions tested.
- [ ] Jobs are idempotent where required.
- [ ] Retries use sane backoff.
- [ ] Infinite retry loops avoided.
- [ ] Battery/network constraints are declared correctly.
- [ ] Background work survives process death where necessary.

---

# 19. Analytics & Product Measurement

Before adding events, define success.

## Baseline
- [ ] Analytics SDK configured only in intended variants.
- [ ] Development/test traffic separable from production.
- [ ] Personally identifiable or sensitive data is not unintentionally sent.
- [ ] Consent gating implemented where required.
- [ ] User IDs are handled appropriately.

## Suggested events
- app_open
- onboarding_started
- onboarding_completed
- sign_up_started
- sign_up_completed
- login_completed
- primary_action_started
- primary_action_completed
- search_performed
- item_viewed
- form_submitted
- payment_started
- payment_completed
- share_clicked
- notification_opened

For each:
- [ ] Event documented.
- [ ] Trigger documented.
- [ ] Properties documented.
- [ ] Duplicate events prevented.
- [ ] Event fires in release build.
- [ ] Funnel can be reconstructed.
- [ ] Attribution/deep link campaign parameters work where relevant.

---

# 20. Crash Monitoring & Observability

A production app is not complete if failures cannot be detected.

- [ ] Crash reporting configured.
- [ ] Non-fatal errors can be reported.
- [ ] ANR monitoring configured where available.
- [ ] Release/version metadata attached to reports.
- [ ] User/session identifiers handled in a privacy-safe way.
- [ ] Network/API failure signals available.
- [ ] Critical workflow failures observable.
- [ ] Backend logs correlate with mobile requests where architecture allows.
- [ ] Alerts exist for abnormal crash/error spikes.
- [ ] Release regressions can be compared by version.
- [ ] Sensitive data excluded from reports.
- [ ] Controlled test crash/error verified in non-production or safe production context.

Suggested production signals:
- crash-free users
- crash-free sessions
- ANR rate
- app start latency
- network error rate
- failed login rate
- failed payment/transaction rate
- sync failure rate
- critical workflow completion rate

---

# 21. Payments / Financial Transactions

If money moves:

- [ ] Amount is calculated/verified server-side.
- [ ] Client cannot alter trusted transaction amount.
- [ ] Payment state machine is clear.
- [ ] Pending states handled.
- [ ] Failure states handled.
- [ ] Retry does not double-charge.
- [ ] Idempotency exists where appropriate.
- [ ] Webhook/server reconciliation exists.
- [ ] Receipt/confirmation shown.
- [ ] Refund behavior works where required.
- [ ] Currency explicit.
- [ ] Test credentials removed from production.
- [ ] Sensitive payment data not logged/stored improperly.
- [ ] Play billing used where required by Play policy.
- [ ] Purchase acknowledgement/consumption handled where applicable.
- [ ] Restore purchases/subscriptions works where applicable.

---

# 22. Camera / Media / Files

If the app handles files/media:

- [ ] Modern Photo Picker used where appropriate.
- [ ] Scoped storage respected.
- [ ] FileProvider configured correctly.
- [ ] MIME type validated.
- [ ] File size limits enforced.
- [ ] Large images compressed/resized.
- [ ] EXIF/privacy implications considered.
- [ ] Failed upload/download states handled.
- [ ] Temporary files cleaned up.
- [ ] Untrusted files are not executed.
- [ ] Camera permission requested only when needed.

---

# 23. Location

If location is used:

- [ ] Location permission is genuinely necessary.
- [ ] Approximate vs precise behavior considered.
- [ ] Foreground-only location preferred.
- [ ] Background location justified and policy-compliant.
- [ ] Permission denial handled.
- [ ] GPS disabled state handled.
- [ ] Location timeout handled.
- [ ] Stale location handled.
- [ ] User understands why location is needed.
- [ ] Sensitive location data minimized and protected.

---

# 24. Testing

## Unit tests
- [ ] Business rules.
- [ ] Validation logic.
- [ ] ViewModel/state reducers.
- [ ] Mapping/parsing.
- [ ] Important utility logic.

## Integration tests
- [ ] Repository/data layer.
- [ ] Database migrations.
- [ ] API integration boundaries.
- [ ] Auth/token flows.

## UI tests
- [ ] Critical Compose/View screens.
- [ ] Navigation.
- [ ] Form validation.
- [ ] Permission handling.
- [ ] Loading/error/success states.

## End-to-end candidates
- install → onboarding → signup/login
- login → primary task → completion
- password reset
- offline → retry → recovery
- deep link → destination
- push notification → destination
- create/edit/delete core entity
- checkout/payment
- logout → local data cleanup

## Test quality
- [ ] Tests run in CI.
- [ ] Flaky tests identified.
- [ ] Tests do not rely unnecessarily on production services.
- [ ] Release variant gets meaningful verification.

---

# 25. Build Configuration

- [ ] `minSdk` intentional.
- [ ] `targetSdk` current enough for Play requirements.
- [ ] `compileSdk` intentional.
- [ ] Debug/release build types configured.
- [ ] Product flavors configured correctly if used.
- [ ] Environment URLs separated.
- [ ] Debug tools excluded from release.
- [ ] Release logging minimized.
- [ ] BuildConfig fields reviewed for secret leakage.
- [ ] Manifest placeholders correct.
- [ ] R8/minification tested.
- [ ] Resource shrinking tested.
- [ ] Native ABI configuration correct if native libs used.
- [ ] 64-bit requirements met.
- [ ] AAB generation works.
- [ ] Reproducible release build process documented.

---

# 26. Signing & Release Security

- [ ] Release keystore not committed to source control.
- [ ] Keystore backup/recovery plan exists.
- [ ] Signing credentials access restricted.
- [ ] Play App Signing enabled/considered.
- [ ] Upload key handled securely.
- [ ] Key rotation/recovery process understood.
- [ ] Release SHA fingerprints documented where needed.
- [ ] OAuth/Firebase/etc production fingerprints configured.
- [ ] Signed AAB/APK verified.
- [ ] Debug-signed artifacts cannot be confused with production releases.

---

# 27. CI/CD

- [ ] Lint runs.
- [ ] Unit tests run.
- [ ] Static analysis runs.
- [ ] Build runs.
- [ ] Release build can be produced automatically or reproducibly.
- [ ] Secrets injected securely.
- [ ] Dependency vulnerability checks considered.
- [ ] Code review / branch protection appropriate.
- [ ] Versioning process defined.
- [ ] Changelog/release notes process defined.
- [ ] Internal testing track deployment supported where useful.
- [ ] Rollout can be paused.
- [ ] Rollback/re-release strategy exists.

---

# 28. Play Store Readiness

- [ ] App title ready.
- [ ] Short description ready.
- [ ] Full description ready.
- [ ] App icon ready.
- [ ] Feature graphic ready where required.
- [ ] Phone screenshots ready.
- [ ] Tablet screenshots ready if applicable.
- [ ] Privacy policy URL ready.
- [ ] Contact email/site ready.
- [ ] App category selected.
- [ ] Content rating completed.
- [ ] Target audience declaration accurate.
- [ ] Ads declaration accurate.
- [ ] Data Safety form accurate.
- [ ] Permissions declarations accurate.
- [ ] Financial/health/news/etc policy requirements reviewed where relevant.
- [ ] Account deletion requirement handled where applicable.
- [ ] App access instructions supplied if review requires login.
- [ ] Testing track requirements satisfied where applicable.
- [ ] Store listing matches actual functionality.
- [ ] No misleading screenshots/claims.
- [ ] Release notes prepared.

---

# 29. App Links / Deep Links

- [ ] URI schemes are intentional.
- [ ] Android App Links use HTTPS where appropriate.
- [ ] `assetlinks.json` configured where verified links are used.
- [ ] Links route correctly from cold start.
- [ ] Links route correctly while app already running.
- [ ] Invalid/malicious parameters handled.
- [ ] Auth-required deep links resume correctly after login.
- [ ] Fallback behavior exists when destination unavailable.

---

# 30. Dependency & SDK Hygiene

- [ ] Dependencies are actively maintained.
- [ ] Known high-severity vulnerabilities reviewed.
- [ ] Unused libraries removed.
- [ ] SDKs do not collect unexpected data.
- [ ] Advertising/analytics SDK privacy reviewed.
- [ ] Transitive dependencies reviewed where risk warrants it.
- [ ] Versions pinned via catalog/lock strategy where appropriate.
- [ ] Deprecated Android APIs identified.
- [ ] Experimental APIs are intentional.

---

# 31. Architecture & Maintainability

- [ ] Clear separation of UI/domain/data concerns.
- [ ] State management is predictable.
- [ ] Dependency injection is coherent.
- [ ] Repository boundaries are meaningful.
- [ ] Error handling is centralized where useful.
- [ ] Network models and domain models are not coupled unnecessarily.
- [ ] Coroutine scopes respect lifecycle.
- [ ] Dispatchers are appropriate.
- [ ] Flows/streams are collected lifecycle-safely.
- [ ] Cancellation is handled.
- [ ] No obvious memory leaks.
- [ ] Configuration/secrets are not scattered.
- [ ] Feature/module boundaries are appropriate to project size.
- [ ] Code style/lint rules are consistent.

---

# 32. Jetpack Compose Checks

If Compose is used:

- [ ] State hoisting is appropriate.
- [ ] Unidirectional data flow is clear.
- [ ] Composables avoid unnecessary side effects.
- [ ] `LaunchedEffect`, `DisposableEffect`, etc. are keyed correctly.
- [ ] Recomposition-sensitive code reviewed.
- [ ] Stable/immutable models considered where useful.
- [ ] Lazy lists use stable keys.
- [ ] `remember` / `rememberSaveable` used correctly.
- [ ] State survives configuration/process recreation where needed.
- [ ] Navigation state is correct.
- [ ] Semantics/accessibility properties are present.
- [ ] Preview-only/demo code excluded from production behavior.
- [ ] Compose UI tests cover critical states.

---

# 33. XML/View System Checks

If classic Views are used:

- [ ] ViewBinding/DataBinding lifecycle usage is correct.
- [ ] Fragment view binding is cleared appropriately.
- [ ] RecyclerView adapters avoid leaks.
- [ ] DiffUtil/ListAdapter used where appropriate.
- [ ] Lifecycle-aware observers are used.
- [ ] Configuration changes handled.
- [ ] Navigation/back stack behavior correct.
- [ ] Layouts scale correctly across screens.
- [ ] Accessibility content descriptions/labels present.

---

# 34. Coroutines / Flow

- [ ] No `GlobalScope` for app business work.
- [ ] Lifecycle-aware scopes used.
- [ ] Exceptions handled intentionally.
- [ ] Cancellation respected.
- [ ] Blocking calls moved off main thread.
- [ ] Flow collection uses lifecycle-aware APIs.
- [ ] Hot/cold stream behavior understood.
- [ ] SharedFlow/StateFlow replay semantics intentional.
- [ ] Backpressure/event duplication considered.
- [ ] One-off UI events are not accidentally re-fired after rotation.

---

# 35. Offline / Sync

If offline capability exists:

- [ ] Source of truth defined.
- [ ] Sync direction defined.
- [ ] Conflict strategy defined.
- [ ] Retry strategy defined.
- [ ] Connectivity changes handled.
- [ ] Offline edits queued safely.
- [ ] Duplicate sync prevented.
- [ ] User sees sync status where important.
- [ ] Partial failures are recoverable.
- [ ] Clock/time conflict assumptions reviewed.
- [ ] Background sync constraints configured appropriately.

---

# 36. Documentation & Handoff

- [ ] README explains setup.
- [ ] Required Android Studio/JDK versions documented.
- [ ] Environment configuration documented.
- [ ] API environments documented.
- [ ] Build variants/flavors documented.
- [ ] Release process documented.
- [ ] Signing process documented securely.
- [ ] External services documented.
- [ ] Analytics events documented.
- [ ] Crash monitoring documented.
- [ ] Push notification setup documented.
- [ ] Deep link/app link setup documented.
- [ ] Known limitations documented.
- [ ] Ownership of Play Console, Firebase, signing keys, backend, analytics, and notification services is clear.

---

# 37. Release Verification

Before calling the Android app shipped:

1. Build the signed release AAB/APK.
2. Install the release build on a physical device.
3. Launch from a clean install.
4. Test onboarding.
5. Test signup/login.
6. Test primary user journey.
7. Test network failure.
8. Test retry.
9. Test background → foreground.
10. Test process death/relaunch on critical state where relevant.
11. Test deep link/app link.
12. Test push notification if used.
13. Test runtime permissions.
14. Test denied permissions.
15. Test dark/light mode where supported.
16. Test large font scaling.
17. Test TalkBack on at least one critical journey.
18. Verify analytics event reaches production analytics.
19. Verify crash/non-fatal monitoring using safe controlled test.
20. Verify no debug/staging endpoint or logging remains.
21. Verify release signing identity.
22. Upload to internal/closed testing track where applicable.
23. Install from Play-distributed test build where possible.
24. Re-test primary flow from distributed artifact.
25. Confirm Play Console policy/data safety metadata.

---

# 38. Completion Report Format

Whenever this skill is run, return:

## Android App Completion Report

**Status:** PASS / PASS WITH ISSUES / FAIL  
**Gate reached:** A / B / C / D  
**Production-ready:** Yes / No  
**Play Store-ready:** Yes / No / N/A

### Scorecard
| Area | Status | Critical issue |
|---|---|---|
| Product/functionality | PASS/WARN/FAIL | ... |
| UI/adaptive layouts | ... | ... |
| Navigation/lifecycle | ... | ... |
| Accessibility | ... | ... |
| Performance | ... | ... |
| Security | ... | ... |
| Permissions/privacy | ... | ... |
| Networking/offline | ... | ... |
| Analytics | ... | ... |
| Crash monitoring | ... | ... |
| Testing | ... | ... |
| Build/signing | ... | ... |
| CI/CD | ... | ... |
| Play Store readiness | ... | ... |
| Documentation | ... | ... |

### Release Blockers
List every P0 and P1.

### Evidence
For each major category, show evidence:
- tests run;
- devices/API levels tested;
- release build result;
- profiler/performance observations;
- security/config checks;
- crash monitoring verification;
- analytics event verification;
- Play Console checks where available.

### Remaining Work
List P2/P3 items.

### Verdict
Use exactly one:
- **READY TO RELEASE**
- **READY TO RELEASE WITH ACCEPTED RISKS**
- **NOT READY TO RELEASE**

Never output READY TO RELEASE with unresolved P0 issues.
Normally do not output READY TO RELEASE with unresolved P1 issues unless the user explicitly accepts them.

---

# 39. Stack-Specific Extensions

## Firebase
- Firebase project separation between dev/prod
- SHA fingerprints correct
- Crashlytics verified
- Analytics verified
- FCM token refresh
- Remote Config defaults
- Firestore/Realtime DB security rules reviewed
- Storage rules reviewed
- App Check considered where useful

## Retrofit / OkHttp
- timeouts configured
- auth interceptor safe
- token refresh race conditions handled
- logging disabled/redacted in release
- TLS/network config reviewed

## Room
- migration tests
- indexes
- transactions
- destructive migration policy
- schema export/versioning

## Hilt / Dagger / Koin
- scopes correct
- no leaked Activity/Fragment references
- test replacement strategy works
- production graph builds correctly

## WorkManager
- unique work behavior intentional
- constraints correct
- retries/backoff correct
- idempotency
- observability of failed jobs

---

# 40. Project-Specific Extensions

Before running the generic checklist, derive additional checks from the app domain.

### Fintech
- transaction integrity
- reconciliation
- device/session risk
- audit logging
- strong auth
- secure storage
- Play Integrity where appropriate
- screenshot/clipboard controls on highly sensitive screens
- anti-fraud controls
- idempotent money movement

### Healthcare
- sensitive-data handling
- encryption
- access logging
- consent
- retention
- notification privacy
- screenshot/lock-screen exposure
- jurisdictional compliance

### Marketplace
- buyer/seller flows
- inventory consistency
- payment/refund/dispute
- push reliability
- search/filter quality
- media upload handling
- moderation/reporting

### Logistics / mobility
- background location
- battery impact
- offline operation
- map/navigation fallback
- stale GPS handling
- job state consistency
- notification reliability

### Media/content
- offline caching
- playback lifecycle
- DRM where applicable
- download storage
- notifications
- deep links
- share flows

### Enterprise
- MDM constraints
- SSO
- certificate/proxy environments
- audit logging
- managed configuration
- work profile compatibility where required

The generic checklist is the minimum, not the maximum.

---

# 41. Core Rule for the Android Builder

When building an Android app:

1. implement;
2. test;
3. inspect;
4. fix;
5. re-test;
6. build a release variant;
7. run this completion skill;
8. resolve P0/P1 issues;
9. distribute through the intended test/release channel where possible;
10. run release verification;
11. only then call it complete.

The skill is a release gate, not a ceremonial checklist.
