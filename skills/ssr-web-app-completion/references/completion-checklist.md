# SSR web app readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Rendering and cache isolation
- Inventory routes as static, server-rendered, streamed, or client-rendered. Compare actual HTML, status codes, redirects, and hydration with intended behavior using production builds.
- Test two users/tenants requesting the same route through origin and CDN. Verify personalized HTML, serialized state, fetch caches, and revalidation keys cannot leak across identities.
- Exercise mutations followed by navigation/revalidation, preview/draft content, stale content tolerance, and cache invalidation failures. Verify cache semantics for the installed framework version.
- Test hydration with locale/timezone/random values, slow streaming boundaries, failed data fetches, and client navigation; check accessible loading/error/not-found states and correct status semantics.

## Server and client trust
- Check each server action, loader mutation, API route, and upload for authorization, validation, CSRF/origin requirements, size limits, and error redaction. Server execution is not proof of authorization.
- Inspect client bundles and serialized props for secrets. Verify public/private configuration separation and server-only dependency boundaries.
- Test user-supplied URLs, image proxies, redirects, HTML rendering, cookies, CSP/nonces, and preview endpoints against the actual runtime. Restrict internal network access where SSRF is reachable.

## Framework and hosting behavior
- Next.js: inspect the installed router model, server/client boundaries, action security, caching/revalidation, image optimization, and metadata using version-matched docs.
- Nuxt: inspect Nitro deployment/runtime config, route rules, server handlers, payload serialization, and hydration. SvelteKit: inspect adapter, hooks, load/actions, private env imports, and serialized errors.
- Verify the chosen node/edge/static adapter supports all used APIs. Test cold start, concurrency, process-local state, pool sizing, request cancellation, and graceful shutdown where applicable.

## Release experience
- Test critical authenticated/public journeys, no-JS behavior where promised, direct URLs, keyboard/screen reader use, mobile layout, and forms after session expiry.
- Measure server latency and client performance separately, including cache misses and representative data. Identify slow dependency waterfalls and streaming failures.
- Verify canonical/robots/sitemap/social metadata only for discoverable pages; keep draft/private pages access-controlled and excluded from public caches/indexes.
- Rehearse mixed-version assets/server/API/schema deployment and rollback, then inspect logs/traces and safe live smoke checks for the exact candidate.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [Next.js production checklist](https://nextjs.org/docs/app/guides/production-checklist)
- [Nuxt deployment](https://nuxt.com/docs/4.x/getting-started/deployment)
- [SvelteKit adapters](https://svelte.dev/docs/kit/adapters)
