#!/usr/bin/env python3
"""Download player images referenced by the latest MySPariEdge raw snapshot."""

from __future__ import annotations

import csv
import glob
import json
import re
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


IMAGE_KEYS = {"img", "player_img", "headshot"}


def latest_raw_dir() -> Path:
    dirs = sorted(Path("data/raw/myspariedge").glob("20??-??-??"))
    if not dirs:
        raise SystemExit("No MySPariEdge raw directory found.")
    return dirs[-1]


def slugify(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value.strip()).strip("-").lower()
    return value or "unknown"


def extension(url: str, content_type: str | None) -> str:
    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp"}:
        return ".jpg" if suffix == ".jpeg" else suffix
    if content_type and "png" in content_type:
        return ".png"
    if content_type and "webp" in content_type:
        return ".webp"
    return ".jpg"


def walk_images(value, context: dict[str, str] | None = None):
    context = dict(context or {})
    if isinstance(value, dict):
        next_context = dict(context)
        for key in ["player_name", "name", "player", "pitcher"]:
            if key in value and isinstance(value[key], str):
                next_context.setdefault("player", value[key])
        for key in ["id", "player_id", "player"]:
            if key in value and isinstance(value[key], (str, int)):
                next_context.setdefault("player_id", str(value[key]))
        for key in ["team", "team_abbreviation"]:
            item = value.get(key)
            if isinstance(item, str):
                next_context.setdefault("team", item)
            elif isinstance(item, dict) and isinstance(item.get("abbreviation"), str):
                next_context.setdefault("team", item["abbreviation"])
        for key, item in value.items():
            if key in IMAGE_KEYS and isinstance(item, str) and item.startswith("http"):
                yield {
                    "player": next_context.get("player") or "",
                    "player_id": next_context.get("player_id") or "",
                    "team": next_context.get("team") or "",
                    "source_key": key,
                    "url": item,
                }
            else:
                yield from walk_images(item, next_context)
    elif isinstance(value, list):
        for item in value:
            yield from walk_images(item, context)


def collect_images(raw_dir: Path) -> list[dict[str, str]]:
    seen = set()
    rows = []
    for path in raw_dir.rglob("*.json"):
        if path.name in {"auth_me.json"}:
            continue
        try:
            payload = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        for row in walk_images(payload):
            key = row["url"]
            if key in seen:
                continue
            seen.add(key)
            row["source_file"] = str(path)
            rows.append(row)
    return rows


def download(url: str) -> tuple[bytes, str | None]:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as response:
        return response.read(), response.headers.get("content-type")


def main() -> None:
    raw_dir = latest_raw_dir()
    out_dir = Path("data/assets/player_images") / raw_dir.name
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for image in collect_images(raw_dir):
        name_part = slugify(image["player"] or image["player_id"] or "player")
        id_part = slugify(image["player_id"]) if image["player_id"] else "no-id"
        team_part = slugify(image["team"]) if image["team"] else "no-team"
        base = f"{name_part}_{id_part}_{team_part}"
        try:
            content, content_type = download(image["url"])
        except Exception as exc:
            rows.append({**image, "local_path": "", "status": f"error: {exc}"})
            continue
        path = out_dir / f"{base}{extension(image['url'], content_type)}"
        if path.exists():
            counter = 2
            while (out_dir / f"{base}-{counter}{path.suffix}").exists():
                counter += 1
            path = out_dir / f"{base}-{counter}{path.suffix}"
        path.write_bytes(content)
        rows.append({**image, "local_path": str(path), "status": "ok"})

    index_path = out_dir / "index.csv"
    with index_path.open("w", newline="") as f:
        fieldnames = ["player", "player_id", "team", "source_key", "url", "source_file", "local_path", "status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    ok = sum(1 for row in rows if row["status"] == "ok")
    print(f"downloaded {ok}/{len(rows)} images")
    print(index_path)


if __name__ == "__main__":
    main()
