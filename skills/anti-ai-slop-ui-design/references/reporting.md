# Reporting

Lead with the decision and its strongest reason. Keep the chat summary short; put a full ledger in a repository-appropriate report when requested or when the review is too large for chat. Do not overwrite a previous report without preserving useful evidence. Avoid copying raw secrets, private URLs with tokens, or customer data into artifacts.

## Report structure

1. Verdict and scope: exact skill verdict, candidate commit/artifact, reviewed units and environments, mode, date, assumptions, and excluded scope.
2. Gates: A/B/C status with evidence links; D live verification status. Distinguish preparation from actual publication.
3. Findings: all open P0/P1 first, then material P2/P3. For each give ID, severity, file/location or runtime evidence, trigger, observed consequence, fix, owner, and retest needed. Separate confirmed failures from hypotheses.
4. Evidence ledger: check ID, criterion, phase, required/optional, status, evidence location, and remaining gap. Group by area if the mapping remains inspectable. Show which checks were skipped or unavailable.
5. Changes and verification: describe fixes and the tests run after them. Include failed commands and unresolved flaky or environmental failures. Scope every performance or security claim to the measured conditions.
6. Remaining actions: exact evidence needed, responsible owner if known, and explicit risk acceptances with expiry/revisit condition. Use "unassigned" when there is no owner.

For several components, give a verdict for each and one overall decision. Any blocking component on a critical path blocks the overall release. Do not average component statuses or hide an untested host behind shared-code test results.

## Plain technical writing

Edit the report after reasoning and verification. State the failing action and consequence: "Retrying checkout created a second order in the integration test" tells the reader more than "Transaction integrity needs enhancement."

Remove promotional claims, staged introductions, repeated conclusions, vague claims of best practice, and decorative emphasis. Keep necessary terminology, exact verdicts, evidence, uncertainty, severity, and accepted-risk qualifications intact. A prose edit must never turn `UNVERIFIED` into `PASS`, weaken a blocker, invent a metric, or hide a failed command. Preserve paths, code, commands, identifiers, and link targets.

If Humanizer is available, use it only for this final prose pass. Its absence does not block a review. These writing principles were informed by [blader/humanizer](https://github.com/blader/humanizer), reviewed at version 3.0.0 on 2026-09-16; this package does not require or vendor that skill.

## Example: honest limited evidence

> NOT READY TO DEPLOY. The retry test creates duplicate orders (P0). Unit tests passed for commit abc123, but the staging migration has not run because database access is unavailable. Live verification: NOT VERIFIED. Fix idempotency, rerun the duplicate-request test, then run the migration against a representative database copy.

This example is illustrative, not evidence about the project under review.
