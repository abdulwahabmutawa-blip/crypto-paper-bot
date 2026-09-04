"""Small-wins lab — a 7-day PAPER study (owner request 2026-09-04).

Question: is there a "many small wins a day" protocol (target +1..+5% per
coin, many coins, never idle) whose hit rate clears its break-even NET of
costs? Pre-study on the last two weeks (1h candles, 7 tactics) said no:
every tactic hit below break-even. This lab runs the same question live,
at 15-minute precision, on a wide grid, so the answer at the end of the
week rests on a real forward record and not on a backtest.

Pre-registered (read before looking at results):
  * Cost per round trip: 0.25% (0.075% x 2 fees + ~0.1% spread/slippage).
  * A tactic PASSES only if, over >= 5 UTC days and >= 60 resolved trades,
    its hit rate beats break-even (stop+cost)/(target+stop) by >= 5 points
    AND its mean net return is positive AND its worst day is > -3 units.
  * One paper position per (coin, tactic) at a time; unit stake = 1.
  * Entries at the close of the 15m candle that fired; exits at the target
    or stop level when a later candle's high/low touches it (STOP FIRST if
    both touch in one candle), else at the close of the max-hold candle.
  * No LLM, no keys, no orders. Observation only. Runs in the Actions
    fleet loop (~13 min cadence) via bot.yml.

Outputs: data/smallwins_state.json (open + resolved), reports/smallwins.md
(scoreboard), docs/smallwins.md (published copy).
"""
from __future__ import annotations

import json
import statistics
import sys
from datetime import datetime, timezone, timedelta

import config
import binance_data

STATE = config.DATA / "smallwins_state.json"
REPORT = config.ROOT / "reports" / "smallwins.md"
COST = 0.0025
UNIVERSE_N = 150
STABLES = {"USDC", "FDUSD", "TUSD", "DAI", "EUR", "USDP", "BUSD", "USD1",
           "USDE", "XUSD", "EURI", "AEUR"}
BAD_SUFFIX = ("UP", "DOWN", "BULL", "BEAR")
MAX_RESOLVED_KEEP = 20000

# (target, stop, max_hold_h) grid applied to every shape
GRID = [(0.01, 0.01, 6), (0.015, 0.015, 8), (0.02, 0.02, 8),
        (0.015, 0.01, 8), (0.03, 0.02, 12),
        # owner 2026-09-04: "+3% and more" cells (two-week backtest: all
        # within a few points of break-even; forward record decides)
        (0.03, 0.03, 24), (0.03, 0.04, 48), (0.05, 0.03, 48), (0.04, 0.02, 24)]

# entry SHAPES on 15m features (F) — see features()
SHAPES = {
    "dip_large":   dict(tier=(0, 40),   f=lambda F: F["r1h"] <= -0.02 and F["btc24"] > -0.01),
    "dip_mid":     dict(tier=(40, 150), f=lambda F: F["r1h"] <= -0.03 and F["btc24"] > -0.01),
    "range_bottom": dict(tier=(0, 60),  f=lambda F: F["rp24"] <= 0.15 and F["r24"] > -0.06),
    "momentum":    dict(tier=(0, 150),  f=lambda F: 0.02 <= F["r4h"] < 0.04 and F["v4h"] >= 2 and F["rp24"] >= 0.7),
    "ignition":    dict(tier=(0, 150),  f=lambda F: F["v4h"] >= 5 and abs(F["r1h"]) < 0.04 and F["tbs4h"] >= 0.6 and F["btc4"] < 0.01 and F["btc24"] < 0.02),
    "btc_lag":     dict(tier=(0, 40),   f=lambda F: F["btc1"] >= 0.01 and F["r1h"] < 0.003),
    "calm_dip":    dict(tier=(0, 40),   f=lambda F: F["r1h"] <= -0.015 and abs(F["btc4"]) < 0.005 and F["rng24"] < 0.06),
}


def _now():
    return datetime.now(timezone.utc)


def _load():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"created": _now().isoformat(timespec="seconds"), "open": [],
            "resolved": [], "runs": 0}


def _save(st):
    tmp = STATE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(st, indent=1), encoding="utf-8")
    tmp.replace(STATE)


def universe():
    t = binance_data.all_tickers_24h() or []
    rows = []
    for x in t:
        s = x.get("symbol", "")
        if not s.endswith("USDT"):
            continue
        base = s[:-4]
        if base in STABLES or any(base.endswith(b) for b in BAD_SUFFIX):
            continue
        try:
            qv = float(x.get("quoteVolume") or 0)
        except Exception:
            continue
        if qv >= 1_000_000:
            rows.append((s, qv))
    rows.sort(key=lambda r: -r[1])
    return [s for s, _ in rows[:UNIVERSE_N]]


def features(k15, btc15):
    """k15: last >= 100 closed 15m candles. Returns feature dict or None."""
    # 97 = 24h of closed candles + 1; the newest fetched candle is still open
    if len(k15) < 97 or len(btc15) < 97:
        return None
    cl = [float(c[4]) for c in k15]
    hi = [float(c[2]) for c in k15]
    lo = [float(c[3]) for c in k15]
    qv = [float(c[7]) for c in k15]
    tb = [float(c[10]) for c in k15]
    b = [float(c[4]) for c in btc15]
    i = len(cl) - 1
    base = statistics.median(qv[i - 96:i - 16]) or 1e-9          # 24h..4h ago
    v4 = sum(qv[i - 15:i + 1]) / 16 / base
    return {
        "px": cl[i],
        "r1h": cl[i] / cl[i - 4] - 1,
        "r4h": cl[i] / cl[i - 16] - 1,
        "r24": cl[i] / cl[i - 96] - 1,
        "v4h": v4,
        "tbs4h": sum(tb[i - 15:i + 1]) / max(1e-9, sum(qv[i - 15:i + 1])),
        "rp24": (cl[i] - min(lo[i - 96:i + 1])) / max(1e-9, max(hi[i - 96:i + 1]) - min(lo[i - 96:i + 1])),
        "rng24": max(hi[i - 96:i + 1]) / max(1e-9, min(lo[i - 96:i + 1])) - 1,
        "btc1": b[-1] / b[-5] - 1,
        "btc4": b[-1] / b[-17] - 1,
        "btc24": b[-1] / b[-97] - 1,
    }


def resolve(pos, k15):
    """Walk candles after entry; return (net_ret, how, hours) or None."""
    entry = pos["entry"]
    t_entry = pos["entry_ms"]
    deadline = t_entry + pos["max_h"] * 3600_000
    for c in k15:
        t = int(c[0])
        if t <= t_entry:
            continue
        hi, lo, cl, close_t = float(c[2]), float(c[3]), float(c[4]), int(c[6])
        if close_t > int(_now().timestamp() * 1000):
            break                                     # still-open candle
        if lo <= entry * (1 - pos["stop"]):
            return -pos["stop"] - COST, "STOP", (t - t_entry) / 3.6e6
        if hi >= entry * (1 + pos["target"]):
            return pos["target"] - COST, "TARGET", (t - t_entry) / 3.6e6
        if t >= deadline:
            return cl / entry - 1 - COST, "TIME", (t - t_entry) / 3.6e6
    return None


def breakeven(target, stop):
    return (stop + COST) / (target + stop)


def scoreboard(st):
    now = _now()
    by = {}
    for r in st["resolved"]:
        by.setdefault(r["tactic"], []).append(r)
    lines = [f"# Small-wins lab — paper study (owner request 2026-09-04)\n",
             f"updated {now.isoformat(timespec='seconds')} · runs {st.get('runs', 0)} · "
             f"open {len(st['open'])} · resolved {len(st['resolved'])} · cost {COST:.2%}/RT\n",
             "PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.\n",
             "| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    rows = []
    for tac, v in by.items():
        rets = [x["ret"] for x in v]
        days = {}
        for x in v:
            days[x["exit_ts"][:10]] = days.get(x["exit_ts"][:10], 0.0) + x["ret"]
        be = breakeven(v[0]["target"], v[0]["stop"])
        hit = sum(1 for x in rets if x > 0) / len(rets)
        mean = statistics.mean(rets)
        worst = min(days.values()) if days else 0.0
        ok = (len(days) >= 5 and len(v) >= 60 and hit >= be + 0.05 and mean > 0 and worst > -3.0)
        verdict = "PASS" if ok else ("watch" if (hit >= be and mean > 0) else "fail")
        rows.append((mean, f"| {tac} | {len(v)} | {len(days)} | {len(v)/max(1,len(days)):.1f} | {hit:.0%} | {be:.0%} | "
                           f"{mean*100:+.2f}% | {sum(1 for x in v if x['how']=='TARGET')/len(v):.0%} | "
                           f"{sum(1 for x in v if x['how']=='STOP')/len(v):.0%} | {sum(1 for x in v if x['how']=='TIME')/len(v):.0%} | "
                           f"{worst*100:+.1f}% | {verdict} |"))
    rows.sort(key=lambda r: -r[0])
    lines += [r[1] for r in rows] or ["| (no resolved trades yet) | | | | | | | | | | | |"]
    lines.append("\n_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); "
                 "worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, "
                 "no keys, no orders._\n")
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main():
    st = _load()
    now = _now()
    syms = universe()
    if not syms:
        print("[smallwins] no universe (ticker fetch failed) — skipping run")
        return 0
    btc15 = binance_data.klines("BTCUSDT", "15m", 120) or []
    if len(btc15) < 97:
        print("[smallwins] no BTC candles — skipping run")
        return 0
    tiers = {s: i for i, s in enumerate(syms)}
    open_keys = {(p["symbol"], p["tactic"]) for p in st["open"]}
    opened = 0
    resolved = 0
    cache = {}
    # resolve first (needs candles for held symbols), then look for entries
    need = set(p["symbol"] for p in st["open"]) | set(syms)
    for s in need:
        k = binance_data.klines(s, "15m", 120)
        if k:
            cache[s] = k
    still_open = []
    for p in st["open"]:
        k = cache.get(p["symbol"])
        r = resolve(p, k) if k else None
        if r is None:
            # give up on a position we cannot price for 48h (delisting etc.)
            if now.timestamp() * 1000 - p["entry_ms"] > 48 * 3600_000 and not k:
                continue
            still_open.append(p)
            continue
        ret, how, hrs = r
        st["resolved"].append({**p, "ret": round(ret, 5), "how": how,
                               "hours": round(hrs, 2),
                               "exit_ts": now.isoformat(timespec="seconds")})
        resolved += 1
    st["open"] = still_open
    open_keys = {(p["symbol"], p["tactic"]) for p in st["open"]}
    for s in syms:
        k = cache.get(s)
        if not k:
            continue
        # use only CLOSED candles for features
        closed = [c for c in k if int(c[6]) <= now.timestamp() * 1000]
        F = features(closed, btc15)
        if not F:
            continue
        tier = tiers[s]
        for shape, spec in SHAPES.items():
            lo_t, hi_t = spec["tier"]
            if not (lo_t <= tier < hi_t):
                continue
            try:
                fired = bool(spec["f"](F))
            except Exception:
                fired = False
            if not fired:
                continue
            for target, stop, max_h in GRID:
                tac = f"{shape}|t{target*100:g}|s{stop*100:g}|h{max_h}"
                if (s, tac) in open_keys:
                    continue
                st["open"].append({"symbol": s, "tactic": tac, "shape": shape,
                                   "target": target, "stop": stop, "max_h": max_h,
                                   "entry": F["px"], "entry_ms": int(closed[-1][6]),
                                   "entry_ts": now.isoformat(timespec="seconds"),
                                   "feat": {k2: round(v2, 5) for k2, v2 in F.items() if k2 != "px"}})
                open_keys.add((s, tac))
                opened += 1
    st["resolved"] = st["resolved"][-MAX_RESOLVED_KEEP:]
    st["runs"] = st.get("runs", 0) + 1
    st["updated"] = now.isoformat(timespec="seconds")
    _save(st)
    scoreboard(st)
    print(f"[smallwins] universe {len(syms)} · opened {opened} · resolved {resolved} · "
          f"open {len(st['open'])} · total resolved {len(st['resolved'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
