# MySPariEdge Projection Clone Plan

**Conclusion:** MySPariEdge projections are cloneable in structure, but the hard part is recreating the adjusted rates behind each stat. `AB` and `IP` are only the volume scalers.

## Visible Formula

For hitters:

```text
projected stat = projected AB × adjusted per-AB rate
```

For pitchers:

```text
projected stat = projected IP × adjusted per-IP rate
outs = projected IP × 3
```

Composite markets:

```text
H+R+RBI = hits + runs + rbi
```

## Hidden Work

The adjusted rates likely blend:

| Component | Why It Matters |
|---|---|
| Player baseline | Season and rolling skill level |
| Handedness split | Batter vs pitcher handedness |
| Opposing starter | Matchup quality, pitch mix, K/BB/HR profile |
| Opposing bullpen | Later plate appearances and run/RBI context |
| Batting order | AB expectation, run/RBI opportunity |
| Team implied total | Run environment |
| Park factor | Hits, HR, total bases, runs |
| Weather | HR, total bases, run environment |
| Recent form | Likely small-weight adjustment |
| Lineup lock | Confirmed opportunity and role |

## Public Data Sources

| Need | Source |
|---|---|
| Schedule, probable pitchers, game ids | MLB Stats API schedule endpoint |
| Confirmed lineups / batting order | MLB Stats API when lineups post; fallback paid/free lineup source if needed |
| Statcast batted-ball data | Baseball Savant / pybaseball |
| Expected stats | Baseball Savant xBA, xSLG, xwOBA, barrel rate, hard-hit rate |
| Player season and rolling stats | pybaseball / FanGraphs / MLB Stats API |
| Park factors | FanGraphs or Statcast park factors |
| Weather | Open-Meteo / NOAA / stadium coordinates |
| Odds / implied team totals | MySPariEdge odds board, The Odds API, or sportsbook scrape |

## Local Model Shape

### 1. Volume Model

Hitters:

```text
AB projection = lineup-slot AB baseline
              × team game total adjustment
              × home/away adjustment
              × player role adjustment
```

Pitchers:

```text
IP projection = starter baseline IP
              × pitch-count / recent workload adjustment
              × opponent strength adjustment
              × team/bullpen context adjustment
```

### 2. Hitter Rate Model

Per-AB rates:

```text
hits_rate
total_bases_rate
rbi_rate
runs_rate
hr_probability_per_ab
```

Inputs:

- Batter season rate
- Batter last 14/30 day rate
- Batter handedness split
- Opposing pitcher allowed rate by handedness
- Park/weather adjustment
- Team implied total
- Batting order opportunity

### 3. Pitcher Rate Model

Per-IP rates:

```text
k_per_ip
hits_allowed_per_ip
walks_per_ip
earned_runs_per_ip
```

Inputs:

- Pitcher season rate
- Pitcher recent rate
- Opponent hitter aggregate rates
- Opponent K/BB profile by handedness
- Park/weather adjustment
- Umpire factor if available

## Calibration Target

Use MySPariEdge pulls as teacher labels:

1. Pull daily MySPariEdge projections.
2. Build public-data features for the same players.
3. Train/calibrate local predictions to match:
   - `AB`
   - `IP`
   - per-stat adjusted rates
   - final projection
   - grade threshold
4. Track prediction error by market.

## First Clone Milestone

Recreate the visible outputs for one slate:

| Output | Target |
|---|---|
| Hitter AB | within `±0.2` AB |
| Pitcher IP | within `±0.2` IP |
| Hits / Runs / RBIs | within `±0.05` |
| Total Bases / H+R+RBI | within `±0.15` |
| Pitcher K / Hits Allowed | within `±0.3` |
| Grade bucket | match or within one grade |

## Build Order

1. Local data warehouse for schedules, players, lineups, probable pitchers, Statcast, weather, and odds.
2. Recreate volume models for `AB` and `IP`.
3. Recreate simple blended rates from season + rolling + handedness splits.
4. Add matchup, park, weather, and implied-total adjustments.
5. Fit against MySPariEdge historical pulls.
6. Use grade surrogate to generate local candidates without waiting on site pulls.
