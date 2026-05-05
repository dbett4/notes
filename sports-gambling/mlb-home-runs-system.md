# MLB Home Runs System

**Status:** active focus
**Goal:** Use MySPariEdge Best Bets to produce a short daily HR card, then target graded `A+` through `B+` candidates.

## Recommendation

Make HR props the first player-prop specialization. Your export shows `+$801.87` on `484` settled MLB HR bets, a `+14.8%` ROI. The target pool should be MySPariEdge Best Bets graded `A+`, `A`, `A-`, or `B+`.

## Daily HR Card

Each candidate should include:

| Field | Purpose |
|---|---|
| Player / team / opponent | Bet matching |
| Lineup spot | HR volume context |
| Pitcher handedness | Platoon context |
| Ballpark | Power environment |
| Weather | Wind/temp boost or drag |
| MySPariEdge Best Bets grade | Must be `A+` through `B+` |
| MySPariEdge history | Win %, wins, losses |
| MySPariEdge projection | Projection versus line |
| Best book and price | Execution |
| Dave-history context | Recordkeeping only; no book exclusions |

## Eligibility Rules

Bet only when:

1. MySPariEdge Best Bets includes the HR prop with grade `A+`, `A`, `A-`, or `B+`.
2. The player is confirmed in the starting lineup.
3. The price is still within the accepted move from signal capture.
4. The available price is competitive with the best captured market price.
5. The bet is a standard `Over 0.5 HR` / `To Hit a HR` market unless manually approved.

## MySPariEdge Best Bets Feed

The Best Bets page calls:

`https://api.myspariedge.com/api/v1/projections/best-bets`

The front-end schema includes:

| Field | Use |
|---|---|
| `player_name` / `player_id` | Player matching |
| `team`, `position`, `game` | Context and slate matching |
| `market`, `market_label` | HR market detection |
| `side`, `line`, `projection` | Bet definition |
| `bet_grade` | Primary targeting filter |
| `win_pct`, `wins`, `losses` | Pattern strength |

Target grades are `A+`, `A`, `A-`, and `B+`. Ignore `B` and lower for the automated daily HR card unless manually reviewed.

## Initial Filters From Dave's Export

| Segment | Treatment |
|---|---|
| Standard HR over / yes | Primary focus |
| Alt-over HR ladders | Manual-only |
| `+800 to +1199` | Best historical profit band; require MySPariEdge confirmation |
| `+1200+` | Lotto-only |
| All sportsbooks | Eligible; use whichever book offers the best playable price |

## Daily Workflow

1. Pull MySPariEdge Best Bets.
2. Keep grade `A+` through `B+`.
3. Filter to home-run markets.
4. Enrich with lineup, handedness, park, and weather.
5. Keep only candidates that pass eligibility rules.
6. Save the daily card to `reports/daily_mlb_home_runs_YYYY-MM-DD.md`.
7. After settlement, join back to `transactions.csv` and update HR performance.

## Bet Sizing

- Standard HR card: `0.25u` to `0.5u` until joined MySPariEdge sample confirms edge.
- Best tier only: `1u` max.
- Ladders and `+1200+`: `0.1u` lotto-only, manual approval.

## Next Build Step

Once authenticated MySPariEdge pulls are working, create `daily_mlb_home_runs.py`:

1. Read `data/processed/myspariedge_mlb_signals_YYYY-MM-DD.csv`.
2. Keep `signal_type=best_bet` and `is_target_grade=true`.
3. Keep HR candidates.
4. Apply the lineup, context, and price filters above.
5. Render a concise daily betting card.
