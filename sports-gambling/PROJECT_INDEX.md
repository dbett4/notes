# d + bet Project Index

**As of:** 2026-05-05  
**Purpose:** Operating map for Dave's sports betting research, model evidence, and app runtime. Read this first before any `d + bet` work.

## Conclusion

`d + bet` has two repos and one model spine:

| Context | Directory | Repo | Role |
|---|---|---|---|
| Notes / research | `~/Documents/Personal/notes/sports-gambling/` | `dbett4/notes` | Strategy docs, raw/processed research data, reports, model ledger |
| App runtime | `~/Documents/Code/betting-bot/` | `davebettner-lsl/d-plus-bet` | FastAPI + Next.js app, SQLite, Discord alerts, daily pipeline |

Current phase is **Phase 2 alert-only**. No auto-placement or live automation should be added until Phase 3 gates are met: **200+ settled bets with positive average CLV**.

## Source of Truth

| File | Role |
|---|---|
| `MODEL_LEDGER.md` | Model control center: active lanes, experimental lanes, validation status, gates |
| `data/catalog/sources.csv` | Source registry: provider/source, layer, cadence, trust level, canonical destination |
| `data/catalog/schemas.md` | Canonical betting spine entity definitions |
| `data/catalog/id_mapping.md` | ID rules for teams, players, events, books, and markets |
| `HANDOFF_FOR_CLAUDE.md` | First-read handoff for Claude if it has not seen the project |

## Current Operating Model

| Lane | Status | Source of Truth | Current Output |
|---|---|---|---|
| MLB MySPariEdge | Active alerting | `myspariedge-system.md`, `myspariedge-learning-protocol.md` | `data/processed/myspariedge_mlb_signals_2026-05-03.csv` |
| MLB performance review | Active evidence | `transactions.csv`, `reports/` | ROI and model-read reports |
| NBA player impact | Experimental priors | `wishlist-and-nba-notes.md`, `MODEL_LEDGER.md` | `data/processed/nba/player_impact_features.csv` |
| NFL | Roadmap | `MODEL_LEDGER.md` | None |
| NHL | Roadmap | `MODEL_LEDGER.md` | None |
| Soccer | Roadmap | `MODEL_LEDGER.md` | None |

## Brand and Design Sources

`d + bet` is independent from LSL. Do not use LSL branding, teal, or green-heavy guidance.

| File | Role |
|---|---|
| `DESIGN.md` | Notes-side brand color tokens, type scale, spacing rhythm |
| `d-plus-bet-design-source-pack.md` | Design references, constraints, and carry-forward prompt |
| `logo-exploration/app-preview.html` | Brand preview, currently modified/uncommitted |
| `logo-exploration/design-system-preview.html` | Component reference |
| `~/Documents/Code/betting-bot/DESIGN.md` | App-side UI direction; intentionally separate from notes-side brand docs |

## MLB Source Files

| File | Role |
|---|---|
| `myspariedge-system.md` | Site map, RL Meta filter settings, Discord channels |
| `myspariedge-learning-protocol.md` | Daily capture and learning protocol |
| `myspariedge-projection-clone-plan.md` | Clone architecture and build order |
| `mlb-player-props-system.md` | Player prop system policy source |
| `mlb-home-runs-system.md` | Home run prop lane policy source |
| `automation-spec.md` | Historical architecture; **book policy is outdated** |
| `transactions.csv` | Historical bets / ROI source |
| `reports/mlb_player_prop_performance.md` | Settled MLB player prop review |
| `reports/mlb_home_run_prop_performance.md` | Settled HR prop review |
| `reports/myspariedge_grade_reverse_engineering.md` | Projection grade thresholds / surrogate model evidence |
| `reports/learning_notes/YYYY-MM-DD.md` | Daily observations |

MLB remains the first production lane. Current active rule: MySPariEdge RL Meta uses Run Line, probability >= 60%, rank <= 7. Straight picks only for the system lane.

## NBA Source Files

| File | Role |
|---|---|
| `wishlist-and-nba-notes.md` | NBA project notes and source references |
| `data/raw/nba/jeremias-nba-metric.xlsx` | Raw Jeremias/RAPM workbook |
| `data/processed/nba/player-impact-starter.csv` | Initial starter/reference output |
| `scripts/build_nba_player_impact_features.py` | Repeatable NBA feature builder |
| `data/processed/nba/player_impact_features.csv` | Canonical NBA player-prior output |

NBA is **not** a pick engine yet. It is a player-prior feature layer until rotations, minutes, injuries, rest, odds, and market movement are integrated.

## App Runtime Boundary

Do not change `~/Documents/Code/betting-bot/` as part of notes/model integration unless explicitly requested.

| Runtime File | Role |
|---|---|
| `betting-bot/signals/base.py` | Canonical `Pick` / `Order` signal contract |
| `betting-bot/signals/myspariedge.py` | Active MySPariEdge scraper / `Pick` producer |
| `betting-bot/signal_router.py` | Signal filtering and EV/probability scoring |
| `betting-bot/config.py` | Signal filters: probability/rank |
| `betting-bot/settings.yaml` | Runtime policy: unit size, Kelly fraction, risk caps, book modes |

NBA feature files do not emit `Pick` objects. Duplicate recommendations should collapse by date/event/market/selection/line/player/pick, with books shown as execution context.

## Book Policy

No books are blanket-banned for ROI reasons. Book treatment is based on execution mode and user preference.

| Mode | Books | Policy |
|---|---|---|
| Auto-eligible later | ProphetX, Novig, Kalshi | ToS/API-compatible candidates for future Phase 3 automation |
| Manual alert-only | DraftKings, FanDuel, BetMGM, Fanatics, Hard Rock, bet365, ESPN BET | User places manually; do not auto-place |
| Preferred display books | DraftKings, FanDuel, Novig | Prefer as primary execution context when the same bet exists at multiple books |

`automation-spec.md` contains older book-policy assumptions. Treat this index and `MODEL_LEDGER.md` as the current policy.

## Daily Start

1. Read `PROJECT_INDEX.md` and `MODEL_LEDGER.md`.
2. For MLB work, read `myspariedge-system.md` and the latest `reports/learning_notes/`.
3. For NBA work, run `python3 scripts/build_nba_player_impact_features.py --validate`.
4. For app runtime work, read `~/Documents/Code/betting-bot/AGENTS.md` first.
5. Before any live/automation discussion, check the Phase 3 gate: 200+ settled bets and positive average CLV.

