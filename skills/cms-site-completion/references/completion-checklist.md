# CMS and content site readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Editorial and content correctness
- Exercise draft, preview, approval, scheduled publishing, correction, unpublish, and restore as the actual editor roles. Test timezone boundaries and overlapping edits.
- Verify preview tokens, restricted content, draft APIs, feeds, search, social cards, and caches do not expose unpublished or private material.
- Validate rich text, embeds, uploads, localized content, redirects, canonical URLs, sitemap updates, link integrity, attribution, and accessible alternatives on representative content.

## Administration and extensions
- Check least-privilege editorial/admin roles, MFA where risk warrants, account recovery, session invalidation, and auditability of sensitive actions.
- For WordPress, inventory core/themes/plugins and reachable advisories, update compatibility, administrative file editing, filesystem permissions, login abuse controls, and XML-RPC/REST exposure as used.
- For headless systems, inspect read/write token scope, public/private API endpoints, preview credentials, webhook signatures, schema permissions, and server/client credential separation.
- Validate unsafe HTML and media content/size, executable uploads, external embeds, secret exposure, and third-party tracking behavior.

## Delivery, upgrades, and recovery
- Rehearse CMS/schema/plugin updates against a representative database and media copy. Restore both content and uploads plus required configuration; prove the restored site renders.
- Test build/revalidation webhooks for duplicates, delivery failure, ordering, and unauthorized requests. Verify publish/unpublish invalidates the correct cache/search records.
- Measure representative archive/search/article pages and editor workflows with realistic content volume; inspect slow queries, large media, and cache misses.
- Verify production TLS/redirects, editor access, controlled form/email delivery, privacy/consent where relevant, diagnostics, and ownership of content corrections and emergency rollback.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [WordPress hardening](https://developer.wordpress.org/advanced-administration/security/hardening/)
- [WordPress backups](https://developer.wordpress.org/advanced-administration/security/backup/)
