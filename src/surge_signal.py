"""SURGE — the book's entry signal from 2026-09-05 (owner decision).

Replaces the scout's ignition/breakout/heat lanes as the ONLY entry lane.
Built from the 60-day pre-move study (trading-research/, local-only):
174,396 coin-hours, 142 coins, forward 24h return measured over BTC.

What the study found (predict60_eval.py, premove_findings.md):
  * nothing free arrives BEFORE the move at 5-minute latency: Binance and
    Upbit listing notices pop inside 1-5 minutes and are median-negative by
    30 min; funding and open-interest extremes only predict DOWN moves.
  * the one shape with a positive mean is a coin near its 24h HIGH on
    HEAVY 24h volume that has NOT already run far, on a day BTC is not
    falling, with the futures crowd not yet piled in. First-touch sim,
    one trade per coin, 0.25% cost, +5%/-3%/48h: 824 trades, +1.18%/trade,
    55% hit, 5 of 8 weeks positive (unfiltered momentum: +0.35%, 45%).
    +3%/-4%/48h: 977 trades, +0.76%, 70% hit.
  It is a modest edge concentrated in hot weeks; the quiet weeks are
  roughly flat (-0.2..-1.0%/trade). That is the "simple win" the owner
  asked for on 2026-09-05, not a big one.

Read-only: computes and ranks; lottery_live decides and trades.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import config
import binance_data

SIGNALS = config.DATA / "surge_signals.json"
LOG = config.DATA / "surge_log.jsonl"

UNIVERSE_N = 150          # top-N USDT pairs by 24h quote volume
V24_MIN = 1.6             # last 24h quote volume vs the prior 6-day daily avg
POS24_MIN = 0.80          # close in the top fifth of the 24h range
R24_MIN = 0.03            # up on the day...
R24_MAX = 0.15            # ...but not already exhausted
BTC24_MIN = -0.01         # BTC not falling on the day
FUNDING_MAX = 0.0003      # perp funding above +0.03%/8h = crowded long
OI_CHG_MAX = 0.20         # open interest up >20% in 24h = crowd piled in
MIN_QV_24H = 2_000_000    # $2M/day so the seat can get out
STABLE = {"USDC", "FDUSD", "TUSD", "USDP", "DAI", "BUSD", "EUR", "USD1",
          "USDE", "XUSD", "WBTC", "WBETH", "BFUSD", "PAXG", "USDS", "RLUSD"}


def _ok_symbol(t: dict) -> bool:
    s = t.get("symbol", "")
    if not s.endswith("USDT") or s == "BTCUSDT":
        return False
    base = s[:-4]
    if base in STABLE or base.endswith("UP") or base.endswith("DOWN"):
        return False
    try:
        return float(t.get("quoteVolume") or 0) >= MIN_QV_24H
    except Exception:
        return False


def features(k1h: list[list]) -> dict | None:
    """From >= 168 hourly candles (oldest first, last one may be open):
    v24, pos24, r24. Uses CLOSED candles only."""
    if not k1h or len(k1h) < 169:
        return None
    rows = k1h[:-1] if len(k1h) >= 170 else k1h   # drop the open candle
    rows = rows[-168:]
    try:
        c = [float(r[4]) for r in rows]
        h = [float(r[2]) for r in rows]
        lo = [float(r[3]) for r in rows]
        qv = [float(r[7]) for r in rows]
    except Exception:
        return None
    prior = sum(qv[:-24]) / 6.0
    v24 = sum(qv[-24:]) / prior if prior > 0 else 0.0
    hi24, lo24 = max(h[-24:]), min(lo[-24:])
    rng = hi24 - lo24
    pos24 = (c[-1] - lo24) / rng if rng > 0 else 0.0
    r24 = c[-1] / c[-25] - 1 if c[-25] > 0 else 0.0
    return {"v24": round(v24, 3), "pos24": round(pos24, 3),
            "r24": round(r24, 4), "close": c[-1]}


def btc_24h(k1h: list[list]) -> float | None:
    f = features(k1h)
    return None if f is None else f["r24"]


def oi_change_24h(symbol: str) -> float | None:
    d = binance_data._fget("/futures/data/openInterestHist",
                           {"symbol": symbol, "period": "1h", "limit": 25},
                           weight=1)
    if not isinstance(d, list) or len(d) < 25:
        return None
    try:
        a, b = float(d[0]["sumOpenInterest"]), float(d[-1]["sumOpenInterest"])
        return b / a - 1 if a > 0 else None
    except Exception:
        return None


def candidates(now: datetime | None = None, *, tickers=None, klines=None,
               funding=None, oi_chg=None, write: bool = True) -> list[dict]:
    """Ranked surge candidates, best first. Every one returned passed every
    filter, so `actionable` is True by construction. Keyword args exist for
    tests; live calls use the public endpoints."""
    now = now or datetime.now(timezone.utc)
    tickers = tickers if tickers is not None else binance_data.all_tickers_24h()
    klines = klines or binance_data.klines
    if not tickers:
        return []
    uni = sorted((t for t in tickers if _ok_symbol(t)),
                 key=lambda t: -float(t.get("quoteVolume") or 0))[:UNIVERSE_N]
    # cheap pre-filter on the ticker's own 24h change before any candle call
    short = []
    for t in uni:
        try:
            chg = float(t["priceChangePercent"]) / 100.0
        except Exception:
            continue
        if R24_MIN - 0.01 <= chg <= R24_MAX + 0.02:
            short.append(t["symbol"])
    btc = btc_24h(klines("BTCUSDT", "1h", 170))
    out, skipped = [], []
    if btc is None or btc < BTC24_MIN:
        why = f"BTC 24h {btc:+.1%} below {BTC24_MIN:+.0%}" if btc is not None \
            else "BTC candles unavailable"
        _write(now, [], {"btc_24h": btc, "why": why, "shortlist": len(short)},
               write)
        return []
    fund = funding if funding is not None else binance_data.funding_extremes()
    for s in short:
        f = features(klines(s, "1h", 170))
        if not f:
            continue
        why = None
        if f["v24"] < V24_MIN:
            why = f"v24 {f['v24']:.2f} < {V24_MIN}"
        elif f["pos24"] < POS24_MIN:
            why = f"pos24 {f['pos24']:.2f} < {POS24_MIN}"
        elif not (R24_MIN < f["r24"] < R24_MAX):
            why = f"r24 {f['r24']:+.1%} outside {R24_MIN:.0%}..{R24_MAX:.0%}"
        elif fund.get(s, 0.0) > FUNDING_MAX:
            why = f"funding {fund[s]:+.4%} > {FUNDING_MAX:+.2%}"
        if why is None and s in fund:
            oc = oi_chg(s) if oi_chg else oi_change_24h(s)
            f["oi_chg_24h"] = oc
            if oc is not None and oc > OI_CHG_MAX:
                why = f"OI +{oc:.0%} in 24h > {OI_CHG_MAX:.0%}"
        f["funding"] = fund.get(s)
        if why:
            skipped.append({"symbol": s, "why": why})
            continue
        score = round(min(f["v24"], 6.0) / 6.0 * f["pos24"], 4)
        out.append({"symbol": s, "signal": "surge", "score": score,
                    "actionable": True, "price": f["close"],
                    "why": (f"v24 {f['v24']:.1f}x, top {100 - f['pos24'] * 100:.0f}% "
                            f"of range, r24 {f['r24']:+.1%}, BTC {btc:+.1%}"),
                    **{k: f[k] for k in ("v24", "pos24", "r24",
                                         "funding", "oi_chg_24h") if k in f}})
    out.sort(key=lambda c: -c["score"])
    _write(now, out, {"btc_24h": btc, "shortlist": len(short),
                      "skipped": skipped[:40]}, write)
    return out


def _write(now, cands, extra, write):
    if not write:
        return
    doc = {"ts": now.isoformat(timespec="seconds"), "candidates": cands,
           "note": "SURGE lane (2026-09-05). Ranked opinion; the book decides.",
           **extra}
    try:
        SIGNALS.write_text(json.dumps(doc, indent=1), encoding="utf-8")
        if cands:
            with LOG.open("a", encoding="utf-8") as fh:
                for c in cands:
                    fh.write(json.dumps({"ts": doc["ts"], **c}) + "\n")
    except Exception as e:
        print(f"[surge] write failed: {e}")


if __name__ == "__main__":
    for c in candidates():
        print(c["symbol"], c["score"], c["why"])
