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
    tickers = sorted(set(universe) | {bench})
    raw = yf.download(tickers, period="5d", interval="5m", auto_adjust=True,
                      progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    close = market_hours.trim_incomplete_bars(close).ffill()
    last = close.iloc[-1]
    ts = close.index[-1]
    ts = ts.tz_convert("UTC") if ts.tzinfo else ts.tz_localize("UTC")
    return ({t: float(last[t]) for t in tickers if t in close.columns
             and pd.notna(last[t])}, ts.isoformat(timespec="seconds"))


def run(spec, start_cash=1000.0):
    key = spec["key"]
    state_path = config.DATA / f"{key}_state.json"
    close, close_raw = _fetch_daily(spec["universe"], spec["bench"])
    live, live_ts = _fetch_live(spec["universe"], spec["bench"])
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
        is_severe, why = sentinel_gate.severe()
        if is_severe and pick != "CASH":
            print(f"[{key}] {why} -> forcing CASH")
            pick = "CASH"

    last = close.iloc[-1]
    asof = str(close.index[-1].date())
    now = datetime.now(timezone.utc)

    # ---- Freeze guards: no mutation of ANY state on a bar we can't trust ----
    # (2026-07-31 review: the old code guarded only the history mark; hwm,
    # stops, and the trade ledger could still act on stale or missing prices.)
    if st is not None:
        newest = st["history"][-1]["date"] if st["history"] else ""
        if asof < newest:
            print(f"[{key}] STALE BAR {asof} < newest mark {newest} — "
                  f"cycle skipped (feed served an old bar)")
            return st
    if pd.isna(last.get(spec["bench"])):
        print(f"[{key}] benchmark {spec['bench']} has no price — cycle skipped")
        return st
    if holding != "CASH":
        if holding not in close.columns or pd.isna(last[holding]):
            print(f"[{key}] held ticker {holding} has no price this cycle — "
                  f"cycle skipped (never trade or mark on a dead column)")
            return st
        if not holding.endswith("-USD") and holding not in live:
            # mixed-frame hazard (2026-07-26 twin): an undelivered equity
            # weekday bar can hide BEHIND legitimate weekend crypto rows where
            # tail-trimming can't reach it, and ffill would mark us a session
            # stale. If the newest weekday row has no real data for the held
            # equity AND the live feed didn't rescue it, freeze.
            wk = [i for i in close_raw.index if i.weekday() < 5]
            if wk and pd.isna(close_raw.loc[wk[-1], holding]):
                print(f"[{key}] held equity {holding} bar undelivered — "
                      f"cycle skipped")
                return st
    if pick != "CASH" and (pick not in close.columns or pd.isna(last[pick])):
        print(f"[{key}] pick {pick} has no price — keeping {holding}")
        pick = holding

    if st is None:
        st = {"created": asof, "starting_cash": start_cash, "holding": "CASH",
              "units": 0.0, "cash": start_cash,
              "bench_units": start_cash / float(last[spec["bench"]]),
              "trades": [], "history": [], "intraday": []}
        print(f"[{key}] NEW sim {asof}")

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
    if trail and st["holding"] != "CASH":
        px = float(last[st["holding"]])
        st["hwm"] = max(st.get("hwm") or px, px)
        if px <= st["hwm"] * (1 - trail):
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
            st["trades"].append({"date": asof, "action": "SELL",
                                 "ticker": prev,
                                 "price": round(float(last[prev]), 2),
                                 "units": round(st["units"], 4),
                                 "value": round(st["units"] * float(last[prev]), 2),
                                 "reason": sell_reason})
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
            spend = value * frac
            st["holding"], st["units"], st["cash"] = pick, spend / p, value - spend
            if trail:
                st["hwm"] = p
            reason = spec.get("buy_reason", "New signal pick")
            if frac < 0.999:
                reason += f" · {frac:.0%} position (vol-targeted), rest cash"
            st["trades"].append({"date": asof, "action": "BUY", "ticker": pick,
                                 "price": round(p, 2),
                                 "units": round(st["units"], 4),
                                 "value": round(spend, 2),
                                 "reason": reason})

    val = st["cash"] + (0.0 if st["holding"] == "CASH"
                        else st["units"] * float(last[st["holding"]]))
    bench = st["bench_units"] * float(last[spec["bench"]])
    st["history"] = sorted(
        [h for h in st["history"] if h["date"] != asof]
        + [{"date": asof, "value": round(val, 2),
            "bench": round(bench, 2), "holding": st["holding"]}],
        key=lambda h: h["date"])
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
