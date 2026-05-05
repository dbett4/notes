#!/usr/bin/env python3
"""Analyze MLB home-run prop performance."""

from __future__ import annotations

import csv
import re
import statistics
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


def money(value: str | None) -> float:
    return float(value or 0)


def american_odds(decimal_odds: float) -> float:
    if decimal_odds >= 2:
        return (decimal_odds - 1) * 100
    if decimal_odds > 1:
        return -100 / (decimal_odds - 1)
    return 0


def odds_band(decimal_odds: float) -> str:
    american = american_odds(decimal_odds)
    if american < 100:
        return "< +100"
    if american < 200:
        return "+100 to +199"
    if american < 300:
        return "+200 to +299"
    if american < 500:
        return "+300 to +499"
    if american < 800:
        return "+500 to +799"
    if american < 1200:
        return "+800 to +1199"
    return "+1200+"


def side(bet_info: str) -> str:
    if re.match(r"^(over|o)\b", bet_info, re.I):
        return "Over 0.5"
    if re.match(r"^\d+\+", bet_info):
        return "Alt Over"
    if re.match(r"^(under|u)\b", bet_info, re.I):
        return "Under 0.5"
    return "Other HR"


def is_home_run(row: dict[str, str]) -> bool:
    return (
        row.get("leagues") == "MLB"
        and row.get("type") == "straight"
        and row.get("status", "").startswith("SETTLED")
        and bool(re.search(r"\bhome runs?\b", row.get("bet_info", ""), re.I))
    )


@dataclass
class Bucket:
    bets: int = 0
    wins: int = 0
    stake: float = 0
    profit: float = 0
    evs: list[float] | None = None

    def add(self, row: dict[str, str]) -> None:
        if self.evs is None:
            self.evs = []
        profit = money(row.get("profit"))
        self.bets += 1
        self.wins += int(profit > 0)
        self.stake += money(row.get("amount"))
        self.profit += profit
        if row.get("ev") not in (None, ""):
            self.evs.append(money(row.get("ev")))

    @property
    def win_rate(self) -> float:
        return self.wins / self.bets if self.bets else 0

    @property
    def roi(self) -> float:
        return self.profit / self.stake if self.stake else 0

    @property
    def avg_ev(self) -> float | None:
        return statistics.mean(self.evs) if self.evs else None


def summarize(rows: list[dict[str, str]], key: str) -> list[tuple[str, Bucket]]:
    buckets: dict[str, Bucket] = defaultdict(Bucket)
    for row in rows:
        buckets[row[key]].add(row)
    return sorted(buckets.items(), key=lambda item: item[1].profit, reverse=True)


def table(groups: list[tuple[str, Bucket]]) -> str:
    lines = ["| Segment | Bets | Win % | Stake | Profit | ROI | Avg EV |", "|---|---:|---:|---:|---:|---:|---:|"]
    for name, bucket in groups:
        ev = "" if bucket.avg_ev is None else f"{bucket.avg_ev:.2%}"
        lines.append(
            f"| {name} | {bucket.bets} | {bucket.win_rate:.1%} | "
            f"${bucket.stake:,.0f} | ${bucket.profit:,.0f} | {bucket.roi:.1%} | {ev} |"
        )
    return "\n".join(lines)


def main() -> None:
    rows = []
    for row in csv.DictReader(open("transactions.csv")):
        if not is_home_run(row):
            continue
        row = dict(row)
        row["side_group"] = side(row.get("bet_info", ""))
        row["odds_band"] = odds_band(money(row.get("odds")))
        rows.append(row)

    total = Bucket()
    for row in rows:
        total.add(row)

    report = "\n".join(
        [
            "# MLB Home Run Prop Performance",
            "",
            "Source: `transactions.csv` settled MLB straight home-run props.",
            "",
            f"Total HR bets: **{total.bets:,}**",
            f"Total stake: **${total.stake:,.2f}**",
            f"Total profit: **${total.profit:,.2f}**",
            f"ROI: **{total.roi:.1%}**",
            "",
            "## By Sportsbook",
            "",
            table(summarize(rows, "sportsbook")),
            "",
            "## By Bet Format",
            "",
            table(summarize(rows, "side_group")),
            "",
            "## By Odds Band",
            "",
            table(summarize(rows, "odds_band")),
            "",
            "## Operating Read",
            "",
            "- Focus on standard HR over / yes markets first.",
            "- Treat alt-over ladders as manual-only; they are negative in this export.",
            "- The best historical zone is `+800 to +1199`, but sample size is modest and should require MySPariEdge confirmation.",
            "- Keep `+1200+` as lotto-only unless MySPariEdge and lineup/context both strongly agree.",
            "- Book-level results are useful for tracking, but they should not restrict eligibility.",
            "- Execute at whichever book offers the best playable HR price.",
            "",
        ]
    )

    out = Path("reports/mlb_home_run_prop_performance.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report)
    print(out)


if __name__ == "__main__":
    main()
