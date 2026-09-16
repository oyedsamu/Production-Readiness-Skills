# Project routing

Choose by executable/deployable behavior, not only by programming language. This list names optional specialist skills; it is not an installation dependency.

| Skill | Review boundary |
| --- | --- |
| `android-app-completion` | native Android apps using Kotlin or Java, Jetpack Compose, or Views |
| `website-completion` | public websites, landing pages, static sites, and general web launch reviews |
| `backend-system-completion` | HTTP/REST or gRPC APIs, modular monoliths, and backend services |
| `flutter-app-completion` | Flutter applications, including Android Flutter, iOS, web, and desktop targets |
| `kmp-project-completion` | Kotlin Multiplatform shared libraries and applications, including Compose Multiplatform |
| `react-native-app-completion` | React Native Android/iOS applications, including Expo and bare workflows |
| `ios-app-completion` | native iOS and iPadOS applications using Swift, SwiftUI, or UIKit |
| `spa-web-app-completion` | client-rendered React, Vue, Angular, or Svelte applications and authenticated dashboards |
| `ssr-web-app-completion` | server-rendered and full-stack web apps using Next.js, Nuxt, SvelteKit, or similar frameworks |
| `pwa-completion` | installable progressive web apps and web applications with offline/service-worker behavior |
| `cms-site-completion` | WordPress, headless CMS, and editorial publishing sites |
| `graphql-api-completion` | GraphQL services, federated graphs, and subscription APIs |
| `event-driven-system-completion` | message brokers, queue workers, scheduled jobs, streaming services, and event-driven backends |
| `serverless-system-completion` | serverless functions, edge workers, and managed event-triggered applications |
| `data-pipeline-completion` | batch/streaming ETL or ELT, analytics transformations, ingestion, and scheduled data products |
| `llm-application-completion` | LLM applications, RAG systems, tool-using agents, and generative AI APIs |
| `ml-system-completion` | predictive ML training pipelines, batch scoring, and online inference services |
| `desktop-app-completion` | Electron, Tauri, and native Windows/macOS/Linux desktop applications |
| `cli-tool-completion` | command-line tools, developer utilities, and shell-facing automation |
| `library-package-completion` | reusable libraries, SDKs, framework packages, and registry publications |
| `infrastructure-completion` | infrastructure as code, container platforms, Kubernetes deployments, and shared runtime infrastructure |
| `browser-extension-completion` | Chrome, Firefox, and other browser extensions with privileged browser APIs |

## Composition examples

- A Flutter Android app uses the Flutter track's Android branch. Do not apply native Compose checks unless that app actually embeds Compose functionality.
- A KMP module with Android and iOS hosts needs target-specific shared-code evidence and each host's release checks. A JVM-only test run does not verify the Apple framework.
- An Expo app uses the React Native track; include OTA checks only if updates are configured. Distinguish the runtime version from the store version and the update ID.
- A Next.js storefront with a queue worker and database uses SSR, event-driven, and backend/persistence checks. Public-page discovery checks apply to indexable routes, not private account pages.
- A React dashboard that calls a GraphQL service needs the SPA experience and GraphQL resolver/resource checks, plus the shared method. Reuse the same authorization test only if it covers both boundaries.
- A static content site can use website checks alone. Use the CMS track if editorial permissions, preview, publishing, or plugin operations are part of the release.
- An LLM service with a nightly retrieval pipeline needs the LLM and data pipeline tracks, with release evidence tied to the model, prompt, and index versions.
- A desktop client that embeds web UI needs desktop privilege/update checks plus applicable web interaction checks. A package consumed by that app needs an isolated consumer installation test.

When the project does not fit a listed class, describe the uncovered runtime and derive its failure cases from the project and official sources. Do not force a checklist fit or label unsupported coverage complete.
