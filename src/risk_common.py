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


# Binance spot standard tier (no BNB discount): 10bps per side. The honest
# best-case crypto venue tier for pilot-size fee math — vs the 25bps Kraken
# model above. Used by fee_reality for the crypto lane.
BINANCE_SPOT_BPS = 10.0


def binance_fee(value: float, spread_bps: float | None = None) -> float:
    spread = CRYPTO_SPREAD_DEFAULT_BPS if spread_bps is None else spread_bps
    return abs(value) * (BINANCE_SPOT_BPS + spread / 2.0) / 10_000.0


# ---- Live-pilot venue fees (IBKR Fixed tier, US stocks) ---------------------
# The paper model above (10bps) flatters a small real account: IBKR Fixed is
# $0.005/share with a $1 MINIMUM per order, capped at 1% of trade value. On a
# $325 full-book order the $1 minimum dominates: ~0.31% per side — 3x the
# paper model's 10bps. Any live-pilot cost math must use THIS, not fee().
IBKR_PER_SHARE = 0.005
IBKR_MIN_ORDER = 1.0
IBKR_MAX_PCT = 0.01


def ibkr_fee(ticker: str, value: float, units: float) -> float:
    """One side, IBKR Fixed tier: commission (per-share, $1 min, 1%-of-value
    cap) + half the bid-ask spread from the table above. Equities only —
    the live pilot has no crypto lane (Kuwait prohibition, research 08-13)."""
    commission = min(max(abs(units) * IBKR_PER_SHARE, IBKR_MIN_ORDER),
                     abs(value) * IBKR_MAX_PCT)
    spread = EQUITY_SPREAD_BPS.get(str(ticker), EQUITY_SPREAD_DEFAULT_BPS)
    return commission + abs(value) * (spread / 2.0) / 10_000.0


def r1_breached(value: float) -> bool:
    return value <= R1_FLOOR


def r1_reason(value: float) -> str:
    return (f"R1 KILL FLOOR — book value ${value:,.2f} <= ${R1_FLOOR:,.0f}; "
            f"liquidated and frozen per kill_criteria.md (code-enforced)")
