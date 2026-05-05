#!/usr/bin/env python3
"""Validate d + bet model source-of-truth files.

This is a drift check, not a betting model. It fails loudly when canonical
docs, catalog entries, or processed feature outputs stop matching the ledger.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "PROJECT_INDEX.md",
    "MODEL_LEDGER.md",
    "data/catalog/sources.csv",
    "data/catalog/schemas.md",
    "data/catalog/id_mapping.md",
    "data/processed/nba/player_impact_features.csv",
    "data/processed/myspariedge_mlb_signals_2026-05-03.csv",
]

PROJECT_INDEX_MARKERS = [
    "MODEL_LEDGER.md",
    "data/catalog/sources.csv",
    "data/catalog/schemas.md",
    "data/catalog/id_mapping.md",
    "Phase 2 alert-only",
    "200+ settled bets with positive average CLV",
]

MODEL_LEDGER_MARKERS = [
    "MLB MySPariEdge",
    "NBA Player Impact",
    "CLV is the primary edge test",
    "Auto-placement",
    "experimental",
]

SOURCE_REQUIRED_COLUMNS = [
    "source_name",
    "sport",
    "layer",
    "cadence",
    "trust_level",
    "canonical_destination",
    "notes",
]

NBA_REQUIRED_COLUMNS = [
    "name",
    "possessions",
    "mp_approx",
    "seasons",
    "off_RAPM",
    "def_RAPM",
    "total_RAPM",
    "off_RAPM_SE",
    "def_RAPM_SE",
    "rapm_reliability",
    "possession_reliability",
    "season_reliability",
    "starter_reliability",
    "model_status",
    "pts_per_100",
    "pts_per_100_z",
]

MLB_REQUIRED_COLUMNS = [
    "sport",
    "source",
    "signal_type",
    "event_id",
    "market",
    "pick",
    "probability",
    "rank",
]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text()


def csv_rows(relative_path: str) -> list[dict[str, str]]:
    with (ROOT / relative_path).open(newline="") as handle:
        return list(csv.DictReader(handle))


def check(condition: bool, message: str, errors: list[str]) -> None:
    status = "OK" if condition else "FAIL"
    print(f"{status} {message}")
    if not condition:
        errors.append(message)


def validate() -> int:
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        check((ROOT / relative_path).exists(), f"required file exists: {relative_path}", errors)

    if errors:
        return 1

    project_index = read_text("PROJECT_INDEX.md")
    for marker in PROJECT_INDEX_MARKERS:
        check(marker in project_index, f"PROJECT_INDEX marker: {marker}", errors)

    model_ledger = read_text("MODEL_LEDGER.md")
    for marker in MODEL_LEDGER_MARKERS:
        check(marker in model_ledger, f"MODEL_LEDGER marker: {marker}", errors)

    sources = csv_rows("data/catalog/sources.csv")
    source_columns = set(sources[0].keys()) if sources else set()
    check(bool(sources), "sources.csv has rows", errors)
    check(set(SOURCE_REQUIRED_COLUMNS).issubset(source_columns), "sources.csv required columns", errors)
    for sport in ["MLB", "NBA", "NFL", "NHL", "Soccer"]:
        check(any(row.get("sport") == sport for row in sources), f"sources.csv has {sport} coverage", errors)

    nba_rows = csv_rows("data/processed/nba/player_impact_features.csv")
    nba_columns = set(nba_rows[0].keys()) if nba_rows else set()
    check(len(nba_rows) + 1 == 1478, "NBA features row count is 1,478 including header", errors)
    check(set(NBA_REQUIRED_COLUMNS).issubset(nba_columns), "NBA features required columns", errors)
    check(
        {row.get("model_status") for row in nba_rows} == {"experimental_player_prior_not_pick"},
        "NBA features labeled experimental player priors",
        errors,
    )

    mlb_rows = csv_rows("data/processed/myspariedge_mlb_signals_2026-05-03.csv")
    mlb_columns = set(mlb_rows[0].keys()) if mlb_rows else set()
    check(bool(mlb_rows), "MLB signals file has rows", errors)
    check(set(MLB_REQUIRED_COLUMNS).issubset(mlb_columns), "MLB signals required columns", errors)

    check("CLV" in model_ledger, "CLV documented in model ledger", errors)
    check("No auto-placement" in project_index or "Auto-placement | Deferred" in model_ledger, "auto-placement deferred", errors)

    if errors:
        print("")
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("")
    print("Model source validation passed.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true", help="accepted for future CI use; current output remains explicit")
    parser.parse_args()
    raise SystemExit(validate())


if __name__ == "__main__":
    main()

