# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-24T04:58:37+00:00

- predictions written: **24428**
- resolved and scored: **12743**
- annulled: **49** (rate 0.4% — OK)

- observed event rate: **0.2751**
- Brier (forecaster): 0.220764
- Brier (baseline):   0.220764
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0256** (mean group 326.71)
- **n_eff 1365.5 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 11569 (n_eff 1174.4), Brier 0.217013, paired d -0.00018657 — indistinguishable from baseline
- `liq_band_v1`: n 11271 (n_eff 1126.2), Brier 0.217481, paired d +0.00027681 — indistinguishable from baseline
- `liqtier_v1`: n 11569 (n_eff 1174.4), Brier 0.216485, paired d +0.00034157 — indistinguishable from baseline
- `momo_v1`: n 11569 (n_eff 1174.4), Brier 0.217350, paired d -0.00052406 — indistinguishable from baseline
- `momo_v2`: n 11271 (n_eff 1126.2), Brier 0.217286, paired d +0.00047170 — indistinguishable from baseline
- `ownrate_v1`: n 11569 (n_eff 1174.4), Brier 0.223844, paired d -0.00701830 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
