# Auto-Bet System Spec

**As of:** 2026-05-01
**Status:** Planning

---

## What It Does

Scrapes MySPariEdge Game Projections daily, identifies qualifying Run Line picks, and auto-places them on target sportsbooks via browser automation.

---

## Signal Source

**URL:** `https://www.myspariedge.com/projections/game` (MLB tab, Full Slate section)

**Filter (RL Meta):**
- Market: Run Line
- Confidence: ≥ 60%
- Rank: ≤ 7 (out of 15 games)
- Both sides must have locked lineups before bet fires

---

## Target Books (profitable, auto-bet priority)

| Book | ROI | Notes |
|------|-----|-------|
| Hard Rock | +2.0% | Highest volume profitable book |
| BetMGM | +3.6% | Solid ROI |
| ProphetX | +3.6% | Good ROI, lower volume |
| Fanatics | +2.2% | Consistent |

**Banned:** DraftKings (-6.2%), FanDuel (-4.0%), Novig (-4.5% — investigate separately)

---

## Bet Sizing

**Pending from Dave:** unit size in dollars + total bankroll

Donuts' recommended sizing:
- Straight picks: 1 unit
- Parlays: 0.25 unit (NOT in automation — manual only)
- Lottos: 0.1 unit (NOT in automation)

---

## Architecture

```
[Scheduler: runs ~9 AM ET daily]
        ↓
[Scraper: myspariedge.com/projections/game]
        ↓
[Filter: RL, ≥60%, rank ≤7, lineup locked]
        ↓
[Dedup: skip already-placed bets]
        ↓
[Bet Placer: Playwright browser automation]
   ├── Hard Rock
   ├── BetMGM
   ├── ProphetX
   └── Fanatics
        ↓
[Logger: bet_id, book, team, odds, amount, timestamp → CSV/Pikkit]
```

---

## Mechanism: Browser Automation

US sportsbooks have no public API. Playwright (Python) drives the browser to:
1. Navigate to the sportsbook
2. Search for the game
3. Click the run line for the target team
4. Set bet amount
5. Confirm slip

**Key challenges:**
- Login session management (cookies/tokens)
- Bot detection (Cloudflare, Akamai) — may need stealth mode / headed browser
- Odds may have moved since model run — add max-odds-degradation guard
- Lineup lock check must happen before bet fires

---

## Tech Stack

- Python 3.x
- Playwright (browser automation)
- BeautifulSoup / requests or Playwright for scraping MySPariEdge
- SQLite for dedup + bet log
- APScheduler or cron for daily trigger
- Pikkit API (if available) or CSV export for P&L tracking

---

## Open Questions

- [ ] Unit size in $? Bankroll?
- [ ] Run NBA tab also, or MLB only to start?
- [ ] How to handle same-game picks on multiple books (full stake each, or split)?
- [ ] What to do if a book doesn't have the line? Skip or fall back to another?
- [ ] Lineup lock check — use MySPariEdge data or external source (RotoBaller, etc.)?
- [ ] Manual override / kill switch?

---

## Phase 1 (MVP)

Start with a **read-only monitor** before auto-placing:
1. Scrape picks daily and log them
2. Compare against what Donuts posts in `#donuts-picks`
3. Verify picks match for 1–2 weeks
4. Then enable auto-placement on one book first (Hard Rock)
