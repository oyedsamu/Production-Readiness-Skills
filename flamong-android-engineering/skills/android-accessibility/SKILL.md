---
name: android-accessibility
description: Review or improve Android accessibility semantics, input behavior, text scaling and assistive technology use.
---
# Accessibility

## Scope
Follow the user’s requested mode: inspection stays read-only; implementation changes only the requested behavior. Preserve existing project conventions and prior authorization. Publishing, production changes and external messages require their own authorization.

## Workflow
1. Exercise the affected flow with TalkBack and inspect control labels, roles, state announcements and reading/focus order. Avoid announcing decorative content twice.
2. Increase font size and display scaling; inspect clipping, reflow, contrast and reachable touch targets. Verify important content is not conveyed only by color.
3. Use keyboard or switch-style focus navigation where applicable. Test error announcements and recovery; make custom controls expose equivalent actions and state.

## Verification evidence
Record device/settings and the flow exercised, with screenshots for layout failures and observed assistive behavior. Automated semantics checks supplement, rather than establish, manual usability.
Record the exact command or manual procedure, candidate/build and environment, observed result, and evidence location. Mark unavailable checks as not run; never invent device, benchmark, security or release outcomes.

## References
Read the [topic-specific official guidance](https://developer.android.com/develop/ui/compose/accessibility) for APIs and version-sensitive details relevant to the installed toolchain.
