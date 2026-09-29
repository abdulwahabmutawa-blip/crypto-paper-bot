# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-29T06:04:11+00:00

- predictions written: **14614**
- resolved and scored: **4268**
- annulled: **27** (rate 0.6% — OK)

- observed event rate: **0.2509**
- Brier (forecaster): 0.203521
- Brier (baseline):   0.203521
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.017** (mean group 304.84)
- **n_eff 691.7 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 3094 (n_eff 1028.3), Brier 0.182411, paired d -0.00015541 — indistinguishable from baseline
- `liq_band_v1`: n 2796 (n_eff 826.6), Brier 0.182145, paired d +0.00018141 — indistinguishable from baseline
- `liqtier_v1`: n 3094 (n_eff 1028.3), Brier 0.182001, paired d +0.00025397 — indistinguishable from baseline
- `momo_v1`: n 3094 (n_eff 1028.3), Brier 0.182735, paired d -0.00047968 — indistinguishable from baseline
- `momo_v2`: n 2796 (n_eff 826.6), Brier 0.181780, paired d +0.00054646 — indistinguishable from baseline
- `ownrate_v1`: n 3094 (n_eff 1028.3), Brier 0.188168, paired d -0.00591303 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
