# Flamong Android Engineering Skills

A cross-agent Android engineering skills starter kit. These are original operational instructions informed by public Android engineering references; upstream repositories are linked, not copied.

## Philosophy
- Correctness over cleverness; measured evidence over assertions.
- Prefer repository conventions over a universal architecture mandate.
- Security and accessibility are requirements, not optional polish.
- Use progressive disclosure: load only relevant skills.
- No skill substitutes for actual builds, device tests or human review.

## Install
Copy selected `skills/android-*` directories into the target repository's `.agents/skills/` folder. For Claude Code, copy them into `.claude/skills/` as needed. Read the target agent's current discovery documentation before installing.

## Catalog

### Architecture
- `android-architecture`
- `android-modularization`
- `android-dependency-injection`
- `android-legacy-migration`

### Implementation
- `android-compose-ui`
- `android-state-management`
- `android-coroutines-flow`
- `android-navigation`
- `android-error-handling`

### Data
- `android-networking`
- `android-persistence`
- `android-offline-sync`
- `android-data-security`

### Quality
- `android-unit-testing`
- `android-compose-testing`
- `android-integration-testing`
- `android-performance`
- `android-accessibility`
- `android-static-analysis`

### Production
- `android-security-review`
- `android-privacy`
- `android-observability`
- `android-release-readiness`
- `android-play-store`

### Delivery
- `android-gradle-build-logic`
- `android-ci-cd`
- `android-dependency-upgrades`

### Workflows
- `android-create-feature`
- `android-debug-issue`
- `android-review-pull-request`
- `android-production-audit`

## Suggested baseline gates
`./gradlew lint testDebugUnitTest assembleDebug` (adapt tasks to modules/flavors). Add instrumented tests, benchmarks, dependency checks, security review, accessibility audits and release checks according to the change and available infrastructure.

## Source inspiration
- https://github.com/lennonpetrick/android-agent-skills
- https://github.com/android/skills
- https://github.com/suchobits/android-skills
- https://github.com/skydoves/android-testing-skills
- https://mas.owasp.org/MASVS/

## License
Original starter content: MIT (see LICENSE). Upstream source code and text are not redistributed.
