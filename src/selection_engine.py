"""Generic single-position paper-trading engine for fleet bots.

A bot supplies a SPEC dict; the engine handles state, live quotes, trades,
mark-to-market, and dashboard rendering (shared fleet template).

SPEC = {
  "key": "meanrev",                # file prefix for state/dashboard
  "universe": [...tickers...],
  "bench": "SPY",
  "signal": fn(close_df, holding) -> (pick_or_CASH, board_rows, board_title),
  "signal_frame": "raw",           # optional: signal sees the PRE-ffill frame
                                   # (mixed universes need native calendars)
  "risk": {"trailing": 0.10, "cooldown_days": 5},   # optional overlay
  "vol_target": 0.20,              # optional: size position to this ann. vol
  "meta": {title, badge, bench_label, board_note},
  "strategy": {name, rule, backtest_cagr, backtest_maxdd, note},
}
board_rows: [{sym, price, line, tag, on(bool), fill(-50..50)}] for the screen.
PAPER MONEY ONLY. Not investment advice.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

import config
import market_hours
import risk_common


def _ann_factor(ticker: str) -> float:
    """Trading days per year for annualization: crypto trades 365, equities 252."""
    return 365.0 if ticker.endswith("-USD") else 252.0


def _fetch_daily(universe, bench):
    """Returns (ffilled, raw) frames. raw keeps native NaNs so callers can see
    each asset's true trading calendar; ffilled is for fills and marks."""
    tickers = sorted(set(universe) | {bench})
    raw = yf.download(tickers, period="15mo", auto_adjust=True, progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    trimmed = market_hours.trim_incomplete_bars(close.dropna(how="all"))
    return trimmed.ffill(), trimmed


def _fetch_live(universe, bench):
    """Returns (prices, live_ts, raw_5m_frame). The raw frame is kept pre-ffill
    so callers can ask which session each price genuinely came from — the
    daily feed lags, and that frame is the only honest record of it."""
    tickers = sorted(set(universe) | {bench})
    raw = yf.download(tickers, period="5d", interval="5m", auto_adjust=True,
                      progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    trimmed = market_hours.trim_incomplete_bars(close)
    filled = trimmed.ffill()
    last = filled.iloc[-1]
    ts = filled.index[-1]
    ts = ts.tz_convert("UTC") if ts.tzinfo else ts.tz_localize("UTC")
    return ({t: float(last[t]) for t in tickers if t in filled.columns
             and pd.notna(last[t])}, ts.isoformat(timespec="seconds"), trimmed)


def _thoughts(spec, st, board, last):
    """Plain-language 'what I'm thinking' note, generated from the bot's own
    live rules and state — honest by construction (it IS the logic)."""
    risk = spec.get("risk") or {}
    lines = []
    if st["holding"] == "CASH":
        lines.append("I'm sitting in cash right now. "
                     + spec.get("cash_reason", "Nothing passes my rules today") + ".")
        if st.get("stopped"):
            cd = risk.get("cooldown_days", 0)
            lines.append(f"I recently sold {st['stopped']['ticker']} after it fell "
                         f"too far, and my cooling-off rule stops me from buying "
                         f"it back for {cd} days (so I don't catch a falling knife twice).")
        lines.append("I'd rather wait than force a trade — patience is part of my design.")
    else:
        h = st["holding"]
        px = float(last[h]) if h in last.index and last[h] == last[h] else None
        lines.append(f"I'm holding {h}. " + spec.get("buy_reason", "It fits my rules") + ".")
        entry = next((t["price"] for t in reversed(st["trades"])
                      if t["action"] == "BUY" and t["ticker"] == h), None)
        if entry and px:
            lines.append(f"I bought at ${entry:,.2f}; it's now ${px:,.2f} "
                         f"({(px / entry - 1) * 100:+.1f}% since I got in).")
        if st.get("cash", 0) > 1:
            lines.append(f"I deliberately kept ${st['cash']:,.2f} aside in cash — "
                         f"I take smaller positions in assets that swing a lot.")
        trail = risk.get("trailing")
        if trail and st.get("hwm"):
            lines.append(f"My safety net: if the price falls to "
                         f"${st['hwm'] * (1 - trail):,.2f} ({trail:.0%} below its "
                         f"recent high), I sell automatically — no exceptions.")
        chal = next((b.get("sym") for b in board
                     if b.get("on") and not b.get("pick")), None)
        if chal:
            lines.append(f"Closest challenger on my list is {chal}, but it would "
                         f"need to look clearly better before I switch — jumping "
                         f"between positions too often just burns money on trades.")
    return " ".join(lines)


def run(spec, start_cash=1000.0):
    key = spec["key"]
    state_path = config.DATA / f"{key}_state.json"
    close, close_raw = _fetch_daily(spec["universe"], spec["bench"])
    # pristine pre-splice copy — the calendar oracle. Live prices are spliced
    # into the last row below, which would make a stale equity look like it
    # had genuine weekend data; last_real_date() must never see those.
    close_cal = close_raw.copy()
    live, live_ts, live_raw = _fetch_live(spec["universe"], spec["bench"])
    for t, p in live.items():
        if t in close.columns:
            close.iloc[-1, close.columns.get_loc(t)] = p
        if t in close_raw.columns:
            close_raw.iloc[-1, close_raw.columns.get_loc(t)] = p

    st = json.loads(state_path.read_text()) if state_path.exists() else None
    holding = st["holding"] if st else "CASH"
    sig_frame = close_raw if spec.get("signal_frame") == "raw" else close
    pick, board, board_title = spec["signal"](sig_frame, holding)

    # Sentinel override (default on; All-Weather doesn't use this engine and
    # stays deliberately unwired as the control group).
    if spec.get("risk_gate", True):
        import sentinel_gate
        gate_state, gate_detail = sentinel_gate.status()
        if gate_state != "ok":
            print(f"[{key}] WATCHER {gate_state.upper()}: {gate_detail}")
        is_severe, why = sentinel_gate.severe()
        if is_severe and pick != "CASH":
            print(f"[{key}] {why} -> forcing CASH")
            pick = "CASH"

    last = close.iloc[-1]
    now = datetime.now(timezone.utc)

    # ---- Date the mark by the asset that DETERMINES its value ----------------
    # A bot holding an equity does not change value on a Saturday, even though
    # a mixed crypto+equity frame HAS Saturday rows. Dating marks by the newest
    # row wrote phantom weekend marks (identical to Friday) and then — because
    # the monotonic guard below refuses to write behind the newest mark — froze
    # the bot solid until the next equity session. Found 2026-08-03, after the
    # Scholar and the Analyst sat frozen through a whole weekend.
    # This is what market_hours.last_real_date() was built for; the engine had
    # never adopted it (hunter/sentinel already did).
    # ...and by the freshest feed that actually supplied the price: Yahoo's
    # daily bars lag the intraday feed by hours, so the daily frame alone
    # dates today's real prices with yesterday's (or Friday's) date.
    value_asset = holding if holding != "CASH" else spec["bench"]
    asof = (market_hours.newest_real_date(close_cal, live_raw, value_asset)
            or str(close.index[-1].date()))
    bench_asof = market_hours.newest_real_date(close_cal, live_raw, spec["bench"])

    # ---- Guards: no mutation of state we can't trust -------------------------
    # (2026-07-31 review: the old code guarded only the history mark; hwm,
    # stops, and the trade ledger could still act on stale or missing prices.)
    #
    # A regressed feed must NOT take the bot offline. Skipping the whole cycle
    # here stopped marking, trading AND rendering — so a few hours of Yahoo lag
    # looked identical to a dead bot (2026-08-03, then again 2026-08-04). We
    # now refuse only the unsafe parts: no trade, no history row written behind
    # the newest mark. The bot still marks its heartbeat and re-renders, and
    # says plainly on its dashboard that its data is delayed.
    feed_delayed = False
    if st is not None:
        newest = st["history"][-1]["date"] if st["history"] else ""
        if asof < newest:
            feed_delayed = True
            print(f"[{key}] FEED DELAYED — freshest genuine price is {asof} but "
                  f"newest mark is {newest}; holding steady, not trading")
    if pd.isna(last.get(spec["bench"])):
        print(f"[{key}] benchmark {spec['bench']} has no price — cycle skipped")
        return st
    if holding != "CASH" and (holding not in close.columns
                              or pd.isna(last[holding])):
        print(f"[{key}] held ticker {holding} has no price this cycle — "
              f"cycle skipped (never trade or mark on a dead column)")
        return st
    if feed_delayed:
        pick = holding                      # never trade on a regressed feed
    if pick != "CASH" and (pick not in close.columns or pd.isna(last[pick])):
        print(f"[{key}] pick {pick} has no price — keeping {holding}")
        pick = holding
    # Undelivered equity bar: don't TRADE on a price the feed hasn't actually
    # delivered (the 2026-07-22 phantom-fill hazard) — but do keep marking and
    # rendering. Freezing the whole cycle here was the second half of the
    # 2026-08-03 lockup.
    for t in {holding, pick} - {"CASH"}:
        if not t.endswith("-USD") and t not in live:
            wk = [i for i in close_cal.index if i.weekday() < 5]
            if wk and pd.isna(close_cal.loc[wk[-1], t]):
                if pick != holding:
                    print(f"[{key}] {t} bar undelivered — trade deferred, "
                          f"still marking")
                pick = holding
                break

    if st is None:
        st = {"created": asof, "starting_cash": start_cash, "holding": "CASH",
              "units": 0.0, "cash": start_cash,
              "bench_units": start_cash / float(last[spec["bench"]]),
              "trades": [], "history": [], "intraday": []}
        print(f"[{key}] NEW sim {asof}")

    # ---- R1 kill floor (code-enforced; audit 2026-08-05) --------------------
    # A frozen book never trades again; a book at/below $750 liquidates now.
    # The freeze is only recorded once the liquidation actually fills — a
    # floor breach while the market is closed defers like any other trade.
    r1_hit = False
    cur_val = st["cash"] + (0.0 if st["holding"] == "CASH"
                            else st["units"] * float(last[st["holding"]]))
    if st.get("frozen"):
        pick = "CASH"
    elif risk_common.r1_breached(cur_val):
        r1_hit = True
        pick = "CASH"
        print(f"[{key}] {risk_common.r1_reason(cur_val)}")

    # ---- Risk overlay (freqtrade pattern: risk is SPEC config, not signal code) ----
    # trailing: force CASH if price falls X% from the high-water mark since
    # entry. The stop is only RECORDED (st['stopped']) when the sell actually
    # fills — a stop that fires while the market is closed defers like any
    # other trade and simply re-evaluates next cycle (2026-07-31 review: the
    # old order persisted 'stopped' for sells that never happened, which could
    # later liquidate a recovered position with a false reason).
    risk = spec.get("risk") or {}
    trail = risk.get("trailing")
    sell_reason, stop_fired = "Signal flip", False
    if r1_hit:
        sell_reason = risk_common.r1_reason(cur_val)
    if trail and st["holding"] != "CASH":
        px = float(last[st["holding"]])
        st["hwm"] = max(st.get("hwm") or px, px)
        if px <= st["hwm"] * (1 - trail) and not r1_hit:
            # not r1_hit: when one gap trips both, the ledger must say R1 —
            # the kill floor is the reason the book is actually dying
            sell_reason = (f"TRAILING STOP — fell {trail:.0%} from high-water "
                           f"${st['hwm']:,.2f}")
            stop_fired = True
            print(f"[{key}] {sell_reason} -> forcing CASH")
            pick = "CASH"
    # cooldown blocks RE-ENTRY into a stopped-out ticker only — it must never
    # touch a position we already hold.
    cd = risk.get("cooldown_days")
    if cd and pick not in ("CASH", st["holding"]) \
            and st.get("stopped", {}).get("ticker") == pick:
        days = (pd.Timestamp(asof) - pd.Timestamp(st["stopped"]["date"])).days
        if days < cd:
            print(f"[{key}] {pick} stopped out {days}d ago -> cooling off "
                  f"({cd} calendar days)")
            pick = st["holding"]
        else:
            st.pop("stopped", None)

    # defer only if a leg actually needs the US session: crypto legs and CASH
    # fill any time (mixed-universe bots switch BTC->ETH on weekends honestly)
    def _fillable(t):
        return t == "CASH" or market_hours.can_fill(t)
    if pick != st["holding"] and not (_fillable(pick) and _fillable(st["holding"])):
        print(f"[{key}] switch {st['holding']} -> {pick} deferred — "
              f"US market closed, will fill at the open")
        pick = st["holding"]
    if pick != st["holding"]:
        prev = st["holding"]
        value = st["cash"] + (0.0 if prev == "CASH"
                              else st["units"] * float(last[prev]))
        if prev != "CASH":
            gross = st["units"] * float(last[prev])
            sell_fee = risk_common.fee(prev, gross)
            value -= sell_fee
            st["costs_paid"] = round(st.get("costs_paid", 0.0) + sell_fee, 4)
            trade = {"date": asof, "action": "SELL",
                     "ticker": prev,
                     "price": round(float(last[prev]), 8),
                     "units": round(st["units"], 4),
                     "value": round(gross, 2),
                     "fee": round(sell_fee, 2),
                     "reason": sell_reason}
            if spec.get("broker_shadow"):
                import alpaca_broker
                bf = alpaca_broker.shadow_fill("SELL", prev, gross)
                if bf:
                    trade["broker_fill"] = bf["price"]
                    trade["fill_gap_bps"] = round(
                        (bf["price"] / float(last[prev]) - 1) * 10_000, 2)
            st["trades"].append(trade)
            if stop_fired:
                st["stopped"] = {"ticker": prev, "date": asof}
        if pick == "CASH":
            st["holding"], st["units"], st["cash"] = "CASH", 0.0, value
            st.pop("hwm", None)
            st["trades"].append({"date": asof, "action": "TO CASH", "ticker": "—",
                                 "price": 0, "units": 0, "value": round(value, 2),
                                 "reason": sell_reason if sell_reason != "Signal flip"
                                 else spec.get("cash_reason", "No qualifying signal")})
        else:
            p = float(last[pick])
            # optional vol-target sizing: risk a fraction, keep the rest in
            # cash. Vol comes from the asset's NATIVE calendar (raw frame) —
            # ffilled weekend rows would fabricate zero returns and understate
            # equity vol ~15% — annualized by the asset's own trading year.
            frac, vt = 1.0, spec.get("vol_target")
            if vt:
                r = close_raw[pick].dropna().pct_change()
                v = r.rolling(90).std().iloc[-1] * (_ann_factor(pick) ** 0.5)
                if pd.notna(v) and v > 0:
                    frac = min(1.0, vt / float(v))
            gross_spend = value * frac
            buy_fee = risk_common.fee(pick, gross_spend)
            spend = gross_spend - buy_fee
            st["costs_paid"] = round(st.get("costs_paid", 0.0) + buy_fee, 4)
            st["holding"], st["units"], st["cash"] = pick, spend / p, value - gross_spend
            if trail:
                st["hwm"] = p
            reason = spec.get("buy_reason", "New signal pick")
            if frac < 0.999:
                reason += f" · {frac:.0%} position (vol-targeted), rest cash"
            trade = {"date": asof, "action": "BUY", "ticker": pick,
                     "price": round(p, 8),
                     "units": round(st["units"], 4),
                     "value": round(spend, 2),
                     "fee": round(buy_fee, 2),
                     "reason": reason}
            if spec.get("broker_shadow"):
                import alpaca_broker
                bf = alpaca_broker.shadow_fill("BUY", pick, spend)
                if bf:
                    trade["broker_fill"] = bf["price"]
                    trade["fill_gap_bps"] = round(
                        (bf["price"] / p - 1) * 10_000, 2)
            st["trades"].append(trade)

    if r1_hit and st["holding"] == "CASH" and not st.get("frozen"):
        st["frozen"] = {"date": asof, "value": round(cur_val, 2),
                        "rule": "R1 kill floor (kill_criteria.md)"}
        print(f"[{key}] book FROZEN — un-freezing is a human decision")

    val = st["cash"] + (0.0 if st["holding"] == "CASH"
                        else st["units"] * float(last[st["holding"]]))
    bench = st["bench_units"] * float(last[spec["bench"]])
    if not feed_delayed:
        row = {"date": asof, "value": round(val, 2),
               "bench": round(bench, 2), "holding": st["holding"]}
        if bench_asof and bench_asof != asof:
            row["bench_asof"] = bench_asof  # benchmark had to be forward-filled
        st["history"] = sorted(
            [h for h in st["history"] if h["date"] != asof] + [row],
            key=lambda h: h["date"])
    st["feed_delayed"] = feed_delayed
    st["data_asof"] = asof
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    st["intraday"] = [p for p in st.get("intraday", [])
                      if p["ts"] != st["last_updated_utc"]][-1499:] + [
        {"ts": st["last_updated_utc"], "value": round(val, 2),
         "bench": round(bench, 2), "holding": st["holding"]}]
    state_path.write_text(json.dumps(st, indent=2))

    payload = {
        "generated_utc": st["last_updated_utc"], "created": st["created"],
        "starting_cash": st["starting_cash"], "live_ts": live_ts,
        "current": st["history"][-1], "board": board,
        "board_title": board_title, "meta": spec["meta"],
        "intraday": st["intraday"], "trades": st["trades"][-20:],
        "history": st["history"], "strategy": spec["strategy"],
        "costs_paid": st.get("costs_paid", 0.0),
        "frozen": st.get("frozen"),
        "thoughts": ((f"🧊 This book is FROZEN: it hit the fleet's $"
                      f"{risk_common.R1_FLOOR:,.0f} kill floor on "
                      f"{st['frozen']['date']} and liquidated per the "
                      "pre-registered rules. It will not trade again.\n\n")
                     if st.get("frozen") else "")
                    + (("⏳ My price feed is running behind right now (freshest "
                      f"confirmed price: {asof}). I'm holding steady and not "
                      "trading until it catches up — acting on stale prices is "
                      "how paper sims tell themselves comfortable lies.\n\n")
                     if feed_delayed else "") + _thoughts(spec, st, board, last),
    }
    (config.REPORTS / f"{key}_dashboard_data.json").write_text(
        json.dumps(payload, indent=2))
    template = (config.ROOT / "src" / "fleet_dashboard_template.html").read_text(
        encoding="utf-8")
    html = template.replace("/*__DATA__*/", json.dumps(payload)).replace(
        "__DATAFILE__", f"{key}_dashboard_data.json")
    (config.REPORTS / f"{key}_dashboard.html").write_text(html, encoding="utf-8")

    print(f"[{key}] {asof} holding {st['holding']} value ${val:,.2f} "
          f"vs {spec['bench']} ${bench:,.2f}")
    return st
