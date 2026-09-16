# Contributing

Keep each skill focused on a release boundary with distinct failure modes. A new framework name alone does not justify copying a checklist. Prefer a conditional reference when the release workflow and evidence are substantially shared, as with backend language runtimes.

## Adding or changing a skill

1. Explain when it applies in the frontmatter description. Distinguish it from neighboring tracks and keep isolated edits outside the trigger unless readiness is requested.
2. Include a short `SKILL.md`, `agents/openai.yaml`, and a technical checklist under `references/`. Match the folder and frontmatter name. The default prompt must mention `$skill-name`; preserve automatic invocation unless a separately approved change requires otherwise.
3. Make checks executable as review actions: specify the failure to exercise, expected property, and evidence to capture. Prefer "kill the worker before acknowledgement and redeliver" over "ensure resilience."
4. Use project scripts and current official documentation for version-dependent behavior. Do not freeze store deadlines, SDK minimums, vendor quotas, or universal performance budgets into the package.
5. Keep shared method/reporting/domain guidance in `templates/`, then run `python3 scripts/sync_shared.py`. Packaged copies must be regular files with no references outside the skill directory.
6. Update `docs/catalog.json`, the README, and the routing skill's project-routing reference when a track is added or renamed. Preserve the original three names unless a migration is deliberately provided.
7. Run the commands in the README. Check at least one realistic scenario from [docs/review-scenarios.md](docs/review-scenarios.md) against changed instructions; record what was actually exercised and any limitations.

## Review criteria

Keep audit, remediation, and publication scope distinct. Preserve prior user authorization without inventing new approval steps. Never require a production mutation to prove a check that can be exercised safely in an isolated environment.

Evidence status and severity are separate. Missing credentials are an evidence gap, not proof of a product defect. P0 and required unverified checks block release. User acceptance must name the actual risk; it cannot fabricate evidence or override a mandatory external release requirement.

Write reports in plain technical language. Preserve uncertainty, evidence locations, code, and exact verdicts during prose editing. Humanizer may help remove repetitive or inflated wording but must not weaken the assessment.

Avoid new executable helpers unless they make repeated work more reliable. Test helpers against meaningful failures. Packaging validation is not a behavioral evaluation of the agent or a security review of a downstream project.
