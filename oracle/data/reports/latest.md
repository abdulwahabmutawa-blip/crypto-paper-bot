# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-30T05:51:43+00:00

- predictions written: **14986**
- resolved and scored: **4585**
- annulled: **29** (rate 0.6% — OK)

- observed event rate: **0.2576**
- Brier (forecaster): 0.208436
- Brier (baseline):   0.208436
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0185** (mean group 305.65)
- **n_eff 689.7 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 3411 (n_eff 670.7), Brier 0.190979, paired d -0.00014073 — indistinguishable from baseline
- `liq_band_v1`: n 3113 (n_eff 556.3), Brier 0.191504, paired d +0.00021924 — indistinguishable from baseline
- `liqtier_v1`: n 3411 (n_eff 670.7), Brier 0.190518, paired d +0.00031967 — indistinguishable from baseline
- `momo_v1`: n 3411 (n_eff 670.7), Brier 0.191292, paired d -0.00045394 — indistinguishable from baseline
- `momo_v2`: n 3113 (n_eff 556.3), Brier 0.191203, paired d +0.00052008 — indistinguishable from baseline
- `ownrate_v1`: n 3411 (n_eff 670.7), Brier 0.197325, paired d -0.00648748 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
