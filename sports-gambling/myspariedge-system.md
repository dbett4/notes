# MySPariEdge System Reference

**As of:** 2026-05-01
**Owner/Creator:** DFSnDonuts (also runs the Discord server)
**Subscription:** $29.99/month (Essentials tier)

---

## Site Map

| URL | Purpose |
|-----|---------|
| `/projections/game` | **Today's picks** — Best Bets + Full Slate grid |
| `/projections/tracker` | **Quick Plays tracker** — historical filter performance |
| `/projections/history` | Season-long model records by market/bet grade |
| `/projections/best-bets` | Player prop patterns with ≥70% historical win rate |
| `/odds/positive-ev` | Positive EV finder (27 sportsbooks) |
| `/sharp-money-radar` | Sharp money movement |
| `/dfs-optimizer` | DFS lineup optimizer |

---

## The RL Meta Filter (Donuts' Core System)

This is the "Quick Plays" preset Donuts uses for his daily MLB picks.

**Location:** `/projections/tracker` → Game Lines tab → **RL Meta** preset

**Filter settings:**
- Market: **Run Line**
- Min Probability: **60%+**
- Max Rank: **≤ 7** (top half of a 15-game slate)
- Direction: Any

**Historical performance (last 10 days, as of 5/1/26):** 43-20 (68%)
**Season sample (per Discord post):** 58-33, 63.7%, 91 picks, +11.3 vs 52.4% baseline

### Other Quick Plays presets
| Preset | Market | Min Prob | Max Rank |
|--------|--------|----------|----------|
| ML Meta | Moneyline | 60% | ≤7 |
| RL Meta | Run Line | 60% | ≤7 |
| ML Elite | Moneyline | higher | tighter |
| RL Elite | Run Line | higher | tighter |

---

## Game Projections Page (`/projections/game`)

**Structure (MLB tab):**
1. **Best Bets** — top 3 ranked picks today (ML/RL/Total) with confidence %
2. **Top Strikeout Plays** — player props
3. **Elite Summary** — extended list, all tagged "Elite" with 59–75% confidence
4. **Full Slate** — complete grid: all games × ML/Spread/Total, each showing `%` confidence and `#` rank
   - Green text = 60%+ confidence
   - Green cell highlight = top pick for that market

**Reading the Full Slate:**
The automation source. Filter green cells with rank ≤7 in the Run Line column = today's RL Meta picks.

---

## Donuts' Betting Strategy (from `#donuts-strategy`)

> "If you're losing: Do less. Too many parlays, too many random plays you make, too many things you're doing on your own."

**Unit sizing:**
- **1 unit** — straight picks (model officials / donuts picks)
- **0.25 unit** — small parlays (sporadic; monitor impact on straight-pick profit)
- **0.1 unit** — lottos (+700, +1500, +2500)

**For automation: straight picks only at 1 unit. No parlays, no lottos.**

---

## Discord Channels

**Server:** DFSnDonuts (server ID: 880636071791181895)

| Channel | Purpose |
|---------|---------|
| `#donuts-strategy` | Pinned strategy post — START HERE |
| `#donuts-picks` | Daily picks via QuickPickBot/Pikkit deeplinks; includes MySPariEdge screenshot |
| `#myspariedge-picks` ⭐ | **NEW** — tracker-based tier picks (not yet on default channel list; add it) |
| `#myspariedge-alerts` | Tool updates, filter changes, win screenshots |
| `#myspariedge-chat` | General discussion |
| `#donuts-models` | Model data |
| `#donuts-sheets` | Spreadsheets |

**`#myspariedge-picks` is the most actionable channel** — Donuts posts specific tier plays with lineup lock timing guidance ("wait until lineup confirmed locked YES").

---

## Pick Format (from `#donuts-picks`)

Daily post structure:
```
MLB 70% Run Lines

[description of filter used and recent performance]

Team A +1.5
Team B +1.5
Team C +1.5
...

[QuickPickBot deeplink] https://quickpick.pikkit.com/betslip/...

@everyone @here @OddsShopper Donuts Picks
[screenshot of MySPariEdge tracker filter]
```

---

## Automation Notes

**Data source for today's picks:** `/projections/game` Full Slate grid
- Scrape Run Line column cells where confidence ≥ 60% AND rank ≤ 7

**Cross-reference:** `/projections/tracker?tab=games` with RL Meta preset to verify picks match

**Target books:** Hard Rock, BetMGM, ProphetX, Fanatics
**Banned books:** DraftKings (-6.2% ROI), FanDuel (-4.0% ROI)

**Timing:** Posts typically go up in the morning (8–9 AM ET). The site updates daily. Wait for lineup lock before placing — Donuts notes picks are "subject to change based on weather, vegas, lineups."
