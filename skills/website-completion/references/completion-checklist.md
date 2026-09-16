# Website readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Journeys and content
- Map public routes and the intended visitor action. Follow navigation, search, downloads, and every primary link; verify real content, prices/units, contact details, media rights, and error recovery.
- Exercise forms with invalid input, duplicate submit, network failure, abuse, and successful delivery to a controlled destination. Confirm success messaging matches the actual backend/provider result.
- Test loading, empty, error, denied-access, and confirmation states where applicable. Review destructive actions and preserve form drafts across recoverable errors.
- Check brand assets/favicon, useful page titles/descriptions, valid external links, and appropriate contact information. Never invent trust claims or publish private home addresses to fill a template.

## Browser experience and accessibility
- Choose browser/device coverage from the intended audience. Test a narrow viewport, touch input, zoom/large text, keyboard-visible layout, long localized content, and supported desktop/mobile engines.
- Complete the critical journey with keyboard and a screen reader. Inspect focus visibility/order, modal focus restoration, landmarks/headings, labels, announced errors, contrast, captions, and reduced motion.
- Use meaningful alternatives for informative images and empty alternatives for decorative images. Combine automated accessibility checks with manual interaction; do not infer conformance from a score alone.
- Check sticky headers/CTAs and dialogs for obscured content and focus. A sticky conversion control is a product choice, not a universal requirement.

## Search and delivery
- For indexable pages, inspect generated HTML, canonical URLs, titles, descriptions, social previews, crawlable links, redirects, and real 404 status. Test old URLs after a migration.
- Decide whether robots.txt, a sitemap, structured data, feeds, and locale annotations apply. Validate canonical public URLs and prevent staging/private content leakage; robots.txt is not access control.
- Measure loading, responsiveness, and layout stability on representative mobile conditions. Record lab versus field evidence, percentiles/sample period where available, image/font/JS weight, cache behavior, and third-party overhead.
- Verify production origin, canonical HTTPS redirects, DNS/TLS renewal ownership, compressed assets, cache headers, and deploy identity. Test direct navigation to nested routes on the actual host.

## Security, privacy, and operations
- Inspect delivered bundles/source maps for secrets, unsafe HTML and third-party scripts. Verify CSP/frame controls, MIME handling, cookies, CSRF where applicable, CORS, and sensitive response caching against actual browser behavior.
- Test server-side authorization if accounts exist; hidden navigation is insufficient. Exercise reset/expiry/logout and cross-user access, rate limits, file size/type checks, and error redaction.
- Match privacy, terms, consent, retention, and deletion requirements to actual collection and target markets. Test tracker behavior before and after consent/withdrawal where needed. An informational site without tracking need not add analytics.
- Verify required analytics without duplicate route/form events, and operational failure detection proportional to the site. Confirm production email sender authentication and delivery only where the site sends email.
- For persistent content or submissions, verify backup/restore and upgrade/migration recovery. Check deployment rollback, ownership, admin protection, and safe production smoke tests.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Web accessibility](https://www.w3.org/WAI/test-evaluate/)
- [Web performance](https://web.dev/articles/vitals)
- [OWASP ASVS](https://owasp.org/projects/asvs)
