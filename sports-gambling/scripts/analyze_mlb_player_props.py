#!/usr/bin/env python3
"""Analyze settled MLB player-prop performance from a Pikkit-style export."""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


MARKET_PATTERNS = [
    ("Pitcher Strikeouts", re.compile(r"\b(strikeouts?|ks?)\b", re.I)),
    ("Pitcher Hits Allowed", re.compile(r"\bhits allowed\b", re.I)),
    ("Home Runs", re.compile(r"\bhome runs?\b", re.I)),
    ("Hits + Runs + RBIs", re.compile(r"\bhits \+ runs \+ rbis\b|\bhr?rbi\b", re.I)),
    ("Total Bases", re.compile(r"\btotal bases\b", re.I)),
    ("Hits", re.compile(r"\bhits?\b", re.I)),
    ("Runs", re.compile(r"\bruns?\b", re.I)),
    ("RBIs", re.compile(r"\brbis?\b", re.I)),
]


@dataclass
class Bucket:
    bets: int = 0
    wins: int = 0
    losses: int = 0
    stake: float = 0.0
    profit: float = 0.0
    ev_sum: float = 0.0
    ev_count: int = 0

    def add(self, row: dict[str, str]) -> None:
        profit = parse_float(row.get("profit"))
        stake = parse_float(row.get("amount"))
        ev = parse_float(row.get("ev"))
        self.bets += 1
        self.wins += int(profit > 0)
        self.losses += int(profit < 0)
        self.stake += stake
        self.profit += profit
        if ev is not None:
            self.ev_sum += ev
            self.ev_count += 1

    @property
    def win_rate(self) -> float:
        return self.wins / self.bets if self.bets else 0.0

    @property
    def roi(self) -> float:
        return self.profit / self.stake if self.stake else 0.0

    @property
    def avg_ev(self) -> float | None:
        return self.ev_sum / self.ev_count if self.ev_count else None


def parse_float(value: str | None) -> float:
    if value in (None, ""):
        return 0.0
    return float(value)


def classify_market(bet_info: str) -> str:
    for market, pattern in MARKET_PATTERNS:
        if pattern.search(bet_info):
            return market
    return "Other"


def normalize_side(bet_info: str) -> str:
    text = bet_info.strip()
    if re.match(r"^(over|o)\b", text, re.I):
        return "Over"
    if re.match(r"^(under|u)\b", text, re.I):
        return "Under"
    if re.match(r"^\d+\+", text):
        return "Alt Over"
    return "Other"


def settled_mlb_props(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    settled = []
    for row in rows:
        if row.get("leagues") != "MLB":
            continue
        if row.get("type") != "straight":
            continue
        if not row.get("status", "").startswith("SETTLED"):
            continue
        row = dict(row)
        row["market"] = classify_market(row.get("bet_info", ""))
        row["side"] = normalize_side(row.get("bet_info", ""))
        settled.append(row)
    return settled


def summarize(rows: list[dict[str, str]], key: str) -> list[tuple[str, Bucket]]:
    buckets: dict[str, Bucket] = defaultdict(Bucket)
    for row in rows:
        buckets[row.get(key) or "Unknown"].add(row)
    return sorted(buckets.items(), key=lambda item: item[1].profit, reverse=True)


def write_summary(path: Path, title: str, groups: list[tuple[str, Bucket]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title, "bets", "wins", "losses", "win_rate", "stake", "profit", "roi", "avg_ev"])
        for name, bucket in groups:
            writer.writerow(
                [
                    name,
                    bucket.bets,
                    bucket.wins,
                    bucket.losses,
                    f"{bucket.win_rate:.4f}",
                    f"{bucket.stake:.2f}",
                    f"{bucket.profit:.2f}",
                    f"{bucket.roi:.4f}",
                    "" if bucket.avg_ev is None else f"{bucket.avg_ev:.4f}",
                ]
            )


def markdown_table(groups: list[tuple[str, Bucket]], limit: int = 12) -> str:
    lines = ["| Segment | Bets | Win % | Stake | Profit | ROI | Avg EV |", "|---|---:|---:|---:|---:|---:|---:|"]
    for name, bucket in groups[:limit]:
        avg_ev = "" if bucket.avg_ev is None else f"{bucket.avg_ev:.2%}"
        lines.append(
            f"| {name} | {bucket.bets} | {bucket.win_rate:.1%} | "
            f"${bucket.stake:,.0f} | ${bucket.profit:,.0f} | {bucket.roi:.1%} | {avg_ev} |"
        )
    return "\n".join(lines)


def write_report(path: Path, rows: list[dict[str, str]]) -> None:
    total = Bucket()
    for row in rows:
        total.add(row)

    by_book = summarize(rows, "sportsbook")
    by_market = summarize(rows, "market")
    by_side = summarize(rows, "side")

    path.write_text(
        "\n".join(
            [
                "# MLB Player Prop Performance",
                "",
                "Source: `transactions.csv` settled MLB straight bets.",
                "",
                f"Total settled MLB straight bets: **{total.bets:,}**",
                f"Total stake: **${total.stake:,.2f}**",
                f"Total profit: **${total.profit:,.2f}**",
                f"Overall ROI: **{total.roi:.1%}**",
                "",
                "## By Sportsbook",
                "",
                markdown_table(by_book),
                "",
                "## By Market",
                "",
                markdown_table(by_market),
                "",
                "## By Side",
                "",
                markdown_table(by_side),
                "",
                "## Read",
                "",
                "- Book-level results are useful for tracking, but they should not restrict eligibility.",
                "- Execute at whichever book offers the best playable price.",
                "- Home runs and runs are the clearest positive markets in this export; strikeouts and broad uncategorized props need MySPariEdge confirmation before firing.",
                "- Use this as a filter layer, not proof of future edge. The next step is joining daily MySPariEdge signals to placed bets and closing-line movement.",
                "",
            ]
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="transactions.csv")
    parser.add_argument("--outdir", default="reports")
    args = parser.parse_args()

    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(input_path.open()))
    props = settled_mlb_props(rows)

    write_summary(outdir / "mlb_player_props_by_book.csv", "sportsbook", summarize(props, "sportsbook"))
    write_summary(outdir / "mlb_player_props_by_market.csv", "market", summarize(props, "market"))
    write_summary(outdir / "mlb_player_props_by_side.csv", "side", summarize(props, "side"))
    write_report(outdir / "mlb_player_prop_performance.md", props)


if __name__ == "__main__":
    main()
