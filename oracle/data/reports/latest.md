# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-23T05:14:20+00:00

- predictions written: **24027**
- resolved and scored: **12385**
- annulled: **48** (rate 0.4% — OK)

- observed event rate: **0.2783**
- Brier (forecaster): 0.223142
- Brier (baseline):   0.223142
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0244** (mean group 325.89)
- **n_eff 1389.5 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 11211 (n_eff 1186.7), Brier 0.219505, paired d -0.00017636 — indistinguishable from baseline
- `liq_band_v1`: n 10913 (n_eff 1138.9), Brier 0.220074, paired d +0.00028483 — indistinguishable from baseline
- `liqtier_v1`: n 11211 (n_eff 1186.7), Brier 0.218968, paired d +0.00036006 — indistinguishable from baseline
- `momo_v1`: n 11211 (n_eff 1186.7), Brier 0.219873, paired d -0.00054428 — indistinguishable from baseline
- `momo_v2`: n 10913 (n_eff 1138.9), Brier 0.219937, paired d +0.00042234 — indistinguishable from baseline
- `ownrate_v1`: n 11211 (n_eff 1186.7), Brier 0.226460, paired d -0.00713173 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
