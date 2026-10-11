# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-11T06:11:45+00:00

- predictions written: **19211**
- resolved and scored: **8204**
- annulled: **36** (rate 0.4% — OK)

- observed event rate: **0.2728**
- Brier (forecaster): 0.219567
- Brier (baseline):   0.219567
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0151** (mean group 315.51)
- **n_eff 1423.3 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 7030 (n_eff 1227.7), Brier 0.213157, paired d -0.00026973 — indistinguishable from baseline
- `liq_band_v1`: n 6732 (n_eff 1152.6), Brier 0.214013, paired d +0.00025929 — indistinguishable from baseline
- `liqtier_v1`: n 7030 (n_eff 1227.7), Brier 0.212546, paired d +0.00034131 — indistinguishable from baseline
- `momo_v1`: n 7030 (n_eff 1227.7), Brier 0.213469, paired d -0.00058147 — worse than baseline
- `momo_v2`: n 6732 (n_eff 1152.6), Brier 0.214000, paired d +0.00027268 — indistinguishable from baseline
- `ownrate_v1`: n 7030 (n_eff 1227.7), Brier 0.221039, paired d -0.00815204 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
