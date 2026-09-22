# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-22T05:17:31+00:00

- predictions written: **12077**
- resolved and scored: **2078**
- annulled: **13** (rate 0.6% — OK)

- observed event rate: **0.2661**
- Brier (forecaster): 0.215135
- Brier (baseline):   0.215135
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.03** (mean group 296.85)
- **n_eff 210.5 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 904 (n_eff 389.3), Brier 0.158054, paired d -0.00061748 — indistinguishable from baseline
- `liq_band_v1`: n 606 (n_eff 348.3), Brier 0.145500, paired d +0.00005815 — indistinguishable from baseline
- `liqtier_v1`: n 904 (n_eff 389.3), Brier 0.157670, paired d -0.00023389 — indistinguishable from baseline
- `momo_v1`: n 904 (n_eff 389.3), Brier 0.157934, paired d -0.00049775 — indistinguishable from baseline
- `momo_v2`: n 606 (n_eff 348.3), Brier 0.144532, paired d +0.00102614 — indistinguishable from baseline
- `ownrate_v1`: n 904 (n_eff 389.3), Brier 0.162072, paired d -0.00463609 — indistinguishable from baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
