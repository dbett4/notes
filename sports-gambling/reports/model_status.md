# d + bet Model Status

Generated: 2026-05-04

## Conclusion

MLB MySPariEdge remains the only active alerting lane. NBA is integrated as an experimental player-prior feature layer, not a pick engine. Phase 3 automation remains closed until there are 200+ settled bets with positive average CLV.

## Governance

| Control | Status |
| --- | --- |
| `PROJECT_INDEX.md` | present |
| `MODEL_LEDGER.md` | present |
| `data/catalog/sources.csv` | 14 registered sources |
| Phase | Phase 2 alert-only |
| Phase 3 gate | 200+ settled bets with positive average CLV |
| Primary validation metric | CLV |

## Source Registry Coverage

| Sport | Registered Sources |
| --- | --- |
| All | 4 |
| MLB | 4 |
| NBA | 3 |
| NFL | 1 |
| NHL | 1 |
| Soccer | 1 |

## Active MLB Lane

| Item | Value |
| --- | --- |
| Processed signal rows | 3,386 |
| Signal file | `data/processed/myspariedge_mlb_signals_2026-05-03.csv` |
| Current status | Active alerting; not auto-placement |
| Filter policy | RL Meta: probability >= 60%, rank <= 7 |

### MLB Signal Types

| Signal Type | Rows |
| --- | --- |
| projection | 1,770 |
| odds_board_best_offer | 496 |
| best_bet | 224 |
| history | 223 |
| positive_ev | 200 |
| dfs_optimizer | 200 |
| saved_bet | 163 |
| sharp_money | 103 |
| top_strikeout_play | 4 |
| top_game_play | 3 |

## Experimental NBA Lane

| Item | Value |
| --- | --- |
| Feature rows | 1,477 |
| Feature file | `data/processed/nba/player_impact_features.csv` |
| Model status | experimental_player_prior_not_pick |
| Runtime signal status | Does not emit `Pick` objects |

### Top NBA Player Priors by Total RAPM

| Player | Off RAPM | Def RAPM | Total RAPM | Reliability |
| --- | --- | --- | --- | --- |
| Nikola Jokić | 7.94 | 2.334 | 10.274 | 0.561167 |
| Kawhi Leonard | 6.536 | 2.124 | 8.66 | 0.581564 |
| Giannis Antetokounmpo | 4.369 | 3.992 | 8.361 | 0.591366 |
| Stephen Curry | 8.26 | 0.021 | 8.281 | 0.558503 |
| Joel Embiid | 3.294 | 4.239 | 7.533 | 0.562588 |
| LeBron James | 5.15 | 1.439 | 6.589 | 0.60698 |
| Chet Holmgren | 2.625 | 3.836 | 6.461 | 0.468933 |
| Steven Adams | 4.29 | 2.072 | 6.362 | 0.563539 |

## Next Validation Work

- Normalize MLB signals into the shared signal schema once the current source files are stable.
- Join signals to settled wagers and closing-line snapshots before any Phase 3 automation discussion.
- Keep NBA at player-prior status until rotations, minutes, injuries, rest, odds, and market movement exist.
