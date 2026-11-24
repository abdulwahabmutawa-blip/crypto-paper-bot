# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-24T10:18:27+00:00

- predictions written: **36135**
- resolved and scored: **24711**
- annulled: **114** (rate 0.5% — OK)

- observed event rate: **0.1762**
- Brier (forecaster): 0.148105
- Brier (baseline):   0.148105
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0928** (mean group 352.97)
- **n_eff 734.0 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 23537 (n_eff 696.0), Brier 0.142577, paired d -0.00003114 — indistinguishable from baseline
- `liq_band_v1`: n 23239 (n_eff 676.3), Brier 0.142017, paired d +0.00002768 — indistinguishable from baseline
- `liqtier_v1`: n 23537 (n_eff 696.0), Brier 0.142519, paired d +0.00002699 — indistinguishable from baseline
- `momo_v1`: n 23537 (n_eff 696.0), Brier 0.142818, paired d -0.00027181 — indistinguishable from baseline
- `momo_v2`: n 23239 (n_eff 676.3), Brier 0.141928, paired d +0.00011730 — indistinguishable from baseline
- `ownrate_v1`: n 23537 (n_eff 696.0), Brier 0.149710, paired d -0.00716448 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
