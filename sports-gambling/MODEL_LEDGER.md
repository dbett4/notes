# d + bet Model Ledger

**As of:** 2026-05-05  
**Purpose:** Canonical state of model lanes, assumptions, validation gates, and source-of-truth status.

## Conclusion

The current model is an alert-only betting research system. MLB MySPariEdge is the only active alerting lane. NBA is an experimental player-prior feature layer. NFL, NHL, and soccer are roadmap lanes. No auto-placement or live wager automation is active.

## Phase Gates

| Phase | Status | Gate |
|---|---|---|
| Phase 2 alert-only | Active | Signals may be generated and reviewed, but user places any bets manually |
| Phase 3 automation | Closed | Requires 200+ settled bets with positive average CLV |

CLV is the primary edge test. ROI matters after sample size exists. Hit rate is secondary and must always be shown with sample size and average price.

## Active Lane: MLB MySPariEdge

| Item | Current Policy |
|---|---|
| Role | First production alerting lane |
| Primary signal | MySPariEdge MLB RL Meta |
| Filter | Run Line, probability >= 60%, rank <= 7 |
| Bet type | Straight picks only |
| Unit policy | 1 unit baseline for system review |
| Validation | CLV first, ROI second, hit rate with sample-size context |
| Current evidence | `reports/`, `transactions.csv`, `data/processed/myspariedge_mlb_signals_2026-05-03.csv` |

Model direction:

- Use MySPariEdge as the current signal source.
- Add baseball context only when it can be traced and validated: starting pitcher, bullpen usage, lineup strength, park, weather, rest, odds movement.
- Longer-term model direction is a negative-binomial run model with pitcher xFIP/SIERA, handedness wRC+, bullpen workload, park factor, weather, rest, and home/away splits.

## Experimental Lane: NBA Player Impact

| Item | Current Policy |
|---|---|
| Role | Player-prior feature layer |
| Source | `data/raw/nba/jeremias-nba-metric.xlsx` |
| Builder | `scripts/build_nba_player_impact_features.py` |
| Output | `data/processed/nba/player_impact_features.csv` |
| Status | Experimental, not a pick engine |

NBA cannot emit picks until these layers exist:

- current rosters
- projected minutes
- injuries and availability
- rest/travel context
- team pace and efficiency
- market odds and line movement

## Roadmap Lanes

| Sport | Model Default | Readiness |
|---|---|---|
| NFL | EPA/DVOA-style efficiency, QB availability, injuries, rest, weather, key numbers, market regression | Roadmap |
| NHL | Goalie confirmation, xG, GSAx, special teams, rest, line movement | Roadmap |
| Soccer | xG-first pricing with provider metadata; Poisson/Dixon-Coles style score distributions | Roadmap |

## Excluded or Deferred

| Item | Status | Reason |
|---|---|---|
| Auto-placement | Deferred | Phase 3 gate not met |
| Direct NBA picks | Deferred | Missing rosters, minutes, injuries, odds, market movement |
| Parlays/lottos | Excluded from system lane | Not part of disciplined model validation |
| Unvalidated model ideas | Experimental only | Must enter the ledger before becoming active |
| Duplicate best-bet cards by book | Excluded | Collapse same bet identity; show books as execution context |

## Shared Signal Standard

Any future model signal should be able to populate the runtime `Pick` concept without changing its meaning:

- sport
- event id/date
- teams or player
- market
- selection
- line
- signal source
- signal probability
- source odds/book/timestamp when available
- rank/confidence when available

Notes-side feature layers do not need to emit `Pick` objects until they are ready for app runtime integration.

## Validation Standard

Every model lane must answer:

1. What source rows produced this signal?
2. What feature set/version was used?
3. What market price was compared?
4. What was the closing line?
5. Did the signal beat the close?
6. What was ROI after settlement?
7. How large is the sample?

No lane is production-ready unless it can answer those questions from files or database rows.

