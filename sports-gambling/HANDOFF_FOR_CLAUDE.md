# d + bet Project Handoff for Claude

Date: 2026-05-04

## Conclusion

This repo is Dave's personal sports betting analytics project, currently called `d + bet`. Claude has not seen it yet. Start by reading this file, then `README.md`, `d-plus-bet-design-source-pack.md`, `myspariedge-system.md`, `myspariedge-learning-protocol.md`, and `wishlist-and-nba-notes.md`.

The project has two active lanes:

1. Build a disciplined, private, analytical betting assistant/product concept under the `d + bet` brand.
2. Reverse-engineer and improve Dave's betting edge using MySPariEdge MLB data first, with NBA player-impact modeling just started.

## Brand and Product Direction

`d + bet` is independent from LSL. Do not use LSL branding, LSL teal, LSL green guidance, or LSL tone.

The current brand should feel:

- Disciplined
- Sharp
- Private
- Analytical
- Personal, not sportsbook/casino/SaaS generic

Current visual language lives in:

- `DESIGN.md`
- `d-plus-bet-design-source-pack.md`
- `logo-exploration/app-preview.html`
- `logo-exploration/design-system-preview.html`

Retired logo-shotgun variants were removed on 2026-05-04. Do not treat `variant-a-graphite-edge.html`, `variant-b-market-pulse.html`, `variant-c-private-ledger.html`, or the old `logo-exploration/index.html` comparison page as active source files.

Important design constraints:

- Brand spelling: `d + bet`, lowercase.
- No teal.
- No casino imagery.
- No neon sportsbook palette.
- No purple-blue AI gradients.
- No glowing blobs/orbs.
- No oversized generic SaaS cards.
- Green may be used when it is clearly not LSL teal/green. Prefer muted analytical greens; keep red for real negative or blocking states.
- Actual app workflows should be compact and useful, not landing-page-first.

## Current Data and Analysis State

### MySPariEdge MLB lane

Core docs:

- `myspariedge-system.md` - site map, Donuts strategy, RL Meta rules, Discord channel notes.
- `myspariedge-learning-protocol.md` - how to learn from daily picks/results.
- `myspariedge-projection-clone-plan.md` - plan for approximating MySPariEdge's projection logic.
- `mlb-player-props-system.md` - player prop analysis lane.
- `mlb-home-runs-system.md` - home run prop lane.

Scripts:

- `scripts/pull_myspariedge_mlb.py`
- `scripts/run_daily_myspariedge_snapshot.py`
- `scripts/analyze_myspariedge_model.py`
- `scripts/reverse_engineer_myspariedge_grades.py`
- `scripts/analyze_mlb_player_props.py`
- `scripts/analyze_mlb_home_runs.py`
- `scripts/download_myspariedge_player_images.py`

Reports:

- `reports/myspariedge_mlb_model_read.md`
- `reports/myspariedge_grade_reverse_engineering.md`
- `reports/myspariedge_projection_grade_thresholds.csv`
- `reports/myspariedge_best_bet_grade_evidence.csv`
- `reports/mlb_player_prop_performance.md`
- `reports/mlb_home_run_prop_performance.md`
- `reports/learning_notes/2026-05-03.md`

Processed signal file:

- `data/processed/myspariedge_mlb_signals_2026-05-03.csv`

Raw MySPariEdge pulls live under:

- `data/raw/myspariedge/2026-05-03/`

Most important betting rule captured so far: Donuts' RL Meta filter is Run Line, min probability 60%+, max rank <= 7. Straight picks only at 1 unit for automation; avoid parlays/lottos in the system lane.

### NBA lane

Just started. Main note:

- `wishlist-and-nba-notes.md`

Imported NBA files:

- `data/raw/nba/jeremias-nba-metric.xlsx`
- `data/processed/nba/player-impact-starter.csv`

Sanity check from Codex:

- `player-impact-starter.csv` has 1,478 rows including header.
- `jeremias-nba-metric.xlsx` has one sheet with 1,478 rows x 52 columns.
- Workbook source is Jeremias Engelmann's 2026-05-04 article, "How to build an NBA box-score metric."

Recommended NBA direction:

Start with a reusable player impact layer, not picks. The workbook is player-level decade data, best used for player priors. Build team/game betting layers later once rosters, projected minutes, injuries, rest, odds, and market movement are available.

First NBA modeling steps:

1. Calculate possession-normalized player rates from raw counts.
2. Z-score player features.
3. Create offensive and defensive player-strength scores using RAPM as the target.
4. Add reliability weights from `off_RAPM_SE`, `def_RAPM_SE`, `possessions`, and `seasons`.
5. Later aggregate to team/game level.

## Current Repo State

The worktree is dirty and intentionally contains a lot of new project files. Do not assume untracked files are trash.

Known status from Codex on 2026-05-04:

- Modified: `logo-exploration/app-preview.html`
- Untracked: `.gitignore`, `data/`, MLB system docs, MySPariEdge protocol/plan docs, `reports/`, `scripts/`, `wishlist-and-nba-notes.md`, and this handoff file.

Do not run destructive git commands. Dave commits code/project changes intentionally.

## How Claude Should Start

1. Read `README.md` for the broad intent.
2. Read `d-plus-bet-design-source-pack.md` before touching any design/UI work.
3. Read `myspariedge-system.md` before touching MySPariEdge logic.
4. Read `wishlist-and-nba-notes.md` before touching NBA.
5. Inspect the relevant script/report pair before changing analysis logic.

Recommended first Claude task:

Create a short project index or roadmap that ties the design lane, MLB MySPariEdge lane, and NBA player-impact lane into one operating model for Dave. Keep it practical: what files are source of truth, what runs daily, what decisions remain open, and what should be built next.

## Guardrails

- Search online for current sports/product/model details before relying on memory.
- For sports betting, distinguish historical model evidence from live market advice.
- Do not fabricate betting performance; cite the report or data file backing a claim.
- Keep the betting system disciplined: fewer plays, straight bets, 1 unit unless Dave explicitly experiments.
- Preserve Dave's authentic notes and writing voice when editing.
