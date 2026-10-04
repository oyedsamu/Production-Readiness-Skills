# Mobile store packaging and first-session readiness

Apply this companion to the app's actual distribution channel and business model. For a shared library without a consumer app, mark store checks N/A with a reason. Review Android and Apple host apps separately; a common codebase does not establish equal listing, billing, or onboarding behavior.

## Scope and evidence

Record the candidate/build, store/territory/locale, asset version, monetization model, first-session journey, and inspection evidence. Split observations into release defects and growth hypotheses. Use the existing review method's severity and evidence rules.

Missing required assets, inaccurate product claims, broken activation, inaccessible purchase controls, incorrect charges/entitlements, or unmet store requirements can block release. An untested marketing variant, lack of a conversion uplift, no paywall in a free app, or a justified longer onboarding flow does not itself block release. Do not label low revenue a packaging defect without funnel evidence. Record inaccessible required evidence as UNVERIFIED.

## 1. App icon

- Inspect the actual exported store icon at thumbnail size, in a search-results composition, and on a representative device. Check recognizability, clipping, contrast, fine-detail loss, and consistency with the app's purpose. Attach the rendered evidence, not only the large source artwork.
- Verify required platform variants and current asset specifications. Keep the store icon distinct from Android adaptive launcher assets where their requirements differ; inspect supported Apple appearances when applicable.
- If recognizability is uncertain, propose materially different concepts and a target-user comparison. Treat color/style preferences as hypotheses. Do not imitate another app's branding or use an unrelated attention-grabbing image.

## 2. Store screenshots and previews

- Build an ordered story from real candidate UI: lead with the main outcome, then demonstrate supporting capabilities. Check the opening images at search-result size and the complete sequence at product-page size; text must remain legible without zooming.
- Map every screenshot claim to a reproducible app state or feature. Capture the correct platform, locale, device family, and current UI; exclude personal information, fake ratings, fabricated results, and unavailable features. Keep promotional overlays truthful.
- Inspect the actual store presentation. On Apple's store, one to three opening screenshots may appear in search depending on orientation and preview availability. Do not assume exactly three or copy Apple presentation rules into Play.
- Check localized text, image dimensions, preview poster frames, and silent comprehension. Record current store specifications and metadata restrictions rather than freezing them into this skill.

## 3. Onboarding and first value

- Define a measurable first useful outcome. Walk a clean installation from the store promise to that outcome; record elapsed time, required actions, confusing decisions, and points of abandonment or failure.
- Keep introductory messaging aligned with the listing and focused on useful outcomes. Consider a short three-to-four-step introduction where it helps, but justify length from user needs. Keep necessary setup, safety information, consent, and contextual instruction.
- Verify back/continue/skip behavior where offered, permission denial, interrupted sessions, relaunch, offline loading, and returning-user behavior. Do not repeatedly force completed onboarding or make swipe the only way forward.
- If using video, test weak connections, loading failure, captions/accessible alternatives, and reduced-motion behavior. Treat video-versus-static conversion as an experiment, not an established improvement for this product.

## 4. Monetization and paywall, when applicable

- Document why the offer appears at its chosen point relative to demonstrated value. Consider early, contextual, freemium, or metered offers as appropriate. Do not add subscriptions to free, enterprise-paid, or one-time-purchase apps merely to satisfy this checklist.
- Confirm localized prices and product/offer identifiers against store configuration. Show the actual charge and billing interval prominently; show any equivalent weekly/monthly price as secondary. Recalculate savings with the real comparator and billing convention; do not invent discounts or copy example prices from an article.
- Explain trial eligibility/duration, the subsequent charge, renewal, cancellation, and what is included. Keep terms/privacy and restore/sign-in options reachable. Preserve an obvious free-access or dismissal path when one exists; do not use hidden controls or fake urgency.
- Test eligible and ineligible trial users, existing subscribers, dismissed/failed/pending purchases, restore, expiration/refund/revocation, and entitlement reconciliation using authorized sandbox accounts. Ensure an existing subscriber is not prompted into a duplicate purchase.
- Treat subscription conversion, retention, refunds, and support complaints as related outcomes. Never optimize the purchase click alone or confuse onboarding media with an actual free trial.

## 5. Core user flow

- Identify the primary next action on each task step; verify that first-time users can find it. Reduce unnecessary choices and duplicate inputs without removing useful navigation, undo, recovery, or accessibility controls.
- Exercise the complete advertised outcome with representative content, denied permissions, cancellation, errors, and large text. Record a screen walkthrough plus expected and observed results; a UI screenshot alone does not prove the flow works.

## Measurement and iteration

Use available store analytics and privacy-appropriate product events. Define each denominator, cohort, time window, and version before calculating rates. Keep store views/downloads separate from observed app first opens; attribution and consent gaps can prevent exact joins.

For example, measure first opens, onboarding completion, first useful outcome, eligible paywall viewers, purchase attempts, verified purchases, and later retention/refunds. State paywall reach as eligible viewers divided by eligible first opens, and paywall conversion as verified purchasers divided by viewers in a compatible cohort/window. Their product estimates the observed install-to-paid rate only when cohorts, attribution, and windows align.

If running an experiment, specify the hypothesis, asset/config versions, primary metric, guardrails, audience, allocation, observation window, and revert condition. Change one major variable where feasible. Use platform-supported experiments when available; report small samples or confounding traffic changes as inconclusive. A test plan can be ready before traffic exists; completed growth experiments are not mandatory launch gates. Do not introduce tracking or publish store/pricing changes beyond the user's authorization.

## Source and interpretation

Inspired by [Paul Solt's article](https://x.com/paulsolt/status/2045580498232373433), *$250 to $5K MRR: 5 App Store Packaging Rules That Actually Work*, published 18 April 2026. Full text recovered from public post metadata on 4 October 2026. Its five themes inform the sections above. Its revenue story is anecdotal; its prices, subscription preference, video claims, screen counts, and paywall timing are product hypotheses, not universal rules or guarantees. The evidence procedures, failure cases, applicability rules, and measurement safeguards above are our operational additions.

Official sources checked 4 October 2026; recheck current rules for each target release:

- [Apple product page](https://developer.apple.com/app-store/product-page/)
- [Apple subscriptions](https://developer.apple.com/app-store/subscriptions/)
- [Apple product page optimization](https://developer.apple.com/app-store/product-page-optimization/)
- [Google Play store listing guidance](https://support.google.com/googleplay/android-developer/answer/13393723?hl=en)
- [Google Play subscription policy](https://support.google.com/googleplay/android-developer/answer/9900533?hl=en)
