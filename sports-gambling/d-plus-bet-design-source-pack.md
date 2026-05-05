# d + bet Design Source Pack

## Purpose

Use this packet to bring the Twitter-bookmark design research into the current `d + bet` design session.

Current source of truth:

- `/Users/davebettner/Documents/Personal/notes/sports-gambling/DESIGN.md`
- `/Users/davebettner/Documents/Personal/notes/sports-gambling/logo-exploration/app-preview.html`
- `/Users/davebettner/Documents/Personal/notes/sports-gambling/logo-exploration/design-system-preview.html`

Important correction: the current brand is exactly `d + bet`, lowercase with spaces around the plus. It is independent from LSL. Do not use LSL teal, LSL green guidance, LSL tone, or LSL visual identity.

## Current d + bet Design Direction

`d + bet` is a personal sports betting analytics brand. It should feel disciplined, sharp, private, and analytical. It is not a sportsbook, casino product, crypto tool, generic SaaS dashboard, or LSL artifact.

Current design language:

- Lowercase wordmark: `d + bet`
- Off-white paper background: `#F7F3EA`
- Ink primary text: `#171717`
- Warm surface cards: `#FFFAF0` / `#FFFDF7`
- Graphite signal accent: `#3F3A34`
- Muted slate for line movement / links / active navigation: `#4E5A61`
- Olive / green / red only for real semantic values, not brand decoration
- Compact, precise, Vercel-like rhythm
- Stripe-like typographic polish
- shadcn-style component restraint
- Betting-specific graphics: odds grids, ticket rails, line movement, model traces

Non-negotiables:

- No teal.
- No casino imagery.
- No neon sportsbook palette.
- No purple-blue AI gradients.
- No glowing blobs/orbs.
- No oversized generic SaaS cards.
- No hero layout for the actual app workflow.
- No green as brand accent.

## Source References To Carry Forward

### Peter Yang / Ravi Mehta 3-Layer Context

Sources:

- https://x.com/petergyang/status/2051306144199737508
- https://x.com/petergyang/status/2050946115374321901
- https://creatoreconomy.so/p/three-layer-system-for-context-engineering-ravi-mehta

Use for:

- Structuring serious AI design work into functional, visual, and data context.
- Preventing generic AI UI by giving the agent realistic product behavior, visual constraints, and content fixtures.
- Turning `d + bet` prompts into reusable source packs instead of one-off vibe prompts.

Apply to `d + bet` as:

- Functional context: alert-only betting research tool, not a sportsbook; current phase is manual review and manual placement.
- Visual context: paper/ink/graphite, dense private analytics, exact `d + bet` brand rules, current `app-preview.html`.
- Data context: realistic bet cards, MySPariEdge grades, book coverage, odds, stale-price states, confidence, CLV/ROI, line movement, blocked-action reasons.

Do not copy:

- Generic prototype examples or consumer-app visual language.
- Any assumption that the 3-layer structure alone creates taste. It is scaffolding, not design judgment.

### KirkMDesign / AI Design Workflow

Sources:

- https://x.com/KirkMDesign/status/2051290968565969363
- https://www.youtube.com/watch?v=JMQ0X_si144
- https://www.youtube.com/watch?v=nbk0PMS0tos
- https://claude.com/plugins/figma
- https://help.figma.com/hc/en-us/articles/39888629089175-Codex-and-Figma-Set-up-the-MCP-server
- https://openai.com/index/figma-partnership/

Use for:

- Round-trip AI design workflow: source pack -> design critique -> file edits -> screenshot review -> correction loop.
- Reusable design-source folders rather than repeated prompt dumps.
- Critique prompts that name purpose, hierarchy, weakest element, and next correction.

Apply to `d + bet` as:

- Organize design references by visual intent: quiet operational dashboard, dense betting review queue, premium private ledger, executive signal summary.
- Keep design packs selective: references, why they matter, forbidden cliches, token guidance, component guidance, and realistic content fixtures.
- Use Figma only as one canvas in the loop; the source of truth remains this pack plus `DESIGN.md` and code.

Do not copy:

- Competitor brand surfaces, Mobbin-style generic SaaS polish, or Figma-generated layouts without code/screenshot review.

### Motion Core

Sources:

- https://x.com/madebyhex/status/2051062415345721643
- https://motion-core.dev/
- https://motion-core.dev/docs/introduction
- https://madewithsvelte.com/motion-core

Use for:

- Motion restraint and state-change polish.
- Interaction ideas even if the active app remains React/HTML rather than Svelte.

Apply to `d + bet` as:

- Motion should clarify state: line moved, bet selected, drawer opened, price stale, card added to betslip, action blocked, provider degraded.
- Keep most motion at 120-240ms using transform/opacity.
- Do not animate critical numeric changes except a short crossfade or stable old/new comparison.

Do not copy:

- Svelte dependency choices by default.
- Spectacle, 3D, or motion that makes betting review feel slower.

### Jakub Krehel / Make Interfaces Feel Better

Source:

- https://jakub.kr/writing/details-that-make-interfaces-feel-better
- https://www.ui-skills.com/skills/jakubkrehel/make-interfaces-feel-better/
- https://github.com/jakubkrehel/make-interfaces-feel-better

Use for:

- Micro-polish: spacing, optical alignment, button feel, surface separation, shadows, and motion restraint.
- Before/after critique of the current `app-preview.html`.
- Rules that make the app feel intentionally designed rather than generated.

Apply to `d + bet` as:

- Tighten alignment across status rail, queue controls, metric cards, and bet rows.
- Use tabular numerals everywhere odds, EV, units, ROI, CLV, and bankroll figures appear.
- Keep surfaces flat and bordered; avoid heavy shadows except overlays.
- Make hover/press states crisp: 1px lift max on cards, `scale(0.97)` on button press.
- Treat small details as trust signals because betting review depends on fast confidence.

Do not copy:

- Any decorative motion or visual flourish that makes the betting workflow slower.

### Jakub Krehel / Shared Layout Animations

Source:

- https://jakub.kr/work/shared-layout-animations
- https://motion.dev/motion/layout-animations/

Use for:

- Ticket-to-detail continuity.
- Queue row to drawer transition.
- Tab changes when the selected object should remain spatially understandable.

Apply to `d + bet` as:

- When a proposed bet opens, the drawer should feel attached to the selected row or card.
- Use shared-layout-style motion for selected ticket rail, line movement detail, or compact row expansion.
- Keep motion subtle: transform/opacity only, 120-240ms for UI movement, no animation on critical number changes except short crossfade.

Do not use for:

- Betting logs, search, filters, or keyboard-heavy review flows.
- Odds/EV/stake numbers changing position.

### MDN / `scrollbar-gutter`

Source:

- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter

Use for:

- Stable scroll areas.
- Tables, ledgers, side drawers, ticket queues, and report panes.

Apply to `d + bet` as:

- Add `scrollbar-gutter: stable;` to the document and any fixed scroll containers where scrollbar appearance could shift odds/tables.
- Test the app preview on both desktop and mobile widths.

Do not assume:

- That overlay scrollbars solve every platform. Check layout shift directly.

### cc-design

Source:

- https://github.com/ZeroZ-lab/cc-design

Use for:

- Workflow, not visual style.
- Design scoring and screenshot verification.
- A quality gate before implementing a style pass.

Apply to `d + bet` as:

- Before editing CSS, inspect `DESIGN.md`, `app-preview.html`, and `design-system-preview.html`.
- Score the design against the current brand rules.
- Make a compact improvement plan.
- Then implement and verify with screenshots.

Do not install or import wholesale unless the session explicitly chooses that route.

### Kigen Color

Source:

- https://kigen.design/color

Use for:

- Token exploration only after the current palette constraints are respected.
- Checking accessible variants of paper/ink/signal/slate.

Apply to `d + bet` as:

- Keep `#F7F3EA`, `#171717`, and `#3F3A34` as the anchor.
- Explore only subtle supporting ramps for surfaces, lines, and muted state.

Do not use for:

- Inventing a new palette.
- Introducing teal, neon, saturated green, or one-note accent systems.

### React Bits / Vue Bits / Svelte Bits

Sources:

- https://reactbits.dev/
- https://vue-bits.dev/
- https://sveltebits.xyz/

Use for:

- Interaction ideas only.
- Empty state patterns, compact animated state changes, subtle model trace treatments.

Apply to `d + bet` as:

- Harvest a single behavior when it supports betting review: line movement trace, selected state, compact queue movement, or loading state.
- Re-skin everything into `d + bet` paper/ink/graphite.

Do not copy:

- Their color, glow, spectacle, or demo-page personality.

### ReUI / Shadcn Space / Shadcn Collections

Sources:

- https://reui.io/
- https://github.com/shadcnspace/shadcnspace

Use for:

- Component structure.
- Tables, drawers, tabs, buttons, inputs, toasts, and command menus.

Apply to `d + bet` as:

- Use shadcn-style restraint: small radius, clear border, dense spacing, readable states.
- Keep components subordinate to the `d + bet` visual system.

Do not copy:

- Generic SaaS block composition.
- Marketing hero sections.
- Big rounded cards.

### Cross-Document View Transitions

Source:

- https://developer.chrome.com/docs/web-platform/view-transitions/cross-document

Use for:

- Static HTML design previews or multipage reference docs.

Apply to `d + bet` as:

- Consider only for transitions between design exploration pages, not the core betting app unless browser support/fallbacks are clean.

### muload

Source:

- https://muload.dev/

Use for:

- Loader-state inspiration.

Apply to `d + bet` as:

- Replace blank spinners with useful status: checking books, loading slate, validating lineups, computing EV, logging decision.
- Keep loader treatment flat, graphite, and minimal.

Do not copy:

- Stylized AI loader aesthetics that feel toy-like.

### Cloudflare API Key UX / Permissions

Source:

- https://developers.cloudflare.com/api/overview/

Use for:

- Human-readable permission and risk explanation.

Apply to `d + bet` as:

- Every manual action should say what it changes: placed, skipped, rejected, logged, imported, or settled.
- Any automation setting should distinguish read-only checks from write/placement actions.

## Design Priorities For The Next Session

1. Preserve current `d + bet` identity: paper/ink/graphite, lowercase wordmark, no LSL.
2. Use the 3-layer context model: functional behavior, visual system, realistic betting data/content.
3. Refine the app preview rather than redesigning it.
4. Tighten scan hierarchy for betting review: proposed bets, odds, EV, line movement, stake, confidence, and action.
5. Make the drawer/selected ticket feel attached without adding decorative motion.
6. Improve state surfaces: empty, loading, degraded provider, stale odds, blocked action, placed, rejected.
7. Keep everything dense, calm, and private.
8. Run a screenshot critique loop after edits; do not rely on code inspection alone.

## Adjacent Non-Design Research Queue

These X bookmark sources are relevant but should not drive the immediate visual design pass:

- Matt Pocock skills: borrow skill/source-pack structure, not visual style. Source: https://github.com/mattpocock/skills
- Vercel `deepsec`: borrow scan -> investigate -> revalidate -> export as a future QA/review harness. Source: https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base
- OpenAI `codex-plugin-cc`: test later for Claude/Codex review delegation. Source: https://github.com/openai/codex-plugin-cc/blob/main/README.md
- Open Slide: test later for a d + bet weekly edge report deck. Source: https://open-slide.dev/
- DeepSeek V4: test later for cheap long-context synthesis using non-client, non-sensitive fixtures. Source: https://api-docs.deepseek.com/news/news260424

## Copyable Prompt

```text
We are working on the current d + bet design in:

/Users/davebettner/Documents/Personal/notes/sports-gambling

Use these files as source of truth:
- /Users/davebettner/Documents/Personal/notes/sports-gambling/DESIGN.md
- /Users/davebettner/Documents/Personal/notes/sports-gambling/logo-exploration/app-preview.html
- /Users/davebettner/Documents/Personal/notes/sports-gambling/logo-exploration/design-system-preview.html
- /Users/davebettner/Documents/Personal/notes/sports-gambling/d-plus-bet-design-source-pack.md

Important: the brand is exactly `d + bet`, lowercase, with spaces around the plus. This is not LSL. Do not use LSL teal, LSL green guidance, LSL tone, or LSL visual identity.

Goal:
Refine the current d + bet design using the source pack, not redesign from scratch. The design should feel like a disciplined private betting analytics tool: paper/ink/graphite, sharp, quiet, dense, and premium. It should not feel like a sportsbook, casino, crypto app, generic SaaS dashboard, or AI-gradient demo.

Current direction to preserve:
- `color-paper` #F7F3EA
- `color-ink` #171717
- `color-surface` #FFFAF0
- `color-surface-2` #FFFDF7
- `color-line` #D8D0C3
- `color-muted` #79736A
- `color-signal` #3F3A34
- `color-slate` #4E5A61
- semantic green/red only for real values and states
- Geist / Satoshi-like typography
- compact 4px/6px/10px/12px/24px rhythm
- 4px buttons, 6px cards/panels, 8px overlays
- tabular numerals for odds, EV, ROI, units, bankroll, and CLV

Use the references this way:
- Peter Yang / Ravi Mehta 3-layer context: structure the work into functional, visual, and data context before editing.
- KirkMDesign AI design workflow: use this source pack as reusable design context, then critique, edit, screenshot, and correct.
- Motion Core: use motion to clarify state changes only; no spectacle.
- Jakub Krehel / Make Interfaces Feel Better: micro-polish, optical alignment, spacing, surfaces, button feel, restrained motion.
- Jakub shared layout animations + Motion docs: selected ticket to drawer continuity only; keep motion subtle.
- MDN scrollbar-gutter: prevent queue/table/drawer layout shift.
- cc-design: use as a design QA workflow, not a visual style.
- Kigen Color: token pressure-test only; do not invent a new palette.
- React/Vue/Svelte Bits: harvest single interaction ideas only; re-skin into d + bet.
- ReUI/shadcn collections: component structure only, not generic SaaS style.
- muload: loader-state inspiration only, flat and useful.
- Cloudflare permissions UX: make actions and automation permissions human-readable.

Concrete task:
1. Read DESIGN.md and the source pack first.
2. Inspect app-preview.html and design-system-preview.html.
3. Write a compact 3-layer working brief:
   - Functional: what the current screen must help Dave decide.
   - Visual: what hierarchy and tone it must preserve.
   - Data: what realistic bet states/content are present or missing.
4. Identify 5-8 high-impact refinements that preserve the current direction.
5. Update the relevant preview/design files.
6. Verify visually at desktop and mobile widths.
7. Summarize what changed and which source-pack references drove each change.

Constraints:
- No teal.
- No LSL styling.
- No casino imagery, neon, chips, dice, cards, flames, or fake big-win energy.
- No purple-blue gradients, glowing orbs, or decorative AI visuals.
- No oversized marketing hero for the actual app.
- No generic SaaS block dump.
- No green as brand accent.
- Do not animate keyboard-heavy workflows or critical number changes.
```
