"""Fleet-wide hard rules every book must obey (audit 2026-08-05).

One module so a rule can never again exist for some bots and not others —
the 7/31 freeze guards lived only in the shared engine and the most active
bot ran with none.

R1 floor: kill_criteria.md R1 ($750) enforced in CODE, not by a supervisor
remembering. A book at/below the floor liquidates and freezes permanently;
un-freezing is a human decision made by editing state, on purpose, in a
commit.

Costs: every fill pays a fee — 10bps equities/ETFs, 25bps crypto, per side.
The audit showed $118k of turnover whose simulated profit ($81) was smaller
than the unmodeled drag; books must feel the cost of their own churn.
"""
from __future__ import annotations

R1_FLOOR = 750.0
EQUITY_BPS = 10.0        # commission-ish base, per side
CRYPTO_BPS = 25.0        # ≈ Kraken taker tier, per side

# Half the bid-ask spread is a real cost of every marketable order. Crypto
# spreads come live from Kraken when the caller has them; equities use this
# honest approximation table (bps of full spread, typical US session):
EQUITY_SPREAD_BPS = {
    "SPY": 1, "QQQ": 1, "IWM": 1, "TLT": 1, "GLD": 1, "BIL": 1, "SLV": 2,
    "TQQQ": 3, "SOXL": 3, "UPRO": 3, "USO": 3, "DBC": 5,
    "NVDA": 2, "TSLA": 3, "MSTR": 8, "COIN": 5, "PLTR": 4,
    "AAPL": 1, "MSFT": 1, "AMZN": 1, "GOOG": 1, "META": 1, "WMT": 1, "PG": 1,
}
EQUITY_SPREAD_DEFAULT_BPS = 5.0   # unknown equity: assume mid-liquidity
CRYPTO_SPREAD_DEFAULT_BPS = 8.0   # no live spread available: alt-coin-ish


def fee(ticker: str, value: float, spread_bps: float | None = None) -> float:
    """Transaction cost for one side of a fill, in dollars:
    base (commission/taker) + half the bid-ask spread. Pass spread_bps when a
    live measured spread exists (crypto via Kraken); otherwise the table or
    default applies."""
    t = str(ticker)
    if t.endswith("-USD"):
        base = CRYPTO_BPS
        spread = CRYPTO_SPREAD_DEFAULT_BPS if spread_bps is None else spread_bps
    else:
        base = EQUITY_BPS
        spread = EQUITY_SPREAD_BPS.get(t, EQUITY_SPREAD_DEFAULT_BPS) \
            if spread_bps is None else spread_bps
    return abs(value) * (base + spread / 2.0) / 10_000.0


def r1_breached(value: float) -> bool:
    return value <= R1_FLOOR


def r1_reason(value: float) -> str:
    return (f"R1 KILL FLOOR — book value ${value:,.2f} <= ${R1_FLOOR:,.0f}; "
            f"liquidated and frozen per kill_criteria.md (code-enforced)")
