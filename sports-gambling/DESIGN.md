# d + bet Design System

## Philosophy

`d + bet` is a personal sports betting analytics brand, not a sportsbook and not a casino. The interface should feel disciplined, sharp, and private: a tool for finding edge, logging decisions, and avoiding noise.

This brand is independent from LSL. Do not use LSL colors, LSL teal, LSL green guidance, LSL tone, or LSL visual identity.

## Brand Name

| Token | Value |
| --- | --- |
| Display name | `d + bet` |
| Case | Always lowercase |
| Spacing | Spaces on both sides of the plus sign |
| Incorrect | Any uppercase, unspaced, or condensed spelling |

## Aesthetic Direction

| Decision | Type | Guidance |
| --- | --- | --- |
| Analytical wordmark | SAFE | The brand should read as a betting edge tool before it reads as entertainment. |
| Graphite plus sign | SAFE | The plus becomes the signal: edge, action, and selection without adding sportsbook heat. |
| Graphite/off-white base | SAFE | Keeps the system calm and durable for logs, dashboards, and reports. |
| Muted slate as secondary accent | SAFE | Useful for live market movement, alerts, or odds movement without feeling loud. |
| Semantic green/red | SAFE | Use only for positive/negative values and operational state, never as brand accent. |

Avoid sportsbook clichés: casino chips, cards, dice, neon, flames, dollar signs, parlay-ticket illustrations, mascots, and fake “big win” energy.

The Twitter-bookmark direction to carry forward is: source-of-truth `DESIGN.md`, precise Vercel-like layout rhythm, Stripe-like typographic polish, shadcn-style component restraint, and graphic elements that look like odds grids, ticket rails, line movement, or model traces. Do not borrow their palettes directly.

## Color

### Core Palette

| Token | Hex | Usage |
| --- | --- | --- |
| `color-ink` | `#171717` | Primary text, logo text, chart axes |
| `color-paper` | `#F7F3EA` | Main app background |
| `color-surface` | `#FFFAF0` | Panels, cards, inputs |
| `color-surface-2` | `#FFFDF7` | Hovered/elevated surface |
| `color-line` | `#D8D0C3` | Borders, dividers, grid lines |
| `color-muted` | `#79736A` | Secondary text |
| `color-signal` | `#3F3A34` | Primary accent, plus sign, selected rail |
| `color-slate` | `#4E5A61` | Line movement, links, active navigation |
| `color-olive` | `#5E6048` | Positive state, secondary trace |
| `color-success` | `#1F7A4D` | Positive value, profit, valid state |
| `color-warning` | `#6F5B3E` | Risk, pending, moved line |
| `color-error` | `#B23A33` | Negative value, failed bet, blocker, rejected condition |

### Dark Palette

| Token | Hex | Usage |
| --- | --- | --- |
| `color-dark-bg` | `#181613` | Dark surfaces |
| `color-dark-surface` | `#201C18` | Dark cards |
| `color-dark-text` | `#FFF9EE` | Dark mode text |
| `color-dark-muted` | `#B9AA99` | Dark mode secondary text |
| `color-dark-line` | `#3A332C` | Dark dividers |

### Color Rules

Do not use teal. Teal reads as LSL and is off-brand here.

Use `color-signal` sparingly. The plus should feel like a decision point, not an error state. The system should read as monochrome first, with state color visible only when it carries meaning.

Use green and red only for literal semantic values: profit/loss, valid/invalid, positive/negative edge, blocker/error. Green and red are not brand colors and should not appear in logo, navigation, primary actions, empty states, or decorative graphics.

## Typography

Primary type should feel technical but not default. Use `Geist` / `Geist Sans` for UI if available. Use `Satoshi` as the brand fallback. Avoid Inter as the only brand typeface because it makes the identity feel generic.

Editorial/report contexts may pair the sans with `Fraunces` for section titles, but the core app should stay sans-first.

| Token | Size | Line Height | Tracking | Weight | Usage |
| --- | ---: | ---: | ---: | ---: | --- |
| `type-micro` | `11px` | `16px` | `0.10em` | `650` | Uppercase labels only |
| `type-xs` | `12px` | `16px` | `0` | `500` | Dense metadata |
| `type-sm` | `13px` | `18px` | `0` | `450` | Secondary UI text |
| `type-md` | `14px` | `22px` | `0` | `450` | Default app body |
| `type-lg` | `16px` | `24px` | `0` | `520` | Card titles, table primary cells |
| `type-xl` | `20px` | `28px` | `-0.01em` | `650` | Section headings |
| `type-2xl` | `28px` | `34px` | `-0.015em` | `700` | Page headings |
| `type-3xl` | `40px` | `46px` | `-0.018em` | `740` | Brand moments |
| `type-4xl` | `56px` | `60px` | `-0.02em` | `760` | Logo/hero-only use |

### Type Rules

Use letter spacing `0` for normal text. Use negative tracking only on headings at `type-xl` and above. Use uppercase label tracking only at micro scale, not on normal body copy.

Keep numerals tabular in tables, odds, bankroll views, and performance summaries.

Never use hero-scale type inside dense dashboards or cards.

Use `type-md` (`14/22`) as the default app body size. Reserve `16px` body copy for prose pages, onboarding, and reports. This keeps betting logs, odds tables, and model cards dense enough to scan.

## Spacing

Base grid: `4px`. UI rhythm uses a compact 4px/6px hybrid inspired by precise technical products: 4px for icon gaps, 6px/10px for small control tuning, 12px for related groups, 24px for panel rhythm, and 48px for page rhythm.

| Token | Value | Usage |
| --- | ---: | --- |
| `space-2xs` | `4px` | Tight icon/text gaps |
| `space-tight` | `6px` | Tiny control tuning |
| `space-xs` | `8px` | Small internal spacing |
| `space-ui` | `10px` | Compact nav/control padding |
| `space-sm` | `12px` | Compact form/control spacing |
| `space-md` | `16px` | Default component padding |
| `space-card` | `20px` | Dense card/panel padding |
| `space-lg` | `24px` | Section rhythm |
| `space-xl` | `32px` | Page group spacing |
| `space-2xl` | `48px` | Major layout separation |
| `space-3xl` | `64px` | Brand/landing moments only |

### Type And Spacing Pairings

| Element | Type | Padding / Gap | Rule |
| --- | --- | --- | --- |
| Top nav item | `type-sm` | `8px 10px` | Compact and quick to scan |
| Primary button | `type-sm` | `0 14px`, `40px` height | Short labels only |
| Form input | `type-md` | `0 12px`, `42px` height | Aligns with button rhythm |
| Card heading | `type-lg` or `type-xl` | `0 0 12px` | No large hero text in cards |
| Metric card | `type-micro` label + `type-2xl` value | `16px` padding, `8px` label gap | Numerals are the hierarchy |
| Data table row | `type-sm` | `12px 0` | Dense but not cramped |
| Page section | `type-2xl` heading | `24px` internal gap | Use `48px` only between major sections |

## Radius

| Token | Value | Usage |
| --- | ---: | --- |
| `radius-xs` | `2px` | Tiny badges, table chips |
| `radius-sm` | `4px` | Buttons, inputs |
| `radius-md` | `6px` | Cards, panels |
| `radius-lg` | `8px` | Modals, large grouped surfaces |

Avoid pill-shaped controls unless the shape conveys a specific binary or segmented state.

## Layout

| Token | Value |
| --- | ---: |
| `container-sm` | `720px` |
| `container-md` | `1040px` |
| `container-lg` | `1280px` |
| `gutter-mobile` | `16px` |
| `gutter-desktop` | `32px` |
| `breakpoint-sm` | `640px` |
| `breakpoint-md` | `900px` |
| `breakpoint-lg` | `1200px` |

Dashboard layouts should be dense but calm. Prefer tables, compact panels, and clear hierarchy over decorative cards.

## Graphic Direction

Use graphics as system language, not decoration.

| Motif | Use | Rule |
| --- | --- | --- |
| Probability grid | Empty states, logo boards, report covers | Thin graphite lines at low opacity; never a busy background behind body text |
| Odds ticket rail | Bet cards, queue items | Small perforation/rail detail is acceptable if subtle |
| Line movement trace | Alerts, model movement, chart headers | Use `color-slate` or `color-olive`; avoid gradient glow |
| Signal plus | Logo, selected state, critical action | Use `color-signal`; keep the plus crisp and flat |
| Mono numerals | Odds, units, ROI, closing-line value | Use tabular figures; right-align where comparable |

Do not use generic abstract blobs, glowing gradients, purple-blue AI backgrounds, or decorative charts that do not correspond to real data.

## Components

### Buttons

| Variant | Background | Text | Border | Usage |
| --- | --- | --- | --- | --- |
| Primary | `color-ink` | `color-paper` | `color-ink` | Main action |
| Signal | `color-signal` | `color-paper` | `color-signal` | Rare decisive action |
| Secondary | `color-surface` | `color-ink` | `color-line` | Normal secondary action |
| Ghost | `transparent` | `color-ink` | `transparent` | Low-emphasis actions |

Buttons must have `:active { transform: scale(0.97); }`.

### Tables

Use tabular numerals, visible row separators, and muted metadata. Avoid heavy fills. Positive/negative values can use semantic color, but confidence should rely on labels and position, not color alone.

### Cards And Panels

Cards should have `1px` borders, subtle surface contrast, and `6px` radius. Do not nest cards inside cards.

## Motion

Motion should make the tool feel responsive, premium, and quietly alive. It should never make betting review feel delayed.

| Token | Value | Usage |
| --- | --- | --- |
| `ease-out` | `cubic-bezier(0.23, 1, 0.32, 1)` | Enter states, button feedback |
| `ease-in-out` | `cubic-bezier(0.77, 0, 0.175, 1)` | On-screen movement |
| `duration-fast` | `120ms` | Press feedback |
| `duration-normal` | `180ms` | Dropdowns, small popovers |
| `duration-slow` | `240ms` | Modals, drawers |
| `duration-enter` | `320ms` | First-load panel reveal only |
| `duration-line` | `900ms` | Rare chart/line-draw reveal |

Do not animate keyboard-heavy workflows. Betting logs, search, filters, and command palette actions should feel instant.

Use `transform` and `opacity` for animation. Avoid `transition: all`.

### Motion Recipes

| Moment | Motion | Rule |
| --- | --- | --- |
| First screen load | Panels fade in and move `6px` upward over `320ms`, staggered by `40ms` | Runs once; never blocks interaction |
| Ticket hover | Move up `1px`, deepen border, reveal selected rail opacity | No scale on hover; scale is reserved for press |
| Button press | `transform: scale(0.97)` for `120ms` | Applies to all pressable controls |
| Line movement graphic | Stroke draws once over `900ms` using `stroke-dashoffset` | Use for charts and hero graphics only |
| Drawer open | Opacity + `translateX(8px)` over `240ms` | Drawer should feel attached to the selected ticket |
| State changes | Crossfade numbers and labels over `160ms`; no position animation | Prevents data changes from feeling slippery |

Reduced motion: remove transform movement and line drawing, keep short opacity changes only.

## Elevation

Prefer flat surfaces with borders. Use shadows only for temporary overlays.

| Token | Value | Usage |
| --- | --- | --- |
| `shadow-sm` | `0 1px 2px rgba(23, 23, 23, 0.08)` | Small menus |
| `shadow-md` | `0 10px 30px rgba(23, 23, 23, 0.14)` | Popovers |
| `shadow-lg` | `0 24px 60px rgba(23, 23, 23, 0.22)` | Modals |

## Logo Rules

Use the wordmark `d + bet` exactly. The plus sign is the only element that should commonly receive accent color.

Preferred lockups:
- Full wordmark: `d + bet`
- Compact mark: `d+`
- App icon: squared `d+` monogram with graphite border and graphite plus

Do not add taglines to the logo. Do not make the plus look like a medical cross.

## Anti-Patterns

Do not use:
- Teal or LSL color language
- Purple gradients
- Glowing orbs
- Casino imagery
- Centered marketing hero layouts for the actual app
- Oversized cards for dense operational views
- Decorative animation on repeated workflows
- Green as a brand accent

## Governance

Changes to brand colors, typography, logo usage, spacing scale, or motion tokens require updating this `DESIGN.md` first.
