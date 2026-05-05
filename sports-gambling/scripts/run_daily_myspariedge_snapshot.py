#!/usr/bin/env python3
"""Run the full daily MySPariEdge snapshot and derived reports."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


COMMANDS = [
    ["scripts/pull_myspariedge_mlb.py", "--cookie-file", "data/raw/myspariedge/cookie.txt"],
    ["scripts/download_myspariedge_player_images.py"],
    ["scripts/analyze_myspariedge_model.py"],
    ["scripts/reverse_engineer_myspariedge_grades.py"],
    ["scripts/analyze_mlb_player_props.py"],
    ["scripts/analyze_mlb_home_runs.py"],
]


def run(command: list[str]) -> None:
    print("$ python3 " + " ".join(command))
    subprocess.run([sys.executable, *command], check=True)


def main() -> None:
    cookie = Path("data/raw/myspariedge/cookie.txt")
    if not cookie.exists():
        raise SystemExit("Missing data/raw/myspariedge/cookie.txt")
    for command in COMMANDS:
        run(command)


if __name__ == "__main__":
    main()
