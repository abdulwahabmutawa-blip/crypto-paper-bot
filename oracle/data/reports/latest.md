# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-28T06:04:45+00:00

- predictions written: **26018**
- resolved and scored: **14193**
- annulled: **53** (rate 0.4% — OK)

- observed event rate: **0.2586**
- Brier (forecaster): 0.208513
- Brier (baseline):   0.208513
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0367** (mean group 330.04)
- **n_eff 1086.8 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 13019 (n_eff 952.9), Brier 0.204129, paired d -0.00021975 — indistinguishable from baseline
- `liq_band_v1`: n 12721 (n_eff 911.1), Brier 0.204198, paired d +0.00023334 — indistinguishable from baseline
- `liqtier_v1`: n 13019 (n_eff 952.9), Brier 0.203632, paired d +0.00027731 — indistinguishable from baseline
- `momo_v1`: n 13019 (n_eff 952.9), Brier 0.204336, paired d -0.00042744 — indistinguishable from baseline
- `momo_v2`: n 12721 (n_eff 911.1), Brier 0.203994, paired d +0.00043740 — indistinguishable from baseline
- `ownrate_v1`: n 13019 (n_eff 952.9), Brier 0.211015, paired d -0.00710571 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
