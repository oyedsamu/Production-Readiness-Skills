# Conditional domain checks

Read only the domains that match actual product behavior. Add concrete checks to the ledger rather than claiming a domain is covered by its label. Identify relevant jurisdictions and current authoritative requirements when legal or policy constraints affect release; technical tests cannot certify compliance.

## Money, commerce, and subscriptions

- Replay an identical charge/order request concurrently and after a timeout. Verify one authoritative outcome, scoped idempotency keys, explicit currency/precision, and reconciliation with the provider.
- Exercise pending, declined, refunded, disputed, expired, and restored purchases where supported. Verify inventory reservations and buyer/seller separation under races.
- Validate webhook authenticity and replay handling, ledger/audit consistency, payout ownership, strong administrative authentication, and safe manual repair. Use sandbox transactions unless real charges are expressly authorized.
- For mobile digital purchases, verify current store billing rules, server-side entitlement verification, acknowledgement where required, revocation, and restore behavior.

## Health, sensitive records, and children

- Trace sensitive fields through access controls, analytics, logs, notifications, exports, backups, and support tools. Verify minimum access and an audit trail for exceptional access.
- Test consent withdrawal, deletion/retention exceptions, guardian or age-related flows where needed, and re-identification risk in shared datasets.
- Identify whether product claims or automated decisions need specialist review; report that review as pending when unavailable. Do not infer approval from encryption or a privacy policy.

## Enterprise and multi-tenant systems

- Exercise SSO expiry, deprovisioning, role changes, tenant switching, invitation reuse, and recovery for administrator lockout.
- Verify tenant scope in database queries, caches, background jobs, exports, search, telemetry, and support impersonation. Test two tenants with similar record identifiers.
- Check audit access, retention, managed configuration, corporate proxies/certificates, work profiles or device management when supported, and contractual availability/data residency commitments.

## Logistics, location, and offline operations

- Replay late, duplicate, out-of-order, and stale location/job updates. Verify dispatch races, conflict resolution, reconnection, and clock skew behavior.
- Test approximate/denied location, no GPS, background restrictions, battery consumption, stale-position UI, and notification delivery. Limit collection and retention to the intended use.

## Public information, editorial, and user content

- Verify source provenance, source dates, corrections, licensing, authorship, and links. Test publish/unpublish and indexing/cache invalidation for removed content.
- Exercise moderation/reporting, abuse limits, unsafe uploads, account sanctions, and appeals where the product provides them. Check captions, transcripts, content warnings, and download/playback rights when relevant.
- Preserve archive and citation integrity during URL or content migrations. Avoid exposing unpublished or restricted content through feeds, previews, search, or social metadata.

## AI-assisted workflows

- Trace retrieval permissions and tool authority independently of model instructions. Test malicious retrieved content, unsupported answers, tool failures, and sensitive-data leakage.
- Define representative evaluations, unacceptable failure classes, user-visible uncertainty or fallback, escalation paths, and cost/concurrency limits. Treat changes to model, prompt, retrieval index, or tools as candidate changes requiring relevant reevaluation.
