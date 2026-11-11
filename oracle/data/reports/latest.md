# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-11T06:56:05+00:00

- predictions written: **31418**
- resolved and scored: **19523**
- annulled: **78** (rate 0.4% — OK)

- observed event rate: **0.2110**
- Brier (forecaster): 0.173463
- Brier (baseline):   0.173463
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0676** (mean group 342.47)
- **n_eff 810.3 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 18349 (n_eff 748.1), Brier 0.168204, paired d -0.00025017 — indistinguishable from baseline
- `liq_band_v1`: n 18051 (n_eff 721.4), Brier 0.167643, paired d +0.00008579 — indistinguishable from baseline
- `liqtier_v1`: n 18349 (n_eff 748.1), Brier 0.167829, paired d +0.00012483 — indistinguishable from baseline
- `momo_v1`: n 18349 (n_eff 748.1), Brier 0.168275, paired d -0.00032142 — indistinguishable from baseline
- `momo_v2`: n 18051 (n_eff 721.4), Brier 0.167222, paired d +0.00050631 — indistinguishable from baseline
- `ownrate_v1`: n 18349 (n_eff 748.1), Brier 0.175319, paired d -0.00736502 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
