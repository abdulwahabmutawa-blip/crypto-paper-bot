# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-12T06:19:28+00:00

- predictions written: **19601**
- resolved and scored: **8545**
- annulled: **37** (rate 0.4% — OK)

- observed event rate: **0.2763**
- Brier (forecaster): 0.222129
- Brier (baseline):   0.222129
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0158** (mean group 316.46)
- **n_eff 1427.7 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 7371 (n_eff 1206.2), Brier 0.216417, paired d -0.00025045 — indistinguishable from baseline
- `liq_band_v1`: n 7073 (n_eff 1139.6), Brier 0.217381, paired d +0.00024203 — indistinguishable from baseline
- `liqtier_v1`: n 7371 (n_eff 1206.2), Brier 0.215822, paired d +0.00034447 — indistinguishable from baseline
- `momo_v1`: n 7371 (n_eff 1206.2), Brier 0.216796, paired d -0.00062951 — worse than baseline
- `momo_v2`: n 7073 (n_eff 1139.6), Brier 0.217273, paired d +0.00035016 — indistinguishable from baseline
- `ownrate_v1`: n 7371 (n_eff 1206.2), Brier 0.224488, paired d -0.00832131 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
