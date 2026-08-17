"""Scoring, effective sample size, and the refusal to overclaim.

THREE RULES, ENFORCED IN CODE RATHER THAN BY DISCIPLINE:

1. PAIRED, never two separately averaged means. The statistic is
   d_i = (p_baseline_i - y_i)^2 - (p_forecaster_i - y_i)^2 on the identical
   slate at the identical timestamp. Positive means the forecaster beat the
   baseline. Pairing is orders of magnitude more sample-efficient than
   comparing two Brier averages with separate confidence intervals.

2. n_eff, never n. Outcomes are not independent: the 2-year study found 64%
   of explosions clustering on market-wide wave days, so dozens of
   predictions can succeed or fail together for one shared reason. rho is
   MEASURED here (intraclass correlation of outcomes across runs), never
   assumed, and n_eff = n / (1 + (m-1) * rho).

3. NO CONCLUSION below MIN_NEFF_FOR_CLAIM. The report prints a countdown
   instead of a verdict. This is the control that stops an early lucky
   stretch from becoming a belief.

AUC, precision, recall and hit rate are deliberately absent. In the audited
literature, models spanning ROC AUC 0.627-0.974 all lost money; those
metrics reward ranking, and this experiment is about calibrated probability.
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path

import oracle.config as config
import oracle.ledger as ledger


def _load() -> tuple[dict, dict]:
    preds: dict[str, dict] = {}
    for pf in sorted(config.PREDICTIONS.rglob("*.jsonl")):
        for line in pf.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                preds[r["prediction_id"]] = r
    res: dict[str, dict] = {}
    for rf in sorted(config.RESOLUTIONS.rglob("*.jsonl")):
        for line in rf.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                # last write wins; resolutions are append-only and a repeat
                # would mean a re-resolution, which the report should show
                res[r["prediction_id"]] = r
    return preds, res


def intraclass_rho(groups: list[list[int]]) -> tuple[float, float]:
    """One-way ICC of binary outcomes grouped by run. Returns (rho, m_bar).

    This is the number that decides how long any later claim will take to
    earn, so it is measured from the data rather than assumed.
    """
    groups = [g for g in groups if len(g) >= 2]
    if len(groups) < 2:
        return 0.0, float(len(groups[0]) if groups else 0)
    n_total = sum(len(g) for g in groups)
    k = len(groups)
    grand = sum(sum(g) for g in groups) / n_total
    ss_b = sum(len(g) * (sum(g) / len(g) - grand) ** 2 for g in groups)
    ss_w = sum(sum((x - sum(g) / len(g)) ** 2 for x in g) for g in groups)
    df_b, df_w = k - 1, n_total - k
    if df_b <= 0 or df_w <= 0:
        return 0.0, n_total / k
    ms_b, ms_w = ss_b / df_b, ss_w / df_w
    m_bar = (n_total - sum(len(g) ** 2 for g in groups) / n_total) / df_b
    if m_bar <= 0:
        return 0.0, n_total / k
    denom = ms_b + (m_bar - 1) * ms_w
    rho = 0.0 if denom <= 0 else (ms_b - ms_w) / denom
    return max(0.0, min(1.0, rho)), m_bar


def required_n(var_d: float, delta: float, alpha: float = 0.05,
               power: float = 0.80) -> int | None:
    """Paired one-sided sample size for detecting a mean difference delta."""
    if var_d <= 0 or delta <= 0:
        return None
    z_a, z_b = 1.645, 0.842      # alpha 0.05 one-sided, power 0.80
    return int(math.ceil((z_a + z_b) ** 2 * var_d / delta ** 2))


def compute() -> dict:
    preds, res = _load()
    rows = []
    annulled = 0
    for pid, r in res.items():
        p = preds.get(pid)
        if not p:
            continue
        if r.get("status") != "resolved" or r.get("outcome") is None:
            annulled += 1
            continue
        rows.append({
            "run_id": p["run_id"], "symbol": p["symbol"],
            "p": float(p["probability"]),
            "p_base": float(p["baseline_p_base_rate"]),
            "y": int(r["outcome"]),
        })

    n = len(rows)
    out = {
        "generated_utc": datetime.now(timezone.utc).isoformat(
            timespec="seconds"),
        "generation_id": config.GENERATION_ID,
        "forecaster_id": config.FORECASTER_ID,
        "n_predictions_written": len(preds),
        "n_resolution_records": len(res),
        "n_scored": n,
        "n_annulled": annulled,
        "annulment_rate": round(annulled / max(1, annulled + n), 4),
        "annulment_target": config.ANNUL_TARGET,
        "annulment_alarm": config.ANNUL_ALARM,
    }
    if not n:
        out["status"] = "no resolved predictions yet"
        return out

    y_mean = sum(r["y"] for r in rows) / n
    bs_f = sum((r["p"] - r["y"]) ** 2 for r in rows) / n
    bs_b = sum((r["p_base"] - r["y"]) ** 2 for r in rows) / n
    d = [(r["p_base"] - r["y"]) ** 2 - (r["p"] - r["y"]) ** 2 for r in rows]
    mean_d = sum(d) / n
    var_d = (sum((x - mean_d) ** 2 for x in d) / (n - 1)) if n > 1 else 0.0

    groups: dict[str, list[int]] = {}
    for r in rows:
        groups.setdefault(r["run_id"], []).append(r["y"])
    rho, m_bar = intraclass_rho(list(groups.values()))
    n_eff = n / (1 + max(0.0, (m_bar - 1)) * rho) if m_bar else float(n)

    # target effect: a 2% Brier skill score over the baseline
    delta = 0.02 * bs_b
    out.update({
        "observed_event_rate": round(y_mean, 5),
        "brier_forecaster": round(bs_f, 6),
        "brier_baseline": round(bs_b, 6),
        "paired_mean_d": round(mean_d, 8),
        "paired_sd_d": round(math.sqrt(var_d), 8),
        "cluster_rho": round(rho, 4),
        "mean_group_size": round(m_bar, 2),
        "n_eff": round(n_eff, 1),
        "n_eff_required_for_claim": config.MIN_NEFF_FOR_CLAIM,
        "target_delta_bss_0.02": round(delta, 8),
        "n_required_for_target": required_n(var_d, delta),
        "n_required_note": ("nominal paired n; multiply by "
                            "(1+(m-1)*rho) for the clustered reality"),
    })
    if n_eff < config.MIN_NEFF_FOR_CLAIM:
        out["status"] = "NO CONCLUSION IS STATISTICALLY POSSIBLE YET"
        out["verdict"] = None
    else:
        se = math.sqrt(var_d / n_eff) if var_d > 0 else 0.0
        lo = mean_d - 1.645 * se
        hi = mean_d + 1.645 * se
        out["status"] = "scored"
        out["paired_d_90ci"] = [round(lo, 8), round(hi, 8)]
        out["verdict"] = ("forecaster beats baseline" if lo > 0 else
                          "worse than baseline (KILL CRITERION 1)"
                          if hi < 0 else "indistinguishable from baseline")
    return out


def report(scores: dict) -> str:
    L = ["# Oracle scoreboard", "",
         f"generation `{scores['generation_id']}` · forecaster "
         f"`{scores['forecaster_id']}` · {scores['generated_utc']}", ""]
    L.append(f"- predictions written: **{scores['n_predictions_written']}**")
    L.append(f"- resolved and scored: **{scores['n_scored']}**")
    ar = scores["annulment_rate"]
    flag = ("OK" if ar <= scores["annulment_target"] else
            "ALARM — the question template may be broken"
            if ar > scores["annulment_alarm"] else "elevated")
    L.append(f"- annulled: **{scores['n_annulled']}** "
             f"(rate {ar:.1%} — {flag})")
    if not scores.get("n_scored"):
        L += ["", "No resolved predictions yet. The first 30-day windows "
              "close 30 days after the first run.", ""]
        return "\n".join(L)

    L += ["",
          f"- observed event rate: **{scores['observed_event_rate']:.4f}**",
          f"- Brier (forecaster): {scores['brier_forecaster']:.6f}",
          f"- Brier (baseline):   {scores['brier_baseline']:.6f}",
          f"- paired mean d: {scores['paired_mean_d']:.8f} "
          f"(sd {scores['paired_sd_d']:.6f})",
          f"- cluster rho: **{scores['cluster_rho']}** "
          f"(mean group {scores['mean_group_size']})",
          f"- **n_eff {scores['n_eff']} / "
          f"{scores['n_eff_required_for_claim']} required**", ""]
    if scores.get("verdict") is None:
        need = scores["n_eff_required_for_claim"] - scores["n_eff"]
        L += [f"> **{scores['status']}**", ">",
              f"> {need:.0f} more effective samples needed before this "
              f"report may characterise performance. Any number above is a "
              f"measurement, not a verdict.", ""]
    else:
        L += [f"> **verdict: {scores['verdict']}** "
              f"(90% CI {scores['paired_d_90ci']})", ""]
    if scores.get("n_required_for_target"):
        L += [f"Nominal paired n for a 0.02 BSS at 80% power: "
              f"**{scores['n_required_for_target']:,}** "
              f"({scores['n_required_note']}).", ""]
    L += ["_AUC, precision, recall and hit rate are deliberately absent — "
          "see oracle/README.md._", ""]
    return "\n".join(L)


def run() -> dict:
    s = compute()
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    sp = config.SCORES / f"{day}.json"
    sp.write_text(json.dumps(s, sort_keys=True, indent=1), encoding="utf-8")
    rp = config.REPORTS / "latest.md"
    rp.write_text(report(s), encoding="utf-8")
    ledger.append("scores", sp, s.get("n_scored", 0))
    print(report(s))
    return s
