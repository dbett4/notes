#!/usr/bin/env python3
"""Infer a surrogate MySPariEdge grading model from pulled projection data."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path


GRADE_ORDER = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
TARGET_GRADES = {"A+", "A", "A-", "B+"}
MARKET_LABELS = {
    "hits": "Hits",
    "tb": "Total Bases",
    "rbi": "RBIs",
    "runs": "Runs",
    "hrr": "Hits + Runs + RBIs",
    "k": "Strikeouts",
    "outs": "Pitcher Outs",
    "walks": "Walks Allowed",
    "earned_runs": "Earned Runs",
    "hits_allowed": "Hits Allowed",
}


def load_projection_grade_rows() -> list[dict[str, object]]:
    payload = json.loads(Path("data/raw/myspariedge/2026-05-03/player_projections.json").read_text())
    rows = []
    for player in payload.get("players") or []:
        projections = player.get("projections") or {}
        stats = projections.get("stats") or {}
        lines = projections.get("lines") or {}
        grades = projections.get("grades") or {}
        for market_key, line in lines.items():
            if market_key not in stats:
                continue
            grade = grades.get(market_key) or projections.get(f"{market_key}Grade")
            if not grade:
                continue
            projection = float(stats[market_key])
            line = float(line)
            edge = projection - line
            rows.append(
                {
                    "player": player.get("player_name"),
                    "team": player.get("team"),
                    "market_key": market_key,
                    "market": MARKET_LABELS.get(market_key, market_key),
                    "line": line,
                    "projection": projection,
                    "edge": edge,
                    "abs_edge": abs(edge),
                    "inferred_side": "Over" if edge > 0 else "Under" if edge < 0 else "Push",
                    "grade": grade,
                }
            )
    return rows


def load_best_bet_rows() -> list[dict[str, object]]:
    payload = json.loads(Path("data/raw/myspariedge/2026-05-03/best_bets.json").read_text())
    rows = []
    for item in payload.get("best_bets") or []:
        projection = float(item.get("projection") or 0)
        line = float(item.get("line") or 0)
        edge = projection - line
        rows.append(
            {
                "player": item.get("player_name"),
                "market": item.get("market"),
                "side": item.get("side"),
                "line": line,
                "projection": projection,
                "edge": edge,
                "abs_edge": abs(edge),
                "grade": item.get("bet_grade"),
                "win_pct": item.get("win_pct"),
                "wins": item.get("wins"),
                "losses": item.get("losses"),
            }
        )
    return rows


def summarize_thresholds(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_market_grade: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_market_grade[(str(row["market"]), str(row["grade"]))].append(row)

    summary = []
    for (market, grade), items in sorted(by_market_grade.items()):
        abs_edges = sorted(float(item["abs_edge"]) for item in items)
        edges = sorted(float(item["edge"]) for item in items)
        sides = defaultdict(int)
        for item in items:
            sides[str(item.get("inferred_side") or item.get("side"))] += 1
        summary.append(
            {
                "market": market,
                "grade": grade,
                "count": len(items),
                "min_abs_edge": min(abs_edges),
                "avg_abs_edge": sum(abs_edges) / len(abs_edges),
                "max_abs_edge": max(abs_edges),
                "min_edge": min(edges),
                "max_edge": max(edges),
                "sides": ", ".join(f"{side}:{count}" for side, count in sorted(sides.items())),
            }
        )
    return sorted(summary, key=lambda row: (row["market"], GRADE_ORDER.index(row["grade"]) if row["grade"] in GRADE_ORDER else 999))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)


def markdown_threshold_table(rows: list[dict[str, object]], markets: list[str]) -> str:
    lines = ["| Market | Grade | Count | Abs Edge Range | Avg Abs Edge | Side Mix |", "|---|---|---:|---:|---:|---|"]
    for row in rows:
        if row["market"] not in markets:
            continue
        lines.append(
            f"| {row['market']} | {row['grade']} | {row['count']} | "
            f"{row['min_abs_edge']:.2f}-{row['max_abs_edge']:.2f} | {row['avg_abs_edge']:.2f} | {row['sides']} |"
        )
    return "\n".join(lines)


def write_report(projection_summary: list[dict[str, object]], best_bet_summary: list[dict[str, object]]) -> None:
    markets = ["RBIs", "Runs", "Hits", "Total Bases", "Hits + Runs + RBIs", "Earned Runs", "Hits Allowed", "Strikeouts", "Walks Allowed"]
    content = "\n".join(
        [
            "# MySPariEdge Grade Reverse Engineering",
            "",
            "This is a surrogate model inferred from pulled MySPariEdge data, not the internal formula.",
            "",
            "## Working Theory",
            "",
            "Projection grades are mostly market-specific thresholds on `abs(projection - line)`.",
            "",
            "- Side is inferred from projection edge: projection above line = Over, below line = Under.",
            "- The same absolute edge has different meaning by market. A `0.25` RBI edge can grade high; a `0.25` H+R+RBI edge is closer to middle tier.",
            "- Best Bets appear to use the same grade field plus historical pattern records. The displayed win percentage is not the grade by itself.",
            "",
            "## Projection Grade Thresholds",
            "",
            markdown_threshold_table(projection_summary, markets),
            "",
            "## Best Bets Grade Evidence",
            "",
            markdown_threshold_table(best_bet_summary, markets),
            "",
            "## Practical Clone",
            "",
            "For a local first pass, use market-specific absolute-edge cutoffs learned from this table:",
            "",
            "1. Compute `edge = projection - line`.",
            "2. Side is `Over` if edge is positive and `Under` if edge is negative.",
            "3. Within each market, assign the highest grade whose observed absolute-edge range contains the edge.",
            "4. Promote candidates only when the inferred grade is `A+`, `A`, `A-`, or `B+` and model history for that market/side/grade is strong.",
            "",
            "This gets us an inspectable approximation. To make it durable, keep daily snapshots and refit thresholds over multiple slates.",
            "",
        ]
    )
    Path("reports/myspariedge_grade_reverse_engineering.md").write_text(content)


def main() -> None:
    projection_rows = load_projection_grade_rows()
    best_bet_rows = load_best_bet_rows()
    projection_summary = summarize_thresholds(projection_rows)
    best_bet_summary = summarize_thresholds(best_bet_rows)
    write_csv(Path("reports/myspariedge_projection_grade_thresholds.csv"), projection_summary)
    write_csv(Path("reports/myspariedge_best_bet_grade_evidence.csv"), best_bet_summary)
    write_report(projection_summary, best_bet_summary)
    print("reports/myspariedge_grade_reverse_engineering.md")


if __name__ == "__main__":
    main()
