# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-08T06:30:21+00:00

- predictions written: **18038**
- resolved and scored: **7192**
- annulled: **33** (rate 0.5% — OK)

- observed event rate: **0.2683**
- Brier (forecaster): 0.216348
- Brier (baseline):   0.216348
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0139** (mean group 312.67)
- **n_eff 1348.1 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 6018 (n_eff 1213.8), Brier 0.208162, paired d -0.00024457 — indistinguishable from baseline
- `liq_band_v1`: n 5720 (n_eff 1121.2), Brier 0.209009, paired d +0.00027938 — indistinguishable from baseline
- `liqtier_v1`: n 6018 (n_eff 1213.8), Brier 0.207503, paired d +0.00041458 — indistinguishable from baseline
- `momo_v1`: n 6018 (n_eff 1213.8), Brier 0.208398, paired d -0.00048079 — indistinguishable from baseline
- `momo_v2`: n 5720 (n_eff 1121.2), Brier 0.208996, paired d +0.00029328 — indistinguishable from baseline
- `ownrate_v1`: n 6018 (n_eff 1213.8), Brier 0.215991, paired d -0.00807424 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
