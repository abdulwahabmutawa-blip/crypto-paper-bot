# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-20T05:13:00+00:00

- predictions written: **11369**
- resolved and scored: **1472**
- annulled: **9** (rate 0.6% — OK)

- observed event rate: **0.3044**
- Brier (forecaster): 0.243779
- Brier (baseline):   0.243779
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0126** (mean group 294.4)
- **n_eff 312.7 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 298 (n_eff 298.0), Brier 0.182639, paired d -0.00104921 — indistinguishable from baseline
- `liqtier_v1`: n 298 (n_eff 298.0), Brier 0.182104, paired d -0.00051426 — indistinguishable from baseline
- `momo_v1`: n 298 (n_eff 298.0), Brier 0.181929, paired d -0.00033895 — indistinguishable from baseline
- `ownrate_v1`: n 298 (n_eff 298.0), Brier 0.187020, paired d -0.00543026 — indistinguishable from baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
