# d + bet ID Mapping Policy

## Conclusion

Use stable canonical IDs before joining model features, odds, and results. If a source lacks stable IDs, preserve its raw source key and create a mapping row before using it in a signal.

## Core Rules

- Keep raw provider IDs unchanged in raw files.
- Create canonical IDs only in normalized or processed layers.
- Never join on display names alone when a stable source ID exists.
- If display-name matching is unavoidable, record the source, match rule, and review status.
- Store provider/source metadata for any derived metric where definitions vary.

## ID Families

| Entity | Canonical Pattern | Notes |
|---|---|---|
| Sport | lowercase code | `mlb`, `nba`, `nfl`, `nhl`, `soccer` |
| League | lowercase source/league code | `mlb`, `nba`, `nfl`, `nhl`, `epl`, `ucl` |
| Event | provider event ID where available | Prefix if provider-specific: `myspariedge:123`, `oddsapi:abc` |
| Team | league team abbreviation + season if needed | Preserve source abbreviation in raw layer |
| Player | provider player ID where available | Name-only rows need mapping before runtime use |
| Sportsbook | normalized lowercase slug | `draftkings`, `fanduel`, `novig`, `prophetx`, `kalshi` |
| Market | runtime-compatible snake case | Match `betting-bot/signals/base.py` where possible |

## Sportsbook Display Policy

When the same underlying bet appears at multiple books, collapse it to one recommendation and show available books as execution options.

Preferred display order:

1. DraftKings
2. FanDuel
3. Novig
4. ProphetX
5. Kalshi
6. Other manual books

Auto-placement remains deferred. Manual books must stay alert-only.

## Market Naming

Use runtime-compatible market names where possible:

- `moneyline`
- `run_line`
- `spread`
- `total`
- `player_points`
- `player_rebounds`
- `player_assists`
- `player_threes`
- `player_hits`
- `player_total_bases`
- `pitcher_strikeouts`

If a new market is needed, add it first to this policy and only later to the runtime app contract.

