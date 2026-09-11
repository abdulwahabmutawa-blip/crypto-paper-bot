"""FUNDING CARRY paper book — long spot, short perp, collect the funding.

Why this bot exists (owner 2026-09-11: "just do one that is successful").
The 2026-09-07 desk study (trading-research/study/) asked which crypto actors
have a VERIFIED multi-year positive record. The answer was not a signal: it
was market makers and market-neutral arbitrage funds — Wintermute ($582M net
profit on $1.5T volume, UK Companies House), Nickel Digital Arbitrage (Sharpe
>4, no negative months in three years), Pythagoras (+8.8% through FTX, +18%
in 2023). None of them forecasts price. They COLLECT: spread, mispricing,
funding. Every book this repo has run so far tried to FORECAST, and every one
of them lost.

Funding carry is the only member of that verified family that a retail Binance
account can actually run (study 03, section 1). Hold spot, short the perp
against it 1:1, and the position has no price exposure — what it earns is the
funding payment longs pay shorts every 8 hours.

WHAT THE STUDY SAYS TO EXPECT, so nobody is surprised later:
  * 3-8% APR net in the 2025-26 regime. 15-30% only in bull-funding spikes.
  * BTC funding sits pinned at the 0.01%/8h floor 78% of the time (ETH 88%),
    which is ~10.9% annualised ON THE PERP LEG but only ~5.5% on the total
    capital deployed, because half of it is sitting in spot earning nothing.
  * Capital floor ~$2,000. Below that the round-trip fee eats a month of
    income and the trade is, in the vendor's own words, economically
    infeasible. THIS IS THE BINDING CONSTRAINT, not the code.
  * Failure mode: funding flips negative (4-8% of intervals in 2025) and you
    pay both legs. One week at -0.05%/8h costs more than a month of floor
    funding earns.

SIZING: the book simulates CAPITAL_USD (default $2,000 = the study's floor)
so the record means something. It ALSO tracks what the owner's real $33 would
have done, side by side, because the gap between those two lines is the whole
argument about account size.

PAPER MONEY ONLY. This module cannot trade: it imports binance_data (public
GET endpoints only) and never touches binance_live or any key.

NOTE ON HOSTING: funding data lives on fapi.binance.com, which has no public
mirror and answers HTTP 451 to US IPs. GitHub's runners are US-hosted, so on
Actions this bot will usually find no data and skip the cycle without failing.
Its real home is the VPS. Skipping is harmless — funding settles only 3x a
day and every settlement is credited from history, so cycles can be missed.

Run any time:  python src/bot_carry.py   ->  reports/carry.md
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import binance_data
import config

STATE = config.DATA / "carry_state.json"
OUT = config.REPORTS / "carry.md"

# --- the book ---------------------------------------------------------------
CAPITAL_USD = 2000.0        # study's floor; half spot, half perp margin
OWNER_USD = 33.0            # the real book's actual size, tracked in parallel
SYMBOLS = ("BTCUSDT", "ETHUSDT")   # deepest perps, most floor-pinned funding

# --- fees, Binance VIP0 with the BNB discount (study 03, section 5) ---------
SPOT_FEE = 0.00075          # 0.075% per side
FUT_FEE = 0.00045           # 0.045% taker per side (maker 0.018% if resting)

# --- entry / exit -----------------------------------------------------------
# The entry bar is DERIVED, not picked. Each leg is half the capital, so one
# open costs (C/2)*SPOT_FEE + (C/2)*FUT_FEE and a round trip is exactly
# C*(SPOT_FEE + FUT_FEE) = 0.12% of capital. The study's own test for whether
# this trade is worth doing at a given size is "does it clear the round trip
# inside a month", so that is the bar: the trailing rate must pay the round
# trip back within BREAKEVEN_DAYS.
#
# A first pass hardcoded 4% APR and the book sat flat against a live regime
# paying 2.4% on capital — a bar with no derivation behind it, refusing a
# trade that clears its costs in 18 days. Deriving it removes the guess.
LOOKBACK = 21               # funding settlements = 7 days
ROUND_TRIP = SPOT_FEE + FUT_FEE          # = 0.12% of capital, both legs
BREAKEVEN_DAYS = 30
ENTER_APR = ROUND_TRIP * 365 / BREAKEVEN_DAYS     # ~1.46% on capital
EXIT_APR = 0.00             # trailing turns negative -> flat


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load() -> dict:
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            print("[carry] state unreadable, starting fresh")
    return {"created": _now()[:10], "capital": CAPITAL_USD, "seat": None,
            "funding_collected": 0.0, "fees_paid": 0.0, "owner_net": 0.0,
            "last_funding_ms": {}, "settlements": 0, "trades": [],
            "history": []}


def save(st: dict) -> None:
    STATE.write_text(json.dumps(st, indent=2), encoding="utf-8")


def funding_history(symbol: str, limit: int = 100) -> list[dict]:
    """Settled funding rates, oldest first. Each row: fundingTime (ms),
    fundingRate (str). Keyless public endpoint."""
    d = binance_data._fget("/fapi/v1/fundingRate",
                           {"symbol": symbol, "limit": limit}, weight=1)
    return d if isinstance(d, list) else []


def trailing_apr(rows: list[dict], n: int = LOOKBACK) -> float | None:
    """Annualised funding on the PERP LEG over the last n settlements.
    3 settlements a day x 365 = 1095 a year."""
    if len(rows) < n:
        return None
    recent = [float(r["fundingRate"]) for r in rows[-n:]]
    return sum(recent) / len(recent) * 1095


def apr_on_capital(perp_apr: float) -> float:
    """Half the capital sits in spot earning nothing, so the rate the book
    actually experiences is half the perp-leg rate. Binance's own carry bot
    halves its displayed APR for exactly this reason."""
    return perp_apr / 2.0


def pick(quotes: dict[str, list[dict]]) -> tuple[str | None, float]:
    """Best symbol by trailing funding, or (None, apr) if none clears the bar."""
    best, best_apr = None, -9.9
    for sym, rows in quotes.items():
        apr = trailing_apr(rows)
        if apr is None:
            continue
        if apr > best_apr:
            best, best_apr = sym, apr
    if best is None:
        return None, 0.0
    return (best, best_apr) if apr_on_capital(best_apr) >= ENTER_APR else (None, best_apr)


def open_seat(st: dict, sym: str, spot: float, apr: float) -> None:
    """Half the capital long spot, the same notional short on the perp."""
    leg = st["capital"] / 2.0
    fee = leg * SPOT_FEE + leg * FUT_FEE
    st["fees_paid"] += fee
    st["owner_net"] -= (OWNER_USD / 2.0) * (SPOT_FEE + FUT_FEE)
    st["seat"] = {"symbol": sym, "opened": _now(), "leg_usd": leg,
                  "spot_entry": spot, "qty": leg / spot, "entry_apr": apr}
    st["trades"].append({"ts": _now(), "action": "OPEN", "symbol": sym,
                         "spot": spot, "leg_usd": round(leg, 2),
                         "fee": round(fee, 4), "apr": round(apr, 4)})
    print(f"[carry] OPEN {sym} {leg:.0f} spot + {leg:.0f} short perp, "
          f"trailing {apr*100:.1f}% APR on the leg, fee ${fee:.2f}")


def close_seat(st: dict, spot: float, why: str) -> None:
    s = st["seat"]
    leg = s["leg_usd"]
    fee = leg * SPOT_FEE + leg * FUT_FEE
    st["fees_paid"] += fee
    st["owner_net"] -= (OWNER_USD / 2.0) * (SPOT_FEE + FUT_FEE)
    st["trades"].append({"ts": _now(), "action": "CLOSE", "symbol": s["symbol"],
                         "spot": spot, "fee": round(fee, 4), "why": why})
    print(f"[carry] CLOSE {s['symbol']} — {why}, fee ${fee:.2f}")
    st["seat"] = None


def credit_funding(st: dict, sym: str, rows: list[dict]) -> float:
    """Credit every settlement newer than the last one we banked. Idempotent,
    so a missed cycle loses nothing and a repeated cycle double-counts
    nothing. The SHORT leg receives when the rate is positive."""
    last = int(st["last_funding_ms"].get(sym, 0))
    seat = st["seat"]
    earned = 0.0
    newest = last
    for r in rows:
        t = int(r["fundingTime"])
        if t <= last:
            continue
        newest = max(newest, t)
        if seat and seat["symbol"] == sym:
            rate = float(r["fundingRate"])
            earned += seat["leg_usd"] * rate
            st["owner_net"] += (OWNER_USD / 2.0) * rate
            st["settlements"] += 1
    st["last_funding_ms"][sym] = newest
    if earned:
        st["funding_collected"] += earned
        print(f"[carry] funding {sym}: {earned:+.4f} USD banked")
    return earned


def report(st: dict, quotes: dict, spot_now: dict) -> None:
    net = st["funding_collected"] - st["fees_paid"]
    days = max((datetime.now(timezone.utc)
                - datetime.fromisoformat(st["created"] + "T00:00:00+00:00")).days, 1)
    # Annualising a few days of a trade whose income arrives 3x a day produces
    # theatre, not information: the entry fee lands on day 1 and the first
    # funding does not, so day 1 always reads like a catastrophe. Hold it back
    # until there is enough elapsed time for the number to mean anything.
    MIN_DAYS_FOR_APR = 14
    apr = ((net / st["capital"]) * (365 / days)
           if st["capital"] and days >= MIN_DAYS_FOR_APR else None)
    seat = st["seat"]
    L = ["# Funding carry (paper)", "",
         f"Updated {_now()}. Paper book, no keys, no orders. "
         f"Capital ${st['capital']:,.0f} (study floor); the owner's real "
         f"${OWNER_USD:.0f} tracked alongside to show the size effect.", "",
         f"- **Net ${net:+.2f}** = ${st['funding_collected']:+.2f} funding "
         f"collected, ${st['fees_paid']:.2f} fees paid",
         (f"- Annualised on capital so far: **{apr*100:+.1f}%** over {days} days"
          if apr is not None else
          f"- Annualised: held back until day {MIN_DAYS_FOR_APR} "
          f"({days} so far) — too few settlements to annualise honestly"),
         f"- Funding settlements banked: {st['settlements']}",
         f"- Same strategy on the owner's ${OWNER_USD:.0f}: "
         f"**${st['owner_net']:+.4f}**",
         ""]
    if seat:
        L.append(f"**Open:** {seat['symbol']} — ${seat['leg_usd']:,.0f} spot long "
                 f"+ ${seat['leg_usd']:,.0f} perp short, opened {seat['opened']}, "
                 f"entry trailing {seat['entry_apr']*100:.1f}% APR on the leg.")
    else:
        L.append("**Flat.** No seat: trailing funding is below the entry bar.")
    L += ["", "| symbol | trailing 7d APR (perp leg) | on capital | spot |",
          "|---|---|---|---|"]
    for sym in SYMBOLS:
        a = trailing_apr(quotes.get(sym, []))
        if a is None:
            L.append(f"| {sym} | no data | | |")
        else:
            L.append(f"| {sym} | {a*100:+.1f}% | {apr_on_capital(a)*100:+.1f}% | "
                     f"{spot_now.get(sym) or 0:,.2f} |")
    L += ["", f"Entry bar {ENTER_APR*100:.2f}% APR on capital (derived: a "
          f"{ROUND_TRIP*100:.2f}% round trip paid back inside "
          f"{BREAKEVEN_DAYS} days), exit at "
          f"{EXIT_APR*100:.0f}%, {LOOKBACK} settlements (7d) trailing. "
          f"Fees: spot {SPOT_FEE*100:.3f}% + futures {FUT_FEE*100:.3f}% per "
          f"side, VIP0 with the BNB discount.",
          "",
          "**Pre-registered judgement:** this book is judged on NET dollars "
          "after fees at 2026-12-11 (three months) or 30 funding settlements, "
          "whichever is later. Below break-even it is retired like the surge "
          "lane was. The study's honest expectation is 3-8% APR, so on "
          f"${st['capital']:,.0f} that is ${st['capital']*0.03/4:.0f}-"
          f"${st['capital']*0.08/4:.0f} a quarter. It is not a moonshot; it "
          "is the only member of the verified-winner family that fits."]
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[:12]))


def main() -> int:
    st = load()
    quotes = {s: funding_history(s) for s in SYMBOLS}
    if not any(quotes.values()):
        print("[carry] no funding data (fapi geo-block or outage) — skipping "
              "cycle, nothing lost; settlements are credited from history")
        return 0

    # bank funding first, so a settlement is never lost to an exit this cycle
    for sym, rows in quotes.items():
        if rows:
            credit_funding(st, sym, rows)

    spot_now = {s: binance_data.price(s) for s in SYMBOLS}
    seat = st["seat"]
    if seat:
        apr = trailing_apr(quotes.get(seat["symbol"], []))
        px = spot_now.get(seat["symbol"])
        if apr is not None and apr_on_capital(apr) < EXIT_APR and px:
            close_seat(st, px, f"trailing funding {apr*100:.1f}% APR on the "
                               f"leg, below the exit line")
    else:
        sym, apr = pick(quotes)
        px = spot_now.get(sym) if sym else None
        if sym and px:
            open_seat(st, sym, px, apr)
        else:
            print(f"[carry] flat — best trailing {apr*100:.1f}% APR on the leg, "
                  f"under the {ENTER_APR*100:.0f}% bar on capital")

    st["history"].append({"date": _now()[:10],
                          "net": round(st["funding_collected"] - st["fees_paid"], 4),
                          "seat": st["seat"]["symbol"] if st["seat"] else None})
    st["history"] = st["history"][-400:]
    st["last_updated_utc"] = _now()
    save(st)
    report(st, quotes, spot_now)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
