# Visual review checklist

Record status, observed evidence, and a concrete fix when needed. Use FAIL for an observed problem, UNVERIFIED for missing inspection, and N/A only with a product-specific reason. A required FAIL or UNVERIFIED blocks visual completion. WARN preserves a minor issue with impact and follow-up.

## Before implementation

- Identify the primary task, audience, environment, emotional character, and existing brand constraints.
- State a visual thesis that changes information presentation, not just ornament.
- Compare three substantive directions or compatible treatments for a small change.
- Select one direction; define type, grid, density, spacing, color semantics, shapes, media, and motion.

## Inspect actual renders

| Dimension | Review action and expected evidence |
| --- | --- |
| Product fit | Locate primary domain objects and the main action; explain how the concept serves them. |
| Distinctiveness | Inspect beyond the logo; identify meaningful composition or content presentation fitting this product. Avoid arbitrary novelty. |
| Hierarchy | Identify the first three things a user sees; compare them with task importance. |
| Coherence | Compare navigation, forms, tables, alerts, and headings with selected tokens and existing components. |
| Usability | Walk the primary task and recovery path; record confusing labels, hidden actions, or obstructive decoration. |
| Accessibility | Check semantics, keyboard/focus, contrast, zoom/font scaling, labels, touch targets, and reduced motion as applicable. Capture test/manual evidence; screenshots alone cannot verify these. |
| Responsiveness | Inspect target sizes, wrapping, overflow, sticky controls, menus, and full-page content. |
| Density | Inspect sparse and realistic dense content; avoid wasteful gaps and unreadable compression. |
| Personality | Identify one memorable, useful decision grounded in the domain or established brand. |
| Restraint | Remove unjustified effects, icons, shapes, and containers; retain justified ones. |
| Copy/content | Replace vague promotional phrases with concrete tasks/benefits; verify metrics, sources, imagery, testimonials, and logos. Label demo data. |

## Anti-pattern scan

- Layout: repeated three-column features, identical centered sections, hero/screenshot/grid templates, endless nested cards, uniform rhythm regardless of content.
- Shapes: pills everywhere, oversized corner radii on unrelated objects, floating blobs or circles without meaning.
- Color/effects: default purple-blue gradients, neon accents, glow, excessive shadow or glass/blur without product rationale.
- Type/icons: identical oversized headings, indiscriminate bold, icons beside every sentence, decorative colored icon boxes.
- Copy: “supercharge,” “unlock the power,” “everything you need,” and “seamlessly integrate” without a concrete explanation.
- Content: fabricated numbers, empty charts, generic avatars, placeholder social proof, decorative dashboards.

Record the actual location and consequence of each problem. These are review prompts, not automatic failures based on a CSS keyword.

## Refinement and completion

- Record the before screenshot, issue, change or evaluated alternatives, and after screenshot.
- Inspect the revised primary view and affected breakpoints/states.
- Preserve required accessibility and platform conventions.
- Account for every checklist item and relevant viewport/state with evidence or justified N/A.
- State VISUAL REVIEW COMPLETE only after required review passes; otherwise state VISUAL REVIEW INCOMPLETE with blockers or missing evidence.
- Never infer production readiness from visual completion.
