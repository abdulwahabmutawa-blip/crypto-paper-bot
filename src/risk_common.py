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
EQUITY_BPS = 10.0
CRYPTO_BPS = 25.0


def fee(ticker: str, value: float) -> float:
    """Transaction cost for one side of a fill, in dollars."""
    bps = CRYPTO_BPS if str(ticker).endswith("-USD") else EQUITY_BPS
    return abs(value) * bps / 10_000.0


def r1_breached(value: float) -> bool:
    return value <= R1_FLOOR


def r1_reason(value: float) -> str:
    return (f"R1 KILL FLOOR — book value ${value:,.2f} <= ${R1_FLOOR:,.0f}; "
            f"liquidated and frozen per kill_criteria.md (code-enforced)")
