# Production Readiness Skills

Three installable Codex skills that prevent a build from being called complete merely because it renders, compiles, or returns a successful response.

## Included skills

| Skill | Use it for | Final verdicts |
| --- | --- | --- |
| `website-completion` | Websites, landing pages, dashboards, and web apps | `READY TO LAUNCH`, `READY TO LAUNCH WITH ACCEPTED RISKS`, `NOT READY TO LAUNCH` |
| `android-app-completion` | Native Android applications and Play Store releases | `READY TO RELEASE`, `READY TO RELEASE WITH ACCEPTED RISKS`, `NOT READY TO RELEASE` |
| `backend-system-completion` | APIs, services, platforms, workers, and backend systems | `READY TO DEPLOY`, `READY TO DEPLOY WITH ACCEPTED RISKS`, `NOT READY TO DEPLOY` |

Each skill uses four progressive gates, an evidence-based `PASS / WARN / FAIL / N/A` scorecard, and P0–P3 severity. P0 issues always block an unconditional ready verdict; unresolved P1 issues require explicit risk acceptance.

## Install

Copy one or more folders from `skills/` into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/website-completion "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/android-app-completion "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/backend-system-completion "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart or reload the Codex environment after installation if the skills are not discovered immediately.

## Invoke

The skills allow automatic invocation for matching work, and can also be named explicitly:

```text
Use $website-completion to build and launch this site.
Use $android-app-completion to prepare this application for Play Store release.
Use $backend-system-completion to make this API production ready.
```

## Repository structure

```text
skills/
├── website-completion/
├── android-app-completion/
└── backend-system-completion/
```

Each directory contains:

- `SKILL.md` — routing, workflow, constraints, and verdict rules.
- `references/completion-checklist.md` — the full production-readiness checklist and report template.
- `agents/openai.yaml` — UI metadata and automatic-invocation policy.

## What the checklists cover

- Product functionality and failure states
- Security, privacy, authorization, secrets, and dependency risk
- Accessibility and inclusive UX
- Performance and reliability
- Analytics, logging, metrics, tracing, crash/error monitoring, and alerts
- Testing, CI/CD, environment configuration, deployment, and rollback
- Data migrations, backups, recovery, and operational handoff
- SEO and launch essentials for websites
- Android lifecycle, offline behavior, signing, permissions, and Play Store readiness
- Backend contracts, consistency, idempotency, queues/jobs, scaling, and resilience
- Domain-specific extensions for higher-risk products

The checklists are decision frameworks, not substitutes for project-specific requirements. Evidence and the user's actual acceptance criteria remain authoritative.

## License

MIT
