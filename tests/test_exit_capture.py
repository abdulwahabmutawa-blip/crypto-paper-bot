"""Market-capture arithmetic — the guard on the number that told the owner
they were up 35% while the book was down 20%.

The 08-21 metric divided the live account balance by the $40 inception
stake. The owner had topped the account up, so their deposits landed in the
balance and were published as profit. These asserts pin the property that
broke: a deposit must never move the reported return.

Offline: no network, no data/ writes.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import exit_auditor as ea  # noqa: E402


def _st(pnls, balance=None):
    st = {"realized": [{"pnl_usd": p, "date": "2026-08-%02d" % (15 + i)}
                       for i, p in enumerate(pnls)]}
    if balance is not None:
        st["last_value_usd"] = balance
    return st


# --- the regression itself: deposits must not register as performance -----
losing = _st([-4.0, -3.88], balance=54.07)
c = ea._capture(losing)
assert c["book_since_inception_pct"] == -19.7, c
assert c["realized_pnl_usd"] == -7.88, c
assert c["implied_deposits_usd"] == 21.95, c

# same trades, owner deposits another $500 -> return must not budge
flush = ea._capture(_st([-4.0, -3.88], balance=554.07))
assert flush["book_since_inception_pct"] == c["book_since_inception_pct"], (
    "a deposit changed the reported return — the 08-21 bug is back")
assert flush["implied_deposits_usd"] == 521.95, flush

# the old formula on this exact input is what we must never print again
assert round((554.07 / ea.INCEPTION_USD - 1) * 100, 2) > 0, "sanity"
assert c["book_since_inception_pct"] < 0, "a losing book must report a loss"

# --- balance is published, but never as the return ------------------------
assert c["balance_usd"] == 54.07
assert "balance_usd" not in ea._capture(_st([1.0]))     # absent when unknown
assert "implied_deposits_usd" not in ea._capture(_st([1.0]))

# --- agrees with the alpha series by construction -------------------------
# alpha compounds daily P&L off INCEPTION_USD; both must land on the same
# terminal figure, or the report contradicts itself the way it used to.
pnls = [2.5, -1.25, 0.75, -3.0]
cap = ea._capture(_st(pnls, balance=999.0))
book_val = ea.INCEPTION_USD
for p in pnls:
    book_val += p
assert round((book_val / ea.INCEPTION_USD - 1) * 100, 2) == \
    cap["book_since_inception_pct"], (book_val, cap)

# --- edges ----------------------------------------------------------------
assert ea._capture({})["book_since_inception_pct"] == 0.0
assert ea._capture({})["trades"] == 0
assert ea._capture(_st([]))["realized_pnl_usd"] == 0.0
# a malformed row must not poison the sum
mixed = {"realized": [{"pnl_usd": 1.0}, {"pnl_usd": None}, {}]}
assert ea._capture(mixed)["realized_pnl_usd"] == 1.0
assert ea._capture(mixed)["trades"] == 3

print("test_exit_capture: OK")
