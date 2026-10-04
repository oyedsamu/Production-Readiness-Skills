---
name: anti-ai-slop-ui-design
description: Design distinctive, product-specific interfaces through concept exploration, coherent visual language, realistic rendering, critique, and refinement. Use when designing, building, redesigning, or finishing websites, web or mobile apps, dashboards, landing pages, admin interfaces, prototypes, design systems, or major UI components. Apply alongside production-readiness skills; preserve existing brand systems and scope small changes to the affected interface.
---

# Anti-AI-Slop UI Design

Produce an intentional, usable interface whose visual choices follow the product. Treat distinctiveness as an evidence-based design review, not a ban on familiar components or a claim that software detects AI authorship.

## Workflow

1. **Establish context.** Identify the product's main task, audience, environment, content model, emotional character, brand constraints, and existing tokens/components. Infer routine details from available material; state material assumptions. Never invent testimonials, metrics, customer logos, or contact details.
2. **State a visual thesis.** Select a relevant visual world such as editorial publishing, transport signage, technical manuals, scientific notebooks, or public archives. Explain how it shapes hierarchy, navigation, density, and content presentation. Avoid decorative metaphors that obstruct the task.
3. **Explore three directions.** Compare materially different layouts, typographic hierarchies, density, navigation, and media strategies. Color swaps do not count. Use quick compositions where useful. For a mature system or small component change, explore three compatible treatments within the existing language; do not redesign unrelated surfaces. In audit-only work, inspect and recommend without modifying UI.
4. **Commit to one language.** Select the strongest direction and explain the tradeoff. Define typography, grid/max-widths, spacing rhythm, semantic colors, shape rules, components, media, and purposeful motion. Respect user-specified designs and platform conventions. Select autonomously unless a missing preference materially changes scope.
5. **Implement the information model.** Choose lists, tables, rows, timelines, master-detail views, maps, or editorial sections when appropriate. Use cards for independently meaningful objects. Read [the review checklist](references/visual-review-checklist.md) before implementation and again during critique.
6. **Render and inspect.** Use the project's browser, emulator, simulator, or design renderer. Inspect actual screenshots at realistic size, both the initial view and full content. For responsive web, cover widths 320, 390, 430, 1280, and 1440 CSS pixels; add 375 or larger widths when relevant. For native or single-platform interfaces, use supported device sizes and document why other sizes are N/A. Cover navigation and relevant loading, empty, error, long-content, and dense-data states. Never call source inspection a visual review.
7. **Critique explicitly.** Record PASS, WARN, FAIL, UNVERIFIED, or justified N/A for product fit, distinctiveness, hierarchy, coherence, usability, accessibility, responsiveness, density, personality, restraint, and copy/content integrity. Attach screenshot paths and specific observations. Use scores only as optional discussion aids; an average cannot erase a failure.
8. **Refine and rerender.** Make at least one deliberate improvement pass, then inspect the affected views again. Choose refinements from observed problems: container removal, stronger hierarchy, better typography, more useful density, clearer copy, meaningful imagery, or fewer effects. If no visual change improves the design, record the alternatives evaluated and why they were rejected. Never fabricate a refinement or claim an unrendered UI is complete.
9. **Report the result.** Summarize the selected concept, completed refinement, evidence, remaining failures, and limitations. Mark visual readiness separately from functional, security, performance, store, deployment, and production checks. If rendering is blocked, deliver the implementation with visual review UNVERIFIED and identify the missing evidence.

## Evidence helper

Use the bundled Python standard-library tool to create and check a review record:

```bash
python3 <skill-directory>/scripts/visual_review.py init --output visual-review.json
python3 <skill-directory>/scripts/visual_review.py check visual-review.json
```

Fill the record after inspecting screenshots. Resolve screenshot paths relative to the record. The checker verifies required entries, status/evidence fields, render-file existence, and refinement records; it does **not** assess visual quality, inspect pixels, run accessibility tests, or prove that evidence is truthful. Capture screenshots using existing project tooling rather than installing a universal renderer. Keep generated review evidence in the user's project, outside the installed skill.

## Constraints and composition

- Preserve semantics, keyboard access, visible focus, contrast, touch targets, responsive behavior, reduced-motion preferences, and familiar navigation. Never sacrifice usability to novelty.
- Treat gradients, rounded corners, icons, dark themes, cards, and whitespace as contextual choices. Require rationale for repetitive or decorative use rather than banning them.
- Ask whether content hierarchy and interactions reveal the domain after removing the logo. A shared brand across products may legitimately share its visual language.
- Apply available website, Android, Flutter, iOS, desktop, or other readiness skills to their respective release boundaries. For service-only work without a UI, skip this skill.
- Use bundled shared review/reporting/domain references when supplied by a repository installation. They support evidence handling and do not expand a visual task into an unsolicited full production audit.
