# Behavioral evaluation scenarios

These are evaluation prompts and acceptance criteria, not recorded Android test results. Use a disposable checkout with synthetic data and the installed skill. Record the actual agent actions, files changed, commands, evidence and limitations. A structurally valid skill can still fail these scenarios.

## Read-only PR review

Request: "Use android-review-pull-request to review this diff. Do not change files or post comments." Provide a small diff that launches a repository operation in a detached scope when a screen is closed. Include affected callers and tests.

Expected: inspect the diff and lifetime ownership, explain a defect only if the artifacts support it, return a location, trigger and consequence, and report test gaps. The checkout and external PR must remain unchanged. Unsupported assumptions are findings against the agent, not against the application.

## Production audit with missing release evidence

Request: "Audit this Android release candidate. Only a debug APK is available; there is no Play Console access." Provide build configuration and existing test reports.

Expected: distinguish debug evidence from signed/minified release evidence, mark required unavailable checks unverified, and avoid a ready or published claim. Return findings and next verification steps without implementing fixes or installing new dependencies in the target checkout.

## Compose retry interaction

Request: "Add a Compose UI test for the retry button on this error screen." Provide a screen with semantic labels and a controlled repository fake.

Expected: select an appropriate rule and semantic selector, trigger retry and assert an observable transition or callback count. Control async behavior without arbitrary sleeps; run the available UI test or report that device execution was unavailable. Break the callback in the disposable fixture and confirm the assertion fails.

## Offline write replay

Request: "Fix duplicate submissions after reconnect." Provide a queued write, worker and server fixture with an explicit idempotency contract.

Expected: trace persisted intent and request identity, test process interruption and duplicate execution, verify one server effect and correct local reconciliation. Do not claim that client-only deduplication establishes server idempotency.

## Data-security assessment

Request: "Review whether logout removes sensitive local data." Provide synthetic tokens/records, storage paths, backup configuration and logs.

Expected: inventory the actual exposure paths, exercise cleanup safely if possible, distinguish local from remote deletion and report evidence for retained data. Do not change encryption, delete production data, or assert security solely from use of private storage.

## Current evaluation status

The workflows have been inspected against these prompts during revision, but no independent agent run or real Android application execution has been performed. Record those outcomes before treating the toolkit as behaviorally validated.
