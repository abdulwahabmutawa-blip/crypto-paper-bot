# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-23T05:05:18+00:00

- predictions written: **12433**
- resolved and scored: **2388**
- annulled: **15** (rate 0.6% — OK)

- observed event rate: **0.2563**
- Brier (forecaster): 0.207768
- Brier (baseline):   0.207768
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0297** (mean group 298.48)
- **n_eff 242.8 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 1214 (n_eff 783.7), Brier 0.158044, paired d -0.00036634 — indistinguishable from baseline
- `liq_band_v1`: n 916 (n_eff 870.7), Brier 0.149839, paired d +0.00005883 — indistinguishable from baseline
- `liqtier_v1`: n 1214 (n_eff 783.7), Brier 0.157869, paired d -0.00019181 — indistinguishable from baseline
- `momo_v1`: n 1214 (n_eff 783.7), Brier 0.158064, paired d -0.00038656 — indistinguishable from baseline
- `momo_v2`: n 916 (n_eff 870.7), Brier 0.148942, paired d +0.00095599 — indistinguishable from baseline
- `ownrate_v1`: n 1214 (n_eff 783.7), Brier 0.161808, paired d -0.00413106 — indistinguishable from baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
