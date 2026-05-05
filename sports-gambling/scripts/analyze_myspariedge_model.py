#!/usr/bin/env python3
"""Summarize MySPariEdge MLB history, best bets, and projections."""

from __future__ import annotations

import csv
import glob
from collections import Counter
from pathlib import Path


GRADE_RANK = {"A+": 13, "A": 12, "A-": 11, "B+": 10, "B": 9, "B-": 8, "C+": 7, "C": 6, "C-": 5, "D+": 4, "D": 3, "D-": 2, "F": 1}
TARGET_GRADES = {"A+", "A", "A-", "B+"}


def latest_signals_path() -> Path:
    paths = sorted(glob.glob("data/processed/myspariedge_mlb_signals_*.csv"))
    if not paths:
        raise SystemExit("No MySPariEdge signal CSV found. Run scripts/pull_myspariedge_mlb.py first.")
    return Path(paths[-1])


def read_rows(path: Path) -> list[dict[str, str]]:
    return list(csv.DictReader(path.open()))


def is_target(row: dict[str, str]) -> bool:
    return row.get("grade") in TARGET_GRADES or row.get("is_target_grade") == "True"


def history_score(row: dict[str, str]) -> tuple[float, int]:
    wins = int(float(row.get("wins") or 0))
    losses = int(float(row.get("losses") or 0))
    win_pct = float(row.get("win_pct") or 0)
    return win_pct, wins + losses


def markdown_history(rows: list[dict[str, str]], limit: int = 30) -> str:
    rows = sorted(rows, key=lambda row: (history_score(row)[0], history_score(row)[1]), reverse=True)
    lines = ["| Type | Market | Side | Grade | W-L | Win % | Season |", "|---|---|---|---|---:|---:|---|"]
    for row in rows[:limit]:
        wins = int(float(row.get("wins") or 0))
        losses = int(float(row.get("losses") or 0))
        lines.append(
            f"| {row.get('history_type') or ''} | {row.get('market') or ''} | {row.get('side') or ''} | "
            f"{row.get('grade') or ''} | {wins}-{losses} | {float(row.get('win_pct') or 0):.1f}% | {row.get('season') or ''} |"
        )
    return "\n".join(lines)


def markdown_counts(title: str, counter: Counter[str]) -> str:
    lines = [f"## {title}", "", "| Segment | Count |", "|---|---:|"]
    for key, count in counter.most_common():
        lines.append(f"| {key or 'blank'} | {count} |")
    return "\n".join(lines)


def sport_is_mlb(row: dict[str, str]) -> bool:
    return row.get("sport") in {"MLB", "baseball_mlb", ""} or row.get("signal_type") in {"best_bet", "projection", "history", "top_strikeout_play", "top_game_play"}


def markdown_top_edges(title: str, rows: list[dict[str, str]], metric: str, limit: int = 20) -> str:
    def metric_value(row: dict[str, str]) -> float:
        try:
            return float(row.get(metric) or 0)
        except ValueError:
            return 0

    lines = [f"## {title}", "", "| Player | Market | Side | Line | Book | Price | Edge | Game |", "|---|---|---|---:|---|---:|---:|---|"]
    for row in sorted(rows, key=metric_value, reverse=True)[:limit]:
        edge = metric_value(row)
        price = row.get("price_american") or ""
        lines.append(
            f"| {row.get('player') or ''} | {row.get('market') or ''} | {row.get('side') or ''} | "
            f"{row.get('line') or ''} | {row.get('book') or ''} | {price} | {edge:.1%} | {row.get('game') or ''} |"
        )
    return "\n".join(lines)


def markdown_market_matrix(rows: list[dict[str, str]]) -> str:
    buckets: dict[str, Counter[str]] = {}
    for row in rows:
        market = row.get("market") or "blank"
        buckets.setdefault(market, Counter())[row.get("signal_type") or "unknown"] += 1

    signal_order = ["best_bet", "projection", "history", "positive_ev", "sharp_money", "dfs_optimizer", "odds_board_best_offer", "saved_bet"]
    lines = [
        "## Market Signal Matrix",
        "",
        "| Market | Best Bets | Target Proj | History | +EV | Sharp | DFS | Odds Offers | Saved Bets |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for market, counter in sorted(buckets.items(), key=lambda item: sum(item[1].values()), reverse=True):
        lines.append(
            f"| {market} | "
            f"{counter.get('best_bet', 0)} | {counter.get('projection', 0)} | {counter.get('history', 0)} | "
            f"{counter.get('positive_ev', 0)} | {counter.get('sharp_money', 0)} | {counter.get('dfs_optimizer', 0)} | "
            f"{counter.get('odds_board_best_offer', 0)} | {counter.get('saved_bet', 0)} |"
        )
    return "\n".join(lines)


def main() -> None:
    path = latest_signals_path()
    rows = read_rows(path)
    best_bets = [row for row in rows if row.get("signal_type") == "best_bet"]
    target_best_bets = [row for row in best_bets if is_target(row)]
    projections = [row for row in rows if row.get("signal_type") == "projection"]
    target_projections = [row for row in projections if is_target(row)]
    history = [row for row in rows if row.get("signal_type") == "history"]
    positive_ev = [row for row in rows if row.get("signal_type") == "positive_ev" and row.get("sport") == "MLB"]
    sharp_money = [row for row in rows if row.get("signal_type") == "sharp_money" and row.get("sport") == "MLB"]
    dfs_optimizer = [row for row in rows if row.get("signal_type") == "dfs_optimizer" and row.get("sport") == "MLB"]
    saved_bets = [row for row in rows if row.get("signal_type") == "saved_bet" and row.get("sport") == "MLB"]
    odds_board = [row for row in rows if row.get("signal_type") == "odds_board_best_offer"]

    player_history = [row for row in history if row.get("history_type") == "PLAYER"]
    target_history = [row for row in player_history if row.get("grade") in TARGET_GRADES]
    matrix_rows = target_best_bets + target_projections + target_history + positive_ev + sharp_money + dfs_optimizer + saved_bets + odds_board

    content = "\n".join(
        [
            "# MySPariEdge MLB Model Read",
            "",
            f"Source: `{path}`",
            "",
            f"Best Bets rows: **{len(best_bets):,}**",
            f"Best Bets `A+` through `B+`: **{len(target_best_bets):,}**",
            f"Projection rows: **{len(projections):,}**",
            f"Projection rows `A+` through `B+`: **{len(target_projections):,}**",
            f"MLB history records: **{len(history):,}**",
            f"MLB +EV rows: **{len(positive_ev):,}**",
            f"MLB sharp-money rows: **{len(sharp_money):,}**",
            f"MLB odds-board best offers: **{len(odds_board):,}**",
            "",
            "## Best Historical Player Markets",
            "",
            markdown_history(target_history),
            "",
            markdown_counts("Target Best Bets By Market", Counter(row.get("market") for row in target_best_bets)),
            "",
            markdown_counts("Target Projections By Market", Counter(row.get("market") for row in target_projections)),
            "",
            markdown_counts("Target Projections By Grade", Counter(row.get("grade") for row in target_projections)),
            "",
            markdown_counts("MLB +EV By Market", Counter(row.get("market") for row in positive_ev)),
            "",
            markdown_counts("MLB Sharp Money By Market", Counter(row.get("market") for row in sharp_money)),
            "",
            markdown_counts("Odds Board Best Offers By Market", Counter(row.get("market") for row in odds_board)),
            "",
            markdown_top_edges("Top MLB +EV Plays", positive_ev, "ev_pct"),
            "",
            markdown_market_matrix(matrix_rows),
            "",
            "## Operating Read",
            "",
            "- Do not filter to HRs by default. Use model history and target grades to identify the strongest markets.",
            "- Best Bets graded `A+` through `B+` are the primary target tier.",
            "- Projection grades `A+` through `B+` are the secondary discovery layer, especially when Best Bets has no HRs.",
            "- Positive EV, sharp-money, and odds-board best offers are now captured for price and confluence checks.",
            "- Book choice remains price-driven only; no book restrictions.",
            "",
        ]
    )
    out = Path("reports/myspariedge_mlb_model_read.md")
    out.write_text(content)
    print(out)


if __name__ == "__main__":
    main()
