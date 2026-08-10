"""LIVE crypto $1,000 paper sim — YOLO 2.0 momentum rotation, 8 coins.

Rule (user choice, lesson from the grid in test_absmom.py applied):
Always 100% in the coin with the hottest 7-day momentum; if all 8 have
negative weekly momentum, sit in cash. Exits carry a dead-band (churn fix
2026-08-10): a seat is kept through small wobbles — TREND until momentum
clearly breaks (< -2%), CHOP until the bounce is harvested (z back to
-0.25) — so boundary noise stops churning fees. Live quotes, 24/7 market.

State: data/crypto_state.json.  Screen: reports/crypto_dashboard.html.
Run any time:  python src/crypto_tracker.py
PAPER MONEY ONLY. Not investment advice.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

import config
import crypto_prices
import risk_common

STATE = config.DATA / "crypto_state.json"
COINS = ["BTC-USD", "ETH-USD", "SOL-USD", "DOGE-USD", "AVAX-USD",
         "LINK-USD", "ADA-USD", "XRP-USD"]
BENCH = "BTC-USD"          # benchmark: $1,000 of BTC held from day one
START_CASH = 1000.0
# REGIME SWITCHER (v3 of the bot, 2026-07-16): two brains, picked daily by
# BTC vs its 200-day MA (crypto's tide gauge).
#   TREND (BTC > MA): momentum brain — hottest 7d coin, only while rising.
#   CHOP  (BTC < MA): reversion brain — most oversold coin (z20 < -1.25),
#                     harvesting bounces; nothing oversold -> cash.
# Only tested variant profitable in the 2024+ chop (+9.2%/yr).
MA_N, MOM_N, Z_N, Z_ENTRY = 200, 7, 20, -1.25
# Churn brake (audit 2026-08-05: 71 trades in 19 days, all "signal flips" —
# with 25bps costs the bot's +6.2% became -1.1%). A challenger must beat the
# incumbent CLEARLY, not merely rank above it.
HYST = 1.25       # TREND: challenger momentum must be > 1.25x the incumbent's
Z_HYST = 0.50     # CHOP: challenger z must be this much deeper than incumbent's
# Exit dead-band (churn fix 2026-08-10): entry and exit shared one knife-edge
# threshold, so a coin wobbling at the boundary was sold and rebought every
# cycle — 15 legs / $26.52 of fees on 08-10 alone, ~51bps per round trip to
# capture ~20bps of noise. A seat earned at z < Z_ENTRY (CHOP) or mom > 0
# (TREND) is only surrendered when the trade clearly completes or clearly
# fails; sentinel-severe and the R1 floor still force CASH regardless.
Z_EXIT = -0.25    # CHOP: hold the bounce until z recovers to here
MOM_EXIT = -2.0   # TREND: tolerate a wobble; exit only on a clear break (pct)
MOM_MARGIN = 2.0  # TREND: a wobbling incumbent (mom <= 0) only loses its seat
                  # to a challenger leading by this many points — the 1.25x
                  # ratio test is meaningless across zero/negative momentum


def fetch() -> pd.DataFrame:
    """Daily closes: Kraken (real exchange bars) first, Yahoo fallback."""
    k = crypto_prices.daily(COINS)
    if k is not None and len(k) >= MA_N:
        return k.ffill()
    if k is not None:
        print(f"[crypto-live] Kraken history too short ({len(k)} rows) — Yahoo fallback")
    raw = yf.download(COINS, period="15mo", auto_adjust=True, progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    return close.dropna(how="all").ffill()


def fetch_live() -> tuple[dict, str, dict]:
    """Latest trade per coin: Kraken ticker first, Yahoo 5m fallback.
    Returns ({coin: price}, iso_timestamp_utc, {coin: live spread bps})."""
    k = crypto_prices.live(COINS)
    if k:
        prices, spreads = k
        return prices, datetime.now(timezone.utc).isoformat(timespec="seconds"), spreads
    raw = yf.download(COINS, period="1d", interval="5m", auto_adjust=True,
                      progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    close = close.ffill()
    last = close.iloc[-1]
    ts = close.index[-1]
    ts = ts.tz_convert("UTC") if ts.tzinfo else ts.tz_localize("UTC")
    return ({c: float(last[c]) for c in COINS if pd.notna(last[c])},
            ts.isoformat(timespec="seconds"), {})


def signal(close: pd.DataFrame) -> tuple[str, dict, str]:
    """Regime switcher. Returns (pick, board, regime).
    TREND: hottest 7d coin if rising. CHOP: most oversold coin (z < Z_ENTRY)."""
    last = close.iloc[-1]
    ma = close.rolling(MA_N).mean().iloc[-1]
    mom = close.pct_change(MOM_N).iloc[-1]
    z20 = ((close - close.rolling(Z_N).mean())
           / close.rolling(Z_N).std()).iloc[-1]
    regime = "TREND" if last["BTC-USD"] > ma["BTC-USD"] else "CHOP"

    board = {}
    for c in COINS:
        board[c] = {
            "price": round(float(last[c]), 4),
            "ma200": round(float(ma[c]), 4),
            "gap_pct": round((float(last[c]) / float(ma[c]) - 1) * 100, 2),
            "mom_pct": round(float(mom[c]) * 100, 2),
            "z": round(float(z20[c]), 2),
            "above_ma": bool(last[c] > ma[c]),
        }
    # rank by the metric the active brain uses
    if regime == "TREND":
        ranked = sorted(COINS, key=lambda c: board[c]["mom_pct"], reverse=True)
        top = ranked[0]
        pick = top if board[top]["mom_pct"] > 0 else "CASH"
    else:
        ranked = sorted(COINS, key=lambda c: board[c]["z"])
        top = ranked[0]
        pick = top if board[top]["z"] < Z_ENTRY else "CASH"
    for i, c in enumerate(ranked):
        board[c]["rank"] = i + 1
    return pick, board, regime


def exit_brake(pick: str, held: str, board: dict, seat_regime: str) -> str:
    """Dead-band on the position->CASH boundary. signal() says CASH the moment
    the held coin slips back across the entry threshold; this keeps the seat
    until the move clearly completes (CHOP: z >= Z_EXIT) or clearly fails
    (TREND: mom <= MOM_EXIT). seat_regime is the regime the seat was EARNED
    under (state's entry_regime), not the regime of the moment — a TREND buy
    that crashes just as BTC crosses its MA must not inherit CHOP's
    dip-holding patience. Pure decision — caller handles logging and the
    sentinel/R1 overrides, which must always win."""
    if pick != "CASH" or held == "CASH":
        return pick
    b = board[held]
    if seat_regime == "TREND":
        if b["mom_pct"] > MOM_EXIT:
            return held
    else:
        # ponytail: no per-coin failure stop in CHOP — a single-coin crash in
        # a calm market rides to the R1 book floor ($750). Add a
        # drawdown-from-entry stop if that ever actually happens.
        if b["z"] < Z_EXIT:
            return held
    return pick


def swap_brake(pick: str, held: str, board: dict, regime: str) -> str:
    """Coin->coin hysteresis (review 2026-08-10: the original gates defended
    an incumbent only while it still cleared the ENTRY threshold, so a seat
    the exit brake keeps through the dead band could be flipped away by a
    challenger 0.01 past entry — same fee bleed, swap door). The incumbent
    keeps its seat unless it has fallen past the dead-band exit or the
    challenger is clearly better. Judged in the CURRENT regime: that is the
    metric the challenger was ranked by."""
    if pick in ("CASH", held) or held == "CASH":
        return pick
    b_new, b_cur = board[pick], board[held]
    if regime == "TREND":
        if b_cur["mom_pct"] > MOM_EXIT:
            # challenger must clear BOTH bars: the 1.25x ratio (dominates for
            # hot incumbents, mom > 8) and an absolute MOM_MARGIN lead
            # (dominates below — a bare ratio gave sub-fee protection at low
            # momentum and made rising incumbents easier to unseat than
            # wobbling ones)
            bar = max(HYST * b_cur["mom_pct"], b_cur["mom_pct"] + MOM_MARGIN)
            if b_new["mom_pct"] < bar:
                return held
    else:
        if b_cur["z"] < Z_EXIT and b_new["z"] > b_cur["z"] - Z_HYST:
            return held
    return pick


def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else None


def init_state(close, pick, board, regime="TREND") -> dict:
    asof = str(close.index[-1].date())
    st = {
        "created": asof, "starting_cash": START_CASH,
        "holding": "CASH", "units": 0.0, "cash": START_CASH,
        "bench_units": START_CASH / board[BENCH]["price"],
        "trades": [], "history": [],
    }
    if pick != "CASH":
        px = board[pick]["price"]
        st["holding"], st["units"], st["cash"] = pick, START_CASH / px, 0.0
        st["entry_regime"] = regime
        st["trades"].append({"date": asof, "action": "BUY", "ticker": pick,
                             "price": px, "units": round(st["units"], 6),
                             "value": START_CASH,
                             "reason": (f"Initial entry — most oversold coin "
                                        f"(z {board[pick]['z']:+.2f})"
                                        if regime == "CHOP" else
                                        f"Initial entry — strongest eligible coin "
                                        f"({board[pick]['mom_pct']:+.1f}% 7d momentum)")})
    else:
        st["trades"].append({"date": asof, "action": "HOLD CASH", "ticker": "—",
                             "price": 0, "units": 0, "value": START_CASH,
                             "reason": ("Nothing oversold enough (z < -1.25) — cash"
                                        if regime == "CHOP" else
                                        "All 8 coins falling on the week — cash until one rises")})
    return st


def update(st, close, pick, board, cash_reason=None, regime="TREND") -> dict:
    asof = str(close.index[-1].date())
    # value before any switch
    cur_px = board[st["holding"]]["price"] if st["holding"] != "CASH" else None

    if pick != st["holding"]:
        # liquidate current (25bps fee per side — the audit's cost model)
        value = st["cash"]
        if st["holding"] != "CASH":
            gross = st["units"] * cur_px
            f = risk_common.fee(st["holding"], gross,
                                board[st["holding"]].get("spread_bps"))
            value += gross - f
            st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
            st["trades"].append({"date": asof, "action": "SELL",
                                 "ticker": st["holding"],
                                 "price": round(cur_px, 8),
                                 "units": round(st["units"], 6),
                                 "value": round(gross, 2),
                                 "fee": round(f, 2),
                                 "reason": "Signal flip"})
        if pick == "CASH":
            st["holding"], st["units"], st["cash"] = "CASH", 0.0, value
            st.pop("entry_regime", None)
            st["trades"].append({"date": asof, "action": "TO CASH", "ticker": "—",
                                 "price": 0, "units": 0, "value": round(value, 2),
                                 "reason": cash_reason or
                                 ("Bounce harvested or nothing oversold enough — cash"
                                  if regime == "CHOP" else
                                  "All 8 coins falling on the week — cash until one rises")})
        else:
            px = board[pick]["price"]
            f = risk_common.fee(pick, value, board[pick].get("spread_bps"))
            spend = value - f
            st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
            st["holding"], st["units"], st["cash"] = pick, spend / px, 0.0
            st["entry_regime"] = regime
            st["trades"].append({"date": asof, "action": "BUY", "ticker": pick,
                                 "price": round(px, 8),
                                 "units": round(st["units"], 6),
                                 "value": round(spend, 2),
                                 "fee": round(f, 2),
                                 "reason": (f"Most oversold coin (z {board[pick]['z']:+.2f}) "
                                            f"— buying the dip"
                                            if regime == "CHOP" else
                                            f"Strongest eligible coin "
                                            f"({board[pick]['mom_pct']:+.1f}% 7d momentum)")})

    val = st["cash"] if st["holding"] == "CASH" else st["units"] * board[st["holding"]]["price"]
    bench = st["bench_units"] * board[BENCH]["price"]
    row = {"date": asof, "value": round(val, 2), "bench": round(bench, 2),
           "holding": st["holding"]}
    st["history"] = sorted([h for h in st["history"] if h["date"] != asof] + [row],
                           key=lambda h: h["date"])
    st["last_updated_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    # live intraday equity stream (rolling ~48h at 2-min cadence)
    st.setdefault("intraday", [])
    st["intraday"] = [p for p in st["intraday"]
                      if p["ts"] != st["last_updated_utc"]]
    st["intraday"].append({"ts": st["last_updated_utc"],
                           "value": round(val, 2), "bench": round(bench, 2),
                           "holding": st["holding"]})
    st["intraday"] = st["intraday"][-1500:]
    return st


def emit(st, board, pick, live_ts="", regime="") -> None:
    payload = {
        "generated_utc": st["last_updated_utc"], "created": st["created"],
        "starting_cash": st["starting_cash"], "live_ts": live_ts,
        "current": st["history"][-1], "board": board, "pick": pick,
        "regime": regime,
        "intraday": st.get("intraday", []),
        "trades": st["trades"][-20:], "history": st["history"],
        "costs_paid": st.get("costs_paid", 0.0),
        "frozen": st.get("frozen"),
        "thoughts": (
            ("Right now I'm in TREND mode: Bitcoin is above its 200-day average, "
             "which historically means crypto is in an uptrend — so my rule is to "
             "ride whichever coin has climbed the most this week. "
             if "TREND" in (regime or "").upper() else
             "Right now I'm in CHOP mode: Bitcoin is below its 200-day average, "
             "which means the market is directionless — chasing momentum here "
             "loses money, so instead I look for a coin that fell unusually hard "
             "and try to catch its bounce back. ")
            + (f"That's why I'm holding {st['holding'].replace('-USD', '')}. "
               "I keep my seat through small wobbles instead of paying fees "
               "on every flicker."
               if st["holding"] != "CASH" else
               "Nothing qualifies at this moment, so I'm in cash — in crypto, "
               "sitting out is often the smartest trade.")),
        "strategy": {
            "name": "Regime Switcher — two brains, one bot",
            "rule": "BTC above its 200-day MA = TREND: ride the hottest "
                    "rising 7-day-momentum coin. Below = CHOP: buy the most "
                    "oversold coin (z20 < -1.25) and harvest the bounce; "
                    "nothing qualifies -> cash. Exits use a dead-band (hold "
                    "until mom < -2% / z back to -0.25) so boundary wobbles "
                    "don't churn fees",
            "backtest_cagr": "+50%/yr since 2017 · +9%/yr in the 2024+ chop",
            "backtest_maxdd": "-93% (2017 era) · experimental — parameters are soft",
        },
    }
    (config.REPORTS / "crypto_dashboard_data.json").write_text(
        json.dumps(payload, indent=2))
    template = (config.ROOT / "src" / "crypto_dashboard_template.html").read_text(
        encoding="utf-8")
    out = config.REPORTS / "crypto_dashboard.html"
    out.write_text(template.replace("/*__DATA__*/", json.dumps(payload)),
                   encoding="utf-8")
    print(f"[dash] rendered {out.name}")


def main():
    close = fetch()
    # Override today's row with LIVE quotes so momentum, ranking, and trade
    # prices all reflect right now, not yesterday's close.
    live, live_ts, spreads = fetch_live()
    if not live:
        # Guard (audit 2026-08-05: this bot had none): a dead live feed means
        # stale ranks and phantom fills — hold everything, try next cycle.
        print("[crypto-live] no live quotes from any source — cycle skipped")
        return
    for c, p in live.items():
        close.iloc[-1, close.columns.get_loc(c)] = p
    pick, board, regime = signal(close)
    for c in COINS:
        if c in spreads:
            board[c]["spread_bps"] = round(spreads[c], 2)
    import sentinel_gate
    gate_state, gate_detail = sentinel_gate.status()
    if gate_state != "ok":
        print(f"[crypto-live] WATCHER {gate_state.upper()}: {gate_detail}")
    is_severe, why = sentinel_gate.severe()
    cash_reason = None
    if is_severe:
        # label ANY severe-cycle liquidation with the Watcher's reason — also
        # the case where signal() itself said CASH and the exit brake is
        # bypassed (cash_reason is only consumed when a TO CASH is written)
        cash_reason = why
        if pick != "CASH":
            print(f"[crypto-live] {why} -> forcing CASH")
            pick = "CASH"
    st = load_state()
    if st is not None:
        held = st["holding"]
        # The regime this seat was earned under. Legacy state predating
        # entry_regime gets its provenance FROZEN at first sight (setdefault,
        # persisted below) — a floating fallback would relabel the seat on a
        # regime flip and judge a CHOP dip by TREND's momentum stop.
        if held != "CASH":
            st.setdefault("entry_regime", regime)
        seat_regime = st.get("entry_regime") or regime
        # Churn brake: don't swap coins on a marginal re-rank. The incumbent
        # keeps its seat unless it's disqualified or clearly outgunned.
        kept = swap_brake(pick, held, board, regime)
        if kept != pick:
            print(f"[crypto-live] churn brake: {pick} "
                  f"(mom {board[pick]['mom_pct']:+.1f}%, z {board[pick]['z']:+.2f}) "
                  f"not clearly better than incumbent {held} "
                  f"(mom {board[held]['mom_pct']:+.1f}%, z {board[held]['z']:+.2f}) "
                  f"— holding")
            pick = kept
        # Exit dead-band: signal() flips to CASH at the same threshold it
        # entered on — never surrender the seat on a boundary wobble. A
        # sentinel-severe CASH is an order, not a wobble; it passes through.
        if pick == "CASH" and held != "CASH" and not is_severe:
            if exit_brake(pick, held, board, seat_regime) == held:
                b = board[held]
                metric = (f"mom {b['mom_pct']:+.1f}% > {MOM_EXIT:+.1f}%"
                          if seat_regime == "TREND" else
                          f"z {b['z']:+.2f} < {Z_EXIT:+.2f}")
                print(f"[crypto-live] exit brake: {held} {metric} — "
                      f"inside dead-band, holding")
                pick = held
        # R1 kill floor, code-enforced (audit 2026-08-05)
        cur_val = st.get("cash", 0.0) if held == "CASH" \
            else st.get("units", 0.0) * board[held]["price"]
        if st.get("frozen"):
            pick = "CASH"
            cash_reason = "Book frozen at the R1 kill floor — no further trades"
        elif risk_common.r1_breached(cur_val):
            pick = "CASH"
            cash_reason = risk_common.r1_reason(cur_val)
            print(f"[crypto-live] {cash_reason}")
    if st is None:
        st = init_state(close, pick, board, regime)
        print(f"[crypto-live] NEW sim {st['created']} — opening position: {pick}")
    st = update(st, close, pick, board, cash_reason, regime)
    if cash_reason and "R1 KILL FLOOR" in cash_reason and st["holding"] == "CASH" \
            and not st.get("frozen"):
        st["frozen"] = {"date": st["history"][-1]["date"] if st["history"] else "",
                        "rule": "R1 kill floor (kill_criteria.md)"}
        print("[crypto-live] book FROZEN — un-freezing is a human decision")
    STATE.write_text(json.dumps(st, indent=2))
    emit(st, board, pick, live_ts, regime)
    print(f"[crypto-live] regime: {regime}")
    print(f"[crypto-live] live quotes as of {live_ts}")

    cur = st["history"][-1]
    print(f"[crypto-live] {cur['date']}  holding {cur['holding']}  "
          f"value ${cur['value']:,.2f}  vs BTC ${cur['bench']:,.2f}  pick={pick}")
    for c in sorted(COINS, key=lambda c: board[c]["rank"]):
        b = board[c]
        print(f"  #{b['rank']} {c:<9} ${b['price']:>10,.2f}  "
              f"mom7 {b['mom_pct']:+7.2f}%  gap-to-MA {b['gap_pct']:+7.2f}%")


if __name__ == "__main__":
    main()
