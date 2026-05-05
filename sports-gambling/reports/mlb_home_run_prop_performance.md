# MLB Home Run Prop Performance

Source: `transactions.csv` settled MLB straight home-run props.

Total HR bets: **484**
Total stake: **$5,410.27**
Total profit: **$801.87**
ROI: **14.8%**

## By Sportsbook

| Segment | Bets | Win % | Stake | Profit | ROI | Avg EV |
|---|---:|---:|---:|---:|---:|---:|
| Bet365 | 38 | 26.3% | $542 | $510 | 94.2% | 3.46% |
| Fanatics | 23 | 26.1% | $169 | $208 | 123.4% | 4.08% |
| theScore Bet | 13 | 30.8% | $190 | $208 | 109.2% | -0.70% |
| Novig | 56 | 57.1% | $1,041 | $180 | 17.2% | 8.28% |
| Hard Rock Sportsbook | 5 | 40.0% | $50 | $64 | 128.0% | 5.54% |
| BetMGM | 37 | 24.3% | $296 | $59 | 20.0% | 2.17% |
| Onyx | 8 | 12.5% | $78 | $-23 | -29.5% | -8.41% |
| ProphetX | 45 | 15.6% | $549 | $-118 | -21.6% | 11.72% |
| Fanduel Sportsbook | 131 | 19.8% | $1,226 | $-141 | -11.5% | 4.30% |
| Draftkings Sportsbook | 128 | 15.6% | $1,269 | $-145 | -11.4% | -0.51% |

## By Bet Format

| Segment | Bets | Win % | Stake | Profit | ROI | Avg EV |
|---|---:|---:|---:|---:|---:|---:|
| Other HR | 197 | 21.8% | $1,993 | $577 | 29.0% | 2.83% |
| Over 0.5 | 112 | 18.8% | $1,100 | $386 | 35.1% | 9.94% |
| Under 0.5 | 41 | 78.0% | $974 | $-48 | -4.9% | 2.99% |
| Alt Over | 134 | 15.7% | $1,344 | $-114 | -8.5% | -0.61% |

## By Odds Band

| Segment | Bets | Win % | Stake | Profit | ROI | Avg EV |
|---|---:|---:|---:|---:|---:|---:|
| +800 to +1199 | 58 | 19.0% | $468 | $643 | 137.6% | 13.29% |
| +300 to +499 | 178 | 22.5% | $1,937 | $230 | 11.9% | -0.48% |
| +100 to +199 | 2 | 50.0% | $25 | $33 | 133.2% | -1.17% |
| +500 to +799 | 164 | 14.6% | $1,638 | $-11 | -0.7% | 6.37% |
| +1200+ | 16 | 6.2% | $100 | $-20 | -19.6% | 16.19% |
| +200 to +299 | 25 | 32.0% | $269 | $-27 | -10.0% | -2.12% |
| < +100 | 41 | 78.0% | $974 | $-48 | -4.9% | 2.99% |

## Operating Read

- Focus on standard HR over / yes markets first.
- Treat alt-over ladders as manual-only; they are negative in this export.
- The best historical zone is `+800 to +1199`, but sample size is modest and should require MySPariEdge confirmation.
- Keep `+1200+` as lotto-only unless MySPariEdge and lineup/context both strongly agree.
- Book-level results are useful for tracking, but they should not restrict eligibility.
- Execute at whichever book offers the best playable HR price.
