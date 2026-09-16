# Integration and release boundary checks

Apply the [review method](review-method.md) and the tracks selected with [project-routing.md](project-routing.md).

- Inventory deployable units and their release dependencies. Map each critical journey through client, API, queue, data store, external service, and infrastructure as applicable. Name the owner and candidate version of each.
- Test a complete critical journey across real component boundaries in a controlled environment. Record simulated dependencies and the corresponding evidence gaps.
- Verify authentication, authorization, and tenant identity survive proxies, gateways, background jobs, search, exports, and caches. Probe mismatched and expired identity context.
- Exercise client/server contract compatibility, old/new event consumers, shared-library host compatibility, and database schema ordering during a rolling release. Include clients that cannot be immediately updated.
- Test interrupted requests, retries at multiple layers, duplicate messages, and a failure between a committed write and an external effect. Confirm one coherent business outcome.
- Check configuration/environment alignment, routing/DNS/TLS, public/private credentials, artifact identity, and feature-flag defaults across all units. A correct app pointed at the wrong service fails the intended release.
- Measure a representative whole journey and identify the limiting dependency, including pool/concurrency limits, queue age, cost bounds, and resource saturation.
- Verify cross-component diagnostics and operational ownership without exposing personal data. Test a safe failure signal and the operator's path to the responsible service.
- Rehearse release order, stop criteria, rollback or forward recovery, and restoration of data plus dependent indexes/caches. Restoring one database may not restore the business workflow.
- After authorized rollout, verify the actual deployed/distributed versions and controlled live critical journeys. Record any component awaiting store approval, production access, or external evidence as pending.
