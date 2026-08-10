"""Congress Copier — LIVE $1,000 paper sim, bot picks whom to copy.

Self-deciding rule, re-evaluated every cycle from the public disclosure feed:
  * FOLLOW list = every member of Congress with >= MIN_SCORED scored buys AND
    positive average excess return vs the market (from returns.json). Purely
    data-driven — members enter/leave the list as their record changes.
  * When a followed member files a NEW stock BUY (filing date on/after this
    sim's start), buy a fixed $ slot at the current market price.
  * Each position is held HOLD_DAYS, then sold at market. Cash earns nothing.
  * Benchmark: $1,000 of SPY bought on day one.

Data: kadoa-org/congress-trading-monitor public JSON (filings + filer scores).
PAPER MONEY ONLY. Not investment advice.
"""
from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

import config
import market_hours
import risk_common

STATE = config.DATA / "congress_state.json"
BASE = ("https://raw.githubusercontent.com/kadoa-org/"
        "congress-trading-monitor/main/public/data/")
BENCH = "SPY"
START_CASH = 1000.0
SLOT = 100.0          # $ per copied trade
HOLD_DAYS = 90
MIN_SCORED = 10       # follow threshold: enough history to judge


def fetch_json(name):
    with urllib.request.urlopen(BASE + name, timeout=60) as r:
        return json.load(r)


def build_follow_list() -> dict:
    """{filer_id: {name, excess_pct, buys}} for positive-alpha members."""
    rows = fetch_json("returns.json")
    out = {}
    for r in rows:
        if (r.get("branch") == "congress" and (r.get("scored_buys") or 0) >= MIN_SCORED
                and (r.get("avg_excess") or 0) > 0):
            out[r["id"]] = {"name": r["full_name"],
                            "excess_pct": round(r["avg_excess"] / 100, 2),
                            "buys": r["scored_buys"]}
    return out


def fresh_buy_filings(since: str) -> list:
    """New BUY filings with real tickers from the live feed."""
    recs = fetch_json("trades.json")
    out = []
    for t in recs:
        tt = str(t.get("transaction_type", "")).lower()
        tick = str(t.get("ticker") or "").strip().upper()
        if ("purchase" not in tt and "buy" not in tt):
            continue
        if not tick or not tick.isalpha() or len(tick) > 6:
            continue
        if str(t.get("branch")) != "congress":
            continue
        if str(t.get("filing_date") or "") < since:
            continue
        out.append({"id": t["id"], "filer_id": t.get("filer_id"),
                    "filer": t.get("filer_name"), "ticker": tick,
                    "filing_date": t.get("filing_date"),
                    "amount": t.get("amount_range_label")})
    return out


def quotes(tickers):
    """Returns (prices, asof) — asof is the date of the BAR the prices came
    from, not today's date. The caller needs it: the feed intermittently
    serves a one-day-stale bar, and a mark must be filed under the date it
    actually belongs to."""
    tickers = sorted(set(tickers) | {BENCH})
    raw = yf.download(tickers, period="5d", auto_adjust=True, progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    if isinstance(close, pd.Series):
        close = close.to_frame(tickers[0])
    close = market_hours.trim_incomplete_bars(close).ffill()
    last = close.iloc[-1]
    return ({t: float(last[t]) for t in tickers
             if t in close.columns and pd.notna(last[t])},
            str(close.index[-1].date()))


def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else None


def main():
    now = datetime.now(timezone.utc)
    today = str(now.date())

    follow = build_follow_list()
    st = load_state()
    if st is None:
        px, _ = quotes([])
        st = {"created": today, "starting_cash": START_CASH, "cash": START_CASH,
              "positions": [], "seen": [], "trades": [], "history": [],
              "bench_units": START_CASH / px[BENCH]}
        print(f"[congress] NEW sim {today} — following {len(follow)} members")

    filings = fresh_buy_filings(since=st["created"])
    new = [f for f in filings if f["id"] not in st["seen"]
           and f["filer_id"] in follow]
    # Fleet review 2026-08-10: this was the only tracker outside the fleet's
    # iron-rule module — fee-free fills and no code-enforced R1 floor. Wired
    # to risk_common below; past fills stay as-filed, fees from now on.
    if st.get("frozen"):
        new = []          # frozen book copies nothing; marking still runs
    import sentinel_gate
    is_severe, why = sentinel_gate.severe()
    if is_severe and new:
        print(f"[congress] {why} -> pausing new copies "
              f"({len(new)} deferred; existing holds ride)")
        new = []

    import market_hours
    if new and not market_hours.us_equities_open():
        print(f"[congress] {len(new)} new filing(s) deferred — US market closed, "
              f"will buy at the open")
        new = []  # ids not yet in 'seen', so they're picked up next open cycle

    tickers = [p["ticker"] for p in st["positions"]] + [f["ticker"] for f in new]
    px, asof = quotes(tickers)

    # R1 pre-gate: a book at/under the floor never opens NEW copies — the
    # full check at 3.5 still liquidates; this just closes the ordering hole
    # where a deferred breach could buy a slot on its own freeze cycle.
    if new:
        pre_val = st["cash"] + sum(p["units"] * px.get(p["ticker"],
                                   p["cost"] / p["units"])
                                   for p in st["positions"])
        if risk_common.r1_breached(pre_val):
            print(f"[congress] {risk_common.r1_reason(pre_val)} — "
                  f"new copies blocked")
            new = []

    # 1) close matured positions
    keep = []
    for p in st["positions"]:
        if today >= p["close_date"] and p["ticker"] in px \
                and market_hours.us_equities_open():
            val = p["units"] * px[p["ticker"]]
            f = risk_common.fee(p["ticker"], val)
            st["cash"] += val - f
            st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
            st["trades"].append({"date": today, "action": "SELL",
                                 "ticker": p["ticker"], "price": round(px[p["ticker"]], 2),
                                 "units": p["units"], "value": round(val, 2),
                                 "fee": round(f, 2),
                                 "reason": f"90-day hold complete (copied {p['filer']})"})
        else:
            keep.append(p)
    st["positions"] = keep

    # 2) open new copied positions
    for f in new:
        st["seen"].append(f["id"])
        if f["ticker"] not in px or px[f["ticker"]] <= 0:
            continue
        invest = min(SLOT, st["cash"])
        if invest < 1:
            break
        price = px[f["ticker"]]
        fee = risk_common.fee(f["ticker"], invest)
        units = (invest - fee) / price
        st["cash"] -= invest
        st["costs_paid"] = round(st.get("costs_paid", 0.0) + fee, 4)
        close_d = str((now + pd.Timedelta(days=HOLD_DAYS)).date())
        st["positions"].append({"ticker": f["ticker"], "units": units,
                                "open_date": today, "close_date": close_d,
                                "filer": f["filer"], "cost": invest})
        st["trades"].append({"date": today, "action": "BUY",
                             "ticker": f["ticker"], "price": round(price, 2),
                             "units": round(units, 4), "value": round(invest, 2),
                             "fee": round(fee, 2),
                             "reason": f"Copying {f['filer']} "
                                       f"({follow[f['filer_id']]['excess_pct']:+.1f}% avg excess, "
                                       f"filed {f['filing_date']}, {f['amount']})"})

    # 3) mark to market
    val = st["cash"] + sum(p["units"] * px.get(p["ticker"], p["cost"] / p["units"])
                           for p in st["positions"])

    # 3.5) R1 kill floor, code-enforced (fleet review 2026-08-10). A breach
    #      while the market is closed defers to the next open cycle, like
    #      every other equity book — no phantom fills at stale prices.
    if not st.get("frozen") and risk_common.r1_breached(val):
        reason = risk_common.r1_reason(val)
        print(f"[congress] {reason}")
        if market_hours.us_equities_open():
            # sell only what has a quote; an unquoted position defers, and the
            # freeze waits until every position is actually sold (a no-quote
            # wipe with no ledger row is the audit-2026-08-05 '$0 wipe' bug)
            unsold = []
            for p in st["positions"]:
                if p["ticker"] not in px:
                    unsold.append(p)
                    continue
                pv = p["units"] * px[p["ticker"]]
                f_ = risk_common.fee(p["ticker"], pv)
                st["cash"] += pv - f_
                st["costs_paid"] = round(st.get("costs_paid", 0.0) + f_, 4)
                st["trades"].append({"date": today, "action": "SELL",
                                     "ticker": p["ticker"],
                                     "price": round(px[p["ticker"]], 2),
                                     "units": p["units"],
                                     "value": round(pv, 2), "fee": round(f_, 2),
                                     "reason": reason})
            st["positions"] = unsold
            if not unsold:
                st["frozen"] = {"date": today,
                                "rule": "R1 kill floor (kill_criteria.md)"}
                print("[congress] book FROZEN — un-freezing is a human decision")
                val = st["cash"]
            else:
                print(f"[congress] {len(unsold)} position(s) have no quote — "
                      f"their liquidation and the freeze defer to next cycle")
                val = st["cash"] + sum(p["units"] * px.get(p["ticker"],
                                       p["cost"] / p["units"]) for p in unsold)
        else:
            print("[congress] liquidation deferred — US market closed")

    bench = st["bench_units"] * px[BENCH]
    newest = st["history"][-1]["date"] if st["history"] else ""
    if asof < newest:
        print(f"[congress] STALE BAR {asof} < newest mark {newest} — "
              f"mark skipped (feed served an old bar)")
    else:
        st["history"] = [h for h in st["history"] if h["date"] != asof]
        st["history"].append({"date": asof, "value": round(val, 2),
                              "bench": round(bench, 2)})
        st["history"].sort(key=lambda h: h["date"])
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    st["seen"] = st["seen"][-5000:]
    STATE.write_text(json.dumps(st, indent=2))

    # 4) dashboard payload + render
    top_follow = sorted(follow.values(), key=lambda x: -x["excess_pct"])[:12]
    payload = {
        "generated_utc": st["last_updated_utc"], "created": st["created"],
        "starting_cash": START_CASH,
        "current": st["history"][-1], "cash": round(st["cash"], 2),
        "positions": [{**p, "units": round(p["units"], 4),
                       "now": round(p["units"] * px.get(p["ticker"], 0), 2)}
                      for p in st["positions"]],
        "follow_count": len(follow), "follow_top": top_follow,
        "trades": st["trades"][-25:], "history": st["history"],
        "thoughts": (
            (f"I'm copying {len(st['positions'])} stock buy(s) filed by members "
             f"of Congress. I don't follow just anyone — I only trust the "
             f"{len(follow)} members whose past filings actually beat the "
             f"market, and I re-check that list every cycle. Each new buy they "
             f"file, I copy with a small $100 slice and hold for 90 days. "
             f"Full honesty: our own history test says this strategy LOSES to "
             f"the market — I exist to re-test that finding live."
             if st["positions"] else
             f"No copied trades open right now — none of the {len(follow)} "
             f"members I trust has filed a fresh stock buy lately. I only copy "
             f"new filings, never old ones, so I wait.")),
        "strategy": {
            "name": "Congress Copier — the bot picks whom to trust",
            "rule": f"Follow every member of Congress with >= {MIN_SCORED} scored "
                    "buys and a positive market-beating record (recomputed every "
                    f"cycle). Copy their new BUY filings with ${SLOT:.0f} slots, "
                    f"hold {HOLD_DAYS} days. Benchmark: SPY.",
            "note": "Backtest verdict was that copying Congress LOSES to SPY — "
                    "this bot is the forward, live retrial of that finding.",
        },
    }
    (config.REPORTS / "congress_dashboard_data.json").write_text(
        json.dumps(payload, indent=2))
    template = (config.ROOT / "src" / "congress_dashboard_template.html").read_text(
        encoding="utf-8")
    (config.REPORTS / "congress_dashboard.html").write_text(
        template.replace("/*__DATA__*/", json.dumps(payload)), encoding="utf-8")

    print(f"[congress] {today} value ${val:,.2f} (cash ${st['cash']:,.2f}, "
          f"{len(st['positions'])} positions) vs SPY ${bench:,.2f} | "
          f"following {len(follow)} members, {len(new)} new copies this cycle")


if __name__ == "__main__":
    main()
