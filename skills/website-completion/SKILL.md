---
name: website-completion
description: Build, finish, audit, or launch a website using an evidence-backed production-readiness gate. Use when a user asks to build, complete, ship, launch, redesign, or verify a website, landing page, dashboard, or web application. Do not use for a narrow isolated code edit unless the user also asks whether the site is complete or production-ready.
---

# Website Completion

Treat a rendered interface as progress, not completion. Apply four gates: Functional Complete, Quality Complete, Production Ready, and Launch Verified.

## Workflow

1. Establish the requested product scope, critical journeys, deployment target, and any unavailable credentials or environments.
2. Build or inspect the site within the user's authorization. Do not invent production access or silently broaden the assignment.
3. Before declaring completion, read [references/completion-checklist.md](references/completion-checklist.md) in full and apply every relevant section.
4. Mark checklist items `PASS`, `WARN`, `FAIL`, or `N/A`. `N/A` requires a short reason. Record observable evidence such as commands, tests, URLs, screenshots, headers, analytics events, logs, or configuration.
5. Fix all issues that are safely within scope, then rerun the affected checks. Do not merely list fixable failures when the user asked to build or complete the site.
6. Classify unresolved findings as P0, P1, P2, or P3 using the checklist definitions. Never downgrade an issue to improve the verdict.
7. Deploy and verify the production environment when the user has authorized deployment and access exists. Otherwise distinguish verified implementation from checks that remain pending in production.
8. Deliver the Website Completion Report in the checklist format with one exact verdict: `READY TO LAUNCH`, `READY TO LAUNCH WITH ACCEPTED RISKS`, or `NOT READY TO LAUNCH`.

## Non-negotiable launch baseline

Explicitly evaluate all 20 baseline items in the reference: custom 404; unique page titles and descriptions; above-fold CTA; favicon; robots.txt; sitemap.xml; Open Graph image; image alt text; mobile breakpoints; sticky mobile CTA when appropriate; loading and form-error states; success/thank-you experience; privacy and terms pages; consent controls when legally or technically required; analytics; legitimate contact information; and optimized images.

Use context rather than cargo-cult requirements. For example, a sticky mobile CTA is relevant to conversion journeys, and a cookie banner is required only when consent is required. Never publish a private home address to satisfy the contact-information check.

## Release integrity

- An unresolved P0 always blocks launch.
- Unresolved P1 issues normally block an unconditional ready verdict; only the user can explicitly accept them.
- Do not claim that analytics, monitoring, backups, DNS, TLS, email, payments, or production flows work without direct evidence.
- Security, accessibility, performance, SEO, monitoring, analytics, legal/privacy, deployment, recovery, and handoff checks are part of completion, not optional polish.
- Add the checklist's project-specific extension for civic/public-data, fintech, healthcare, marketplace, AI, content/editorial, or other applicable domains.

When access prevents a check, report it as unverified with the exact action needed; absence of evidence is not a pass.
