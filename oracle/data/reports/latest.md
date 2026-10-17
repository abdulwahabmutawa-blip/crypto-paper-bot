# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-17T04:49:20+00:00

- predictions written: **21597**
- resolved and scored: **10275**
- annulled: **42** (rate 0.4% — OK)

- observed event rate: **0.2925**
- Brier (forecaster): 0.233833
- Brier (baseline):   0.233833
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0191** (mean group 321.06)
- **n_eff 1442.1 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 9101 (n_eff 1176.9), Brier 0.230692, paired d -0.00017744 — indistinguishable from baseline
- `liq_band_v1`: n 8803 (n_eff 1137.8), Brier 0.231914, paired d +0.00025666 — indistinguishable from baseline
- `liqtier_v1`: n 9101 (n_eff 1176.9), Brier 0.230060, paired d +0.00045441 — indistinguishable from baseline
- `momo_v1`: n 9101 (n_eff 1176.9), Brier 0.231120, paired d -0.00060620 — indistinguishable from baseline
- `momo_v2`: n 8803 (n_eff 1137.8), Brier 0.231996, paired d +0.00017475 — indistinguishable from baseline
- `ownrate_v1`: n 9101 (n_eff 1176.9), Brier 0.238351, paired d -0.00783655 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
