# SPA frontend readiness checks

Apply the [review method](review-method.md) before evaluating these checks. Split compound checks into separate ledger rows when outcomes or evidence differ. Conditional checks require a reason for N/A.

## Routing and state
- Open nested routes directly, refresh them, navigate back/forward, and test unknown routes on the production host. Confirm fallback rewrites do not serve HTML for missing JS/assets or API requests.
- Test expired sessions on protected routes, login return paths, logout in multiple tabs, role changes, and tenant switches. Clear identity-scoped query caches and persisted state.
- Exercise request races, navigation during fetch, cancellation, optimistic failure/rollback, duplicate mutation, pagination changes, and reconnect. Compare rendered state with authoritative server state.

## Framework boundaries
- React: test effect cleanup/repeated mounting and stale closures; verify error boundaries plus async/event error handling. Inspect bundle duplication and lazy-route loading failures.
- Vue: test watcher cleanup, reactive state identity, async components, and route guards. Angular: inspect subscription cleanup, route guards, dependency scopes, and change-detection hotspots.
- Svelte: inspect store/subscription lifetime, reactive updates, async teardown, and compiled output behavior. Use only the applicable framework branch.

## Browser security and delivery
- Inspect public environment substitution, bundles, source maps, HTML injection sinks, third-party dependencies, CSP, and browser storage for exposed secrets or sensitive data.
- Verify cookie/session settings, CSRF when cookies authenticate mutations, CORS, and server-side authorization. Frontend route guards provide UX, not access enforcement.
- Test stale tabs after a deployment, missing lazy chunks, asset cache lifetime, base paths, and recovery without losing unsaved user work. Verify versioned asset retention or reload policy.
- Test unsupported APIs, browser/private-storage limits, cross-origin downloads, and service worker interference if present.

## Quality and operations
- Exercise critical forms and tables with keyboard/screen reader, zoom, narrow viewports, touch, long data, error announcements, and focus restoration after navigation/modals.
- Measure initial JS, route transitions, input latency, large lists, repeated navigation memory, and API waterfalls under representative CPU/network conditions. Use explicit budgets.
- Run component tests for meaningful states and integration/E2E tests through real API contracts. Verify diagnostics map to the exact deployed bundle; track route events only if analytics is required.
- Verify production host/API configuration and release smoke tests, rollback compatibility with old bundles, and ownership of browser failures versus API failures.

## Evidence starting points

Inspect the project-defined build/test/release commands and CI before running them. Capture the actual candidate artifact, meaningful tests of the critical journey and its failure path, platform/runtime matrix, and recovery evidence. Static inspection and execution results must remain distinguishable.

## Official references

Use documentation matching the detected version and release channel. Record source and access date for version-sensitive decisions; an inaccessible reference leaves that decision unverified.

- [React effects](https://react.dev/reference/react/useEffect)
- [Vue production](https://vuejs.org/guide/best-practices/production-deployment.html)
- [Angular security](https://angular.dev/best-practices/security)
