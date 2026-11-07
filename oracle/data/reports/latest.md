# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-07T06:26:28+00:00

- predictions written: **29925**
- resolved and scored: **17968**
- annulled: **70** (rate 0.4% — OK)

- observed event rate: **0.2240**
- Brier (forecaster): 0.182998
- Brier (baseline):   0.182998
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0581** (mean group 338.98)
- **n_eff 871.3 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 16794 (n_eff 795.8), Brier 0.177872, paired d -0.00022627 — indistinguishable from baseline
- `liq_band_v1`: n 16496 (n_eff 765.3), Brier 0.177457, paired d +0.00011749 — indistinguishable from baseline
- `liqtier_v1`: n 16794 (n_eff 795.8), Brier 0.177505, paired d +0.00014061 — indistinguishable from baseline
- `momo_v1`: n 16794 (n_eff 795.8), Brier 0.178014, paired d -0.00036824 — indistinguishable from baseline
- `momo_v2`: n 16496 (n_eff 765.3), Brier 0.177052, paired d +0.00052203 — indistinguishable from baseline
- `ownrate_v1`: n 16794 (n_eff 795.8), Brier 0.184954, paired d -0.00730830 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
