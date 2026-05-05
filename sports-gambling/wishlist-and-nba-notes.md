# Wishlist + NBA Betting Project Notes

Date: 2026-05-04

## Recommended Actions

1. DeepSeek V4 Pro: test as a low-cost coding/research model, not as a trusted replacement for client work.
   - Bookmark signal: Michael Guo reported 31M coding tokens for $0.55, estimating 19x to 32x lower cost than Claude models for the same workload.
   - Official DeepSeek docs list `deepseek-v4-pro` with 1M context, 384K max output, JSON output, tool calls, and OpenAI/Anthropic-compatible endpoints.
   - Current official pricing: $0.145/M cache-hit input, $1.74/M cache-miss input, $3.48/M output.
   - Use case: bulk exploration, draft code scaffolds, cheap long-context reads, non-client experiments.
   - Do not use for Workiva/client data or canonical decisions without verification.

2. Hermes Agent: watch and sandbox, do not adopt into the main workflow yet.
   - Bookmark signal: Hermes Kanban adds named agent profiles, shared SQLite task board, handoffs, retries, comments, crash recovery, and human supervision dashboard.
   - Official NousResearch repo describes Hermes as a self-improving agent with memory, skills, messaging gateways, scheduled automations, subagents, and multi-provider model access.
   - Use case: local scratch pilot for personal/research workflows.
   - Risk: overlaps heavily with existing Codex/Claude/Git-backed memory workflow; adoption would create another memory and automation surface.

3. NBA data: start this one now.
   - Downloaded source workbook: `nba-data/jeremias-nba-metric.xlsx`
   - Source article: Jeremias Engelmann, "How to build an NBA box-score metric", 2026-05-04.
   - Best immediate project fit: build a player-strength feature table first, then connect it to game/team/betting lines later.

## NBA Workbook Shape

The downloaded workbook has one sheet with 1,478 player rows and 52 columns.

Key columns:
- Identity: `name`
- Scoring/shooting: `FG2_miss`, `FG3_miss`, `FG2_make_ua`, `FG3_make_ua`, `FG2_make_a`, `FG3_make_a`, `FT_miss`, `FT_make`, `pts`
- Turnovers/steals: `live_to_bad_pass`, `live_to_lost_ball`, `dead_to`, `steal_bad_pass`, `steal_lost_ball`
- Fouls/blocks/rebounds: `shooting_foul`, `fouled_3`, `goaltend`, `blocked`, `blocks_to_def`, `blocks_to_off`, `oreb`, several defensive rebound columns
- Tracking/defense: `DEFLECTIONS`, `CHARGES_DRAWN`, defended shot make/miss buckets
- Availability/scale: `possessions`, `gp`, `starts`, `mp_approx`, `seasons`
- Targets: `off_RAPM`, `def_RAPM`, `off_RAPM_SE`, `def_RAPM_SE`

Top rows by the workbook order appear to be high-impact players:
- Stephen Curry: `off_RAPM` 8.260, `def_RAPM` 0.021
- Nikola Jokic: `off_RAPM` 7.940, `def_RAPM` 2.334
- Kawhi Leonard: `off_RAPM` 6.536, `def_RAPM` 2.124
- Damian Lillard: `off_RAPM` 6.340, `def_RAPM` -0.584
- James Harden: `off_RAPM` 5.653, `def_RAPM` -1.046

## Betting Project Direction

Recommendation: do not start with "pick winners." Start with a reusable player impact layer.

First build:
- Calculate possession-normalized rates from the raw counts.
- Z-score player features.
- Create offensive and defensive player-strength scores using RAPM as the target.
- Add reliability weights from `off_RAPM_SE`, `def_RAPM_SE`, `possessions`, and `seasons`.
- Aggregate to team/game level after we bring in rosters, minutes projections, injuries, rest, and odds.

Why this order:
- The workbook is player-level decade data, not game-level betting data.
- It is ideal for priors: "how strong is this player when available?"
- Betting needs matchup/time-sensitive layers later: current season form, rotations, injuries, lines, market movement, schedule, and opponent context.

## Sources

- X bookmark: https://x.com/Michaelzsguo/status/2051063189693956134
- X bookmark: https://x.com/NeoAIForecast/status/2051088223645151557
- X bookmark: https://x.com/JerryEngelmann/status/2051327559867236764
- Article: https://roycewebb.com/p/how-to-build-an-nba-box-score-metric
- Spreadsheet: https://docs.google.com/spreadsheets/d/1HqMMxpZWx4KwYKWJzvrEvd7S2OW4iAJikEevnpZ_c-g/edit?usp=sharing
- Hermes Agent repo: https://github.com/NousResearch/hermes-agent
- DeepSeek pricing docs: https://api-docs.deepseek.com/quick_start/pricing
