# MLB Player Props System

**Status:** Phase 1 read-only build
**Signal source:** MySPariEdge Best Bets, player projections, and model history
**Goal:** Turn MySPariEdge `A+` through `B+` Best Bets plus strong projection/history markets into a disciplined daily prop shortlist, then compare every pick against Dave's actual betting history and closing-line movement.

## Recommendation

Start with a read-only daily card, not auto-betting. The first filter is MySPariEdge Best Bets graded `A+`, `A`, `A-`, or `B+`; the second layer is player projections and model history by market. Price and player context decide whether those make the betting card.

## Daily Inputs

| Source | Pull | Purpose |
|---|---|---|
| MySPariEdge `/projections/best-bets` | `A+` through `B+` player prop patterns | Primary model signal |
| MySPariEdge `/projections?league=mlb` | Player-level lines, projections, directions, grades, HR%, lineup order | Projection discovery |
| MySPariEdge `/projections/history` | Model performance by market, side, grade, season | Market selection |
| MySPariEdge `/projections/game` | Top Strikeout Plays and slate context | Slate context |
| MySPariEdge `/odds/positive-ev` | Best available prop price by book | Price confirmation |
| `transactions.csv` | Dave's historical results | Recordkeeping and later validation |
| Sportsbook lines | All available books | Execution and price shopping |

## Bet Eligibility

A prop becomes a candidate only when all of these pass:

1. MySPariEdge Best Bets grades it `A+`, `A`, `A-`, or `B+`.
2. The target book price is competitive with the best captured market price.
3. The market has enough projection/history strength to justify the variance.
4. The player is confirmed active or in the expected lineup.
5. The odds have not degraded beyond the configured threshold from the captured MySPariEdge price.

## Initial Dave-History Read

Based on the current `transactions.csv` export:

| Treatment | Markets |
|---|---|
| Strongest current read | Home runs and runs props |
| Require stronger confirmation | Pitcher strikeouts; Hits; Total Bases; H+R+RBI |

Do not restrict books based on previous performance. Book-level history is for tracking, not eligibility.

## Data Model

Create one row per candidate prop per book.

| Field | Notes |
|---|---|
| `pulled_at` | Timestamp from daily scrape |
| `game_date` | MLB slate date |
| `player` | Normalized player name |
| `team` | Player team |
| `opponent` | Opponent team |
| `market` | Strikeouts, hits, runs, RBIs, total bases, HR, H+R+RBI |
| `side` | Over / Under / Alt Over |
| `line` | Prop threshold |
| `myspariedge_projection` | If available |
| `myspariedge_probability` | If available |
| `myspariedge_edge` | If available |
| `myspariedge_grade` | `A+` through `B+` target flag |
| `myspariedge_win_pct` | Historical pattern win rate |
| `myspariedge_wins` / `myspariedge_losses` | Pattern sample size |
| `model_history_win_pct` | Market/side/grade history where available |
| `projection_direction` | Over / Under from player projections |
| `book` | Sportsbook |
| `price` | American or decimal, stored consistently |
| `best_available_price` | Best line across tracked books |
| `lineup_status` | Confirmed / expected / unknown |
| `recommendation` | Bet / watch / pass |
| `reason` | Short machine-readable explanation |
| `bet_id` | Joined after placement/export |
| `closing_line` | From transaction export or odds snapshot |
| `result` | Win/loss/push/void |
| `profit` | Settled P&L |

## Phase 1 Workflow

1. Pull MySPariEdge props each morning into `data/raw/myspariedge/YYYY-MM-DD/`.
2. Normalize into `data/processed/mlb_player_props_YYYY-MM-DD.csv`.
3. Generate `reports/myspariedge_mlb_model_read.md` to identify the best-performing markets.
4. Generate `reports/daily_mlb_player_props_YYYY-MM-DD.md` with eligible candidates.
5. After settlement, join candidates to `transactions.csv`.
6. Review weekly by market, book, side, line movement, and MySPariEdge signal type.

## Guardrails

- Straight bets only.
- One unit max until the joined signal sample proves durable.
- No parlays or home-run ladders in automation.
- Do not place a bet when the prop cannot be matched cleanly to player, market, line, side, and book.

## Open Items

- Confirm MySPariEdge login/session method for repeatable pulls.
- Capture the exact fields exposed by `/projections/best-bets` for MLB props.
- Decide the max acceptable price move from signal capture to bet placement.
- Confirm unit size and bankroll cap.
