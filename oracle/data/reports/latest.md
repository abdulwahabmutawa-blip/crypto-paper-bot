# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-10T06:13:58+00:00

- predictions written: **18819**
- resolved and scored: **7864**
- annulled: **35** (rate 0.4% — OK)

- observed event rate: **0.2676**
- Brier (forecaster): 0.215711
- Brier (baseline):   0.215711
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0127** (mean group 314.54)
- **n_eff 1582.5 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 6690 (n_eff 1476.2), Brier 0.208258, paired d -0.00024182 — indistinguishable from baseline
- `liq_band_v1`: n 6392 (n_eff 1377.6), Brier 0.208982, paired d +0.00026566 — indistinguishable from baseline
- `liqtier_v1`: n 6690 (n_eff 1476.2), Brier 0.207651, paired d +0.00036432 — indistinguishable from baseline
- `momo_v1`: n 6690 (n_eff 1476.2), Brier 0.208549, paired d -0.00053367 — worse than baseline
- `momo_v2`: n 6392 (n_eff 1377.6), Brier 0.208990, paired d +0.00025755 — indistinguishable from baseline
- `ownrate_v1`: n 6690 (n_eff 1476.2), Brier 0.216189, paired d -0.00817304 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
