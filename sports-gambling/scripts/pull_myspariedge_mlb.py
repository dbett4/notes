#!/usr/bin/env python3
"""Pull and normalize MySPariEdge MLB projection feeds.

The public pages call authenticated API endpoints with browser credentials.
Pass an authenticated Cookie header with either:

    MYSPARIEDGE_COOKIE='name=value; ...' python3 scripts/pull_myspariedge_mlb.py

or:

    python3 scripts/pull_myspariedge_mlb.py --cookie-file data/raw/myspariedge/cookie.txt
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


GAME_API_URL = "https://api.myspariedge.com/api/v1/projections/game/mlb"
BEST_BETS_API_URL = "https://api.myspariedge.com/api/v1/projections/best-bets"
PLAYER_PROJECTIONS_API_URL = "https://api.myspariedge.com/api/v1/projections?league=mlb"
HISTORY_API_URL = "https://api.myspariedge.com/api/v1/projections/history"
POSITIVE_EV_API_URL = "https://api.myspariedge.com/api/v1/odds/positive-ev"
SHARP_MONEY_API_URL = "https://api.myspariedge.com/api/v1/odds/sharp-money"
DFS_OPTIMIZER_API_URL = "https://api.myspariedge.com/api/v1/odds/dfs-optimizer"
BETS_API_URL = "https://api.myspariedge.com/api/v1/bets/"
ODDS_BOOKMAKERS_API_URL = "https://api.myspariedge.com/api/v1/odds/bookmakers"
ODDS_LEAGUES_API_URL = "https://api.myspariedge.com/api/v1/odds/leagues"
ODDS_MARKETS_API_URL = "https://api.myspariedge.com/api/v1/odds/markets"
ODDS_MLB_MARKETS_API_URL = "https://api.myspariedge.com/api/v1/odds/markets?sport_key=baseball_mlb"
ODDS_REFERENCE_API_URL = "https://api.myspariedge.com/api/v1/odds/reference"
ODDS_BOARD_URL_TEMPLATE = "https://api.myspariedge.com/api/v1/odds/leagues/mlb/markets/{market_key}"
TARGET_GRADES = {"A+", "A", "A-", "B+"}
MLB_MARKET_LABELS = {
    "hits": "Hits",
    "tb": "Total Bases",
    "hr_prob": "HR%",
    "rbi": "RBIs",
    "runs": "Runs",
    "hrr": "Hits + Runs + RBIs",
    "k": "Strikeouts",
    "ip": "Innings Pitched",
    "outs": "Pitcher Outs",
    "walks": "Walks Allowed",
    "earned_runs": "Earned Runs",
    "hits_allowed": "Hits Allowed",
}
MLB_ODDS_MARKETS = [
    "batter_hits",
    "batter_hits_runs_rbis",
    "batter_home_runs",
    "h2h",
    "pitcher_earned_runs",
    "pitcher_hits_allowed",
    "pitcher_outs",
    "pitcher_strikeouts",
    "pitcher_walks",
    "batter_rbis",
    "batter_runs_scored",
    "batter_singles",
    "spreads",
    "batter_total_bases",
    "totals",
]


def read_cookie(args: argparse.Namespace) -> str | None:
    if args.cookie:
        return args.cookie
    if args.cookie_file:
        return Path(args.cookie_file).read_text().strip()
    return os.environ.get("MYSPARIEDGE_COOKIE")


def fetch_json(url: str, cookie: str | None, referer: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Origin": "https://www.myspariedge.com",
        "Referer": referer,
    }
    if cookie:
        headers["Cookie"] = cookie

    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        raise SystemExit(f"MySPariEdge request failed for {url}: HTTP {exc.code} {body}") from exc


def top_strikeout_rows(payload: dict, pulled_at: str) -> list[dict[str, object]]:
    slate = payload.get("slate") or {}
    rows = []
    for item in slate.get("top5K") or []:
        rows.append(
            {
                "pulled_at": pulled_at,
                "signal_type": "top_strikeout_play",
                "rank": item.get("rank"),
                "player": item.get("pitcher"),
                "team": item.get("team"),
                "matchup": item.get("matchup"),
                "market": "Pitcher Strikeouts",
                "side": item.get("direction"),
                "line": item.get("line"),
                "projection": item.get("proj"),
                "diff": item.get("diff"),
                "probability": item.get("prob"),
                "grade": item.get("grade"),
            }
        )
    return rows


def top_game_rows(payload: dict, pulled_at: str) -> list[dict[str, object]]:
    slate = payload.get("slate") or {}
    rows = []
    for item in slate.get("top5Game") or []:
        rows.append(
            {
                "pulled_at": pulled_at,
                "signal_type": "top_game_play",
                "rank": item.get("rank"),
                "pick": item.get("pick"),
                "matchup": item.get("matchup"),
                "market": item.get("type"),
                "probability": item.get("prob"),
                "grade": item.get("grade"),
            }
        )
    return rows


def best_bet_rows(payload: dict, pulled_at: str) -> list[dict[str, object]]:
    rows = []
    for item in payload.get("best_bets") or []:
        rows.append(
            {
                "pulled_at": pulled_at,
                "signal_type": "best_bet",
                "is_target_grade": item.get("bet_grade") in TARGET_GRADES,
                "player_id": item.get("player_id"),
                "player": item.get("player_name"),
                "position": item.get("position"),
                "team": item.get("team"),
                "game": item.get("game"),
                "market": item.get("market"),
                "market_label": item.get("market_label"),
                "side": item.get("side"),
                "line": item.get("line"),
                "projection": item.get("projection"),
                "grade": item.get("bet_grade"),
                "win_pct": item.get("win_pct"),
                "wins": item.get("wins"),
                "losses": item.get("losses"),
                "player_img": item.get("player_img"),
            }
        )
    return rows


def projection_rows(payload: dict, pulled_at: str) -> list[dict[str, object]]:
    rows = []
    for player in payload.get("players") or []:
        projections = player.get("projections") or {}
        stats = projections.get("stats") or {}
        lines = projections.get("lines") or {}
        grades = projections.get("grades") or {}
        labels = (projections.get("display") or {}).get("projection_labels") or {}
        for market_key, projection in stats.items():
            if market_key in {"ab", "avg", "ops", "slg"}:
                continue
            line = lines.get(market_key)
            direction = projections.get(f"{market_key}Dir")
            grade = grades.get(market_key) or projections.get(f"{market_key}Grade")
            rows.append(
                {
                    "pulled_at": pulled_at,
                    "signal_type": "projection",
                    "is_target_grade": grade in TARGET_GRADES,
                    "player_id": player.get("player"),
                    "player": player.get("player_name") or projections.get("player_name"),
                    "position": projections.get("pos"),
                    "team": player.get("team"),
                    "game": player.get("game"),
                    "gametime": player.get("gametime"),
                    "market_key": market_key,
                    "market": MLB_MARKET_LABELS.get(market_key) or labels.get(market_key) or market_key,
                    "side": direction,
                    "line": line,
                    "projection": projection,
                    "grade": grade,
                    "batting_order": projections.get("batting_order"),
                    "locked_at": projections.get("lockedAt"),
                    "player_img": player.get("player_img"),
                }
            )
    return rows


def history_rows(payload: dict, pulled_at: str) -> list[dict[str, object]]:
    rows = []
    for item in payload.get("records") or []:
        if item.get("sport") != "MLB":
            continue
        rows.append(
            {
                "pulled_at": pulled_at,
                "signal_type": "history",
                "history_type": item.get("type"),
                "season": item.get("season"),
                "sport": item.get("sport"),
                "market": item.get("market"),
                "side": item.get("side"),
                "grade": item.get("bet_grade"),
                "wins": item.get("wins"),
                "losses": item.get("losses"),
                "win_pct": item.get("win_pct"),
                "updated_datetime": item.get("updated_datetime"),
            }
        )
    return rows


def nested_get(payload: dict, *keys: str) -> object:
    value = payload
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def positive_ev_rows(payload: dict, pulled_at: str) -> list[dict[str, object]]:
    rows = []
    for item in payload.get("plays") or []:
        event = item.get("event") or {}
        player = item.get("player") or {}
        market = item.get("market") or {}
        primary = item.get("primary_odd") or {}
        fair = item.get("fair_odds") or {}
        rows.append(
            {
                "pulled_at": pulled_at,
                "signal_type": "positive_ev",
                "sport": event.get("sport_title") or event.get("sport_key"),
                "event_id": event.get("id"),
                "game": f"{nested_get(event, 'away_team', 'abbreviation') or nested_get(event, 'away_team', 'name')}@{nested_get(event, 'home_team', 'abbreviation') or nested_get(event, 'home_team', 'name')}",
                "gametime": event.get("commence_time"),
                "player_id": player.get("id"),
                "player": player.get("name"),
                "team": nested_get(player, "team", "abbreviation"),
                "market_key": market.get("key"),
                "market": market.get("name"),
                "side": item.get("label"),
                "line": item.get("point"),
                "book": primary.get("bookmaker_name"),
                "book_key": primary.get("bookmaker_key"),
                "price_decimal": primary.get("price_decimal"),
                "price_american": primary.get("price_american"),
                "ev_pct": primary.get("ev_percentage"),
                "fair_price_decimal": fair.get("fair_odds_decimal"),
                "fair_price_american": fair.get("fair_odds_american"),
                "chance_to_hit": fair.get("fair_probability"),
            }
        )
    return rows


def sharp_money_rows(payload: dict, pulled_at: str) -> list[dict[str, object]]:
    rows = []
    for item in payload.get("plays") or []:
        event = item.get("event") or {}
        player = item.get("player") or {}
        market = item.get("market") or {}
        best = item.get("best_odd") or {}
        rows.append(
            {
                "pulled_at": pulled_at,
                "signal_type": "sharp_money",
                "sport": event.get("sport_title") or event.get("sport_key"),
                "event_id": event.get("id"),
                "game": f"{nested_get(event, 'away_team', 'abbreviation') or nested_get(event, 'away_team', 'name')}@{nested_get(event, 'home_team', 'abbreviation') or nested_get(event, 'home_team', 'name')}",
                "gametime": event.get("commence_time"),
                "player": player.get("name") if isinstance(player, dict) else None,
                "team": nested_get(player, "team", "abbreviation") if isinstance(player, dict) else None,
                "market_key": market.get("key"),
                "market": market.get("name"),
                "side": item.get("sharp_side"),
                "whale_side": item.get("whale_side"),
                "line": item.get("point"),
                "total_whale_limit": item.get("total_whale_limit"),
                "book": best.get("bookmaker_name"),
                "book_key": best.get("bookmaker_key"),
                "price_decimal": best.get("price_decimal"),
                "price_american": best.get("price_american"),
            }
        )
    return rows


def dfs_optimizer_rows(payload: dict, pulled_at: str) -> list[dict[str, object]]:
    rows = []
    for item in payload.get("plays") or []:
        event = item.get("event") or {}
        player = item.get("player") or {}
        market = item.get("market") or {}
        bookmaker = item.get("bookmaker") or {}
        rows.append(
            {
                "pulled_at": pulled_at,
                "signal_type": "dfs_optimizer",
                "sport": event.get("sport_title") or event.get("sport_key"),
                "event_id": event.get("id"),
                "game": f"{nested_get(event, 'away_team', 'abbreviation') or nested_get(event, 'away_team', 'name')}@{nested_get(event, 'home_team', 'abbreviation') or nested_get(event, 'home_team', 'name')}",
                "gametime": event.get("commence_time"),
                "player_id": player.get("id"),
                "player": player.get("name"),
                "team": nested_get(player, "team", "abbreviation"),
                "market_key": market.get("key"),
                "market": market.get("name"),
                "side": item.get("label"),
                "line": item.get("point"),
                "book": bookmaker.get("name"),
                "book_key": bookmaker.get("key"),
                "price_decimal": item.get("dfs_price_decimal"),
                "price_american": item.get("dfs_price_american"),
                "ev_pct": item.get("dfs_ev_percentage"),
                "avg_odds_decimal": item.get("avg_odds_decimal"),
                "avg_odds_american": item.get("avg_odds_american"),
                "chance_to_hit": item.get("chance_to_hit"),
            }
        )
    return rows


def saved_bet_rows(payload: list[dict], pulled_at: str) -> list[dict[str, object]]:
    rows = []
    for item in payload or []:
        rows.append(
            {
                "pulled_at": pulled_at,
                "signal_type": "saved_bet",
                "source": item.get("source"),
                "sport": item.get("sport_title") or item.get("sport_key"),
                "event_id": item.get("event_id"),
                "game": f"{item.get('away_team')}@{item.get('home_team')}",
                "gametime": item.get("commence_time"),
                "player": item.get("player_name"),
                "team": item.get("team_abbreviation"),
                "market_key": item.get("market_key"),
                "market": item.get("market_name"),
                "side": item.get("side"),
                "line": item.get("point"),
                "book": item.get("bookmaker_name"),
                "book_key": item.get("bookmaker_key"),
                "price_decimal": item.get("odds_decimal"),
                "price_american": item.get("odds_american"),
                "wager_amount": item.get("wager_amount"),
                "outcome": item.get("outcome"),
                "pnl": item.get("pnl"),
                "created_at": item.get("created_at"),
            }
        )
    return rows


def odds_board_best_offer_rows(payloads: dict[str, dict], pulled_at: str) -> list[dict[str, object]]:
    rows = []
    for market_key, payload in payloads.items():
        market = payload.get("market") or {}
        market_name = market.get("name") if isinstance(market, dict) else market_key
        props = payload.get("player_props") or {}
        best_offers = payload.get("player_best_offers") or {}
        events = payload.get("events") or {}
        for player_name, offers in best_offers.items():
            prop = props.get(str(player_name)) or props.get(player_name) or {}
            event = events.get(str(prop.get("event_id"))) if prop.get("event_id") else None
            for best_key in ["best_over", "best_under", "best_yes", "best_no"]:
                offer = (offers or {}).get(best_key)
                if not offer:
                    continue
                rows.append(
                    {
                        "pulled_at": pulled_at,
                        "signal_type": "odds_board_best_offer",
                        "event_id": prop.get("event_id"),
                        "game": None
                        if not event
                        else f"{nested_get(event, 'away_team', 'abbreviation') or nested_get(event, 'away_team', 'name')}@{nested_get(event, 'home_team', 'abbreviation') or nested_get(event, 'home_team', 'name')}",
                        "gametime": event.get("commence_time") if event else None,
                        "player_id": prop.get("player_id"),
                        "player": player_name,
                        "position": None,
                        "team": None,
                        "market_key": market_key,
                        "market": market_name,
                        "side": offer.get("label") or best_key.replace("best_", ""),
                        "line": offer.get("point"),
                        "book": offer.get("bookmaker_name"),
                        "book_key": offer.get("bookmaker"),
                        "price_decimal": offer.get("price_decimal"),
                        "price_american": offer.get("price_american"),
                        "last_update": offer.get("last_update"),
                    }
                )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = sorted({key for row in rows for key in row})
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cookie")
    parser.add_argument("--cookie-file")
    parser.add_argument("--outdir", default="data/raw/myspariedge")
    args = parser.parse_args()

    pulled_at = datetime.now(timezone.utc).isoformat()
    stamp = pulled_at[:10]
    outdir = Path(args.outdir) / stamp
    outdir.mkdir(parents=True, exist_ok=True)

    cookie = read_cookie(args)
    game_payload = fetch_json(cookie=cookie, url=GAME_API_URL, referer="https://www.myspariedge.com/projections/game")
    best_bets_payload = fetch_json(
        cookie=cookie,
        url=BEST_BETS_API_URL,
        referer="https://www.myspariedge.com/projections/best-bets",
    )
    projections_payload = fetch_json(
        cookie=cookie,
        url=PLAYER_PROJECTIONS_API_URL,
        referer="https://www.myspariedge.com/projections/player",
    )
    history_payload = fetch_json(
        cookie=cookie,
        url=HISTORY_API_URL,
        referer="https://www.myspariedge.com/projections/history",
    )
    positive_ev_payload = fetch_json(
        cookie=cookie,
        url=POSITIVE_EV_API_URL,
        referer="https://www.myspariedge.com/odds/positive-ev",
    )
    sharp_money_payload = fetch_json(
        cookie=cookie,
        url=SHARP_MONEY_API_URL,
        referer="https://www.myspariedge.com/sharp-money-radar",
    )
    dfs_optimizer_payload = fetch_json(
        cookie=cookie,
        url=DFS_OPTIMIZER_API_URL,
        referer="https://www.myspariedge.com/odds/dfs-optimizer",
    )
    saved_bets_payload = fetch_json(
        cookie=cookie,
        url=BETS_API_URL,
        referer="https://www.myspariedge.com/my-bets",
    )
    odds_bookmakers_payload = fetch_json(
        cookie=cookie,
        url=ODDS_BOOKMAKERS_API_URL,
        referer="https://www.myspariedge.com/sharp-money-radar",
    )
    odds_leagues_payload = fetch_json(
        cookie=cookie,
        url=ODDS_LEAGUES_API_URL,
        referer="https://www.myspariedge.com/sharp-money-radar",
    )
    odds_markets_payload = fetch_json(
        cookie=cookie,
        url=ODDS_MARKETS_API_URL,
        referer="https://www.myspariedge.com/sharp-money-radar",
    )
    odds_mlb_markets_payload = fetch_json(
        cookie=cookie,
        url=ODDS_MLB_MARKETS_API_URL,
        referer="https://www.myspariedge.com/my-bets",
    )
    odds_reference_payload = fetch_json(
        cookie=cookie,
        url=ODDS_REFERENCE_API_URL,
        referer="https://www.myspariedge.com/odds-board",
    )
    odds_board_payloads = {}
    for market_key in MLB_ODDS_MARKETS:
        odds_board_payloads[market_key] = fetch_json(
            cookie=cookie,
            url=ODDS_BOARD_URL_TEMPLATE.format(market_key=market_key),
            referer="https://www.myspariedge.com/odds-board",
        )
    (outdir / "game_mlb.json").write_text(json.dumps(game_payload, indent=2, sort_keys=True))
    (outdir / "best_bets.json").write_text(json.dumps(best_bets_payload, indent=2, sort_keys=True))
    (outdir / "player_projections.json").write_text(json.dumps(projections_payload, indent=2, sort_keys=True))
    (outdir / "history.json").write_text(json.dumps(history_payload, indent=2, sort_keys=True))
    (outdir / "positive_ev.json").write_text(json.dumps(positive_ev_payload, indent=2, sort_keys=True))
    (outdir / "sharp_money.json").write_text(json.dumps(sharp_money_payload, indent=2, sort_keys=True))
    (outdir / "dfs_optimizer.json").write_text(json.dumps(dfs_optimizer_payload, indent=2, sort_keys=True))
    (outdir / "saved_bets.json").write_text(json.dumps(saved_bets_payload, indent=2, sort_keys=True))
    (outdir / "odds_bookmakers.json").write_text(json.dumps(odds_bookmakers_payload, indent=2, sort_keys=True))
    (outdir / "odds_leagues.json").write_text(json.dumps(odds_leagues_payload, indent=2, sort_keys=True))
    (outdir / "odds_markets.json").write_text(json.dumps(odds_markets_payload, indent=2, sort_keys=True))
    (outdir / "odds_mlb_markets.json").write_text(json.dumps(odds_mlb_markets_payload, indent=2, sort_keys=True))
    (outdir / "odds_reference.json").write_text(json.dumps(odds_reference_payload, indent=2, sort_keys=True))
    odds_board_dir = outdir / "odds_board"
    odds_board_dir.mkdir(exist_ok=True)
    for market_key, payload in odds_board_payloads.items():
        (odds_board_dir / f"{market_key}.json").write_text(json.dumps(payload, indent=2, sort_keys=True))

    rows = (
        top_strikeout_rows(game_payload, pulled_at)
        + top_game_rows(game_payload, pulled_at)
        + best_bet_rows(best_bets_payload, pulled_at)
        + projection_rows(projections_payload, pulled_at)
        + history_rows(history_payload, pulled_at)
        + positive_ev_rows(positive_ev_payload, pulled_at)
        + sharp_money_rows(sharp_money_payload, pulled_at)
        + dfs_optimizer_rows(dfs_optimizer_payload, pulled_at)
        + saved_bet_rows(saved_bets_payload, pulled_at)
        + odds_board_best_offer_rows(odds_board_payloads, pulled_at)
    )
    write_csv(Path("data/processed") / f"myspariedge_mlb_signals_{stamp}.csv", rows)
    target_rows = [row for row in rows if row.get("signal_type") == "best_bet" and row.get("is_target_grade")]
    target_projection_rows = [row for row in rows if row.get("signal_type") == "projection" and row.get("is_target_grade")]
    history_count = sum(1 for row in rows if row.get("signal_type") == "history")
    positive_ev_count = sum(1 for row in rows if row.get("signal_type") == "positive_ev")
    sharp_count = sum(1 for row in rows if row.get("signal_type") == "sharp_money")
    odds_best_count = sum(1 for row in rows if row.get("signal_type") == "odds_board_best_offer")
    print(
        f"wrote {len(rows)} signals, including {len(target_rows)} A+ through B+ best bets, "
        f"{len(target_projection_rows)} A+ through B+ projections, {history_count} MLB history records, "
        f"{positive_ev_count} +EV plays, {sharp_count} sharp-money plays, and {odds_best_count} odds-board best offers"
    )


if __name__ == "__main__":
    main()
