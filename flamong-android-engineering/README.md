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
- [`android-architecture`](skills/android-architecture/SKILL.md)
- [`android-modularization`](skills/android-modularization/SKILL.md)
- [`android-dependency-injection`](skills/android-dependency-injection/SKILL.md)
- [`android-legacy-migration`](skills/android-legacy-migration/SKILL.md)

### Implementation
- [`android-compose-ui`](skills/android-compose-ui/SKILL.md)
- [`android-state-management`](skills/android-state-management/SKILL.md)
- [`android-coroutines-flow`](skills/android-coroutines-flow/SKILL.md)
- [`android-navigation`](skills/android-navigation/SKILL.md)
- [`android-error-handling`](skills/android-error-handling/SKILL.md)

### Data
- [`android-networking`](skills/android-networking/SKILL.md)
- [`android-persistence`](skills/android-persistence/SKILL.md)
- [`android-offline-sync`](skills/android-offline-sync/SKILL.md)
- [`android-data-security`](skills/android-data-security/SKILL.md)

### Quality
- [`android-unit-testing`](skills/android-unit-testing/SKILL.md)
- [`android-compose-testing`](skills/android-compose-testing/SKILL.md)
- [`android-integration-testing`](skills/android-integration-testing/SKILL.md)
- [`android-performance`](skills/android-performance/SKILL.md)
- [`android-accessibility`](skills/android-accessibility/SKILL.md)
- [`android-static-analysis`](skills/android-static-analysis/SKILL.md)

### Production
- [`android-security-review`](skills/android-security-review/SKILL.md)
- [`android-privacy`](skills/android-privacy/SKILL.md)
- [`android-observability`](skills/android-observability/SKILL.md)
- [`android-release-readiness`](skills/android-release-readiness/SKILL.md)
- [`android-play-store`](skills/android-play-store/SKILL.md)

### Delivery
- [`android-gradle-build-logic`](skills/android-gradle-build-logic/SKILL.md)
- [`android-ci-cd`](skills/android-ci-cd/SKILL.md)
- [`android-dependency-upgrades`](skills/android-dependency-upgrades/SKILL.md)

### Workflows
- [`android-create-feature`](skills/android-create-feature/SKILL.md)
- [`android-debug-issue`](skills/android-debug-issue/SKILL.md)
- [`android-review-pull-request`](skills/android-review-pull-request/SKILL.md)
- [`android-production-audit`](skills/android-production-audit/SKILL.md)

## Validation
Run `python scripts/validate_android_skills.py` from the repository root after installing `requirements-dev.txt`. CI runs this check alongside the original catalog validator and its tests. Structural validation does not establish agent behavior; see [VALIDATION.md](VALIDATION.md) and [review scenarios](SCENARIOS.md).

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
