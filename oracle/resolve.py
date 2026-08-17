"""Mechanical resolution. Reads five fields and nothing else.

THE RESOLVER NEVER SEES REASONING. It is handed symbol, reference price,
threshold, window start and window end — deliberately not the forecast, not
the probability, not any narrative — so there is no channel through which a
story could influence whether it counts as a hit. `_question()` below is the
whole interface, and tests assert it.

A question that the data cannot answer is ANNULLED, never guessed. The
annulment rate is a headline metric: sustained above ANNUL_ALARM the
question template is broken, which is a contract problem to fix openly
rather than noise to quietly discard.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import oracle.config as config
import oracle.fetch as fetch
import oracle.ledger as ledger

RESOLVER_VERSION = "resolve_v1"
DAY_MS = 86_400_000


def _question(rec: dict) -> dict:
    """The ONLY fields the resolver may use. Anything else is invisible."""
    return {
        "prediction_id": rec["prediction_id"],
        "symbol": rec["symbol"],
        "ref_close": float(rec["reference"]["close_price"]),
        "threshold_mult": float(rec["event"]["threshold_mult"]),
        "window_start_ms": int(rec["event"]["window_start_ms"]),
        "window_end_ms": int(rec["event"]["window_end_ms"]),
    }


def prediction_files() -> list[Path]:
    return sorted(config.PREDICTIONS.rglob("*.jsonl"))


def resolved_ids() -> set[str]:
    done = set()
    for p in sorted(config.RESOLUTIONS.rglob("*.jsonl")):
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done.add(json.loads(line)["prediction_id"])
    return done


def resolve_one(q: dict) -> dict:
    """Fetch the window and decide. Pure function of public market data."""
    now = datetime.now(timezone.utc)
    out = {
        "prediction_id": q["prediction_id"],
        "resolved_utc": now.isoformat(timespec="seconds"),
        "resolver_version": RESOLVER_VERSION,
        "outcome": None, "status": "annulled", "annul_reason": None,
        "max_high": None, "n_bars": 0, "expected_bars": 0,
    }
    try:
        rows = fetch.klines(q["symbol"], "1d", limit=1000,
                            start_ms=q["window_start_ms"],
                            end_ms=q["window_end_ms"])
    except Exception as e:
        out["annul_reason"] = f"fetch failed: {e}"
        return out

    expected = max(1, round((q["window_end_ms"] - q["window_start_ms"])
                            / DAY_MS))
    out["expected_bars"] = expected
    out["n_bars"] = len(rows)
    if not rows:
        # no data across the whole window: delisted or halted throughout
        out["annul_reason"] = "no bars in window (delisted/halted)"
        return out
    if expected - len(rows) > config.MAX_MISSING_DAYS:
        out["annul_reason"] = (f"missing bars: {len(rows)}/{expected} "
                               f"(halt or delisting mid-window)")
        return out

    max_high = max(float(r[2]) for r in rows)
    target = q["ref_close"] * q["threshold_mult"]
    out["max_high"] = f"{max_high:.10g}"
    out["target"] = f"{target:.10g}"
    out["outcome"] = 1 if max_high >= target else 0
    out["status"] = "resolved"
    out["annul_reason"] = None
    return out


def run(pause: float = 0.05) -> int:
    now_ms = datetime.now(timezone.utc).timestamp() * 1000
    done = resolved_ids()
    by_run: dict[str, list[dict]] = {}

    for pf in prediction_files():
        for line in pf.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec["prediction_id"] in done:
                continue
            if rec["event"]["window_end_ms"] > now_ms:
                continue          # not due yet — never resolve early
            by_run.setdefault(rec["run_id"], []).append(_question(rec))

    if not by_run:
        print("[oracle] nothing due for resolution")
        return 0

    import time
    total = 0
    # One file per resolution PASS, never appended to. A run can resolve
    # across several passes (a symbol's data may be briefly unavailable),
    # and appending to a file the chain already committed to would break
    # verification — the same flaw that killed cycle #2 on the scores file.
    # Chained artifacts are write-once; passes get new names.
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")[:-4]
    for run_id, questions in sorted(by_run.items()):
        path = config.RESOLUTIONS / f"{run_id}__{stamp}.jsonl"
        with path.open("w", encoding="utf-8", newline="\n") as fh:
            for q in questions:
                r = resolve_one(q)
                fh.write(json.dumps(r, sort_keys=True) + "\n")
                total += 1
                time.sleep(pause)
        ledger.append("resolutions", path, len(questions), {"run_id": run_id})
        print(f"[oracle] resolved {len(questions)} from {run_id}")
    print(f"[oracle] {total} resolutions written")
    return total
