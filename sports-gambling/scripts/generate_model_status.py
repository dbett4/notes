#!/usr/bin/env python3
"""Generate the daily d + bet model status report."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_rows(relative_path: str) -> list[dict[str, str]]:
    path = ROOT / relative_path
    if not path.exists():
        return []
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def exists_label(relative_path: str) -> str:
    return "present" if (ROOT / relative_path).exists() else "missing"


def top_nba_players(rows: list[dict[str, str]], limit: int = 8) -> list[dict[str, str]]:
    def total_rapm(row: dict[str, str]) -> float:
        try:
            return float(row.get("total_RAPM") or 0)
        except ValueError:
            return 0.0

    return sorted(rows, key=total_rapm, reverse=True)[:limit]


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines)


def generate() -> str:
    sources = read_rows("data/catalog/sources.csv")
    nba = read_rows("data/processed/nba/player_impact_features.csv")
    mlb = read_rows("data/processed/myspariedge_mlb_signals_2026-05-03.csv")

    source_sports = Counter(row.get("sport") or "Unknown" for row in sources)
    mlb_signal_types = Counter(row.get("signal_type") or "Unknown" for row in mlb)

    lines: list[str] = [
        "# d + bet Model Status",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Conclusion",
        "",
        "MLB MySPariEdge remains the only active alerting lane. NBA is integrated as an experimental player-prior feature layer, not a pick engine. Phase 3 automation remains closed until there are 200+ settled bets with positive average CLV.",
        "",
        "## Governance",
        "",
        markdown_table(
            ["Control", "Status"],
            [
                ["`PROJECT_INDEX.md`", exists_label("PROJECT_INDEX.md")],
                ["`MODEL_LEDGER.md`", exists_label("MODEL_LEDGER.md")],
                ["`data/catalog/sources.csv`", f"{len(sources)} registered sources"],
                ["Phase", "Phase 2 alert-only"],
                ["Phase 3 gate", "200+ settled bets with positive average CLV"],
                ["Primary validation metric", "CLV"],
            ],
        ),
        "",
        "## Source Registry Coverage",
        "",
        markdown_table(
            ["Sport", "Registered Sources"],
            [[sport, str(count)] for sport, count in sorted(source_sports.items())],
        ),
        "",
        "## Active MLB Lane",
        "",
        markdown_table(
            ["Item", "Value"],
            [
                ["Processed signal rows", f"{len(mlb):,}"],
                ["Signal file", "`data/processed/myspariedge_mlb_signals_2026-05-03.csv`"],
                ["Current status", "Active alerting; not auto-placement"],
                ["Filter policy", "RL Meta: probability >= 60%, rank <= 7"],
            ],
        ),
        "",
        "### MLB Signal Types",
        "",
        markdown_table(
            ["Signal Type", "Rows"],
            [[signal_type, f"{count:,}"] for signal_type, count in mlb_signal_types.most_common()],
        ) if mlb_signal_types else "No MLB signals found.",
        "",
        "## Experimental NBA Lane",
        "",
        markdown_table(
            ["Item", "Value"],
            [
                ["Feature rows", f"{len(nba):,}"],
                ["Feature file", "`data/processed/nba/player_impact_features.csv`"],
                ["Model status", "experimental_player_prior_not_pick"],
                ["Runtime signal status", "Does not emit `Pick` objects"],
            ],
        ),
        "",
        "### Top NBA Player Priors by Total RAPM",
        "",
    ]

    if nba:
        lines.append(
            markdown_table(
                ["Player", "Off RAPM", "Def RAPM", "Total RAPM", "Reliability"],
                [
                    [
                        row.get("name", ""),
                        row.get("off_RAPM", ""),
                        row.get("def_RAPM", ""),
                        row.get("total_RAPM", ""),
                        row.get("rapm_reliability", ""),
                    ]
                    for row in top_nba_players(nba)
                ],
            )
        )
    else:
        lines.append("No NBA features found.")

    lines.extend(
        [
            "",
            "## Next Validation Work",
            "",
            "- Normalize MLB signals into the shared signal schema once the current source files are stable.",
            "- Join signals to settled wagers and closing-line snapshots before any Phase 3 automation discussion.",
            "- Keep NBA at player-prior status until rotations, minutes, injuries, rest, odds, and market movement exist.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="reports/model_status.md")
    args = parser.parse_args()

    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(generate())
    print(f"Wrote {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

