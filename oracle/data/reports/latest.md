# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-24T05:14:20+00:00

- predictions written: **12792**
- resolved and scored: **2700**
- annulled: **17** (rate 0.6% — OK)

- observed event rate: **0.2511**
- Brier (forecaster): 0.203879
- Brier (baseline):   0.203879
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0271** (mean group 299.98)
- **n_eff 296.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 1526 (n_eff 1143.1), Brier 0.161244, paired d -0.00020581 — indistinguishable from baseline
- `liq_band_v1`: n 1228 (n_eff 1010.6), Brier 0.156011, paired d +0.00003938 — indistinguishable from baseline
- `liqtier_v1`: n 1526 (n_eff 1143.1), Brier 0.161212, paired d -0.00017444 — indistinguishable from baseline
- `momo_v1`: n 1526 (n_eff 1143.1), Brier 0.161312, paired d -0.00027454 — indistinguishable from baseline
- `momo_v2`: n 1228 (n_eff 1010.6), Brier 0.154586, paired d +0.00146417 — indistinguishable from baseline
- `ownrate_v1`: n 1526 (n_eff 1143.1), Brier 0.165241, paired d -0.00420293 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
