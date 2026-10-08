# Validation status

## Automated packaging checks

Run from the repository root with `requirements-dev.txt` installed:

```bash
python scripts/validate_android_skills.py
python scripts/sync_shared.py --check
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

The Android validator covers all nested starter skills: YAML (including duplicate keys), directory-matching names, description bounds, nonempty bodies, catalog coverage, portable local links and symlinks. CI runs it separately from the original readiness-catalog validator. Failure fixtures exercise malformed metadata, catalog drift, missing files, broken links and nonportable dependencies.

## Editorial revision

- All 31 skills now define focused triggers, distinct procedures, observable verification and topic-specific official references.
- PR/security reviews, privacy/release assessments and production audits default to read-only work. Remediation and external actions follow user authorization.
- API/toolchain-sensitive guidance must be checked against current official references when used.

## Pending behavioral evidence

- Run the [evaluation scenarios](SCENARIOS.md) with independent agents against disposable Android fixtures.
- Execute relevant Android builds, device tests and failure-mode checks on real applications.
- Review security and architecture guidance with Android maintainers.
- Confirm installation/discovery with each target agent.

Packaging checks and editorial review do not prove agent compliance or downstream application readiness.
