# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-22T07:16:54+00:00

- predictions written: **35422**
- resolved and scored: **23919**
- annulled: **108** (rate 0.4% — OK)

- observed event rate: **0.1809**
- Brier (forecaster): 0.151448
- Brier (baseline):   0.151448
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0895** (mean group 351.7)
- **n_eff 738.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 22745 (n_eff 698.3), Brier 0.145940, paired d -0.00007277 — indistinguishable from baseline
- `liq_band_v1`: n 22447 (n_eff 677.9), Brier 0.145364, paired d +0.00002945 — indistinguishable from baseline
- `liqtier_v1`: n 22745 (n_eff 698.3), Brier 0.145828, paired d +0.00003966 — indistinguishable from baseline
- `momo_v1`: n 22745 (n_eff 698.3), Brier 0.146145, paired d -0.00027781 — indistinguishable from baseline
- `momo_v2`: n 22447 (n_eff 677.9), Brier 0.145203, paired d +0.00019047 — indistinguishable from baseline
- `ownrate_v1`: n 22745 (n_eff 698.3), Brier 0.153086, paired d -0.00721879 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
