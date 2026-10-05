# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-05T06:03:03+00:00

- predictions written: **16877**
- resolved and scored: **6207**
- annulled: **33** (rate 0.5% — OK)

- observed event rate: **0.2718**
- Brier (forecaster): 0.218953
- Brier (baseline):   0.218953
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0159** (mean group 310.33)
- **n_eff 1051.1 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 5033 (n_eff 872.6), Brier 0.209718, paired d -0.00023810 — indistinguishable from baseline
- `liq_band_v1`: n 4735 (n_eff 792.4), Brier 0.210939, paired d +0.00029621 — indistinguishable from baseline
- `liqtier_v1`: n 5033 (n_eff 872.6), Brier 0.208987, paired d +0.00049203 — indistinguishable from baseline
- `momo_v1`: n 5033 (n_eff 872.6), Brier 0.209852, paired d -0.00037226 — indistinguishable from baseline
- `momo_v2`: n 4735 (n_eff 792.4), Brier 0.211018, paired d +0.00021651 — indistinguishable from baseline
- `ownrate_v1`: n 5033 (n_eff 872.6), Brier 0.217041, paired d -0.00756190 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
