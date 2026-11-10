# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-10T07:39:05+00:00

- predictions written: **31045**
- resolved and scored: **19135**
- annulled: **76** (rate 0.4% — OK)

- observed event rate: **0.2145**
- Brier (forecaster): 0.176021
- Brier (baseline):   0.176021
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0645** (mean group 341.65)
- **n_eff 832.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 17961 (n_eff 767.5), Brier 0.170806, paired d -0.00024632 — indistinguishable from baseline
- `liq_band_v1`: n 17663 (n_eff 739.6), Brier 0.170285, paired d +0.00008884 — indistinguishable from baseline
- `liqtier_v1`: n 17961 (n_eff 767.5), Brier 0.170430, paired d +0.00012954 — indistinguishable from baseline
- `momo_v1`: n 17961 (n_eff 767.5), Brier 0.170893, paired d -0.00033332 — indistinguishable from baseline
- `momo_v2`: n 17663 (n_eff 739.6), Brier 0.169843, paired d +0.00053052 — indistinguishable from baseline
- `ownrate_v1`: n 17961 (n_eff 767.5), Brier 0.177898, paired d -0.00733829 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
