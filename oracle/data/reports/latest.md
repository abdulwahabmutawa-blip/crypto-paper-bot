# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-29T06:09:45+00:00

- predictions written: **26415**
- resolved and scored: **14560**
- annulled: **54** (rate 0.4% — OK)

- observed event rate: **0.2550**
- Brier (forecaster): 0.205824
- Brier (baseline):   0.205824
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0388** (mean group 330.88)
- **n_eff 1056.4 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 13386 (n_eff 930.9), Brier 0.201327, paired d -0.00021634 — indistinguishable from baseline
- `liq_band_v1`: n 13088 (n_eff 890.3), Brier 0.201325, paired d +0.00023014 — indistinguishable from baseline
- `liqtier_v1`: n 13386 (n_eff 930.9), Brier 0.200845, paired d +0.00026617 — indistinguishable from baseline
- `momo_v1`: n 13386 (n_eff 930.9), Brier 0.201532, paired d -0.00042111 — indistinguishable from baseline
- `momo_v2`: n 13088 (n_eff 890.3), Brier 0.201105, paired d +0.00044977 — indistinguishable from baseline
- `ownrate_v1`: n 13386 (n_eff 930.9), Brier 0.208190, paired d -0.00707971 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
