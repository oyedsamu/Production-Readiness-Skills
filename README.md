# Production Readiness Skills

24 installable skills for reviewing, finishing, and releasing software. Each skill asks for evidence from the actual candidate, tests failure and recovery paths, and reports what is still unknown.

Use a focused skill for a known project type, or start with `production-readiness-review` for a monorepo or mixed system. The original `android-app-completion`, `backend-system-completion`, and `website-completion` names remain available. Android's original name is the native Kotlin/Java track.

## Design companion

Use [`anti-ai-slop-ui-design`](skills/anti-ai-slop-ui-design/SKILL.md) when designing or building an interface. It requires three visual directions, a coherent selected language, realistic screenshots, critique, and refinement alongside the relevant readiness track. Its Python evidence checker tracks review completeness; visual judgment remains manual. It preserves established brand systems and scopes small edits to the affected interface.

## Choose a skill

### Start here

| Skill | Use it for |
| --- | --- |
| [`production-readiness-review`](skills/production-readiness-review/SKILL.md) | mixed projects, monorepos, and project-type selection |

### Mobile

All five mobile tracks include store packaging and first-session checks: icon legibility, screenshot accuracy and sequence, onboarding to first value, transparent paid offers when applicable, and the core user flow. Growth experiments are recommendations, not universal release blockers. Shared-library-only KMP releases and non-mobile targets use justified N/A.

| Skill | Use it for |
| --- | --- |
| [`android-app-completion`](skills/android-app-completion/SKILL.md) | native Android apps using Kotlin or Java, Jetpack Compose, or Views |
| [`flutter-app-completion`](skills/flutter-app-completion/SKILL.md) | Flutter applications, including Android Flutter, iOS, web, and desktop targets |
| [`kmp-project-completion`](skills/kmp-project-completion/SKILL.md) | Kotlin Multiplatform shared libraries and applications, including Compose Multiplatform |
| [`react-native-app-completion`](skills/react-native-app-completion/SKILL.md) | React Native Android/iOS applications, including Expo and bare workflows |
| [`ios-app-completion`](skills/ios-app-completion/SKILL.md) | native iOS and iPadOS applications using Swift, SwiftUI, or UIKit |

### Web

| Skill | Use it for |
| --- | --- |
| [`website-completion`](skills/website-completion/SKILL.md) | public websites, landing pages, static sites, and general web launch reviews |
| [`spa-web-app-completion`](skills/spa-web-app-completion/SKILL.md) | client-rendered React, Vue, Angular, or Svelte applications and authenticated dashboards |
| [`ssr-web-app-completion`](skills/ssr-web-app-completion/SKILL.md) | server-rendered and full-stack web apps using Next.js, Nuxt, SvelteKit, or similar frameworks |
| [`pwa-completion`](skills/pwa-completion/SKILL.md) | installable progressive web apps and web applications with offline/service-worker behavior |
| [`cms-site-completion`](skills/cms-site-completion/SKILL.md) | WordPress, headless CMS, and editorial publishing sites |

### Services

| Skill | Use it for |
| --- | --- |
| [`backend-system-completion`](skills/backend-system-completion/SKILL.md) | HTTP/REST or gRPC APIs, modular monoliths, and backend services |
| [`graphql-api-completion`](skills/graphql-api-completion/SKILL.md) | GraphQL services, federated graphs, and subscription APIs |
| [`event-driven-system-completion`](skills/event-driven-system-completion/SKILL.md) | message brokers, queue workers, scheduled jobs, streaming services, and event-driven backends |
| [`serverless-system-completion`](skills/serverless-system-completion/SKILL.md) | serverless functions, edge workers, and managed event-triggered applications |

### Data and AI

| Skill | Use it for |
| --- | --- |
| [`data-pipeline-completion`](skills/data-pipeline-completion/SKILL.md) | batch/streaming ETL or ELT, analytics transformations, ingestion, and scheduled data products |
| [`llm-application-completion`](skills/llm-application-completion/SKILL.md) | LLM applications, RAG systems, tool-using agents, and generative AI APIs |
| [`ml-system-completion`](skills/ml-system-completion/SKILL.md) | predictive ML training pipelines, batch scoring, and online inference services |

### Desktop, tooling, and infrastructure

| Skill | Use it for |
| --- | --- |
| [`desktop-app-completion`](skills/desktop-app-completion/SKILL.md) | Electron, Tauri, and native Windows/macOS/Linux desktop applications |
| [`cli-tool-completion`](skills/cli-tool-completion/SKILL.md) | command-line tools, developer utilities, and shell-facing automation |
| [`library-package-completion`](skills/library-package-completion/SKILL.md) | reusable libraries, SDKs, framework packages, and registry publications |
| [`infrastructure-completion`](skills/infrastructure-completion/SKILL.md) | infrastructure as code, container platforms, Kubernetes deployments, and shared runtime infrastructure |
| [`browser-extension-completion`](skills/browser-extension-completion/SKILL.md) | Chrome, Firefox, and other browser extensions with privileged browser APIs |

The backend skill also has conditional checks for Node.js, Python, JVM/Ktor/Spring, Go, .NET, PostgreSQL, Redis, and container deployments. Mobile skills cover platform-specific release requirements within their own packages. All skills include conditional checks for money, health/sensitive records, enterprise/tenancy, logistics, public/editorial content, and AI-assisted workflows.

## Install

Clone this repository and copy the skill folders you need into your agent's skills directory. For a Codex installation using `~/.codex/skills`:

```bash
git clone https://github.com/oyedsamu/Production-Readiness-Skills.git
cd Production-Readiness-Skills
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/flutter-app-completion "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/backend-system-completion "${CODEX_HOME:-$HOME/.codex}/skills/"
```

To install the whole catalog instead:

```bash
cp -R skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Check existing copies before replacing locally customized skills. Each folder is self-contained: it includes `SKILL.md`, UI metadata, its technical checklist, and local copies of the review/reporting references. You do not need to install all skills or keep this repository beside them. Other agents that support `SKILL.md` can use their own skill-directory conventions.

## Use

```text
Use $production-readiness-review to audit this monorepo. Do not modify code.
Use $android-app-completion to check this native Compose app before Play release.
Use $flutter-app-completion to finish release preparation for the Android flavor.
Use $kmp-project-completion to assess the shared SDK and its Android/iOS hosts.
Use $react-native-app-completion to check our Expo release and OTA compatibility.
Use $ssr-web-app-completion to fix release blockers in this Next.js app.
Use $backend-system-completion to prepare this API for deployment, without deploying.
```

Audit mode inspects and tests. Remediation mode fixes issues within the requested scope and retests. Release mode uses the user's authorization to publish or deploy. A readiness request alone does not authorize production writes, real payments, customer messages, or publication.

## Decisions and evidence

Checks use `PASS`, `WARN`, `FAIL`, `UNVERIFIED`, or `N/A`. Evidence includes the candidate/version, environment, command or manual procedure, observed result, and a test/log/artifact location. `UNVERIFIED` covers missing access, skipped tests, and inconclusive evidence. `N/A` requires a reason tied to the product.

The four gates separate functionality, quality, release preparation, and live verification. Pre-release decisions use the first three; live verification is reported independently. A candidate can be ready to release before publication, but a local build cannot establish that it has shipped.

- P0 blocks release.
- P1 blocks unless the user explicitly accepts an eligible, documented risk.
- Required unverified checks block readiness. Missing evidence cannot be accepted as a passing check.
- P2/P3 remain visible with impact and follow-up. Mandatory external release requirements cannot be waived by informal acceptance.

Skills return `READY TO LAUNCH`, `READY TO DEPLOY`, or `READY TO RELEASE`, with `WITH ACCEPTED RISKS` when needed, or the corresponding `NOT READY TO …` verdict. Live verification is `VERIFIED`, `PARTIAL`, `NOT VERIFIED`, or `N/A` with a reason. There is no aggregate score that can cancel a blocker.

Checks are conditional on actual functionality and risk. Analytics, a sitemap, a queue, or a particular vendor is not mandatory for every project. Version-sensitive platform/store requirements are checked against current official documentation rather than frozen into the checklist. These skills guide technical review; they do not certify legal compliance or guarantee that software has no defects.

## Maintain and validate

Python 3.10 or newer is required for repository validation. Skill users do not need Python.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/sync_shared.py --check
.venv/bin/python scripts/validate_skills.py
.venv/bin/python -m unittest discover -s tests -v
```

Edit shared workflow/reporting/domain guidance in `templates/`, then run `python3 scripts/sync_shared.py`. It copies those references into each skill so a single-folder installation stays portable. Edit technical checks directly inside the relevant skill. Keep the catalog, routing reference, and README current when adding a track.

The validator checks YAML, names, invocation metadata, local links, independent packaging, shared-reference drift, and catalog coverage. Tests exercise invalid packages and synchronization. They do not prove an agent will apply every instruction correctly; use the [review scenarios](docs/review-scenarios.md) to evaluate behavior. See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution contract.

## Writing and sources

Report-writing guidance was informed by [blader/humanizer](https://github.com/blader/humanizer), reviewed at version 3.0.0. Reports should state the observed failure and consequence, preserve uncertainty, and avoid inflated readiness claims. Humanizer is optional and is not vendored or required. Each technical checklist links to official references for version-sensitive verification.

## License

[MIT](LICENSE)
