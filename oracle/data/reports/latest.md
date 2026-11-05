# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-05T07:13:40+00:00

- predictions written: **29156**
- resolved and scored: **17195**
- annulled: **66** (rate 0.4% — OK)

- observed event rate: **0.2305**
- Brier (forecaster): 0.187804
- Brier (baseline):   0.187804
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0539** (mean group 337.12)
- **n_eff 900.2 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 16021 (n_eff 816.7), Brier 0.182774, paired d -0.00022843 — indistinguishable from baseline
- `liq_band_v1`: n 15723 (n_eff 784.2), Brier 0.182407, paired d +0.00015652 — indistinguishable from baseline
- `liqtier_v1`: n 16021 (n_eff 816.7), Brier 0.182392, paired d +0.00015360 — indistinguishable from baseline
- `momo_v1`: n 16021 (n_eff 816.7), Brier 0.182917, paired d -0.00037119 — indistinguishable from baseline
- `momo_v2`: n 15723 (n_eff 784.2), Brier 0.182095, paired d +0.00046887 — indistinguishable from baseline
- `ownrate_v1`: n 16021 (n_eff 816.7), Brier 0.189794, paired d -0.00724787 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
