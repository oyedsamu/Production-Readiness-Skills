# Website Completion Skill

Version: 1.0
Purpose: A reusable production-readiness skill to run whenever the user asks to build, finish, ship, launch, redesign, or complete a website.

---

## 1. Trigger

Run this skill whenever the user says anything equivalent to:

- "Build this website."
- "Create this website."
- "Finish this website."
- "Make this production ready."
- "Launch this site."
- "Redesign this site."
- "Build the landing page / dashboard / web app."
- "Is this site done?"
- "Check whether this website is complete."

Do not treat a site as complete merely because the UI renders.

A website is **complete** only when:
1. the requested product experience works;
2. critical user journeys pass;
3. production-readiness checks pass;
4. failures and remaining risks are explicitly reported;
5. launch verification has been performed where deployment access exists.

---

# 2. Completion Levels

Use these gates.

## GATE A — Functional Complete
The requested product works end-to-end.

## GATE B — Quality Complete
Responsive design, accessibility, performance, browser compatibility, edge cases, and content quality are acceptable.

## GATE C — Production Ready
Security, privacy, monitoring, analytics, SEO, deployment, backups, operational readiness, and legal requirements are in place.

## GATE D — Launch Verified
The live production URL, real forms, authentication, analytics events, monitoring, indexing settings, SSL/TLS, redirects, and critical journeys have been tested after deployment.

Never say "complete" unless all applicable gates pass.

---


# 2A. Mandatory 20-Point Shipping Baseline

These 20 items are a **hard baseline** for any normal public-facing website. They must be checked explicitly and surfaced in the completion report.

- [ ] Custom 404 page
- [ ] Meta title on every page
- [ ] Meta description on every page
- [ ] CTA above the fold
- [ ] Favicon set
- [ ] robots.txt file
- [ ] sitemap.xml
- [ ] Open Graph image
- [ ] Alt text on every image
- [ ] Mobile breakpoints
- [ ] Sticky mobile CTA where the product benefits from persistent conversion access
- [ ] Loading states
- [ ] Form error states
- [ ] Thank-you page or equivalent explicit post-submission success experience
- [ ] Privacy policy page
- [ ] Terms and conditions
- [ ] Cookie banner where cookies/trackers or applicable law require consent
- [ ] Analytics installed and verified
- [ ] Real contact address or appropriate verifiable business contact information
- [ ] Compressed/optimized images

## Baseline enforcement

For applicable public websites:

- Missing **analytics**, **privacy/terms where required**, **robots/sitemap**, **page metadata**, **form states**, **mobile behavior**, or a working conversion path should normally be treated as at least **P1**.
- Missing a custom 404, favicon, Open Graph image, image optimization, or similar shipping polish is normally **P2**, unless it creates a larger functional, trust, accessibility, or SEO failure.
- The sticky mobile CTA is **context-sensitive**: require it on conversion-focused sites where persistent access to the primary action materially improves the experience; do not force it onto products where it obstructs content or has no conversion value.
- “Real contact address” should be interpreted safely and appropriately. Prefer a legitimate business/office/postal contact location where one is required or useful; do not publish a founder’s private residential address by default.
- A cookie banner is not automatically required everywhere. It should be implemented when consent is legally required or when non-essential tracking/advertising cookies are used. If only strictly necessary cookies are used, document the decision instead of adding a misleading banner.
- Every baseline item must be marked PASS, WARN, FAIL, or N/A with justification. Do not silently skip items.


# 3. Severity System

Classify every failure:

- **P0 — Launch blocker:** security flaw, broken primary journey, data-loss risk, payment/auth failure, inaccessible production, exposed secret, destructive bug.
- **P1 — Must fix before normal launch:** major UX defect, significant accessibility issue, major SEO/indexing mistake, analytics unavailable, no error monitoring, severe performance issue.
- **P2 — Should fix:** non-critical UX, content, maintainability, minor SEO/performance/accessibility issue.
- **P3 — Improvement:** polish, experimentation, optimization, convenience.

Final output must show open P0/P1 items clearly.

---

# 4. Product & Requirements

- [ ] Primary site objective is clear.
- [ ] Target audience is clear.
- [ ] Primary CTA is obvious.
- [ ] Required pages/routes exist.
- [ ] Required user roles are implemented.
- [ ] Required states and workflows exist.
- [ ] Business rules match the specification.
- [ ] Navigation structure is coherent.
- [ ] Empty states exist.
- [ ] Loading states exist.
- [ ] Error states exist.
- [ ] Success states exist.
- [ ] Permission-denied states exist where relevant.
- [ ] Offline/retry behaviour considered where relevant.
- [ ] Destructive actions require appropriate confirmation.
- [ ] Important actions provide user feedback.
- [ ] No placeholder functionality remains unintentionally.
- [ ] No dead buttons or fake links.
- [ ] No TODO/FIXME that affects launch-critical functionality.
- [ ] No demo/test content unintentionally visible in production.

---

# 5. UI / Visual Completion

Check every important route at minimum on mobile, tablet, laptop, and large desktop.

- [ ] Layout matches approved design/direction.
- [ ] Typography is consistent.
- [ ] Spacing system is consistent.
- [ ] Color usage is consistent.
- [ ] Icons are stylistically consistent.
- [ ] Components share consistent states and behaviour.
- [ ] Navbar is complete.
- [ ] Hero is complete where applicable.
- [ ] CTA sections are complete.
- [ ] Footer is complete.
- [ ] 404 page exists.
- [ ] 500/error experience exists when appropriate.
- [ ] Favicon is set.
- [ ] Brand logo renders correctly.
- [ ] No stretched/blurry assets.
- [ ] Images have intentional crop behaviour.
- [ ] Hover states work.
- [ ] Focus states work.
- [ ] Active states work.
- [ ] Disabled states are visually clear.
- [ ] Long text does not break layouts.
- [ ] Very short content does not break layouts.
- [ ] Tables behave correctly on small screens.
- [ ] Modals and drawers work on small screens.
- [ ] Sticky/fixed UI does not cover important content.
- [ ] Mobile keyboard does not break forms/dialogs.
- [ ] Orientation changes are acceptable where relevant.
- [ ] No horizontal overflow unless intentional.

---

# 6. Responsive Behaviour

Validate representative widths rather than relying only on framework breakpoints.

Suggested test widths:
320, 360, 375, 390, 414, 768, 1024, 1280, 1440, 1920px.

- [ ] Navigation remains usable.
- [ ] Text remains readable.
- [ ] Tap targets remain usable.
- [ ] Forms fit without clipping.
- [ ] Dialogs fit without clipping.
- [ ] Images retain meaningful framing.
- [ ] No important feature disappears accidentally.
- [ ] Content hierarchy remains clear.

---

# 7. Forms & Input

For every form:

- [ ] Labels exist.
- [ ] Required fields are identified.
- [ ] Client validation exists where useful.
- [ ] Server validation exists.
- [ ] Validation messages are clear.
- [ ] Invalid data cannot bypass client checks.
- [ ] Correct keyboard/input type is used.
- [ ] Autofill/autocomplete attributes are sensible.
- [ ] Submit button prevents accidental duplicate submission.
- [ ] Loading state shown during submission.
- [ ] Success state shown.
- [ ] Server/network failure state shown.
- [ ] User input survives recoverable errors where appropriate.
- [ ] File constraints are enforced where uploads exist.
- [ ] Spam/bot protection considered for public forms.
- [ ] Form delivery is verified in production.
- [ ] Email/SMS/webhook side effects are verified where applicable.

---

# 8. Authentication & Authorization

If accounts exist:

- [ ] Signup works.
- [ ] Login works.
- [ ] Logout works.
- [ ] Password reset works.
- [ ] Email/phone verification works where required.
- [ ] Session expiration behaves correctly.
- [ ] Remember-me behaviour is intentional.
- [ ] Account lockout/rate limiting exists where appropriate.
- [ ] MFA considered for sensitive/admin accounts.
- [ ] Role-based permissions are server-enforced.
- [ ] Object-level authorization is enforced.
- [ ] Users cannot access another user's data by changing IDs.
- [ ] Admin pages are actually protected, not merely hidden.
- [ ] Privilege escalation attempts fail.
- [ ] Auth cookies use secure settings.
- [ ] Sensitive actions can require re-authentication where appropriate.

---

# 9. Security

Use OWASP ASVS as the reference baseline for applicable web security verification.

## Transport & headers
- [ ] HTTPS only.
- [ ] HTTP redirects to HTTPS.
- [ ] Valid TLS certificate.
- [ ] HSTS configured where appropriate.
- [ ] Content-Security-Policy configured appropriately.
- [ ] X-Content-Type-Options configured.
- [ ] Referrer-Policy configured.
- [ ] Permissions-Policy reviewed.
- [ ] Clickjacking protection configured via CSP/frame controls.

## Injection & untrusted input
- [ ] SQL/NoSQL queries are parameterized/safely constructed.
- [ ] XSS mitigated through escaping/sanitization.
- [ ] CSRF protected for relevant state-changing requests.
- [ ] Command injection prevented.
- [ ] Template injection considered.
- [ ] SSRF controls exist where URLs can be supplied.
- [ ] Open redirect behaviour prevented.
- [ ] Path traversal prevented.
- [ ] Deserialization risks considered.

## APIs
- [ ] API authorization is server-side.
- [ ] Rate limiting exists for sensitive endpoints.
- [ ] Payload size limits exist.
- [ ] Pagination/limits prevent accidental resource exhaustion.
- [ ] CORS allows only intended origins/methods/headers.
- [ ] Error responses do not leak internals.
- [ ] API versions/deprecation strategy considered where needed.

## Secrets
- [ ] No API keys in frontend bundles unless explicitly public-safe.
- [ ] No credentials committed to source control.
- [ ] Secrets stored in secret/environment management.
- [ ] Production secrets differ from development secrets.
- [ ] Secret rotation procedure exists for sensitive systems.

## Dependencies & supply chain
- [ ] Dependency vulnerability scan passes.
- [ ] Lockfile committed.
- [ ] Critical dependencies are maintained.
- [ ] Unused dependencies removed.
- [ ] Build/deploy dependencies are pinned appropriately.
- [ ] Third-party scripts are reviewed.
- [ ] Webhooks verify signatures where applicable.

## Sensitive data
- [ ] Sensitive data encrypted in transit.
- [ ] Sensitive data encrypted at rest where appropriate.
- [ ] Passwords use a modern password-hashing function.
- [ ] Logs do not contain passwords, tokens, secrets, or sensitive personal data.
- [ ] Data exposure through browser storage reviewed.
- [ ] Cache headers prevent sensitive content being cached improperly.

## Abuse prevention
- [ ] Brute-force protection.
- [ ] Bot/spam controls where relevant.
- [ ] Enumeration risks reviewed.
- [ ] Uploads validated by type and size.
- [ ] Uploaded files are not executed.
- [ ] Malware scanning considered for high-risk upload flows.

---

# 10. Accessibility

Target WCAG 2.2 AA unless the project specifies otherwise.

- [ ] Semantic HTML used.
- [ ] Exactly one meaningful primary H1 where appropriate.
- [ ] Heading order is logical.
- [ ] Landmarks are meaningful.
- [ ] Skip link provided for complex pages where useful.
- [ ] Keyboard-only navigation works.
- [ ] Focus order is logical.
- [ ] Focus is visible.
- [ ] Modals trap and restore focus correctly.
- [ ] Menus work with keyboard.
- [ ] Forms have programmatic labels.
- [ ] Validation errors are announced/readable.
- [ ] Images have meaningful alt text or empty alt when decorative.
- [ ] Icons/buttons have accessible names.
- [ ] Color is not the sole carrier of meaning.
- [ ] Color contrast passes.
- [ ] Text can zoom without breaking layout.
- [ ] Motion respects reduced-motion preferences where appropriate.
- [ ] Video captions/transcripts provided where needed.
- [ ] ARIA used only where needed and correctly.
- [ ] Automated accessibility scan run.
- [ ] Critical flows receive manual keyboard/screen-reader spot checks.

---

# 11. Performance

Measure, do not guess.

Core Web Vitals target at the 75th percentile:
- LCP <= 2.5s
- INP <= 200ms
- CLS <= 0.1

Also verify:

- [ ] Page weight is reasonable.
- [ ] Images use appropriate sizes and modern formats.
- [ ] Responsive images used where useful.
- [ ] Above-the-fold/LCP asset prioritized.
- [ ] Below-the-fold media lazy-loaded appropriately.
- [ ] Fonts optimized and unnecessary weights removed.
- [ ] Render-blocking assets minimized.
- [ ] JavaScript bundle reviewed.
- [ ] Unused CSS/JS minimized.
- [ ] Caching configured.
- [ ] CDN used where beneficial.
- [ ] Compression enabled.
- [ ] Server response time acceptable.
- [ ] Database queries checked for obvious N+1/slow queries.
- [ ] API payloads are not unnecessarily large.
- [ ] Performance tested on mobile throttling, not only fast desktop.
- [ ] No major memory leak in long-lived pages.
- [ ] Third-party scripts do not dominate performance.

---

# 12. SEO / Discoverability

For public pages:

- [ ] Unique page title.
- [ ] Useful meta description.
- [ ] Correct canonical URL.
- [ ] Crawlable links.
- [ ] robots.txt intentional.
- [ ] sitemap.xml exists and reflects canonical public URLs.
- [ ] Staging/dev environment is not indexable.
- [ ] Production is not accidentally noindexed.
- [ ] Redirects preserve intended SEO value.
- [ ] Old URLs redirect appropriately after redesign/migration.
- [ ] Broken internal links removed.
- [ ] 404 pages return real 404 status.
- [ ] Soft-404 behaviour avoided.
- [ ] Structured data added only where appropriate and valid.
- [ ] Organization/Website/Breadcrumb/Article/Product/etc schema considered based on page type.
- [ ] Structured data validated.
- [ ] Open Graph metadata exists.
- [ ] X/Twitter card metadata exists.
- [ ] Social preview image exists.
- [ ] Image alt text is useful.
- [ ] Important content is present in indexable HTML.
- [ ] Pagination/filter/indexing strategy is intentional.
- [ ] hreflang implemented correctly if multilingual/multiregional.
- [ ] Search Console configured where access exists.
- [ ] Sitemap submitted where access exists.
- [ ] Important production URLs inspected after launch.

---

# 13. Content Quality

- [ ] No lorem ipsum.
- [ ] No obvious spelling/grammar issues.
- [ ] Product terminology is consistent.
- [ ] Calls to action use clear language.
- [ ] Empty/placeholder legal pages removed or completed.
- [ ] Contact details correct.
- [ ] Addresses, phone numbers, email addresses verified.
- [ ] Prices and units correct.
- [ ] Dates/timezones displayed intentionally.
- [ ] Copyright year correct/automated where suitable.
- [ ] Broken media removed.
- [ ] External links checked.
- [ ] Downloadable files exist and are current.
- [ ] Content authorship/update date shown where important.
- [ ] Trust information is sufficient for the domain.

---

# 14. Analytics & Measurement

Before adding events, define what success means.

## Baseline
- [ ] Analytics platform installed where appropriate.
- [ ] Production traffic separated from development/test traffic.
- [ ] Page views recorded correctly for SPA routing where applicable.
- [ ] Consent requirements handled where applicable.
- [ ] Personally identifiable/sensitive data is not unintentionally sent.

## Event tracking
Define and validate meaningful events, e.g.:

- page_view
- sign_up_started
- sign_up_completed
- login_completed
- primary_cta_clicked
- search_performed
- form_started
- form_submitted
- checkout_started
- payment_completed
- download_clicked
- share_clicked

For each:
- [ ] Event name documented.
- [ ] Trigger documented.
- [ ] Properties documented.
- [ ] Event fires exactly when expected.
- [ ] Duplicate firing prevented.
- [ ] Funnel can be reconstructed.
- [ ] Campaign/UTM attribution works where relevant.

## Business metrics
- [ ] Primary conversion defined.
- [ ] Supporting funnel metrics defined.
- [ ] Retention/engagement metric defined where applicable.
- [ ] Dashboard/reporting path exists.

---

# 15. Monitoring & Observability

A production website is not complete if failures cannot be detected.

- [ ] Uptime monitoring configured.
- [ ] Health endpoint exists where appropriate.
- [ ] Frontend error tracking configured.
- [ ] Backend exception tracking configured.
- [ ] Structured application logs exist.
- [ ] Request/correlation IDs used where useful.
- [ ] Logs, metrics, and traces correlated where architecture warrants it.
- [ ] Critical jobs/queues monitored.
- [ ] Database/resource saturation monitored.
- [ ] Latency monitored.
- [ ] Error rate monitored.
- [ ] Availability monitored.
- [ ] Key business workflow monitored.
- [ ] Alerts route to a real owner/channel.
- [ ] Alert thresholds are meaningful.
- [ ] Synthetic check runs against at least one critical user journey where justified.
- [ ] Monitoring does not leak secrets/PII.
- [ ] Production diagnostics can distinguish deploy-related regressions.

Suggested baseline signals:
- HTTP 5xx rate
- HTTP 4xx anomaly rate
- p50/p95/p99 latency
- uptime
- CPU/memory if server-managed
- DB connection/latency
- queue depth
- JS error rate
- failed login rate
- failed payment/form rate where applicable

---

# 16. Reliability, Data, Backups & Recovery

If the site stores important data:

- [ ] Database backups configured.
- [ ] Backup retention defined.
- [ ] Restore procedure documented.
- [ ] A restore has actually been tested where risk warrants it.
- [ ] Migration rollback strategy exists.
- [ ] Destructive migrations are reviewed.
- [ ] Idempotency used for sensitive/retryable operations where relevant.
- [ ] Background jobs handle retries/dead letters appropriately.
- [ ] External-service outages degrade gracefully.
- [ ] Timeouts configured for network dependencies.
- [ ] Retry storms avoided.
- [ ] User-visible status/recovery messaging exists.
- [ ] Recovery Point Objective considered.
- [ ] Recovery Time Objective considered.
- [ ] Single points of failure identified.

---

# 17. Payments / Commerce

If money moves:

- [ ] Never store raw card data unless explicitly designed and compliant.
- [ ] Payment provider uses production credentials.
- [ ] Webhook signatures verified.
- [ ] Webhooks are idempotent.
- [ ] Duplicate charge protection.
- [ ] Failed payment states work.
- [ ] Pending payment states work.
- [ ] Refund path works where required.
- [ ] Currency is explicit.
- [ ] Amount is calculated/verified server-side.
- [ ] User cannot alter payable amount client-side.
- [ ] Receipts/confirmations work.
- [ ] Reconciliation data available.
- [ ] Test mode cannot accidentally remain enabled in production.

---

# 18. Email / Notifications

- [ ] Correct production sender/domain.
- [ ] SPF configured where applicable.
- [ ] DKIM configured.
- [ ] DMARC considered/configured.
- [ ] Transactional templates tested.
- [ ] Links point to production.
- [ ] Unsubscribe exists for applicable non-transactional mail.
- [ ] Duplicate notifications prevented.
- [ ] Notification preferences respected.
- [ ] Bounces/failures observable.
- [ ] Rate limiting/abuse prevention exists.

---

# 19. Privacy & Legal

Apply based on jurisdiction, audience, and product.

- [ ] Privacy policy exists where personal data is collected.
- [ ] Terms exist where appropriate.
- [ ] Cookie/consent mechanism exists where legally required.
- [ ] Data collected is minimized.
- [ ] Retention policy considered.
- [ ] User deletion/export workflow exists where required.
- [ ] Third-party processors are identified.
- [ ] Marketing consent is separated where required.
- [ ] Children's-data rules reviewed if relevant.
- [ ] Copyright/trademark usage is lawful.
- [ ] Accessibility/legal obligations reviewed for target market.
- [ ] Company/business disclosures present where required.

---

# 20. Browser & Device Compatibility

At minimum test:
- latest Chrome
- latest Safari
- latest Firefox
- latest Edge
- iOS Safari
- Android Chrome

Also test older/support-matrix versions where the audience requires them.

- [ ] Navigation.
- [ ] Forms.
- [ ] Authentication.
- [ ] Payments if applicable.
- [ ] File upload/download.
- [ ] Clipboard/share APIs.
- [ ] Camera/location APIs if used.
- [ ] Date/time inputs.
- [ ] CSS layout.
- [ ] Fonts.
- [ ] Sticky/fixed elements.

---

# 21. Testing

## Automated
- [ ] Unit tests for important business rules.
- [ ] Integration tests for important boundaries.
- [ ] API tests.
- [ ] Component tests where useful.
- [ ] End-to-end tests for critical flows.
- [ ] Authorization tests.
- [ ] Regression tests for important past bugs.

## Required E2E candidates
- visitor → primary conversion
- signup → verify → login
- login → core task → logout
- password reset
- create/edit/delete key entity
- purchase/payment flow
- search/filter flow
- contact/application submission
- admin moderation/approval where applicable

## CI
- [ ] Tests run in CI.
- [ ] Lint passes.
- [ ] Type checks pass.
- [ ] Build passes.
- [ ] Dependency/security check included where practical.

---

# 22. Deployment / DevOps

- [ ] Production build reproducible.
- [ ] Environment separation exists.
- [ ] Development credentials are not used in production.
- [ ] CI/CD pipeline works.
- [ ] Deployment is repeatable.
- [ ] Rollback procedure exists.
- [ ] Database migration process is controlled.
- [ ] Preview/staging environment available where useful.
- [ ] Branch protections/code review appropriate to team size.
- [ ] Infrastructure configuration documented.
- [ ] Runtime versions pinned/supported.
- [ ] Disk/storage limits monitored where relevant.
- [ ] Scheduled jobs use correct timezone.
- [ ] Server clock/time sync correct.
- [ ] No debug mode in production.
- [ ] Source maps handled intentionally.
- [ ] Production admin/debug interfaces are protected.

---

# 23. Domain, DNS & TLS

- [ ] Correct production domain.
- [ ] www/non-www strategy intentional.
- [ ] Redirect to canonical host.
- [ ] DNS records correct.
- [ ] TLS valid.
- [ ] Certificate auto-renewal confirmed.
- [ ] Mixed content absent.
- [ ] Email DNS records correct if email sent.
- [ ] Old domains/subdomains redirect where appropriate.
- [ ] Staging domains protected/noindexed.
- [ ] Domain ownership/recovery access documented.

---

# 24. Admin & Operations

Where relevant:

- [ ] Admin can manage required entities.
- [ ] Dangerous admin actions protected.
- [ ] Admin audit trail exists for sensitive actions.
- [ ] Support team can locate user/order/request records.
- [ ] Content can be corrected without engineering where intended.
- [ ] Feature flags documented.
- [ ] Operational runbook exists.
- [ ] Escalation contact exists.
- [ ] Status page considered for critical products.

---

# 25. Documentation & Handoff

- [ ] README explains local setup.
- [ ] Required environment variables documented without secret values.
- [ ] Architecture overview exists.
- [ ] Data model documented where useful.
- [ ] External services documented.
- [ ] Deployment procedure documented.
- [ ] Rollback procedure documented.
- [ ] Backup/restore documented.
- [ ] Admin operations documented.
- [ ] Analytics events documented.
- [ ] Monitoring/alerting documented.
- [ ] Known limitations documented.
- [ ] Ownership of domain, hosting, DB, analytics, email, and external services is clear.

---

# 26. Launch-Day Verification

After deploying production:

1. Open the real production URL.
2. Confirm canonical HTTPS host.
3. Test homepage.
4. Test every top-level nav item.
5. Test primary CTA.
6. Test signup/login if present.
7. Test at least one real form submission.
8. Test email/notification delivery.
9. Test real payment in a controlled manner if applicable.
10. Confirm analytics receives production events.
11. Confirm error tracker receives a controlled test error if safe.
12. Confirm uptime monitor sees the site.
13. Confirm robots/indexing settings.
14. Confirm sitemap production URLs.
15. Confirm social sharing preview.
16. Confirm favicon and app icons.
17. Confirm 404 response/status.
18. Verify no staging links or localhost references.
19. Check browser console/network for production errors.
20. Re-run key mobile flow.

---

# 27. Completion Report Format

Whenever this skill is run, return a report in this structure:

## Website Completion Report

**Status:** PASS / PASS WITH ISSUES / FAIL  
**Gate reached:** A / B / C / D  
**Production-ready:** Yes / No

### Scorecard
| Area | Status | Critical issue |
|---|---|---|
| Product/functionality | PASS/WARN/FAIL | ... |
| UI/responsiveness | ... | ... |
| Accessibility | ... | ... |
| Performance | ... | ... |
| Security | ... | ... |
| SEO | ... | ... |
| Analytics | ... | ... |
| Monitoring | ... | ... |
| Reliability/backups | ... | ... |
| Testing | ... | ... |
| Deployment | ... | ... |
| Privacy/legal | ... | ... |
| Documentation | ... | ... |

### Launch Blockers
List every P0 and P1.

### Evidence
For each major category, show the evidence used:
- tests run;
- routes inspected;
- scans/results;
- screenshots where useful;
- live checks;
- logs/events;
- Lighthouse/Web Vitals measurements;
- header/security checks;
- SEO/indexing checks.

### Remaining Work
List P2/P3 items.

### Verdict
Use exactly one:
- **READY TO LAUNCH**
- **READY TO LAUNCH WITH ACCEPTED RISKS**
- **NOT READY TO LAUNCH**

Never output READY TO LAUNCH while an unresolved P0 exists.
Normally do not output READY TO LAUNCH while unresolved P1 issues exist unless the user explicitly accepts them.

---

# 28. Automatic Stack-Specific Checks

Adapt the checklist to the detected stack.

## Next.js / React
- Server/client boundary correctness
- hydration errors
- metadata API
- image optimization
- route caching/revalidation
- server action/API authorization
- bundle size
- environment variable exposure
- error/loading/not-found route behaviour

## Vue / Nuxt
- hydration
- SSR/CSR correctness
- route middleware
- metadata
- runtime config exposure
- bundle/code splitting

## Svelte / SvelteKit
- load/action security
- SSR behaviour
- form actions
- environment separation
- adapter/deployment behaviour

## Laravel / Django / Rails
- production debug disabled
- CSRF/auth middleware
- migrations
- queues/jobs
- cache/session configuration
- storage permissions
- admin exposure
- ORM query performance

## WordPress
- plugin/theme vulnerability status
- administrator hardening
- XML-RPC/rest exposure as applicable
- backups
- caching
- spam protection
- updates
- file editing/config permissions

## Static site
- forms actually have a backend/provider
- 404 behaviour
- cache headers
- build artifact correctness
- redirects
- sitemap/robots/canonical
- third-party script/privacy review

---

# 29. Project-Specific Extension

Before running the generic checklist, derive additional checks from the website itself.

Examples:

### Civic / public-information site
- source provenance
- correction policy
- update timestamps
- citation links
- content moderation
- search relevance
- archival integrity

### Fintech
- authorization/IDOR
- transaction integrity
- audit logging
- reconciliation
- fraud/rate controls
- strong admin security

### Healthcare
- sensitive-data handling
- access logging
- encryption
- retention
- consent
- jurisdictional compliance

### Marketplace
- buyer/seller flows
- dispute/refund
- inventory consistency
- notification reliability
- search/filter quality

### Media/content
- article metadata
- authoring workflow
- canonical URLs
- social cards
- feeds/sitemaps
- structured data
- moderation/editorial workflow

The generic checklist is the minimum, not the maximum.

---

# 30. Core Rule for the Builder

When building a website:
1. implement;
2. test;
3. inspect;
4. fix;
5. re-test;
6. run this completion skill;
7. resolve P0/P1 issues;
8. deploy if requested and possible;
9. run launch verification;
10. only then call it complete.

The skill is not a ceremonial checklist. It is a release gate.
