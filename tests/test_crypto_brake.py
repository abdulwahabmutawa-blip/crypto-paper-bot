"""Offline check of the crypto churn brakes (fix 2026-08-10 + review round).

The bug: signal() enters and exits at the same knife-edge threshold, so a
coin wobbling at the boundary was sold and rebought every cycle (15 legs /
$26.52 fees on 2026-08-10). Two pure brakes now guard the two doors:
exit_brake (position->CASH: hold until the trade clearly completes or
clearly fails, judged by the regime the seat was EARNED under) and
swap_brake (coin->coin: a dead-band incumbent is defended by hysteresis,
not just an entry-qualified one). Run directly:
python tests/test_crypto_brake.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import crypto_tracker as ct


def board(z=0.0, mom=0.0, z2=0.0, mom2=0.0):
    return {"XRP-USD": {"z": z, "mom_pct": mom},
            "ADA-USD": {"z": z2, "mom_pct": mom2}}


# ---- exit_brake: the position->CASH door -------------------------------
# CHOP: bounce not harvested yet (z inside dead-band) -> keep the seat
assert ct.exit_brake("CASH", "XRP-USD", board(z=-0.80), "CHOP") == "XRP-USD"
# CHOP: exactly at the old knife edge (the churn case) -> keep the seat
assert ct.exit_brake("CASH", "XRP-USD", board(z=-1.24), "CHOP") == "XRP-USD"
# CHOP: bounce harvested (z recovered past Z_EXIT) -> let it exit
assert ct.exit_brake("CASH", "XRP-USD", board(z=-0.10), "CHOP") == "CASH"
# TREND: small wobble below zero -> keep the seat
assert ct.exit_brake("CASH", "XRP-USD", board(mom=-1.0), "TREND") == "XRP-USD"
# TREND: clear break -> let it exit
assert ct.exit_brake("CASH", "XRP-USD", board(mom=-3.0), "TREND") == "CASH"
# brake only guards the ->CASH boundary: coin picks pass through untouched
assert ct.exit_brake("ADA-USD", "XRP-USD", board(z=-0.80), "CHOP") == "ADA-USD"
# nothing held -> nothing to protect
assert ct.exit_brake("CASH", "CASH", board(z=-0.80), "CHOP") == "CASH"
# NaN metric (short history) -> fail safe, exit allowed
assert ct.exit_brake("CASH", "XRP-USD", board(z=float("nan")), "CHOP") == "CASH"
# seat regime beats current regime: TREND seat crashing during a flip to
# CHOP must NOT inherit dip-holding patience (mom -6 fails MOM_EXIT even
# though z -0.6 would hold in CHOP)
assert ct.exit_brake("CASH", "XRP-USD", board(z=-0.60, mom=-6.0),
                     "TREND") == "CASH"
# ...and a CHOP seat judged as CHOP still holds that same board
assert ct.exit_brake("CASH", "XRP-USD", board(z=-0.60, mom=-6.0),
                     "CHOP") == "XRP-USD"

# ---- swap_brake: the coin->coin door -----------------------------------
# CHOP, the review scenario: incumbent in the dead band (z -1.20), challenger
# 0.06 deeper (-1.26) -> Z_HYST now applies, incumbent defended
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(z=-1.20, z2=-1.26), "CHOP") == "XRP-USD"
# CHOP: challenger clearly deeper (Z_HYST=0.50 cleared) -> swap
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(z=-1.20, z2=-1.75), "CHOP") == "ADA-USD"
# CHOP: incumbent past the dead-band exit -> disqualified, swap allowed
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(z=-0.10, z2=-1.30), "CHOP") == "ADA-USD"
# TREND: rising incumbent, challenger under both bars -> defended
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=2.0, mom2=2.2), "TREND") == "XRP-USD"
# TREND: challenger clears the ratio but not the absolute lead (bar =
# max(2.5, 4.0) = 4.0) -> still defended
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=2.0, mom2=3.0), "TREND") == "XRP-USD"
# TREND: challenger clears both bars -> swap
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=2.0, mom2=4.5), "TREND") == "ADA-USD"
# TREND: hot incumbent (mom 10) — ratio bar dominates (12.5 > 12.0)
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=10.0, mom2=12.2), "TREND") == "XRP-USD"
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=10.0, mom2=13.0), "TREND") == "ADA-USD"
# TREND, verifier's probe: low-momentum ping-pong (+0.40 vs +0.55) — the
# bare 1.25x ratio allowed this round trip; the absolute lead kills it
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=0.40, mom2=0.55), "TREND") == "XRP-USD"
# TREND, verifier's probe: no protection discontinuity at zero — +0.01 and
# -0.01 incumbents both defend against a +1.0 challenger
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=0.01, mom2=1.0), "TREND") == "XRP-USD"
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=-0.01, mom2=1.0), "TREND") == "XRP-USD"
# TREND, the ping-pong case: coins straddling zero (incumbent -0.1,
# challenger +0.05) -> MOM_MARGIN defends the incumbent
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=-0.1, mom2=0.05), "TREND") == "XRP-USD"
# TREND: wobbling incumbent vs a challenger leading by > MOM_MARGIN -> swap
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=-1.0, mom2=3.0), "TREND") == "ADA-USD"
# TREND: incumbent below MOM_EXIT -> disqualified, swap allowed
assert ct.swap_brake("ADA-USD", "XRP-USD",
                     board(mom=-3.0, mom2=0.5), "TREND") == "ADA-USD"
# no-ops: CASH pick, same coin, nothing held
assert ct.swap_brake("CASH", "XRP-USD", board(), "CHOP") == "CASH"
assert ct.swap_brake("XRP-USD", "XRP-USD", board(), "CHOP") == "XRP-USD"
assert ct.swap_brake("ADA-USD", "CASH", board(z2=-1.30), "CHOP") == "ADA-USD"

print("OK — exit_brake 10/10, swap_brake 17/17")
