"""Build the slate, compute the climatology, write predictions.

PHASE 0 CONTAINS NO LLM. The forecaster emits the base rate for every slate
member. That is not a placeholder for something smarter — it is the
incumbent every later forecaster must beat, and running it first is what
turns the base rate, the annulment rate and the cluster correlation from
assumptions into measurements.

NOTHING HERE CAN LOOK AHEAD. The reference is the last CLOSED daily candle,
and the climatology is computed only from questions that had already fully
resolved before that candle.
"""
from __future__ import annotations

import json
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import oracle.comparators as comparators
import oracle.config as config
import oracle.fetch as fetch
import oracle.ledger as ledger
import oracle.universe as universe

DAY_MS = 86_400_000
# 90d listing floor + 365d climatology window + 30d horizon + slack
HISTORY_DAYS = config.MIN_LISTED_DAYS + config.BASE_RATE_LOOKBACK_DAYS \
    + config.HORIZON_DAYS + 20


def _iso(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat(
        timespec="seconds")


def explosion_rate(rows: list[list], horizon: int, mult: float,
                   lookback: int) -> tuple[int, int]:
    """(hits, windows) over START days whose whole horizon already closed.

    A window starting at index i is only counted if i + horizon <= last
    index, i.e. it had fully resolved before the reference candle. That is
    the no-lookahead guarantee, enforced by arithmetic rather than by care.
    """
    last_start = len(rows) - 1 - horizon
    if last_start < 1:
        return 0, 0
    first_start = max(0, last_start - lookback + 1)
    hits = windows = 0
    for i in range(first_start, last_start + 1):
        ref = float(rows[i][4])
        if ref <= 0:
            continue
        hi = max(float(r[2]) for r in rows[i + 1:i + 1 + horizon])
        windows += 1
        if hi >= mult * ref:
            hits += 1
    return hits, windows


def build_slate(limit: int | None = None, pause: float = 0.05) -> dict:
    """Fetch, filter by universe_rule_v1, and compute per-symbol history."""
    info = fetch.exchange_info()
    candidates = universe.candidate_symbols(info)
    if limit:
        candidates = candidates[:limit]
    print(f"[oracle] {len(candidates)} symbols pass name/status filter")

    slate, rejected = [], {}
    hits_total = windows_total = 0
    for i, sym in enumerate(candidates):
        if i and i % 50 == 0:
            print(f"[oracle]   {i}/{len(candidates)}...")
        try:
            rows = fetch.klines(sym, "1d", limit=min(1000, HISTORY_DAYS))
        except Exception as e:
            rejected[sym] = f"fetch failed: {e}"
            continue
        # drop the still-forming candle: only CLOSED days may be referenced
        now_ms = time.time() * 1000
        rows = [r for r in rows if r[6] < now_ms]
        ok, why = universe.eligible_history(rows)
        if not ok:
            rejected[sym] = why
            continue
        h, w = explosion_rate(rows, config.HORIZON_DAYS,
                              config.THRESHOLD_MULT,
                              config.BASE_RATE_LOOKBACK_DAYS)
        hits_total += h
        windows_total += w
        ref = rows[-1]
        qv30 = sorted(float(r[7]) for r in rows[-30:])
        # trailing 30d return from CLOSED candles only (rows already
        # excludes the forming day) — feeds momo_v1; eligible_history
        # guarantees >=90 rows so [-31] always exists
        c_now, c_then = float(rows[-1][4]), float(rows[-31][4])
        slate.append({
            "symbol": sym,
            "ref_open_time_ms": int(ref[0]),
            "ref_close_time_ms": int(ref[6]),
            "ref_close": f"{float(ref[4]):.10g}",
            "listed_days": len(rows),
            "median_qv_30d": round(qv30[len(qv30) // 2], 2),
            "own_hits": h, "own_windows": w,
            "ret_30d": round(c_now / c_then - 1.0, 6) if c_then > 0 else 0.0,
        })
        time.sleep(pause)

    base_rate = (hits_total / windows_total) if windows_total else 0.0
    print(f"[oracle] slate {len(slate)} symbols | climatology "
          f"{hits_total}/{windows_total} = {base_rate:.4f}")
    return {"slate": slate, "rejected": rejected, "base_rate": base_rate,
            "base_rate_hits": hits_total, "base_rate_windows": windows_total}


def run(limit: int | None = None) -> Path:
    now = datetime.now(timezone.utc)
    built = build_slate(limit=limit)
    slate = built["slate"]
    if not slate:
        raise SystemExit("[oracle] empty slate — refusing to write a run")

    # Phase-1 comparators (added 08-20, additive only): four naive
    # forecasters recorded ALONGSIDE the baseline on the same rows. The
    # question, the baseline and its probability are untouched — this does
    # not open a new generation; it widens what September can conclude.
    comp_probs, comp_meta = comparators.probabilities(
        slate, built["base_rate"])

    # T0 is the latest reference close on the slate; windows are measured
    # from each symbol's own reference candle.
    # filesystem-safe: run_id becomes a directory name, and colons are
    # illegal on Windows (the VPS is Linux, but the repo must stay portable
    # so the record can be audited anywhere)
    run_id = (now.strftime("%Y%m%dT%H%M%SZ") + "_"
              + ledger.sha256_text(json.dumps(
                  [s["symbol"] for s in slate], sort_keys=True))[:6])

    snap_dir = config.SNAPSHOTS / run_id
    snap_dir.mkdir(parents=True, exist_ok=True)
    snap_path = snap_dir / "manifest.json"
    snap = {
        "run_id": run_id,
        "created_utc": now.isoformat(timespec="seconds"),
        "universe_rule": config.UNIVERSE_RULE,
        "generation_id": config.GENERATION_ID,
        "base_rate": built["base_rate"],
        "base_rate_hits": built["base_rate_hits"],
        "base_rate_windows": built["base_rate_windows"],
        "base_rate_window_label": config.BASE_RATE_WINDOW_LABEL,
        "n_slate": len(slate),
        "n_rejected": len(built["rejected"]),
        # Stored by value: the exact inputs each decision rests on. The full
        # kline payloads are NOT committed (they would be ~100MB/yr); what
        # is committed is every field the rule and the forecast used, so a
        # reviewer can recompute both without trusting a re-fetch.
        "slate": slate,
        "rejected": built["rejected"],
        "comparators": comp_meta,
    }
    # newline="\n" everywhere — see the note in ledger.append()
    snap_path.write_text(json.dumps(snap, sort_keys=True, indent=1),
                         encoding="utf-8", newline="\n")
    snap_hash = ledger.sha256_file(snap_path)

    day_dir = config.PREDICTIONS / now.strftime("%Y-%m-%d")
    day_dir.mkdir(parents=True, exist_ok=True)
    pred_path = day_dir / f"{run_id}.jsonl"

    p = round(built["base_rate"], 6)
    with pred_path.open("w", encoding="utf-8", newline="\n") as fh:
        for s in slate:
            w_start = s["ref_close_time_ms"] + 1
            w_end = s["ref_close_time_ms"] + config.HORIZON_DAYS * DAY_MS
            rec = {
                "schema_version": config.SCHEMA_VERSION,
                "run_id": run_id,
                "generation_id": config.GENERATION_ID,
                "forecaster_id": config.FORECASTER_ID,
                "symbol": s["symbol"],
                "exchange": "binance-spot",
                "reference": {
                    "endpoint": "/api/v3/klines", "interval": "1d",
                    "open_time_utc": _iso(s["ref_open_time_ms"]),
                    "close_time_utc": _iso(s["ref_close_time_ms"]),
                    "close_price": s["ref_close"],
                },
                "event": {
                    "rule": config.EVENT_RULE,
                    "threshold_mult": config.THRESHOLD_MULT,
                    "window_start_utc": _iso(w_start),
                    "window_end_utc": _iso(w_end),
                    "window_start_ms": w_start, "window_end_ms": w_end,
                },
                "horizon_days": config.HORIZON_DAYS,
                "probability": p,
                "probability_raw": p,
                "baseline_p_base_rate": p,
                "baseline_window": config.BASE_RATE_WINDOW_LABEL,
                # emit=False everywhere in phase 0: the base-rate forecaster
                # has no conviction subset to flag, and a selective score
                # without a selector would be meaningless.
                "emit": False,
                "abstain_reason": None,
                "covariates_recorded": {
                    "listed_days": s["listed_days"],
                    "median_qv_30d": s["median_qv_30d"],
                    "own_hits": s["own_hits"], "own_windows": s["own_windows"],
                    "ret_30d": s["ret_30d"],
                },
                # phase-1 comparators (see oracle/comparators.py): scored
                # against the SAME resolution via the same paired statistic
                "comparators": comp_probs[s["symbol"]],
                "universe_rule": config.UNIVERSE_RULE,
                "snapshot_sha256": snap_hash,
                "created_utc": now.isoformat(timespec="seconds"),
            }
            # prediction_id binds the question to its exact terms: same
            # symbol, different threshold or window -> different id.
            rec["prediction_id"] = ledger.sha256_text(json.dumps({
                "run_id": run_id, "symbol": s["symbol"],
                "ref": rec["reference"], "event": rec["event"],
                "gen": config.GENERATION_ID}, sort_keys=True))
            fh.write(json.dumps(rec, sort_keys=True) + "\n")

    ledger.append("snapshot", snap_path, 1, {"run_id": run_id})
    entry = ledger.append("predictions", pred_path, len(slate),
                          {"run_id": run_id, "base_rate": p})
    print(f"[oracle] wrote {len(slate)} predictions -> {pred_path.name}")
    print(f"[oracle] chain seq {entry['seq']} "
          f"head {entry['chain_self'][:12]}")
    return pred_path
