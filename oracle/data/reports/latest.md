# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-31T06:05:38+00:00

- predictions written: **27210**
- resolved and scored: **15302**
- annulled: **57** (rate 0.4% — OK)

- observed event rate: **0.2477**
- Brier (forecaster): 0.200502
- Brier (baseline):   0.200502
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0431** (mean group 332.62)
- **n_eff 1001.4 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 14128 (n_eff 890.7), Brier 0.195811, paired d -0.00021702 — indistinguishable from baseline
- `liq_band_v1`: n 13830 (n_eff 852.6), Brier 0.195674, paired d +0.00022192 — indistinguishable from baseline
- `liqtier_v1`: n 14128 (n_eff 890.7), Brier 0.195364, paired d +0.00023033 — indistinguishable from baseline
- `momo_v1`: n 14128 (n_eff 890.7), Brier 0.195997, paired d -0.00040342 — indistinguishable from baseline
- `momo_v2`: n 13830 (n_eff 852.6), Brier 0.195468, paired d +0.00042755 — indistinguishable from baseline
- `ownrate_v1`: n 14128 (n_eff 890.7), Brier 0.202744, paired d -0.00714981 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
