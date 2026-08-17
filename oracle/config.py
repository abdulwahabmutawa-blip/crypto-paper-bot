"""Frozen contract constants and paths.

Everything tagged FROZEN is part of the pre-registration (oracle/README.md).
Changing one opens a NEW GENERATION and restarts the track record at zero —
which is the whole point: a moving question cannot accumulate evidence.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
PREDICTIONS = DATA / "predictions"
RESOLUTIONS = DATA / "resolutions"
SNAPSHOTS = DATA / "snapshots"
LEDGER_DIR = DATA / "ledger"
SCORES = DATA / "scores"
REPORTS = DATA / "reports"
CHAIN = LEDGER_DIR / "chain.jsonl"

for _d in (PREDICTIONS, RESOLUTIONS, SNAPSHOTS, LEDGER_DIR, SCORES, REPORTS):
    _d.mkdir(parents=True, exist_ok=True)

# ---- the question (FROZEN) --------------------------------------------------
SCHEMA_VERSION = "pred.v1"
GENERATION_ID = "gen-000-baserate"   # phase 0: no LLM, base rate only
FORECASTER_ID = "baserate_v1"
HORIZON_DAYS = 30
THRESHOLD_MULT = 1.50
EVENT_RULE = ("max(high[t]) for t in [window_start, window_end] "
              ">= threshold_mult * reference.close_price")

# ---- universe_rule_v1 (FROZEN) ----------------------------------------------
UNIVERSE_RULE = "universe_rule_v1"
MIN_LISTED_DAYS = 90            # needs history before it can be judged
MIN_MEDIAN_QV_30D = 200_000.0   # below this an exit is not plausible
MAX_MEDIAN_QV_30D = 50_000_000.0  # above this the coin rarely moves 50%
STABLES = {"USDC", "FDUSD", "TUSD", "DAI", "EUR", "GBP", "USDP", "BUSD",
           "AEUR", "USD1", "XUSD", "PYUSD", "EURI", "U"}
LEVERAGED_SUFFIXES = ("UPUSDT", "DOWNUSDT", "BULLUSDT", "BEARUSDT")

# ---- base rate (FROZEN) -----------------------------------------------------
# Climatology from a rolling window ending strictly BEFORE the earliest
# question that could still have been open at T0. No lookahead by
# construction: every window used has already fully resolved.
BASE_RATE_LOOKBACK_DAYS = 365
BASE_RATE_WINDOW_LABEL = "rolling_365d_ending_T0_minus_31d"

# ---- resolution (FROZEN) ----------------------------------------------------
# A question is ANNULLED, never guessed, when the data cannot answer it.
# The annulment RATE is itself a headline metric: above ANNUL_ALARM the
# question template is broken, which is a contract problem, not noise to
# be discarded.
MAX_MISSING_DAYS = 2
ANNUL_TARGET = 0.04
ANNUL_ALARM = 0.08

# ---- scoring (FROZEN) -------------------------------------------------------
# No conclusion about performance may be stated below this effective sample
# size. Enforced in code, not by discipline — see score.py.
MIN_NEFF_FOR_CLAIM = 100
# Banned from every report. Models spanning ROC AUC 0.627-0.974 all lost
# money in the audited literature; these metrics reward the wrong thing.
BANNED_METRICS = ("auc", "roc", "precision", "recall", "hit_rate", "f1")

# ---- data source ------------------------------------------------------------
BINANCE_HOST = "https://api.binance.com"
USER_AGENT = "oracle-predict-only/1.0"
