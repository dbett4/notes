# MySPariEdge Learning Protocol

**Conclusion:** We should capture MySPariEdge for several consecutive MLB slates and treat it as teacher data. The goal is not to depend on the site forever; the goal is to learn its projection and grading behavior.

## Daily Capture Times

Pull at least twice:

| Time | Why |
|---|---|
| Morning | Captures early projections, opener-ish odds, and pre-lineup assumptions |
| After lineups lock | Captures final AB/order adjustments and stronger bet candidates |

Optional third pull near first pitch for price movement and late edge decay.

## Command

```bash
python3 scripts/run_daily_myspariedge_snapshot.py
```

This runs:

1. Full MySPariEdge data pull.
2. Player image download.
3. Model read report.
4. Grade reverse-engineering report.
5. Dave-history prop reports.

## What We Are Learning

### Projection Engine

Target fields:

- Hitter `AB`
- Pitcher `IP`
- Per-market rates
- Final projections
- Direction
- Grade

### Grade Engine

Target fields:

- Market
- Line
- Projection
- Absolute edge
- Grade
- Model history win rate
- Wins / losses

### Betting Edge Layer

Target fields:

- Best Bets grade
- Positive EV
- Sharp money
- Odds-board best price
- Closing line
- Actual result from `transactions.csv`

## Minimum Useful Dataset

Three to five slates should be enough to learn rough grade thresholds.

Ten to twenty slates should be enough to fit a better local projection clone.

## Daily Notes To Record

After each run, write one short note:

```text
Date:
Pull time:
Lineups locked?:
Best target markets:
Strongest +EV markets:
Notable surprises:
Model clone observations:
```

Save notes under:

`reports/learning_notes/YYYY-MM-DD.md`

## Success Criteria

The clone is useful when it can:

1. Match MySPariEdge projection grades within one grade for most props.
2. Recreate direction correctly for target-grade plays.
3. Identify the same top markets before relying on MySPariEdge Best Bets.
4. Explain disagreements in terms of volume, matchup, price, or weather.
