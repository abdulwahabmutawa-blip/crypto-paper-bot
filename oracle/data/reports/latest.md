# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-02T06:37:42+00:00

- predictions written: **27988**
- resolved and scored: **16052**
- annulled: **61** (rate 0.4% — OK)

- observed event rate: **0.2408**
- Brier (forecaster): 0.195359
- Brier (baseline):   0.195359
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0473** (mean group 334.38)
- **n_eff 957.6 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 14878 (n_eff 859.1), Brier 0.190526, paired d -0.00023419 — indistinguishable from baseline
- `liq_band_v1`: n 14580 (n_eff 823.3), Brier 0.190270, paired d +0.00020043 — indistinguishable from baseline
- `liqtier_v1`: n 14878 (n_eff 859.1), Brier 0.190100, paired d +0.00019250 — indistinguishable from baseline
- `momo_v1`: n 14878 (n_eff 859.1), Brier 0.190677, paired d -0.00038457 — indistinguishable from baseline
- `momo_v2`: n 14580 (n_eff 823.3), Brier 0.190034, paired d +0.00043615 — indistinguishable from baseline
- `ownrate_v1`: n 14878 (n_eff 859.1), Brier 0.197457, paired d -0.00716479 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
