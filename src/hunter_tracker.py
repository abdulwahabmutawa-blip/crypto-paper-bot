"""The Hunter — cross-asset opportunist, the fleet's aggressive risk-taker.

Rule (mechanical, lab config L20/T8 — see hunter_lab.py grid):
  * Universe: 3x equity ETFs, high-beta stocks, crypto majors, commodities.
  * Score EVERYTHING every cycle: 20-day momentum / 20-day volatility —
    reward per unit of risk. ALL-IN on the top scorer.
  * Switch only when a challenger scores 1.25x the current holding (hysteresis
    kills churn), or the holding's score turns negative.
  * TRAILING STOP 8% from the high-water mark — winners run, reversals cut.
  * Cash only when every score on the board is negative, or the Watcher
    calls SEVERE. Aggression with a seatbelt, not without one.
Benchmark: SPY. Backtest: +100%/yr since 2017 but -78% max drawdown and it
LAGGED SPY in the 2024+ chop — the cost of aggression, on the label.
PAPER MONEY ONLY. Not investment advice.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import yfinance as yf

import config
import sentinel_gate
import market_hours
import risk_common

UNIVERSE = ["TQQQ", "SOXL", "UPRO", "NVDA", "TSLA", "MSTR", "COIN", "PLTR",
            "BTC-USD", "ETH-USD", "SOL-USD", "USO", "GLD", "SLV"]
BENCH = "SPY"
LOOK, TRAIL, HYST = 20, 0.08, 1.25
# Audit 2026-08-05: both trailing stops re-bought the SAME ticker the SAME
# day at the SAME price — the stop protected nothing. A stopped ticker now
# cools off before this bot may touch it again.
STOP_COOLDOWN_DAYS = 5
START_CASH = 1000.0
KEY = "hunter"
STATE = config.DATA / f"{KEY}_state.json"
NAMES = {"TQQQ": "3x Nasdaq", "SOXL": "3x Semis", "UPRO": "3x S&P",
         "NVDA": "Nvidia", "TSLA": "Tesla", "MSTR": "MicroStrategy",
         "COIN": "Coinbase", "PLTR": "Palantir", "BTC-USD": "Bitcoin",
         "ETH-USD": "Ethereum", "SOL-USD": "Solana", "USO": "Oil",
         "GLD": "Gold", "SLV": "Silver"}


def fetch() -> pd.DataFrame:
    raw = yf.download(sorted(set(UNIVERSE) | {BENCH}), period="6mo",
                      auto_adjust=True, progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    close = market_hours.trim_incomplete_bars(close.dropna(how="all"))
    # both frames: filled for signals, raw for dating marks honestly
    return close.ffill(), close


def main():
    now = datetime.now(timezone.utc)
    today = str(now.date())
    close, rawc = fetch()
    last = close.iloc[-1]

    mom = close[UNIVERSE].pct_change(LOOK).iloc[-1]
    vol = close[UNIVERSE].pct_change().rolling(LOOK).std().iloc[-1]
    score = (mom / vol.replace(0, np.nan)).dropna()

    st = json.loads(STATE.read_text()) if STATE.exists() else None
    if st is None:
        st = {"created": today, "starting_cash": START_CASH, "holding": "CASH",
              "units": 0.0, "cash": START_CASH, "high_water": None,
              "bench_units": START_CASH / float(last[BENCH]),
              "trades": [], "history": [], "intraday": []}
        print(f"[{KEY}] NEW sim {today}")

    # Guard (audit 2026-08-05): never act while the held ticker has no price.
    if st["holding"] != "CASH" and (st["holding"] not in close.columns
                                    or pd.isna(last[st["holding"]])):
        print(f"[{KEY}] held ticker {st['holding']} has no price this cycle — "
              f"cycle skipped (never trade or mark on a dead column)")
        return

    def sell(reason):
        p = float(last[st["holding"]])
        gross = st["units"] * p
        f = risk_common.fee(st["holding"], gross)
        st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
        st["trades"].append({"date": today, "action": "SELL",
                             "ticker": st["holding"], "price": round(p, 8),
                             "units": round(st["units"], 4),
                             "value": round(gross, 2), "fee": round(f, 2),
                             "reason": reason})
        # Fleet review 2026-08-10: EVERY exit starts the cooldown clock, not
        # just stop-outs — the ledger's 2nd-biggest loss (-$62.92) was a
        # next-day rebuy of USO at 7.8% ABOVE its own "Outgunned" exit price.
        st["stopped"] = {"ticker": st["holding"], "date": today}
        st["cash"], st["holding"], st["units"] = gross - f, "CASH", 0.0
        st["high_water"] = None

    import market_hours

    # 1) trailing stop (high-water follows price up, never down; the sell
    #    itself waits until the holding's market can actually fill it).
    #    A stop-out starts the cooldown clock for that ticker.
    if st["holding"] != "CASH" and st["holding"] in close.columns:
        p = float(last[st["holding"]])
        st["high_water"] = max(st["high_water"] or p, p)
        if p / st["high_water"] - 1 <= -TRAIL \
                and market_hours.can_fill(st["holding"]):
            sell(f"TRAILING STOP — fell {TRAIL:.0%} from its high-water mark")

    # 2) Watcher severe gate (surface silence — a stale Watcher is not calm)
    gate_state, gate_detail = sentinel_gate.status()
    if gate_state != "ok":
        print(f"[{KEY}] WATCHER {gate_state.upper()}: {gate_detail}")
    is_severe, why = sentinel_gate.severe()
    if is_severe and st["holding"] != "CASH" \
            and market_hours.can_fill(st["holding"]):
        sell(why + " — hunter stands down in a crisis")

    # 2.5) R1 kill floor, code-enforced (audit 2026-08-05: this bot was 13.5%
    #      above the floor with nothing automated that would liquidate it)
    r1_hit = False
    cur_val = st["cash"] if st["holding"] == "CASH" \
        else st["units"] * float(last[st["holding"]])
    if not st.get("frozen") and risk_common.r1_breached(cur_val):
        r1_hit = True
        print(f"[{KEY}] {risk_common.r1_reason(cur_val)}")
        if st["holding"] != "CASH" and market_hours.can_fill(st["holding"]):
            sell(risk_common.r1_reason(cur_val))
        if st["holding"] == "CASH":
            st["frozen"] = {"date": today,
                            "rule": "R1 kill floor (kill_criteria.md)"}
            print(f"[{KEY}] book FROZEN — un-freezing is a human decision")

    # 3) hunt: decide the best bet
    top = score.idxmax() if len(score) else None
    desired = st["holding"]
    if st.get("frozen") or r1_hit or is_severe or top is None or score[top] <= 0:
        desired = "CASH"
    elif st["holding"] == "CASH":
        desired = top
    elif top != st["holding"]:
        cur = score.get(st["holding"], np.nan)
        if np.isnan(cur) or cur <= 0 or score[top] > HYST * cur:
            desired = top

    # 3.5) exit cooldown: a ticker exited for ANY reason is untouchable for
    #      STOP_COOLDOWN_DAYS — take the next-best positive score instead.
    stop = st.get("stopped") or {}
    if desired not in ("CASH",) and desired == stop.get("ticker"):
        days = (pd.Timestamp(today) - pd.Timestamp(stop["date"])).days
        if days < STOP_COOLDOWN_DAYS:
            if st["holding"] != "CASH":
                # holding a live seat: keep it — substituting the next-best
                # name here would switch seats without the 1.25x hysteresis
                # bar and record a false "Outgunned" reason for it
                print(f"[{KEY}] {desired} exited {days}d ago — cooling off "
                      f"({STOP_COOLDOWN_DAYS}d); keeping {st['holding']}")
                desired = st["holding"]
            else:
                ranked = sorted(score.index, key=lambda x: -score[x])
                alt = next((t for t in ranked
                            if t != desired and float(score[t]) > 0), None)
                print(f"[{KEY}] {desired} exited {days}d ago — cooling off "
                      f"({STOP_COOLDOWN_DAYS}d); taking {alt or 'CASH'} instead")
                desired = alt or "CASH"
        else:
            st.pop("stopped", None)

    sell_ok = st["holding"] == "CASH" or market_hours.can_fill(st["holding"])
    buy_ok = desired == "CASH" or market_hours.can_fill(desired)
    if desired != st["holding"] and not (sell_ok and buy_ok):
        print(f"[{KEY}] switch {st['holding']} -> {desired} deferred — "
              f"US market closed, will fill at the open")
    if desired != st["holding"] and sell_ok and buy_ok:
        if st["holding"] != "CASH":
            sell(f"Outgunned — {NAMES.get(desired, desired)} now scores "
                 f">{HYST}x better on reward/risk")
        if desired != "CASH":
            p = float(last[desired])
            f = risk_common.fee(desired, st["cash"])
            invest = st["cash"] - f
            st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
            st["units"], st["cash"] = invest / p, 0.0
            st["holding"], st["high_water"] = desired, p
            st["trades"].append({"date": today, "action": "BUY",
                                 "ticker": desired, "price": round(p, 8),
                                 "units": round(st["units"], 4),
                                 "value": round(invest, 2), "fee": round(f, 2),
                                 "reason": f"Top reward/risk score "
                                           f"({score[desired]:.2f}) — "
                                           f"{NAMES.get(desired, desired)}, all-in"})

    # 4) mark to market
    val = st["cash"] if st["holding"] == "CASH" else st["units"] * float(last[st["holding"]])
    bench = st["bench_units"] * float(last[BENCH])
    # Date the mark by the asset that determines its value, not by the wall
    # clock: the feed serves stale/undelivered bars and a mark must be filed
    # under the session it actually reflects.
    priced = BENCH if st["holding"] == "CASH" else st["holding"]
    asof = market_hours.last_real_date(rawc, priced) or str(now.date())
    bench_asof = market_hours.last_real_date(rawc, BENCH)
    newest = st["history"][-1]["date"] if st["history"] else ""
    if asof < newest:
        print(f"[{KEY}] STALE BAR {asof} < newest mark {newest} — "
              f"mark skipped (feed served an old bar)")
    else:
        row = {"date": asof, "value": round(val, 2),
               "bench": round(bench, 2), "holding": st["holding"]}
        if bench_asof and bench_asof != asof:
            # the bench was forward-filled to reach this row; label it rather
            # than let a fabricated comparison look like a measured one
            row["bench_asof"] = bench_asof
        st["history"] = sorted([h for h in st["history"] if h["date"] != asof]
                               + [row], key=lambda h: h["date"])
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    st["intraday"] = [x for x in st.get("intraday", [])
                      if x["ts"] != st["last_updated_utc"]][-1499:] + [
        {"ts": st["last_updated_utc"], "value": round(val, 2),
         "bench": round(bench, 2), "holding": st["holding"]}]
    STATE.write_text(json.dumps(st, indent=2))

    # 5) dashboard
    board = []
    for t in sorted(score.index, key=lambda x: -score[x])[:10]:
        s = float(score[t])
        board.append({
            "sym": t.replace("-USD", ""), "price": round(float(last[t]), 2),
            "line": f"{NAMES.get(t, t)} · score {s:+.2f} · "
                    f"mom{LOOK} {float(mom[t])*100:+.1f}%",
            "tag": "HELD" if t == st["holding"] else
                   ("hunting" if s > 0 else "falling"),
            "on": s > 0, "pick": t == st["holding"],
            "fill": max(-50, min(50, s * 15)),
        })
    payload = {
        "generated_utc": st["last_updated_utc"], "created": st["created"],
        "starting_cash": START_CASH, "live_ts": st["last_updated_utc"],
        "current": st["history"][-1], "board": board,
        "board_title": "The whole market, scored by reward-per-unit-of-risk",
        "meta": {
            "title": "The Hunter — $1,000 Challenge",
            "badge": "PAPER SIM · MAXIMUM AGGRESSION",
            "bench_label": "SPY benchmark ($1,000 same day)",
            "board_note": "Always hunting across leveraged ETFs, high-beta "
                          "stocks, crypto and commodities — all-in on the "
                          "best score, 8% trailing stop, cash only when "
                          "everything falls. Aggression with a seatbelt.",
        },
        "intraday": st["intraday"], "trades": st["trades"][-20:],
        "history": st["history"],
        "costs_paid": st.get("costs_paid", 0.0),
        "frozen": st.get("frozen"),
        "thoughts": (
            (f"I'm all-in on {st['holding'].replace('-USD', '')} — right now it has the "
             f"best combination of 'going up' and 'not too wild' of the 14 things "
             f"I watch. My safety net: if it drops "
             f"{TRAIL:.0%} from its recent high of ${st['high_water']:,.2f} "
             f"(that's ${st['high_water'] * (1 - TRAIL):,.2f}), I sell instantly, no "
             f"questions asked. I only switch to something else if it looks clearly "
             f"better than what I hold — not just slightly better."
             if st["holding"] != "CASH" and st.get("high_water") else
             "I'm in cash. Everything I watch is falling, or the Watcher called a "
             "crisis — either way, an aggressive bot with no seatbelt dies fast, "
             "so I hunt only when something is actually rising.")),
        "strategy": {
            "name": "The Hunter — cross-asset opportunist",
            "rule": "Score 14 instruments by 20-day momentum/volatility; "
                    "all-in on the best (1.25x hysteresis); 8% trailing stop; "
                    "cash only if every score is negative or Watcher SEVERE",
            "backtest_cagr": "+100%/yr since 2017 · but LAGGED SPY in 2024+ chop",
            "backtest_maxdd": "-78% — the honest price of maximum aggression",
        },
    }
    (config.REPORTS / f"{KEY}_dashboard_data.json").write_text(
        json.dumps(payload, indent=2))
    template = (config.ROOT / "src" / "fleet_dashboard_template.html").read_text(
        encoding="utf-8")
    (config.REPORTS / f"{KEY}_dashboard.html").write_text(
        template.replace("/*__DATA__*/", json.dumps(payload)).replace(
            "__DATAFILE__", f"{KEY}_dashboard_data.json"), encoding="utf-8")
    print(f"[{KEY}] {today} holding {st['holding']} value ${val:,.2f} "
          f"vs SPY ${bench:,.2f} | top scores: "
          + ", ".join(f"{t.replace('-USD','')} {score[t]:+.2f}"
                      for t in sorted(score.index, key=lambda x: -score[x])[:3]))


if __name__ == "__main__":
    main()
