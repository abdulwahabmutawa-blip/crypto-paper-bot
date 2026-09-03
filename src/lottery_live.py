"""Lottery Live — the owner's explicitly-sacrificial real-money book.

Bot #13, and deliberately NOT the pilot: real Binance spot, one seat,
armed only by the owner's keys + LOTTERY_LIVE=1. Pre-registered 2026-08-15
with the owner's stated intent verbatim: "explode or burn — mostly
explode". The documented base rate says burn; this file makes the attempt
mechanical and honest. NO BOOK CAP as of 2026-08-16 (owner decision): every
BUY spends the account's full free USDT balance — see binance_live.py.

Selector (mechanical, no discretion anywhere):
  1. Watcher's euphoric CRYPTO symbols (same source as the hypecrypto paper
     twin), freshest scan only (<= 3h — ENTRY_FRESH_H, shared with the
     twin) — and ONLY while the watcher path has EARNED entry rights on the
     twin's rolling paper record (binance_live.watcher_earned; owner
     decision 2026-08-19 after the path went 0-for-7 for -$10.95, every
     loss this book had ever taken). The Watcher's risk-officer roles are
     untouched; only its power to open real positions is gated.;
  2. the Scout's ranked signals — but ONLY candidates whose signal type has
     EARNED the `actionable` flag on the Scout's own scorecard (see
     binance_scout.signal_actionable). Unproven signals are logged and
     displayed, never traded: the 08-16 autopsy showed every scout signal
     type losing to fees at the book's horizon, so real money waits for a
     signal type to prove itself under the current ruleset.
  3. EVERY pick, from any source, then passes the LATE-ENTRY GUARD at the
     moment of purchase (binance_live.late_entry): already +25% on the day,
     or red on the hour, means the pump being described already happened —
     the trade autopsy of this book's first four real entries (COW -11.2%
     bought 9h after its top; CHIP -7.8% bought AT its top) is the
     evidence. Grok's "euphoric" trails price by construction; the guard
     is what turns "the crowd is loud" into "and the move is still alive".

Exits run EVERY cycle (~10 min) off live Binance prices, because Grok scans
land at most every 8h and anything gated on a fresh scan reacts long after
a pump has rolled over. Price is free, instant and 24/7, so price owns the
fast exits and the Watcher owns the slow qualitative ones:
  1. -10% hard stop from entry
  2. progressive trailing stop from the high-water mark (-15% while small,
     tightening to -8% past +100% — binance_live.trail_pct)  <- anti-crash
  3. FUEL GONE (08-21, replaced the stall clock): volume surge dead vs
     pre-entry baseline AND under +3% AND no breadth wave — thesis-based,
     not clock-based (binance_live.fuel_verdict)
  3b. CLIMAX (08-23): red 1h close on the move's max volume closing in the
     lower half of its range — the top being distributed in real time
     (binance_live.climax_verdict; 8/10 forensic autopsies + AXS live)
  3c. TERMINAL DIP (08-23): 3 post-entry hourly closes >=12% under the
     high-water — 82% of such dips were the top (binance_live.
     terminal_dip_verdict)
  4. max hold as a SAFETY NET behind the tape exits: ignition 48h, other
     scout seats 24h, hype 24h, revival 28d (REVAMP 08-23; exit_params)
  Entry-side REVAMP 08-23 (REVAMP_2026-08-23.md): circuit breaker (2 losing
  exits or -10% of peak in a UTC day), API-burst freeze, depth gate,
  unlock-cliff veto, regime gate (revival stands down on wave days), and a
  hardened learning gate (4x fees, both halves, payoff shape).
  5. momentum gone: no longer a top-25 24h mover
  6. Watcher SEVERE, or scans stale > 24h (a blind risk officer grounds it)
  7. hype faded on a NEWER scan (Watcher-sourced entries)
Up to 3 entries per UTC day, any day — crypto trades 24/7. Full-balance
sizing: this book YOLOs its whole balance by design.

THE BOT MANAGES ONLY WHAT THE BOT BOUGHT. This runs on the owner's real
account, which already holds ~23 other coins; the bot records the exact
filled quantity of its own seat and can never sell more than that, and it
never adopts a balance it did not buy. Crash recovery reads the LEDGER (a
BUY fill with no matching exit), not the balance sheet.
REAL MONEY. Not investment advice — the opposite: the odds are printed on
the ticket.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import config
import binance_live
from sentinel_trader import scan_age_hours, scan_is_stale
from hype_crypto_tracker import crypto_candidates, ENTRY_FRESH_H

STATE = config.DATA / "lottery_state.json"
SENTINEL = config.DATA / "sentinel_state.json"
# Per-seat stop/stall/max-hold live in binance_live.exit_params(): the
# explosion study split the prey into species with incompatible clocks —
# hype spikes (hours), scout bursts (minutes-to-hours), and wave grinds
# (median 26 DAYS trough->peak at 2y scale, which the old universal 24h
# clock would force-sell on day one, guaranteeing the book could never
# hold a winner). The trailing stop is PROGRESSIVE — binance_live.
# trail_pct(): -15% while small, -10% past +50%, -8% past +100% — because
# the study's retention gradient says big gains die most completely.
STALL_MIN_GAIN = 0.03   # legacy name; the fuel-gone check now carries this
                        # threshold as binance_live.FUEL_MIN_GAIN


def wave_fresh() -> bool:
    """Is a breadth wave active on FRESH data right now? Used by the
    fuel-gone exit as its market-pulse input: a wave regime holds seats
    (coins re-ignite), so a stale or missing breadth file must read as
    'no wave' — failing toward the exit being ALLOWED, i.e. the old
    conservative behavior, never toward an indefinite hold."""
    try:
        bd = json.loads((config.DATA / "breadth.json").read_text())
        hist = bd.get("history") or []
        fresh = hist and (datetime.now(timezone.utc) - datetime.fromisoformat(
            hist[-1]["ts"])).total_seconds() < 2700
        return bool(fresh and bd.get("wave"))
    except Exception:
        return False
# Re-entry cooldown after ANY protective exit (audit 08-15: the old
# blacklist was keyed on the Watcher's scan_ts — meaningless for scout
# entries, and only the hard stop set it, so a trailing-stopped coin could
# be rebought the very next 5-minute cycle while still crashing).
COOLDOWN_H = 3.0
# Crypto trades 24/7 — the weekday-only rule was inherited from a book whose
# universe collapsed to crypto-only at weekends while equities were shut.
# That reasoning does not transfer to a crypto-native book: weekend hype is
# real hype, and every exit already runs 24/7 anyway.
WEEKEND_ENTRIES = True
MAX_ENTRIES_PER_DAY = 3
STABLES = {"USDC", "FDUSD", "TUSD", "DAI", "EUR", "USDP", "BUSD"}
KEY = "lottery"


def scout_candidates(max_age_min: float = 30.0) -> list[dict]:
    """The Scout's ranked opinion, if it is fresh enough to act on.

    Read-only handoff through a file: the Scout cannot trade and this book
    cannot scan, so neither can break the other. A stale signals file (the
    Scout crashed, or the cycle is running without it) yields an empty list
    rather than a stale trade — the same rule the Watcher gets."""
    p = config.DATA / "scout_signals.json"
    if not p.exists():
        return []
    try:
        d = json.loads(p.read_text())
        age = (datetime.now(timezone.utc)
               - datetime.fromisoformat(d["ts"])).total_seconds() / 60.0
    except Exception:
        return []
    if age > max_age_min:
        print(f"[{KEY}] scout signals {age:.0f}min old — ignoring")
        return []
    return d.get("candidates") or []


# top_gainer() removed 2026-08-16: the naive top-24h-gainer fallback was
# dead code since the Scout superseded it, and its one live pick (the LINK
# entry) plus its philosophy ("buy whatever already ran the furthest") is
# exactly the late-chasing the autopsy showed losing. in_top_gainers stays —
# the momentum-decay EXIT is a different question from entry selection.


def in_top_gainers(symbol: str, n: int = 10) -> bool:
    d = binance_live._call("GET", "/v3/ticker/24hr")
    if not isinstance(d, list):
        return True   # feed failure must not force a panic exit
    ranked = sorted(
        (t for t in d if t.get("symbol", "").endswith("USDT")
         and t["symbol"][:-4] not in STABLES
         and float(t.get("quoteVolume", 0) or 0) > 20_000_000),
        key=lambda t: float(t.get("priceChangePercent", 0) or 0), reverse=True)
    return symbol in {t["symbol"] for t in ranked[:n]}


def main():
    now = datetime.now(timezone.utc)
    today = str(now.date())

    if not binance_live.armed():
        print(f"[{KEY}] not armed (needs BINANCE_LIVE keys + LOTTERY_LIVE=1) "
              f"— skipping")
        return

    sent = json.loads(SENTINEL.read_text()) if SENTINEL.exists() else {"scans": []}
    scan = sent["scans"][-1] if sent["scans"] else None
    prev_scan = sent["scans"][-2] if len(sent.get("scans", [])) > 1 else None
    scan_ts = scan["ts"] if scan else ""
    age_h = scan_age_hours(scan)
    stale = scan_is_stale(scan)
    fresh = age_h is not None and age_h <= ENTRY_FRESH_H
    severe = bool(scan and scan.get("risk_level") == "severe")

    st = json.loads(STATE.read_text()) if STATE.exists() else {
        "created": today, "held_symbol": None, "entry_price": None,
        "units": 0.0, "entry_scan_ts": None, "entry_source": None,
        "stopped": {}, "entries": {}, "realized": []}

    # TURBO MODE (owner-directed 2026-08-28): a data/TURBO_MODE file in the
    # repo (same phone-operable pattern as KILL_SWITCH) flips the book from
    # gate-disciplined to best-score hunting: the learning gate turns
    # advisory (rows keep logging, records keep building), budget 8/day,
    # cooldown 1h, LATE cap 25%, and a held seat rotates into a candidate
    # scoring 25%+ above its own. Floor, stops, ratchet, vetoes, severe/
    # stale grounding and the watcher bench all stay. Pre-registered
    # evaluation in LOTTERY_CRITERIA.md; delete the file to revert.
    turbo = (config.DATA / "TURBO_MODE").exists()
    if turbo:
        print(f"[{KEY}] TURBO MODE active — gate advisory, hunting best score")

    def _turbo_rank(cands: list) -> list:
        """Best score first — with one demotion learned from the 08-28
        Oracle cohort study: symbols in the serial-exploder top quartile
        (explosion_history n >= 6) ranked LAST among candidates, because
        the highest-history quartile locked +50% at 16% vs 28% for
        modest-history coins this regime — the prior ran backwards. A
        demotion, not a block: if nothing else is on the board they can
        still be taken. In-sample caveat applies; turbo's own 20-RT
        pre-registered evaluation judges this along with everything else."""
        try:
            _eh = json.loads((config.DATA / "explosion_history.json")
                             .read_text()).get("symbols", {})
        except Exception:
            _eh = {}
        return sorted(cands, key=lambda c: (
            (_eh.get(c["symbol"], {}).get("n", 0) >= 6),
            -(c.get("score") or 0.0)))

    bals = binance_live.balances()
    if not bals:
        print(f"[{KEY}] could not read balances — cycle skipped")
        return

    # LEDGER RECONCILIATION, every cycle — never from the balance sheet.
    #
    # THE BOT MANAGES ONLY WHAT THE BOT BOUGHT (the account holds ~23 other
    # coins). The ledger is the record of that. Audit 08-15 rewrote this
    # from a recover-only-when-stateless scan into a full reconciliation,
    # closing two critical holes:
    #   * a SELL whose "fill" line landed but whose "exit" line (or the
    #     state write) was lost to a crash left the old scan re-adopting an
    #     ALREADY-SOLD seat — whose next exit would sell the owner's own
    #     holding of that coin up to `units`. A SELL fill now closes the
    #     seat in the scan, and a state seat the ledger says is closed is
    #     cleared loudly (the phantom-seat self-heal).
    #   * an unconfirmed order (POST timed out after the exchange accepted
    #     it) is surfaced as a marker the owner can see in the ledger.
    ledger_open = None          # last BUY fill with no closing SELL/exit
    unconfirmed = None          # last BUY whose POST timed out, unresolved
    last_stop_placed = None     # last stop this book rested, uncancelled
    if binance_live.LEDGER.exists():
        for line in binance_live.LEDGER.read_text(encoding="utf-8").splitlines():
            try:
                e = json.loads(line)
            except Exception:
                continue
            ev = e.get("event")
            if ev == "fill" and e.get("action") == "BUY":
                ledger_open = e
                last_stop_placed = None
                if unconfirmed and unconfirmed.get("symbol") == e.get("symbol"):
                    unconfirmed = None
            elif ev == "order_unconfirmed" and e.get("action") == "BUY" \
                    and e.get("client_order_id"):
                unconfirmed = e
            elif ev == "order_unconfirmed_resolved" and unconfirmed \
                    and e.get("client_order_id") == unconfirmed.get("client_order_id"):
                unconfirmed = None
            elif ev == "stop_placed" and ledger_open \
                    and e.get("symbol") == ledger_open.get("symbol"):
                last_stop_placed = e
            elif ev in ("stop_cancelled", "stop_orphan_found") and last_stop_placed \
                    and str(e.get("order_id")) == str(last_stop_placed.get("order_id")):
                last_stop_placed = None if ev == "stop_cancelled" else last_stop_placed
            elif ledger_open and e.get("symbol") == ledger_open.get("symbol") \
                    and (ev == "exit"
                         or (ev == "fill" and e.get("action") == "SELL")):
                ledger_open = None
                last_stop_placed = None
    # UNCONFIRMED BUY (review 2026-09-02): a POST that timed out AFTER the
    # exchange accepted it used to leave the whole book in a coin the state
    # called CASH — no stop, no exit rule, and by the "never adopt what the
    # bot did not buy" rule, never sold. Orders now carry a client id, so
    # the exchange is simply asked.
    if unconfirmed and not ledger_open and not st["held_symbol"]:
        _sym, _cid = unconfirmed["symbol"], unconfirmed["client_order_id"]
        _o = binance_live.order_by_client(_sym, _cid)
        _status = str((_o or {}).get("status", ""))
        if _status == "FILLED":
            _q = float(_o.get("executedQty") or 0)
            _quote = float(_o.get("cummulativeQuoteQty") or 0)
            if _q > 0 and _quote > 0:
                _ts = None
                try:
                    _ts = datetime.fromtimestamp(
                        float(_o.get("time")) / 1000, tz=timezone.utc
                    ).isoformat(timespec="seconds")
                except Exception:
                    _ts = now.isoformat(timespec="seconds")
                _fill = {"price": _quote / _q, "qty": _q,
                         "order_id": str(_o.get("orderId", "")),
                         "client_order_id": _cid, "commission": 0.0,
                         "commission_asset": ""}
                binance_live.log({"event": "fill", "action": "BUY",
                                  "symbol": _sym, **_fill,
                                  "note": "recovered: the POST timed out "
                                          "after the exchange filled it"})
                ledger_open = {"symbol": _sym, "price": _fill["price"],
                               "qty": _q, "ts": _ts}
                print(f"[{KEY}] RECOVERED unconfirmed BUY {_sym} "
                      f"{_q} @ {_fill['price']:.8g}")
        elif _status in ("NEW", "PARTIALLY_FILLED"):
            binance_live.cancel_by_client(_sym, _cid)
            binance_live.log({"event": "order_unconfirmed_resolved",
                              "symbol": _sym, "client_order_id": _cid,
                              "status": _status, "note": "still open — cancelled"})
        elif _o is not None or binance_live.LAST_ERROR.get("code") == -2013:
            # -2013 = order does not exist: the POST never reached the book
            binance_live.log({"event": "order_unconfirmed_resolved",
                              "symbol": _sym, "client_order_id": _cid,
                              "status": _status or "not_found"})
    if st["held_symbol"] and (not ledger_open
                              or ledger_open.get("symbol") != st["held_symbol"]):
        binance_live.log({"event": "reconciled_closed_seat",
                          "symbol": st["held_symbol"],
                          "note": "ledger says this seat was already sold; "
                                  "state file was stale (crash window)"})
        print(f"[{KEY}] RECONCILED: ledger says {st['held_symbol']} was "
              f"already closed — clearing the stale seat")
        st["held_symbol"] = st["entry_price"] = st["entry_scan_ts"] = None
        st["entry_source"] = None
        st.pop("fade_flagged", None)
        st["units"] = 0.0
        st["spent_usd"] = None
        st.pop("hwm", None)
        st.pop("entry_time", None)
        for _k in ("move_max_qv", "move_qv_sum", "move_qv_n",
                   "move_last_ms"):
            st.pop(_k, None)
    if not st["held_symbol"] and ledger_open:
        st["held_symbol"] = ledger_open["symbol"]
        st["entry_price"] = ledger_open.get("price")
        st["units"] = ledger_open.get("qty", 0.0)
        st["hwm"] = ledger_open.get("price")
        st["entry_time"] = ledger_open.get("ts")
        st["entry_scan_ts"], st["entry_source"] = scan_ts, "recovered"
        binance_live.log({"event": "recovered_from_ledger",
                          "symbol": st["held_symbol"], "units": st["units"]})
        print(f"[{KEY}] recovered unfinished seat {st['held_symbol']} "
              f"from the ledger (state file had lost it)")
    # LOST STOP RECORD (review 2026-09-02): a crash between placing the
    # resting stop and writing state leaves an order the state does not
    # know about. If it then FILLS, nothing in openOrders remembers it and
    # the seat wedges open forever ("nothing sellable"). The ledger does
    # remember: re-adopt the last uncancelled stop_placed for this seat.
    if st["held_symbol"] and not (st.get("stop_order") or {}).get("order_id") \
            and last_stop_placed and last_stop_placed.get("symbol") == st["held_symbol"] \
            and last_stop_placed.get("order_id"):
        st["stop_order"] = {"order_id": str(last_stop_placed["order_id"]),
                            "stop": last_stop_placed.get("stop"),
                            "limit": last_stop_placed.get("limit"),
                            "qty": last_stop_placed.get("qty"),
                            "recovered": True}
        binance_live.log({"event": "stop_record_recovered",
                          "symbol": st["held_symbol"],
                          "order_id": st["stop_order"]["order_id"]})
        print(f"[{KEY}] re-adopted resting stop {st['stop_order']['order_id']} "
              f"from the ledger (state file had lost it)")

    # SEAT CLOSED OUTSIDE THE BOT (2026-09-03: the owner sold BERAUSDT by
    # hand during the VPS outage). If the exchange holds none of the seat's
    # base asset, free OR locked, the position is gone: clear the seat with
    # a ledger event instead of trying to sell coins that are not there
    # (which would log sell_blocked every cycle and freeze entries on a
    # phantom -100% valuation). No realized row: the bot did not sell it.
    if st["held_symbol"]:
        _base = st["held_symbol"][:-4]
        _bv = binance_live.balances_valuation(st["held_symbol"])
        # the exchange OMITS assets with a zero balance: a missing key on a
        # non-empty account read means zero, not unknown. Anything under 1%
        # of the recorded units is dust the bot cannot sell either.
        _have = (_bv.get(_base, 0.0) if _bv else None)
        if (_have is not None
                and _have < max(1e-9, 0.01 * float(st.get("units") or 0.0))
                and not (st.get("stop_order") or {}).get("order_id")):
            binance_live.log({"event": "reconciled_external_close",
                              "symbol": st["held_symbol"],
                              "units": st.get("units"), "remaining": _have,
                              "note": "exchange holds none of this asset — "
                                      "seat was closed outside the bot"})
            print(f"[{KEY}] {st['held_symbol']} is no longer in the account "
                  f"— seat closed outside the bot; clearing it")
            st["stopped"][st["held_symbol"]] = now.isoformat(timespec="seconds")
            st["held_symbol"] = st["entry_price"] = st["entry_scan_ts"] = None
            st["entry_source"] = None
            st["units"] = 0.0
            st["spent_usd"] = None
            for _k in ("hwm", "entry_time", "entry_fee_usd", "fade_flagged",
                       "stop_order", "move_max_qv", "move_qv_sum",
                       "move_qv_n", "move_last_ms"):
                st.pop(_k, None)

    held = st["held_symbol"]

    def _retire_stop() -> None:
        """Cancel and forget the resting protective stop, if any.

        Falls back to ASKING the exchange when the state file has no id.
        The state file and the exchange can disagree -- a crash between
        placing an order and writing state leaves an order nobody remembers
        -- and an orphan stop is not harmless: it holds the units a market
        sell needs, and it can still fire days later against a seat the book
        closed long ago. The exchange, not the state file, is the authority
        on what is actually resting.
        """
        so = st.get("stop_order") or {}
        oid = so.get("order_id")
        if not oid and binance_live.exchange_stops_armed():
            found = binance_live.resting_stop(held)
            oid = str(found.get("orderId", "")) if found else None
            if oid:
                binance_live.log({"event": "stop_orphan_found",
                                  "symbol": held, "order_id": oid})
        if oid:
            binance_live.cancel_stop(held, oid)
        st.pop("stop_order", None)

    def _stop_filled() -> dict | None:
        """Did the resting stop trigger between cycles? Returns a fill dict
        shaped like market()'s, or None.

        Checked BEFORE any exit rule runs: if the exchange already sold the
        seat, every downstream rule is reasoning about a position that is
        not there, and the market-sell path would find nothing sellable and
        wedge the seat open forever.
        """
        so = st.get("stop_order") or {}
        oid = so.get("order_id")
        if not oid or not binance_live.exchange_stops_armed():
            return None
        o = binance_live.order_status(held, oid)
        if not o:
            return None
        status = str(o.get("status", ""))
        if status in ("NEW", "PARTIALLY_FILLED"):
            # STRANDED STOP-LIMIT (review 2026-09-02): once a STOP_LOSS_LIMIT
            # triggers, Binance reports it as a WORKING limit order (status
            # still NEW, isWorking true). If the market is now below that
            # limit — the AXS-style sweep the stop existed for — the order sits
            # above the bid forever, the units stay locked, and the seat has
            # no protection at all. Cancel it so this cycle's poll rules can
            # market-sell; the limit leg is a price, the fill is the point.
            if o.get("isWorking") and "LIMIT" in str(o.get("type", "")):
                lim = float(o.get("price") or 0)
                px = binance_live.price(held)
                if lim and px and px < lim:
                    binance_live.log({"event": "stop_stranded", "symbol": held,
                                      "order_id": str(oid), "limit": lim,
                                      "market": px})
                    print(f"[{KEY}] resting stop on {held} triggered but its "
                          f"limit {lim} is above market {px} — cancelling so "
                          f"the poll exit can sell")
                    if binance_live.cancel_stop(held, oid):
                        st.pop("stop_order", None)
            return None            # still resting / still working
        if status != "FILLED":
            # CANCELED / EXPIRED / REJECTED: the protection is gone but the
            # seat is not. Forget it and let this cycle re-place one.
            st.pop("stop_order", None)
            return None
        qty = float(o.get("executedQty", 0) or 0)
        quote = float(o.get("cummulativeQuoteQty", 0) or 0)
        if qty <= 0 or quote <= 0:
            st.pop("stop_order", None)
            return None
        st.pop("stop_order", None)
        return {"price": quote / qty, "qty": qty,
                "order_id": str(oid), "commission": 0.0,
                "commission_asset": ""}

    def _sync_stop(entry_px, hwm_px, stop_pct) -> None:
        """Keep a resting stop at the floor the poll rules would defend.

        Purely additive: every poll-based exit still runs this cycle and
        next. If anything here fails the book is exactly as protected as it
        was before this feature existed.
        """
        if not binance_live.exchange_stops_armed():
            return
        floor = binance_live.protective_floor(entry_px, hwm_px, stop_pct)
        units = float(st.get("units") or 0.0)
        if not floor or units <= 0:
            return
        so = st.get("stop_order") or {}
        cur = float(so.get("stop") or 0.0)
        # The floor ratchets UP as a winner rises; re-placing on every tick
        # of that climb is pure API churn, so move only on a real change.
        if cur and abs(floor - cur) / cur <= binance_live.STOP_REPLACE_EPS:
            return
        if so.get("order_id"):
            if not binance_live.cancel_stop(held, so["order_id"]):
                return          # could not clear the old one: do not stack
            st.pop("stop_order", None)
        else:
            # Nothing recorded -- but the exchange may still be holding an
            # order this book has forgotten. Clear it before placing, or the
            # seat ends up under two stops locking the same units.
            _retire_stop()
        placed = binance_live.place_protective_stop(held, units, floor)
        if placed:
            st["stop_order"] = placed

    def sell(reason: str, prefilled: dict | None = None) -> bool:
        """prefilled = a sale the EXCHANGE already executed (a resting
        protective stop that triggered between cycles). The position is
        already gone; everything after the order placement — the realized
        record, the ledger exit, the cooldown stamp, clearing the seat — is
        identical, so it runs through this one path rather than a parallel
        bookkeeping copy that could drift out of step with it."""
        base = held[:-4]
        if prefilled:
            # Cancel nothing, sell nothing, guard nothing: the units are
            # already sold. Skip straight to recording it.
            return _book_exit(reason, prefilled)
        # Sell ONLY what this bot bought. Selling the whole free balance
        # would liquidate coins the owner already held in the same account
        # (they hold 23 assets) — the bot's units are the ceiling, the
        # exchange balance only caps it lower if something is missing.
        owned = float(st.get("units") or 0.0)
        if owned <= 0:
            print(f"[{KEY}] no recorded units for {held} — refusing to sell "
                  f"a balance this bot did not buy")
            return False
        why = binance_live.guard("SELL", held, bals, held, owned)
        if why:
            binance_live.log({"event": "refused", "action": "SELL",
                              "symbol": held, "reason": why})
            print(f"[{KEY}] SELL refused: {why}")
            return False
        # REVIEW 2026-09-02 (critical): a resting protective stop LOCKS the
        # seat's units. Sizing from the cycle-start free balance read 0 the
        # moment a stop rested, so every poll exit (ratchet, climax, fuel,
        # max-hold, even the -6% stop on a gap) silently no-op'd — and on an
        # account that also holds the owner's own coins of the same asset,
        # min(owned, free) would have sold THEIR coins and forgotten ours.
        # Order now: retire the stop FIRST, then re-read what is free.
        _so_id = (st.get("stop_order") or {}).get("order_id")
        _had_stop = bool(_so_id) or binance_live.exchange_stops_armed()
        _retire_stop()
        if _had_stop:
            fresh = binance_live.balances()
            qty_free = fresh.get(base, 0.0) if fresh else 0.0
        else:
            qty_free = bals.get(base, 0.0)
        sellable = min(owned, qty_free)
        if sellable <= 0 and _so_id:
            # Nothing free even after the cancel: the stop may have FILLED in
            # the gap (the cancel then fails against a closed order). Ask.
            o = binance_live.order_status(held, _so_id)
            if o and str(o.get("status", "")) == "FILLED":
                q = float(o.get("executedQty", 0) or 0)
                quote = float(o.get("cummulativeQuoteQty", 0) or 0)
                if q > 0 and quote > 0:
                    return _book_exit(
                        f"PROTECTIVE STOP filled at the exchange before "
                        f"this rule ({reason[:40]})",
                        {"price": quote / q, "qty": q, "order_id": str(_so_id),
                         "commission": 0.0, "commission_asset": ""})
        # mainnet lot steps (binance_broker's cache is testnet's — different)
        info = binance_live._call("GET", "/v3/exchangeInfo", {"symbol": held})
        step = 0.0
        for f in ((info or {}).get("symbols") or [{}])[0].get("filters", []):
            if f.get("filterType") == "LOT_SIZE":
                step = float(f.get("stepSize", 0) or 0)
        qty = binance_live._down_to(sellable, step) if step > 0 else sellable
        if qty <= 0:
            binance_live.log({"event": "sell_blocked", "symbol": held,
                              "reason": f"no free units to sell (owned "
                                        f"{owned}, free {qty_free}) — {reason[:60]}"})
            print(f"[{KEY}] nothing sellable in {base} — skip")
            return False
        fill = binance_live.market("SELL", held, qty=qty)
        if not fill:
            return False
        return _book_exit(reason, fill)

    def _book_exit(reason: str, fill: dict) -> bool:
        """Record a completed sale: realized row, ledger exit, cooldown,
        seat cleared. Shared by the market-sell path and the exchange-stop
        path so the two can never disagree about what an exit looks like."""
        entry_px = st.get("entry_price")
        exit_px = fill["price"]
        u = float(st.get("units") or 0.0)
        pnl = ((exit_px / entry_px - 1) * 100) if entry_px else None
        # spent priced on the SOLD qty, not the recorded units: lot-step
        # truncation left dust that turned +1.6% winners into -$0.02 rows
        # (review 08-23) and would have tripped the circuit breaker
        spent = round(entry_px * fill["qty"], 4) if entry_px else None
        got = round(exit_px * fill["qty"], 4)
        # FEES NETTED (owner sign-off 2026-09-03): $2.64 of commissions were
        # invisible to pnl_usd, the breaker and every pre-registered test.
        fees = float(st.get("entry_fee_usd") or 0.0) + binance_live.fee_usd(
            fill, held, exit_px)
        pnl_usd = round(got - spent - fees, 4) if spent is not None else None
        rec = {"symbol": held,
               # source recorded since 08-19: the per-source review had to
               # reconstruct it from git history of the state file, and the
               # answer (watcher 0/6 -$7.90, scout +$0.94) was too important
               # to keep excavating
               "source": st.get("entry_source"),
               "entry_score": st.get("entry_score"),
               "entry_time": st.get("entry_time"),
               "exit_time": now.isoformat(timespec="seconds"),
               "entry_price": entry_px, "exit_price": exit_px,
               "units": round(u, 8), "spent_usd": spent, "got_usd": got,
               "pnl_pct": round(pnl, 2) if pnl is not None else None,
               "pnl_usd": pnl_usd, "fees_usd": round(fees, 4), "reason": reason,
               "date": today, "exit": exit_px, "entry": entry_px}
        st["realized"].append(rec)
        binance_live.log({"event": "exit", "symbol": held, "reason": reason,
                          "source": st.get("entry_source"),
                          "entry_price": entry_px, "exit_price": exit_px,
                          "pnl_pct": rec["pnl_pct"], "pnl_usd": pnl_usd})
        # EVERY exit stamps the re-entry cooldown, not just the stop family
        # (audit 08-16: the hype-faded exit didn't stamp it, so when Grok
        # flip-flopped on CHIP the book sold at 0.02827 and re-bought the
        # SAME coin at 0.03007 two hours later — a -6.4% whipsaw plus two
        # rounds of fees. Whatever the exit reason, the thesis on this coin
        # just ended; 3h of distance applies to all of them.)
        st["stopped"][held] = now.isoformat(timespec="seconds")
        st["held_symbol"] = st["entry_price"] = st["entry_scan_ts"] = None
        st["entry_source"] = None
        st["units"] = 0.0
        st["spent_usd"] = None
        st.pop("hwm", None)
        st.pop("entry_time", None)
        st.pop("entry_fee_usd", None)
        st.pop("fade_flagged", None)
        for _k in ("move_max_qv", "move_qv_sum", "move_qv_n",
                   "move_last_ms"):
            st.pop(_k, None)
        return True

    # exchange announcements (08-23): delisting = instant exit + entry veto
    try:
        announcements = json.loads(
            (config.DATA / "announcements.json").read_text(encoding="utf-8"))
    except Exception:
        announcements = None

    def _halt_state() -> tuple:
        """REVAMP 08-23 exposure caps, evaluated OUTSIDE the strategy: the
        daily circuit breaker (2 losing exits or -10% of peak per UTC day)
        and the API-burst freeze. Returns (breaker_why, burst_why, halt_why).

        Called BEFORE the exit rules (the turbo hop may not fire while
        halted) and AGAIN before the entry lane (a losing exit this cycle
        can be today's second and must halt this same cycle's entry).

        INCIDENT 2026-09-01: the golden-ticket commit (ad621af1e) made the
        turbo-hop rule read `halt_why` here, while the variable was only
        assigned further down in the entry section. Every cycle that held a
        seat under TURBO_MODE died with UnboundLocalError after the exit
        rules and before the state write — the dashboard froze at the
        BERAUSDT buy (01:06 UTC) and no resting stop was ever synced. The
        cycle test in tests/test_lottery_cycle.py now runs main() end to end
        against a mocked exchange so this class of bug cannot ship again.
        """
        # ROLLING 24h (owner sign-off 2026-09-03): the UTC-date window gave
        # 6h/11h/22h of cooling-off after the three halts.
        _win = []
        for t in st.get("realized", []):
            try:
                _dt = datetime.fromisoformat(str(t.get("exit_time")))
                if (now - _dt).total_seconds() <= 86400:
                    _win.append(t)
            except Exception:
                if t.get("date") == today:
                    _win.append(t)
        _b = binance_live.circuit_breaker_reason(_win, st.get("book_hwm_usd"))
        _u = None
        try:
            _tail = []
            if binance_live.LEDGER.exists():
                for _line in binance_live.LEDGER.read_text(
                        encoding="utf-8").splitlines()[-300:]:
                    if _line.strip():
                        _tail.append(json.loads(_line))
            _u = binance_live.api_burst_reason(_tail, now)
        except Exception:
            _u = None
        return _b, _u, (_b or _u)

    breaker_why, burst_why, halt_why = _halt_state()

    # ---- exits ----
    # These run EVERY cycle (~10 min) off live Binance prices, deliberately
    # not off the Watcher: Grok scans arrive at most every 8h, so anything
    # gated on a new scan reacts hours after a pump has already rolled over.
    # Price is free, instant, and 24/7 — so price carries the fast exits and
    # the Watcher carries the slow, qualitative ones.
    if held:
        p = binance_live.price(held)
        entry = st.get("entry_price")
        ep = binance_live.exit_params(str(st.get("entry_source") or ""))
        stop_pct = ep["stop_pct"]
        stall_h = ep["stall_h"]          # None = no stall clock (grind seat)
        max_hold = ep["max_hold_h"]

        # high-water mark, updated live
        if p:
            st["hwm"] = max(float(st.get("hwm") or p), p)
        hwm = float(st.get("hwm") or 0)
        held_h = None
        if st.get("entry_time"):
            try:
                held_h = (now - datetime.fromisoformat(
                    st["entry_time"])).total_seconds() / 3600.0
            except Exception:
                held_h = None

        # DID THE EXCHANGE ALREADY SELL THIS SEAT? Asked before every exit
        # rule, because each one below reasons about a position that may no
        # longer exist -- and the market-sell path would find nothing
        # sellable and leave the seat wedged open. This is the gap the
        # resting stop exists to cover: AXSUSDT's floor was +5.9% and the
        # poll filled it at +1.29%.
        _pf = _stop_filled()
        if _pf:
            gain = (_pf["price"] / entry - 1) if entry else 0.0
            if sell(f"PROTECTIVE STOP ({gain:+.1%} vs peak "
                    f"{((hwm / entry - 1) if entry and hwm else 0):+.1%}) — "
                    f"the floor held at the exchange, between cycles",
                    prefilled=_pf):
                held = None

        # DELISTING NOTICE (08-23): ahead of every other rule — the coin is
        # being removed; the documented path from here is -16..-33%
        _dl = binance_live.delisting_exit(held, announcements)
        if held and _dl:
            if sell(_dl):
                held = None
        if held and p and entry and p / entry - 1 <= stop_pct:
            if sell(f"STOP-LOSS ({(p / entry - 1):.1%} from entry) — "
                    f"hype that bleeds gets cut"):
                held = None
        # CLIMAX EXIT (owner-directed 08-23, playbook rule promoted early):
        # a red 1h close on the move's maximum volume, closing in the lower
        # half of its range, IS the top being distributed — 8/10 forensic
        # autopsies, and AXS's own +12.2%→+1.29% waterfall started on
        # exactly such a bar. Judged on POST-ENTRY closed candles only,
        # each folded into the move statistics exactly once, and the judged
        # candle is always compared against statistics that EXCLUDE it.
        if held and entry and st.get("entry_time"):
            try:
                _ems = int(datetime.fromisoformat(
                    st["entry_time"]).timestamp() * 1000)
            except Exception:
                _ems = None
            _kl = binance_live._call(
                "GET", "/v3/klines",
                {"symbol": held, "interval": "1h", "limit": 56}) \
                if _ems else None
            if _kl:
                import time as _time
                _now_ms = _time.time() * 1000
                _fresh = [r for r in _kl
                          if float(r[6]) < _now_ms
                          and float(r[0]) >= _ems
                          and float(r[0]) > float(st.get("move_last_ms")
                                                  or 0)]
                if _fresh:
                    _pmax = float(st.get("move_max_qv") or 0.0)
                    _psum = float(st.get("move_qv_sum") or 0.0)
                    _pn = int(st.get("move_qv_n") or 0)
                    for r in _fresh[:-1]:
                        _qv = float(r[7])
                        _pmax = max(_pmax, _qv)
                        _psum += _qv
                        _pn += 1
                    # OWNER DECISION 2026-08-31 (forensics rec 3): CLIMAX
                    # may not fire on a 2-candle-old position. UNI was sold
                    # -2.54% within 1% of the local bottom because the
                    # move's "maximum volume" was built from exactly ONE
                    # prior candle — a coin flip dressed as a distribution
                    # signal. Now needs >=4 closed post-entry candles of
                    # move history AND a ride that actually paid (MFE
                    # >= +5%), since a blow-off top presupposes a top.
                    _why = None
                    _mfe = (hwm / entry - 1.0) if (hwm and entry) else 0.0
                    if _pn >= 4 and _mfe >= 0.05:
                        _why = binance_live.climax_verdict(
                            _fresh[-1], _pmax,
                            (_psum / _pn) if _pn else 0.0)
                    _qv = float(_fresh[-1][7])
                    st["move_max_qv"] = max(_pmax, _qv)
                    st["move_qv_sum"] = _psum + _qv
                    st["move_qv_n"] = _pn + 1
                    st["move_last_ms"] = int(float(_fresh[-1][0]))
                    if _why and sell(_why):
                        held = None
                # TERMINAL DIP (REVAMP 08-23): 3 post-entry hourly closes
                # >=12% under the high-water = 82% the top, not a shakeout
                if held and p and entry and ep.get("kind") != "grind":
                    _post = [float(r[4]) for r in _kl
                             if float(r[6]) < _now_ms
                             and float(r[0]) >= _ems]
                    _td = binance_live.terminal_dip_verdict(_post)
                    if _td and sell(_td):
                        held = None
        # PROFIT RATCHET (exit audit 08-19): a ride that has paid never goes
        # red again; a ride that paid well keeps half its peak. This is the
        # asymmetry fix — winners peaked +4..8% and were round-tripping into
        # -8..-11% losses while the trailing leash waited for gains that
        # never come at this horizon.
        floor = binance_live.ratchet_stop(entry, hwm)
        if held and p and floor and p <= floor:
            if sell(f"RATCHET ({(p / entry - 1):+.1%} vs peak "
                    f"{(hwm / entry - 1):+.1%}) — a ride that paid never "
                    f"goes red again"):
                held = None
        # trailing stop: the pump gave back too much of its peak. THIS is the
        # exit that gets the book out before a hype crash instead of after.
        # Progressive: the more the ride has paid, the tighter the leash.
        tp = binance_live.trail_pct((hwm / entry - 1) if (entry and hwm)
                                    else None)
        if held and p and hwm and p / hwm - 1 <= tp:
            if sell(f"TRAILING STOP ({(p / hwm - 1):.1%} off the "
                    f"{hwm:.8g} peak, leash {tp:.0%}) — riding it down is "
                    f"not the strategy"):
                held = None
        # FUEL GONE removed 2026-09-03 (owner sign-off): 0/6, -$6.85 realized;
        # replay: a 4h clock in a volume hat (+$18 saved / -$22 given up).
        # Price rules (stop, ratchet, 10% trail, max hold) own the exit.
        # hard time cap: never marry a coin
        if held and held_h is not None and held_h >= max_hold:
            if sell(f"MAX HOLD ({held_h:.0f}h) — hype has a half-life"):
                held = None
        # NON-PRICE SIGNALS TIGHTEN THE LEASH, NEVER SELL (owner sign-off
        # 2026-09-03; replay: clock/sentiment/rotation exits gave up ~$36 vs
        # the mechanical core; Grok-stale sold WLD on an API-budget bug).
        # Momentum-gone, Watcher SEVERE, stale scans and hype-faded all set
        # fade_flagged; the 10%-off-peak leash below then lets PRICE decide.
        _flag_why = None
        if held and ep.get("momentum_exit") and not in_top_gainers(held, n=25):
            _flag_why = "no longer a top-25 24h mover"
        if held and severe:
            _flag_why = "Watcher SEVERE"
        if held and stale:
            _flag_why = "Grok scans stale"
        if (held and st.get("entry_source") == "watcher" and not stale
                and scan_ts and st.get("entry_scan_ts")
                and scan_ts > st["entry_scan_ts"]):
            hype_now = {c.replace("-USD", "") + "USDT"
                        for c in crypto_candidates(scan)}
            if held not in hype_now:
                _flag_why = "off the euphoric scan"
        if held and _flag_why and not st.get("fade_flagged"):
            st["fade_flagged"] = True
            binance_live.log({"event": "fade_tighten", "symbol": held,
                              "reason": f"{_flag_why}; leash tightened to "
                                        f"10% off peak, no market sell"})
            print(f"[{KEY}] {_flag_why} on {held} — leash 10% off peak")
        if held and st.get("fade_flagged") and p and hwm and p <= hwm * 0.90:
            if sell(f"LEASH ({(p / entry - 1):+.1%} vs peak "
                    f"{(hwm / entry - 1):+.1%}) — thesis flagged and the "
                    f"tape gave back 10%"):
                held = None

        # TURBO HOP removed 2026-09-03 (owner sign-off): hop keyed to a score
        # with corr(score, pnl) -0.02; DASH->HOME chain -$1.94.
        # The seat survived every poll rule, so leave a floor resting AT the
        # exchange to cover the ~5 minutes until the next cycle. Last, so it
        # is only ever placed on a position that is genuinely still open.
        if held:
            _sync_stop(entry, hwm, stop_pct)

    # ---- entry ----
    bals = binance_live.balances() or bals
    entries_today = st.get("entries", {}).get(today, 0)

    # WAVE-DAY ENTRY BONUS (owner-accepted 08-20): a breadth wave grants one
    # extra entry for that UTC day. Read from the scout's breadth file,
    # trusted only while fresh; once observed, the bonus sticks for the day
    # even if breadth dips back (a wave that started still happened).
    try:
        _bd = json.loads((config.DATA / "breadth.json").read_text())
        _hist = _bd.get("history") or []
        _fresh = _hist and (now - datetime.fromisoformat(_hist[-1]["ts"])
                            ).total_seconds() < 1800
        if _fresh and _bd.get("wave"):
            if st.get("wave_bonus_date") != today:
                print(f"[{KEY}] WAVE DAY — entry budget +1 for {today}")
            st["wave_bonus_date"] = today
    except Exception:
        pass
    budget = 8 if turbo else binance_live.entry_budget(
        st.get("wave_bonus_date") == today)

    # BOOK FLOOR (percentage form, owner decision 08-21): entries stop when
    # the book is 37.5%+ below its own peak value — the same protection the
    # old $25-of-$40 line encoded, now scale-free so deposits neither
    # loosen nor tighten it. Exits still run — a breach never traps a seat.
    # free+locked: a resting protective stop locks the seat's units, and
    # valuing only the free balance would read as a total loss of the
    # position and breach this very floor on a book that never lost a cent.
    # Falls back to the free-only read if the totals call fails, which is
    # the pre-feature behaviour rather than a halt.
    _val_now = binance_live.managed_value(
        (binance_live.balances_valuation(st.get("held_symbol"))
         if binance_live.exchange_stops_armed() else None) or bals,
        st.get("held_symbol"), st.get("units"))
    if _val_now is not None:
        # COST BASIS peak (owner sign-off 2026-09-03): the $58.43 peak was a
        # deposit plus AXS marked at an unrealized +12.4%; the floor, day-loss
        # and retire lines were calibrated to money never realized. Held
        # units count at their entry price; deposits still raise the peak.
        _cost_val = float(bals.get("USDT", 0.0)) + (
            float(st.get("units") or 0.0) * float(st.get("entry_price") or 0.0)
            if st.get("held_symbol") else 0.0)
        st["book_hwm_usd"] = round(
            max(float(st.get("book_hwm_usd") or 0.0), _cost_val), 4)
    floor_why = binance_live.book_floor_reason(_val_now,
                                               st.get("book_hwm_usd"))
    if floor_why and not st.get("floor_flagged"):
        st["floor_flagged"] = True
        binance_live.log({"event": "floor_breached", "value": round(_val_now, 2),
                          "reason": floor_why})
    if not floor_why:
        st.pop("floor_flagged", None)

    # REVAMP 08-23 — exposure caps enforced OUTSIDE the strategy (the one
    # mechanic every verified durable winner shares): a daily circuit
    # breaker and an exchange-health freeze sit above every entry lane.
    # Re-evaluated here, AFTER the exit rules: an exit this cycle can be
    # today's second loss and must halt this same cycle's entry.
    breaker_why, burst_why, halt_why = _halt_state()
    # GOLDEN TICKET (owner amendment 2026-08-31): "it's ok to stop for a
    # while, but a high-percentage opportunity should not be missed." The
    # loss-COUNT breaker becomes overridable for exactly ONE entry per UTC
    # day, and only for the setups whose win rate is PROVEN, not scored:
    # an actionable candidate arriving on an active breadth wave (54-64%
    # of explosions cluster there) or an actionable revival (the 2y
    # study's profile). Score is NOT a key (corr with pnl +0.09). The
    # -10% day-loss line and the API-burst freeze stay absolute.
    golden = bool(breaker_why and "losing exits" in breaker_why
                  and burst_why is None
                  and st.get("breaker_override_date") != today)
    if halt_why and held is None and st.get("halt_flagged") != halt_why[:24]:
        st["halt_flagged"] = halt_why[:24]
        binance_live.log({"event": "entries_halted", "reason": halt_why})
        print(f"[{KEY}] {halt_why}")
    if not halt_why:
        st.pop("halt_flagged", None)

    can_enter = (held is None and not (severe or stale)
                 and floor_why is None and (halt_why is None or golden)
                 and (WEEKEND_ENTRIES or now.weekday() < 5)
                 and entries_today < budget)
    if floor_why and held is None:
        print(f"[{KEY}] {floor_why}")
    if can_enter:
        # time-based cooldown: a coin exited by ANY protective rule stays
        # untouchable for COOLDOWN_H regardless of which source re-suggests
        # it — and expired entries are pruned so the dict cannot grow forever
        def _in_cooldown(ts_str) -> bool:
            try:
                return (now - datetime.fromisoformat(ts_str)
                        ).total_seconds() / 3600.0 < (1.0 if turbo
                                                       else COOLDOWN_H)
            except Exception:
                return False    # legacy scan_ts values: not parseable = expired
        st["stopped"] = {s: ts for s, ts in st.get("stopped", {}).items()
                         if _in_cooldown(ts)}
        blacklisted = set(st["stopped"])
        # Retired symbols fold into the SAME set the cooldown uses, so both
        # entry lanes (watcher and scout) are covered by the checks that
        # already exist rather than a second guard each path could forget.
        # Announced once per cycle, never per candidate: the no_pair bug
        # (08-16) showed what a per-candidate line does to the ledger.
        retired = binance_live.retired_symbols(st.get("realized"),
                                               st.get("book_hwm_usd"))
        if retired:
            blacklisted |= set(retired)
            print(f"[{KEY}] retired, will not re-enter: "
                  + ", ".join(sorted(retired)))


        def _pre_buy_veto(sym: str) -> str | None:
            """REVAMP 08-23 vetoes that must FALL THROUGH to the next candidate
            (review: running them after the pick ended the cycle's entry
            instead of trying the next coin): the exit side must absorb the
            seat (depth gate) and we never open into an unlock cliff."""
            why = binance_live.announcement_veto(sym, announcements, now)
            if why:
                return why
            _bid, _ask = binance_live.depth_5pct(sym)
            why = binance_live.depth_gate(bals.get("USDT", 0.0), _bid, _ask)
            if why:
                return why
            try:
                _u = json.loads((config.DATA / "unlocks.json")
                                .read_text(encoding="utf-8"))
                _ev = (_u.get("events") or {}).get(sym) or {}
                _days = _ev.get("days_to_unlock")
                # the file is a snapshot: age it (review 08-23 minor)
                try:
                    _age_d = (now - datetime.fromisoformat(
                        _u.get("generated_utc"))).total_seconds() / 86400.0
                    if _days is not None:
                        _days = _days - _age_d
                except Exception:
                    pass
                return binance_live.unlock_veto(_days, _ev.get("adv_ratio"))
            except Exception:
                return None

        pick, source, pick_score = None, None, 0.0
        # OWNER DECISION 2026-08-19: watcher entries only when the paper
        # twin's rolling record has earned them (see binance_live). The
        # bench announces itself once per cycle rather than spamming the
        # ledger with a standing condition.
        twin_p = config.DATA / "hypecrypto_state.json"
        try:
            twin_trades = json.loads(twin_p.read_text()).get("trades", [])
        except Exception:
            twin_trades = []
        watcher_ok, watcher_why = binance_live.watcher_earned(
            binance_live.twin_round_trips(twin_trades))
        if fresh and not watcher_ok:
            print(f"[{KEY}] watcher entries {watcher_why}")
        # Grok names coins, not exchange pairs — some have no Binance spot
        # listing at all (the ANSEM class). Probing the same dead symbol
        # every cycle wrote one Invalid-symbol ledger line per cycle for
        # four hours (08-16). Remember the misses PER SCAN: one probe, one
        # error line, then silence until a new scan names new coins.
        np = st.get("no_pair") or {}
        if np.get("scan_ts") != scan_ts:
            np = {"scan_ts": scan_ts, "syms": []}
        st["no_pair"] = np
        if fresh and watcher_ok and halt_why is None:
            for c in crypto_candidates(scan, prev_scan):
                sym = c.replace("-USD", "") + "USDT"
                if sym in blacklisted or sym in np["syms"]:
                    continue
                binance_live.LAST_ERROR.clear()
                if not binance_live.price(sym):
                    if binance_live.LAST_ERROR.get("code") == -1121:
                        np["syms"].append(sym)
                        print(f"[{KEY}] {sym} has no Binance spot pair — "
                              f"muted for the rest of this scan")
                    continue
                # the guard that was missing from this path: COW and CHIP
                # were both Watcher picks bought after their pump was over
                late = binance_live.late_entry_check(sym, wave=wave_fresh() or turbo)
                if late:
                    binance_live.log({"event": "refused", "action": "BUY",
                                      "symbol": sym, "reason": late})
                    print(f"[{KEY}] {sym} (watcher) refused: {late}")
                    continue
                veto = _pre_buy_veto(sym)
                if veto:
                    binance_live.log({"event": "refused", "action": "BUY",
                                      "symbol": sym, "reason": veto})
                    print(f"[{KEY}] {sym} (watcher) refused: {veto}")
                    continue
                pick, source = sym, "watcher"
                pick_score = 0.0
                break
        # The Scout: fast, quantitative, every cycle across all ~670 pairs.
        # It supersedes the old naive top-24h-gainer fallback, which happily
        # bought a coin that pumped six hours ago and was already rolling
        # over (the live COWUSDT case: +49% on the day, -6.5% in the hour, on
        # BELOW-average volume). The Scout requires the move to be alive now.
        if pick is None:
            _cands = scout_candidates()
            if turbo:
                _cands = _turbo_rank(_cands)
            for c in _cands:
                if c["symbol"] in blacklisted:
                    continue
                # golden-ticket mode: trading THROUGH a halt — only the
                # proven-context setups qualify, and never a coin that
                # already took today's money.
                if halt_why:
                    if not (wave_fresh() or c.get("signal") == "revival"):
                        continue
                    if str(st.get("stopped", {}).get(c["symbol"], ""))[:10]                             == today:
                        continue
                # THE GATE (autopsy 08-16): a signal type trades only after
                # its own scorecard shows it beating fees under the current
                # ruleset. Benched candidates still teach — the scout
                # resolves outcomes from its log, not from our fills.
                # OWNER DECISION 2026-08-31 (forensics rec 2): turbo lost
                # its benched-signal privilege. actionable=TRUE is a HARD
                # entry requirement in every mode. Evidence: benched-taken-
                # by-turbo went 6 trades / -$4.95 including both biggest
                # losses of the account (SOXLB -6.66%, ENA -5.25%), while
                # actionable scout trades made +$2.99 over 14. The gate was
                # right on every lane for 16 days; the only policy that
                # fought it lost. Turbo keeps its speed (8 entries/day, 1h
                # cooldown, 25% LATE cap, hop) — it just may not override
                # the scorecard.
                if c.get("signal") == "heat":
                    continue        # retired 2026-09-03: lagging, 0/2 real
                if not c.get("actionable"):     # missing/null = NOT proven
                    print(f"[{KEY}] scout {c['symbol']} ({c['signal']}) "
                          f"is on the bench — "
                          f"{c.get('status', 'unproven signal')}; logged "
                          f"for learning, not traded")
                    continue
                if not binance_live.price(c["symbol"]):
                    continue
                # REVAMP 08-23: regime gating by family — revival stands
                # down on wave days (no capitulation to rebound from)
                reg = binance_live.regime_allows(c["signal"], wave_fresh())
                if reg:
                    binance_live.log({"event": "refused", "action": "BUY",
                                      "symbol": c["symbol"], "reason": reg})
                    print(f"[{KEY}] {c['symbol']} ({c['signal']}) refused: "
                          f"{reg}")
                    continue
                late = binance_live.late_entry_check(c["symbol"], wave=wave_fresh() or turbo)
                if late:
                    binance_live.log({"event": "refused", "action": "BUY",
                                      "symbol": c["symbol"], "reason": late})
                    print(f"[{KEY}] {c['symbol']} (scout) refused: {late}")
                    continue
                veto = _pre_buy_veto(c["symbol"])
                if veto:
                    binance_live.log({"event": "refused", "action": "BUY",
                                      "symbol": c["symbol"], "reason": veto})
                    print(f"[{KEY}] {c['symbol']} (scout) refused: {veto}")
                    continue
                pick = c["symbol"]
                source = f"scout:{c['signal']}"
                pick_score = float(c.get("score") or 0.0)
                print(f"[{KEY}] scout says {c['symbol']} "
                      f"({c['signal']}, score {c.get('score')}): "
                      f"{c.get('why', '')}")
                break
        if pick:
            why = binance_live.guard("BUY", pick, bals, None)
            if why:
                binance_live.log({"event": "refused", "action": "BUY",
                                  "symbol": pick, "reason": why})
                print(f"[{KEY}] BUY refused: {why}")
            else:
                spend = bals.get("USDT", 0.0)
                fill = binance_live.market("BUY", pick, quote_qty=spend)
                if fill:
                    st["held_symbol"], st["entry_price"] = pick, fill["price"]
                    # exact filled quantity: the ONLY amount this bot may
                    # ever sell back (the account holds other coins)
                    st["units"] = fill["qty"]
                    st["spent_usd"] = round(fill["price"] * fill["qty"], 4)
                    st["entry_fee_usd"] = binance_live.fee_usd(
                        fill, pick, fill["price"])
                    # seeds the trailing stop and the hold clock
                    st["hwm"] = fill["price"]
                    # climax-exit move statistics start empty at entry
                    st["move_max_qv"] = st["move_qv_sum"] = 0.0
                    st["move_qv_n"] = 0
                    st["move_last_ms"] = 0
                    st["entry_time"] = now.isoformat(timespec="seconds")
                    st["entry_scan_ts"], st["entry_source"] = scan_ts, source
                    st["entry_score"] = pick_score
                    # rest the floor NOW, not next cycle: the 5 minutes after
                    # a fill are as exposed as any other 5 minutes
                    held = pick
                    _sync_stop(fill["price"], fill["price"],
                               binance_live.exit_params(source)["stop_pct"])
                    st.setdefault("entries", {})
                    st["entries"] = {d: c for d, c in st["entries"].items()
                                     if d >= today}
                    st["entries"][today] = entries_today + 1
                    if halt_why:
                        st["breaker_override_date"] = today
                        binance_live.log({
                            "event": "breaker_override", "symbol": pick,
                            "reason": f"golden ticket through the breaker: "
                                      f"{source}, wave={wave_fresh()}, "
                                      f"one per UTC day"})
                        print(f"[{KEY}] GOLDEN TICKET spent on {pick} "
                              f"({source}) — breaker back in force")

    # balances_valuation(), not balances(): a resting protective stop LOCKS the
    # position's units, so a free-only read prices the seat at $0 -- a
    # phantom -100% that would trip the drawdown floor and freeze entries on
    # a book that never lost anything.
    val = binance_live.managed_value(
        (binance_live.balances_valuation(st.get("held_symbol"))
         if binance_live.exchange_stops_armed()
         else binance_live.balances()) or bals,
        st["held_symbol"], st.get("units"))
    st["last_value_usd"] = round(val, 2)
    st["last_updated_utc"] = now.isoformat(timespec="seconds")

    # live snapshot of the OPEN position for the dashboard: what it cost, what
    # it is worth now, and the unrealized P/L — the numbers the owner asked to
    # see on their phone
    if st.get("held_symbol"):
        cur = binance_live.price(st["held_symbol"])
        u = float(st.get("units") or 0.0)
        # fall back to entry_price * units for seats opened before spent_usd
        # was recorded (pre-08-15 fills, or ledger-recovered ones)
        spent = st.get("spent_usd")
        if spent is None and st.get("entry_price") and u:
            spent = round(st["entry_price"] * u, 4)
        now_val = round(cur * u, 4) if cur else None
        st["open_position"] = {
            "symbol": st["held_symbol"], "entry_time": st.get("entry_time"),
            "entry_price": st.get("entry_price"), "current_price": cur,
            "units": round(u, 8), "spent_usd": spent, "value_usd": now_val,
            "pnl_usd": (round(now_val - spent, 4)
                        if (now_val is not None and spent is not None) else None),
            "pnl_pct": (round((cur / st["entry_price"] - 1) * 100, 2)
                        if (cur and st.get("entry_price")) else None),
            "source": st.get("entry_source"),
        }
    else:
        st["open_position"] = None
    # ATOMIC write (review 2026-09-02): a kill mid-write (the host event
    # class) left half a JSON file, and state_preflight then blocks EVERY
    # later cycle, exits included. Write beside, then rename over.
    _tmp = STATE.with_suffix(".json.tmp")
    _tmp.write_text(json.dumps(st, indent=2), encoding="utf-8")
    import os as _os
    _os.replace(_tmp, STATE)
    print(f"[{KEY}] {today} seat={st['held_symbol'] or 'CASH'} "
          f"book ${val:.2f} (no cap) — "
          f"ticket odds printed in the docstring")


if __name__ == "__main__":
    main()
