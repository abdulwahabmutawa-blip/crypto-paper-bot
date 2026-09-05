"""Scan scorecard — grade every symbol Grok ever named by what price did next.

Owner question 2026-09-05: "which scans were accurate, which lost money,
how do we scan more efficiently?" This answers the first half with data,
not opinion: for every hype / crypto_hype entry in every scan on record
(current state file + every historical copy in git, since scans list is
capped at 90), fetch the forward return 1h/4h/24h/48h after the scan time
and the best high within 48h, then group by the fields Grok fills in
(mood, stage, organic, promo_risk, catalyst, list rank, scan hour).

Read-only. No xAI spend. Prices: Binance 1h klines for coins, yfinance 1h
bars for stocks (entry = first bar at/after scan time, so a weekend scan of
a stock enters Monday open, exactly like the IBKR bot would).

Usage:  python src/scan_scorecard.py            -> reports/scan_scorecard.md + .json
        python src/scan_scorecard.py --no-git   -> current state file only
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from statistics import mean, median

import config
import binance_data
from sentinel_trader import CRYPTO, to_ticker

STATE = config.DATA / "sentinel_state.json"
OUT_MD = config.REPORTS / "scan_scorecard.md"
OUT_JSON = config.REPORTS / "scan_scorecard.json"
CACHE = Path(tempfile.gettempdir()) / "scan_scorecard_prices.json"
HORIZONS_H = (1, 4, 24, 48)
STOP_PCT = -0.10


# ---------------------------------------------------------------- scans
def load_scans(use_git: bool = True) -> list[dict]:
    seen: dict[str, dict] = {}

    def take(doc):
        for s in doc.get("scans", []) or []:
            if s.get("ts") and s["ts"] not in seen:
                seen[s["ts"]] = s

    if STATE.exists():
        take(json.loads(STATE.read_text(encoding="utf-8")))
    if use_git:
        rel = STATE.relative_to(config.ROOT).as_posix()
        shas = subprocess.run(["git", "log", "--format=%H", "--", rel],
                              cwd=config.ROOT, capture_output=True, text=True).stdout.split()
        for sha in shas:
            try:
                raw = subprocess.run(["git", "show", f"{sha}:{rel}"], cwd=config.ROOT,
                                     capture_output=True, text=True, encoding="utf-8").stdout
                take(json.loads(raw))
            except Exception:
                continue
    return [seen[k] for k in sorted(seen)]


def binance_symbols() -> set[str]:
    """Every base asset with a USDT spot pair. The 'hype' list mixes stocks and
    coins with no asset tag, and CRYPTO only knows 20 majors: ZEC, DASH,
    MARSCOIN would otherwise be sent to yfinance as stock tickers."""
    try:
        return {t["symbol"][:-4] for t in binance_data.all_tickers_24h()
                if t.get("symbol", "").endswith("USDT")}
    except Exception:
        return set()


def rows_from_scans(scans: list[dict]) -> list[dict]:
    rows = []
    coins = binance_symbols() | CRYPTO
    for s in scans:
        coins |= {str(h.get("symbol", "")).upper().lstrip("$")
                  for h in (s.get("crypto_hype") or [])}
    for s in scans:
        ts = datetime.fromisoformat(s["ts"])
        base = {"ts": s["ts"], "hour_utc": ts.hour, "weekday": ts.weekday(),
                "risk_level": s.get("risk_level")}
        for i, h in enumerate(s.get("hype", []) or []):
            sym = str(h.get("symbol", "")).upper().lstrip("$")
            if not sym or not sym.replace("-", "").isalnum():
                continue
            is_crypto = sym in coins
            rows.append({**base, "section": "hype", "symbol": sym, "rank": i + 1,
                         "asset": "crypto" if is_crypto else "stock",
                         "mood": h.get("mood"), "stage": None, "organic": None,
                         "promo_risk": None, "catalyst": None})
        for i, h in enumerate(s.get("crypto_hype", []) or []):
            sym = str(h.get("symbol", "")).upper().lstrip("$")
            if not sym or not sym.isalnum():
                continue
            cat = str(h.get("catalyst") or "none").strip().lower()
            rows.append({**base, "section": "crypto_hype", "symbol": sym, "rank": i + 1,
                         "asset": "crypto", "mood": h.get("mood"), "stage": h.get("stage"),
                         "organic": h.get("organic"), "promo_risk": h.get("promo_risk"),
                         "catalyst": "none" if cat in ("", "none", "n/a") else "yes"})
    return rows


# ---------------------------------------------------------------- prices
def _load_cache() -> dict:
    try:
        return json.loads(CACHE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_cache(c: dict) -> None:
    CACHE.write_text(json.dumps(c), encoding="utf-8")


def crypto_bars(symbol: str, start: datetime, end: datetime) -> list[list]:
    """[ms, high, low, close] hourly from Binance, oldest first."""
    out, cur = [], int(start.timestamp() * 1000)
    end_ms = int(end.timestamp() * 1000)
    pair = symbol + "USDT"
    while cur < end_ms:
        d = binance_data._get("/api/v3/klines", {"symbol": pair, "interval": "1h",
                                                 "startTime": cur, "limit": 1000}, weight=2)
        if not isinstance(d, list) or not d:
            break
        out += [[r[0], float(r[2]), float(r[3]), float(r[4])] for r in d]
        nxt = d[-1][6] + 1
        if nxt <= cur:
            break
        cur = nxt
    return out


def stock_bars(symbol: str, start: datetime, end: datetime) -> list[list]:
    try:
        import yfinance as yf
        df = yf.download(symbol, start=start.date() - timedelta(days=1),
                         end=end.date() + timedelta(days=1), interval="1h",
                         auto_adjust=True, progress=False, threads=False)
    except Exception:
        return []
    if df is None or df.empty:
        return []
    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)
    out = []
    for idx, r in df.iterrows():
        t = idx.to_pydatetime()
        if t.tzinfo is None:
            t = t.replace(tzinfo=timezone.utc)
        try:
            out.append([int(t.timestamp() * 1000), float(r["High"]), float(r["Low"]),
                        float(r["Close"])])
        except Exception:
            continue
    return out


def get_bars(cache: dict, symbol: str, asset: str, start: datetime, end: datetime):
    key = f"{asset}:{symbol}"
    if key in cache:
        return cache[key]
    bars = crypto_bars(symbol, start, end) if asset == "crypto" else stock_bars(symbol, start, end)
    cache[key] = bars
    return bars


def forward(bars: list[list], ts: datetime) -> dict | None:
    """Entry = first bar closing at/after ts; returns per horizon, peak high,
    worst low within 48h, and the entry delay in hours."""
    t0 = int(ts.timestamp() * 1000)
    i0 = next((i for i, b in enumerate(bars) if b[0] >= t0), None)
    if i0 is None:
        return None
    entry_ms, entry = bars[i0][0], bars[i0][3]
    if entry <= 0:
        return None
    res = {"entry_delay_h": round((entry_ms - t0) / 3.6e6, 1)}
    for h in HORIZONS_H:
        tgt = entry_ms + h * 3.6e6
        j = next((i for i in range(i0, len(bars)) if bars[i][0] >= tgt), None)
        res[f"r{h}h"] = None if j is None else round(bars[j][3] / entry - 1, 4)
    win = [b for b in bars[i0:] if b[0] <= entry_ms + 48 * 3.6e6]
    if win:
        res["peak48"] = round(max(b[1] for b in win) / entry - 1, 4)
        res["trough48"] = round(min(b[2] for b in win) / entry - 1, 4)
        # IBKR-bot style: 48h hold with a -10% stop hit on the low
        res["r48_stopped"] = STOP_PCT if res["trough48"] <= STOP_PCT else res["r48h"]
    return res


# ---------------------------------------------------------------- stats
def summarise(rows: list[dict], key) -> dict:
    groups = defaultdict(list)
    for r in rows:
        if r.get("r24h") is None:
            continue
        groups[str(key(r))].append(r)
    out = {}
    for g, rs in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        d = {"n": len(rs)}
        for h in ("r1h", "r4h", "r24h", "r48h", "r48_stopped", "peak48"):
            vals = [r[h] for r in rs if r.get(h) is not None]
            if vals:
                d[h] = {"hit": round(sum(v > 0 for v in vals) / len(vals), 2),
                        "mean": round(mean(vals) * 100, 2), "median": round(median(vals) * 100, 2)}
        out[g] = d
    return out


def table(title: str, stats: dict, cols=("r4h", "r24h", "r48h", "r48_stopped", "peak48")) -> str:
    lines = [f"### {title}", "", "| group | n | " + " | ".join(f"{c} hit / mean% / med%" for c in cols) + " |",
             "|---|---|" + "---|" * len(cols)]
    for g, d in stats.items():
        cells = []
        for c in cols:
            s = d.get(c)
            cells.append("-" if not s else f"{s['hit']:.0%} / {s['mean']:+.1f} / {s['median']:+.1f}")
        lines.append(f"| {g} | {d['n']} | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main(use_git: bool = True) -> int:
    scans = load_scans(use_git)
    rows = rows_from_scans(scans)
    if not rows:
        print("no scans found"); return 1
    start = datetime.fromisoformat(scans[0]["ts"]) - timedelta(hours=2)
    end = datetime.now(timezone.utc)
    cache = _load_cache()
    syms = sorted({(r["symbol"], r["asset"]) for r in rows})
    print(f"{len(scans)} scans, {len(rows)} symbol mentions, {len(syms)} distinct symbols")
    for n, (sym, asset) in enumerate(syms, 1):
        bars = get_bars(cache, sym, asset, start, end)
        if n % 10 == 0:
            _save_cache(cache); print(f"  prices {n}/{len(syms)}")
    _save_cache(cache)
    priced = 0
    for r in rows:
        bars = cache.get(f"{r['asset']}:{r['symbol']}") or []
        fw = forward(bars, datetime.fromisoformat(r["ts"])) if bars else None
        if fw:
            r.update(fw); priced += 1
    stocks = [r for r in rows if r["asset"] == "stock"]
    coins = [r for r in rows if r["asset"] == "crypto"]
    ch = [r for r in coins if r["section"] == "crypto_hype"]
    euph_stock = [r for r in stocks if r["mood"] == "euphoric"]
    report = {
        "generated": end.isoformat(timespec="seconds"), "scans": len(scans),
        "first_scan": scans[0]["ts"], "last_scan": scans[-1]["ts"],
        "mentions": len(rows), "priced": priced,
        "stock_by_mood": summarise(stocks, lambda r: r["mood"]),
        "stock_euphoric_by_rank": summarise(euph_stock, lambda r: "rank1" if r["rank"] == 1 else "rank2+"),
        "stock_euphoric_by_risk": summarise(euph_stock, lambda r: r["risk_level"]),
        "stock_euphoric_by_hour": summarise(euph_stock, lambda r: f"{r['hour_utc']:02d}h"),
        "stock_euphoric_by_weekday": summarise(euph_stock, lambda r: "weekend" if r["weekday"] >= 5 else "weekday"),
        "crypto_by_mood": summarise(coins, lambda r: r["mood"]),
        "crypto_hype_by_stage": summarise(ch, lambda r: r["stage"]),
        "crypto_hype_by_organic": summarise(ch, lambda r: f"organic={r['organic']}"),
        "crypto_hype_by_promo": summarise(ch, lambda r: f"promo={r['promo_risk']}"),
        "crypto_hype_by_catalyst": summarise(ch, lambda r: f"catalyst={r['catalyst']}"),
        "crypto_hype_stage_x_organic": summarise(ch, lambda r: f"{r['stage']}/organic={r['organic']}"),
        "top_symbols": summarise(rows, lambda r: r["symbol"]),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=1), encoding="utf-8")
    md = [f"# Grok scan scorecard", "",
          f"{len(scans)} scans {scans[0]['ts'][:10]} to {scans[-1]['ts'][:10]}, "
          f"{len(rows)} symbol mentions, {priced} priced. Returns are from the first "
          f"price bar at/after the scan (stocks: next market bar). `r48_stopped` = 48h "
          f"hold with a -10% stop on the low, the IBKR bot's rule. Hit = share of "
          f"mentions that were positive.", ""]
    md.append(table("US stocks by mood (what the IBKR hype bot buys = euphoric)", report["stock_by_mood"]))
    md.append(table("Euphoric stocks: first-listed vs rest", report["stock_euphoric_by_rank"]))
    md.append(table("Euphoric stocks by scan risk level", report["stock_euphoric_by_risk"]))
    md.append(table("Euphoric stocks by scan weekday", report["stock_euphoric_by_weekday"]))
    md.append(table("Euphoric stocks by scan hour (UTC)", report["stock_euphoric_by_hour"]))
    md.append(table("Coins by mood (all sections)", report["crypto_by_mood"]))
    md.append(table("crypto_hype by stage", report["crypto_hype_by_stage"]))
    md.append(table("crypto_hype by organic flag", report["crypto_hype_by_organic"]))
    md.append(table("crypto_hype by promo_risk", report["crypto_hype_by_promo"]))
    md.append(table("crypto_hype by catalyst present", report["crypto_hype_by_catalyst"]))
    md.append(table("crypto_hype stage x organic", report["crypto_hype_stage_x_organic"]))
    top = dict(list(report["top_symbols"].items())[:25])
    md.append(table("25 most-mentioned symbols", top, cols=("r24h", "r48h", "peak48")))
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"wrote {OUT_MD} and {OUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(use_git="--no-git" not in sys.argv))
