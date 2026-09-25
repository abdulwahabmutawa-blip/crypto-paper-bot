# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-25T05:18:02+00:00

- predictions written: **13152**
- resolved and scored: **3015**
- annulled: **19** (rate 0.6% — OK)

- observed event rate: **0.2488**
- Brier (forecaster): 0.202092
- Brier (baseline):   0.202092
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.024** (mean group 301.48)
- **n_eff 366.6 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 1841 (n_eff 1283.2), Brier 0.165523, paired d -0.00008171 — indistinguishable from baseline
- `liq_band_v1`: n 1543 (n_eff 989.9), Brier 0.162210, paired d +0.00011242 — indistinguishable from baseline
- `liqtier_v1`: n 1841 (n_eff 1283.2), Brier 0.165536, paired d -0.00009507 — indistinguishable from baseline
- `momo_v1`: n 1841 (n_eff 1283.2), Brier 0.165717, paired d -0.00027600 — indistinguishable from baseline
- `momo_v2`: n 1543 (n_eff 989.9), Brier 0.160772, paired d +0.00155001 — indistinguishable from baseline
- `ownrate_v1`: n 1841 (n_eff 1283.2), Brier 0.169379, paired d -0.00393761 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
