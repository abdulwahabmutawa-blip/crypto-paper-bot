# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-30T06:12:27+00:00

- predictions written: **26812**
- resolved and scored: **14931**
- annulled: **55** (rate 0.4% — OK)

- observed event rate: **0.2514**
- Brier (forecaster): 0.203218
- Brier (baseline):   0.203218
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0407** (mean group 331.77)
- **n_eff 1031.8 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 13757 (n_eff 913.8), Brier 0.198619, paired d -0.00020986 — indistinguishable from baseline
- `liq_band_v1`: n 13459 (n_eff 874.3), Brier 0.198554, paired d +0.00022808 — indistinguishable from baseline
- `liqtier_v1`: n 13757 (n_eff 913.8), Brier 0.198162, paired d +0.00024791 — indistinguishable from baseline
- `momo_v1`: n 13757 (n_eff 913.8), Brier 0.198821, paired d -0.00041097 — indistinguishable from baseline
- `momo_v2`: n 13459 (n_eff 874.3), Brier 0.198338, paired d +0.00044432 — indistinguishable from baseline
- `ownrate_v1`: n 13757 (n_eff 913.8), Brier 0.205512, paired d -0.00710190 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
