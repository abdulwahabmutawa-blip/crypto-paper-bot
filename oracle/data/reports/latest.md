# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-23T08:02:17+00:00

- predictions written: **35779**
- resolved and scored: **24317**
- annulled: **111** (rate 0.4% — OK)

- observed event rate: **0.1785**
- Brier (forecaster): 0.149752
- Brier (baseline):   0.149752
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0911** (mean group 352.37)
- **n_eff 736.3 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 23143 (n_eff 697.1), Brier 0.144234, paired d -0.00005283 — indistinguishable from baseline
- `liq_band_v1`: n 22845 (n_eff 677.0), Brier 0.143665, paired d +0.00002870 — indistinguishable from baseline
- `liqtier_v1`: n 23143 (n_eff 697.1), Brier 0.144148, paired d +0.00003273 — indistinguishable from baseline
- `momo_v1`: n 23143 (n_eff 697.1), Brier 0.144457, paired d -0.00027583 — indistinguishable from baseline
- `momo_v2`: n 22845 (n_eff 677.0), Brier 0.143542, paired d +0.00015093 — indistinguishable from baseline
- `ownrate_v1`: n 23143 (n_eff 697.1), Brier 0.151381, paired d -0.00719980 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
