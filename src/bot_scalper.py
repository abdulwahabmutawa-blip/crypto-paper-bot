"""SCALPER — hyper-aggressive small-wins PAPER bot (owner request 2026-09-05).

$1,000 of PAPER capital, no keys, no orders. Built from the two studies that
were running when the owner asked for it:
  * small-wins lab (src/smallwins_lab.py, 979 resolved paper trades by
    09-05 12:00): every +1..2% target sits at break-even; the +3% cells with
    a 24-48h leash are the only ones with margin (+3/-3/24h: 68% hit,
    +0.83%/trade on 50; range_bottom shape +0.77%, 62% hit on 166).
  * 60-day tape (trading-research/, local): momentum near the 24h high on
    heavy volume, not yet exhausted, BTC not falling: +3/-3/24h first-touch
    62% hit, +0.54%/trade after cost; unfiltered 52%, -0.03%.

Protocol (pre-registered, judge on >= 100 round trips):
  * up to SEATS concurrent positions of equal size; freed cash is re-deployed
    the SAME cycle — the book is never idle while setups exist.
  * two entry shapes on 15m candles: SURGE (momentum with the crowd not yet
    in) and BOTTOM (range-bottom rebound). Either fires -> buy.
  * exit at +3% target or -3% stop, whichever a later candle touches first
    (STOP FIRST when both touch in one candle), else at the close 24h later.
  * cost 0.25% per round trip charged on every exit. Per-coin cooldown 2h
    after a stop. Marks: open seats at last close.
Runs in the Actions fleet loop (~13 min). Outputs data/scalper_state.json,
reports/scalper.md -> docs/scalper.md.
"""
from __future__ import annotations

import json
import statistics
import sys
from datetime import datetime, timezone

import config
import binance_data
import smallwins_lab as lab          # universe(), features(), resolve(), merge

STATE = config.DATA / "scalper_state.json"
REPORT = config.ROOT / "reports" / "scalper.md"
START_USD = 1000.0
SEATS = 10                 # concurrent positions
TARGET = 0.03
STOP = 0.03
MAX_H = 24
COST = lab.COST            # 0.25% per round trip
COOLDOWN_H = 2.0
MAX_TRADES_KEEP = 20000

# entry shapes on the lab's 15m feature dict
SHAPES = {
    "surge": lambda F: (F["v4h"] >= 2.0 and F["rp24"] >= 0.70
                        and 0.01 <= F["r4h"] <= 0.06 and 0.01 <= F["r24"] <= 0.20
                        and F["btc24"] > -0.02),
    "bottom": lambda F: (F["rp24"] <= 0.15 and F["r24"] > -0.06
                         and F["btc24"] > -0.02),
}


def _now():
    return datetime.now(timezone.utc)


def _load():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"created": _now().isoformat(timespec="seconds"), "cash": START_USD,
            "open": [], "trades": [], "cooldown": {}, "runs": 0}


def _key(p):
    return (p.get("symbol"), p.get("entry_ms"))


def merge_states(a, b):
    """Union, same guard as the lab (a stale checkout must not erase
    trades). Cash is re-derived: START - open stakes + realized P&L."""
    tr = {}
    for st in (a, b):
        for r in st.get("trades", []):
            tr.setdefault(_key(r), r)
    opn = {}
    for st in (a, b):
        for p in st.get("open", []):
            if _key(p) not in tr:
                opn.setdefault(_key(p), p)
    trades = sorted(tr.values(), key=lambda r: r.get("exit_ts", ""))
    open_ = list(opn.values())
    cash = START_USD + sum(r["pnl_usd"] for r in trades) - sum(p["stake"] for p in open_)
    cd = {**a.get("cooldown", {}), **b.get("cooldown", {})}
    return {"created": min(a.get("created") or "9", b.get("created") or "9"),
            "cash": round(cash, 4), "open": open_, "trades": trades,
            "cooldown": cd, "runs": max(a.get("runs", 0), b.get("runs", 0)),
            "updated": max(a.get("updated", ""), b.get("updated", ""))}


def _remote_state():
    import subprocess
    try:
        subprocess.run(["git", "fetch", "-q", "origin", "main"], timeout=40,
                       check=True, capture_output=True)
        out = subprocess.run(["git", "show", "origin/main:data/scalper_state.json"],
                             timeout=20, check=True, capture_output=True)
        return json.loads(out.stdout.decode("utf-8"))
    except Exception:
        return None


def _save(st):
    tmp = STATE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(st, indent=1), encoding="utf-8")
    tmp.replace(STATE)


def equity(st, marks: dict) -> float:
    eq = st["cash"]
    for p in st["open"]:
        px = marks.get(p["symbol"], p["entry"])
        eq += p["stake"] * (px / p["entry"])
    return eq


def report(st, marks):
    now = _now()
    tr = st["trades"]
    eq = equity(st, marks)
    lines = [f"# Scalper — hyper-aggressive small-wins PAPER bot\n",
             f"updated {now.isoformat(timespec='seconds')} · runs {st.get('runs', 0)} · "
             f"equity **${eq:,.2f}** ({(eq / START_USD - 1) * 100:+.2f}%) · cash ${st['cash']:,.2f} · "
             f"open {len(st['open'])}/{SEATS} · round trips {len(tr)}\n",
             f"Rule: {SEATS} seats, +{TARGET:.0%} target / -{STOP:.0%} stop / {MAX_H}h, cost {COST:.2%}/RT, "
             f"shapes surge + bottom on 15m candles. Judge on >= 100 round trips.\n"]
    if tr:
        rets = [r["ret"] for r in tr]
        hit = sum(1 for x in rets if x > 0) / len(rets)
        be = lab.breakeven(TARGET, STOP)
        days = {}
        for r in tr:
            days[r["exit_ts"][:10]] = days.get(r["exit_ts"][:10], 0.0) + r["pnl_usd"]
        lines += [f"- hit {hit:.0%} (break-even {be:.0%}) · mean {statistics.mean(rets) * 100:+.2f}%/trade · "
                  f"realized ${sum(r['pnl_usd'] for r in tr):+,.2f} · worst day ${min(days.values()):+,.2f} · "
                  f"trades/day {len(tr) / max(1, len(days)):.1f}",
                  "", "| shape | n | hit | mean | target% | stop% | time% |", "|---|---|---|---|---|---|---|"]
        for sh in SHAPES:
            v = [r for r in tr if r["shape"] == sh]
            if not v:
                continue
            lines.append(f"| {sh} | {len(v)} | {sum(1 for r in v if r['ret'] > 0) / len(v):.0%} | "
                         f"{statistics.mean(r['ret'] for r in v) * 100:+.2f}% | "
                         f"{sum(1 for r in v if r['how'] == 'TARGET') / len(v):.0%} | "
                         f"{sum(1 for r in v if r['how'] == 'STOP') / len(v):.0%} | "
                         f"{sum(1 for r in v if r['how'] == 'TIME') / len(v):.0%} |")
        lines += ["", "## Last 15 round trips", "| exit (UTC) | coin | shape | how | hours | net | P&L |",
                  "|---|---|---|---|---|---|---|"]
        for r in tr[-15:][::-1]:
            lines.append(f"| {r['exit_ts'][:16]} | {r['symbol']} | {r['shape']} | {r['how']} | "
                         f"{r['hours']:.1f} | {r['ret'] * 100:+.2f}% | ${r['pnl_usd']:+.2f} |")
    if st["open"]:
        lines += ["", "## Open seats", "| entry (UTC) | coin | shape | entry | mark | unrealized |", "|---|---|---|---|---|---|"]
        for p in st["open"]:
            px = marks.get(p["symbol"], p["entry"])
            lines.append(f"| {p['entry_ts'][:16]} | {p['symbol']} | {p['shape']} | {p['entry']:g} | {px:g} | "
                         f"{(px / p['entry'] - 1) * 100:+.2f}% |")
    lines.append("\n_Paper only. $1,000 start, equal stakes = cash / free seats at entry. "
                 "Entries at the close of the 15m candle that fired; exits on the first later candle touching "
                 "target or stop (stop first if both), else the 24h close._\n")
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main():
    st = _load()
    remote = _remote_state()
    if remote:
        st = merge_states(st, remote)
    now = _now()
    now_ms = int(now.timestamp() * 1000)
    syms = lab.universe()
    if not syms:
        print("[scalper] no universe — skipping run")
        return 0
    btc15 = binance_data.klines("BTCUSDT", "15m", 120) or []
    if len(btc15) < 97:
        print("[scalper] no BTC candles — skipping run")
        return 0
    cache = {}
    for s in set(p["symbol"] for p in st["open"]) | set(syms):
        k = binance_data.klines(s, "15m", 120)
        if k:
            cache[s] = k
    marks = {s: float(k[-1][4]) for s, k in cache.items()}
    # 1) resolve open seats
    still = []
    closed_n = 0
    for p in st["open"]:
        k = cache.get(p["symbol"])
        r = lab.resolve({**p, "target": TARGET, "stop": STOP, "max_h": MAX_H}, k) if k else None
        if r is None:
            if now_ms - p["entry_ms"] > 48 * 3600_000 and not k:
                st["cash"] += p["stake"]          # unpriceable for 2 days: return stake, no P&L
                continue
            still.append(p)
            continue
        ret, how, hrs = r
        pnl = round(p["stake"] * ret, 4)
        st["cash"] = round(st["cash"] + p["stake"] + pnl, 4)
        st["trades"].append({**p, "ret": round(ret, 5), "how": how, "hours": round(hrs, 2),
                             "pnl_usd": pnl, "exit_ts": now.isoformat(timespec="seconds")})
        if how == "STOP":
            st["cooldown"][p["symbol"]] = now_ms
        closed_n += 1
    st["open"] = still
    # 2) fill every free seat this cycle
    st["cooldown"] = {s: t for s, t in st.get("cooldown", {}).items()
                      if now_ms - t < COOLDOWN_H * 3600_000}
    held = {p["symbol"] for p in st["open"]}
    cands = []
    for s in syms:
        if s in held or s in st["cooldown"]:
            continue
        k = cache.get(s)
        if not k:
            continue
        closed = [c for c in k if int(c[6]) <= now_ms]
        F = lab.features(closed, btc15)
        if not F:
            continue
        for sh, f in SHAPES.items():
            try:
                if f(F):
                    cands.append((F["v4h"] if sh == "surge" else 1.0 / max(F["rp24"], 0.01),
                                  s, sh, F, int(closed[-1][6])))
                    break
            except Exception:
                pass
    cands.sort(key=lambda c: -c[0])
    opened = 0
    for _, s, sh, F, ems in cands:
        free = SEATS - len(st["open"])
        if free <= 0 or st["cash"] < 5:
            break
        stake = round(st["cash"] / free, 4)
        st["cash"] = round(st["cash"] - stake, 4)
        st["open"].append({"symbol": s, "shape": sh, "entry": F["px"], "entry_ms": ems,
                           "entry_ts": now.isoformat(timespec="seconds"), "stake": stake,
                           "feat": {k2: round(v2, 5) for k2, v2 in F.items() if k2 != "px"}})
        opened += 1
    st["trades"] = st["trades"][-MAX_TRADES_KEEP:]
    st["runs"] = st.get("runs", 0) + 1
    st["updated"] = now.isoformat(timespec="seconds")
    st["equity"] = round(equity(st, marks), 4)
    st["last_value_usd"] = st["equity"]
    st["last_updated_utc"] = st["updated"]
    _save(st)
    report(st, marks)
    print(f"[scalper] equity ${st['equity']:,.2f} · cash ${st['cash']:,.2f} · opened {opened} · "
          f"closed {closed_n} · open {len(st['open'])}/{SEATS} · trades {len(st['trades'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
