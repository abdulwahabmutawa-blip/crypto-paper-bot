"""Funding carry book — the invariants that would silently corrupt the record.

The dangerous failure here is not a crash, it is a quiet miscount: the fleet
re-runs this bot every few minutes, so a credit path that is not idempotent
would inflate the funding line a little on every cycle and the book would
look profitable while earning nothing. That is the first test below.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import bot_carry  # noqa: E402


def _rows(start_ms: int, n: int, rate: float):
    """n settled funding rows, 8h apart, oldest first — the shape
    /fapi/v1/fundingRate returns."""
    return [{"fundingTime": start_ms + i * 8 * 3600 * 1000,
             "fundingRate": str(rate)} for i in range(n)]


def _state(seat_symbol="BTCUSDT", leg=1000.0):
    return {"seat": {"symbol": seat_symbol, "leg_usd": leg},
            "funding_collected": 0.0, "owner_net": 0.0,
            "settlements": 0, "last_funding_ms": {}}


def test_credit_is_idempotent():
    """Re-running the same cycle must bank the funding exactly once."""
    st = _state()
    rows = _rows(1_700_000_000_000, 21, 0.0001)   # 0.01%/8h, the floor
    first = bot_carry.credit_funding(st, "BTCUSDT", rows)
    banked_once = st["funding_collected"]
    assert st["settlements"] == 21
    assert first > 0

    for _ in range(5):                            # the fleet re-runs constantly
        again = bot_carry.credit_funding(st, "BTCUSDT", rows)
        assert again == 0.0
    assert st["funding_collected"] == banked_once
    assert st["settlements"] == 21


def test_only_new_settlements_are_credited():
    """A later fetch overlapping the previous one credits just the new tail."""
    st = _state()
    start = 1_700_000_000_000
    bot_carry.credit_funding(st, "BTCUSDT", _rows(start, 10, 0.0001))
    after_first = st["funding_collected"]
    # same window plus 3 new settlements
    bot_carry.credit_funding(st, "BTCUSDT", _rows(start, 13, 0.0001))
    assert st["settlements"] == 13
    # exactly three more settlements' worth, nothing re-counted
    expected = after_first + 3 * 1000.0 * 0.0001
    assert abs(st["funding_collected"] - expected) < 1e-9


def test_negative_funding_is_a_cost_not_income():
    """The short leg PAYS when funding is negative. A sign error here would
    turn the study's documented failure mode into fake profit."""
    st = _state()
    bot_carry.credit_funding(st, "BTCUSDT", _rows(1_700_000_000_000, 3, -0.0005))
    assert st["funding_collected"] < 0
    assert st["owner_net"] < 0


def test_funding_for_a_symbol_we_do_not_hold_is_not_banked():
    """Watching ETH while holding BTC must not pay us ETH's funding."""
    st = _state(seat_symbol="BTCUSDT")
    earned = bot_carry.credit_funding(st, "ETHUSDT",
                                      _rows(1_700_000_000_000, 9, 0.0003))
    assert earned == 0.0
    assert st["funding_collected"] == 0.0
    # but the watermark still advances, so switching seats later cannot
    # retroactively claim funding from before the seat existed
    assert st["last_funding_ms"]["ETHUSDT"] > 0


def test_flat_book_banks_nothing():
    st = _state()
    st["seat"] = None
    assert bot_carry.credit_funding(st, "BTCUSDT",
                                    _rows(1_700_000_000_000, 21, 0.0001)) == 0.0
    assert st["funding_collected"] == 0.0


def test_trailing_apr_matches_the_known_floor():
    """0.01% per 8h is the documented floor = ~10.95% annualised on the leg."""
    apr = bot_carry.trailing_apr(_rows(1_700_000_000_000, 21, 0.0001))
    assert abs(apr - 0.1095) < 1e-6
    # half the capital sits in spot earning nothing
    assert abs(bot_carry.apr_on_capital(apr) - 0.05475) < 1e-6


def test_trailing_apr_needs_a_full_window():
    """Too few settlements must read None, not a confident wrong number."""
    assert bot_carry.trailing_apr(_rows(1_700_000_000_000, 5, 0.0001)) is None


def test_entry_bar_is_derived_from_the_fee_model():
    """The bar must be 'round trip paid back inside BREAKEVEN_DAYS', not a
    hardcoded guess — a guessed 4% bar sat flat against a live 2.4% regime."""
    assert abs(bot_carry.ROUND_TRIP - 0.0012) < 1e-9
    expected = 0.0012 * 365 / bot_carry.BREAKEVEN_DAYS
    assert abs(bot_carry.ENTER_APR - expected) < 1e-9
    # and it must be reachable in the regime the study documents (5.5% on
    # capital at the funding floor), or the book never trades at all
    assert bot_carry.ENTER_APR < 0.05475


def test_pick_refuses_when_nothing_clears_the_bar():
    thin = {"BTCUSDT": _rows(1_700_000_000_000, 21, 0.000002)}
    sym, _ = bot_carry.pick(thin)
    assert sym is None


def test_pick_takes_the_better_payer():
    base = 1_700_000_000_000
    quotes = {"BTCUSDT": _rows(base, 21, 0.0001),
              "ETHUSDT": _rows(base, 21, 0.0003)}
    sym, apr = bot_carry.pick(quotes)
    assert sym == "ETHUSDT"
    assert apr > 0.3
