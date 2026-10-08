---
name: android-privacy
description: Review Android data collection, SDK behavior, permission use, retention and user deletion for a requested privacy task.
---
# Privacy

## Scope
Start in read-only assessment mode. Do not edit project files, install new dependencies in the target checkout, or remediate findings unless the user requests those actions. Existing safe checks and isolated reproductions are allowed. A review request does not authorize posting to external services or publication.

## Workflow
1. Inventory collected data, purpose, recipient and retention, including third-party SDK traffic. Compare actual behavior with the product disclosures rather than trusting SDK labels.
2. Exercise permission denial and revocation. Collect only data needed for the feature and ensure optional collection respects the product choice across restart.
3. Trace logout and deletion through local caches and backend requests. Distinguish local deletion from verified remote deletion and record policy/legal questions for the responsible owner.

## Verification evidence
Use synthetic data to capture collection with consent enabled and disabled, revoke permissions, and exercise deletion. Report observed endpoints/data classes and any remote outcome not verifiable.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/training/permissions/requesting) for APIs and version-sensitive details relevant to the installed toolchain.
