# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-04T06:53:16+00:00

- predictions written: **28767**
- resolved and scored: **16812**
- annulled: **65** (rate 0.4% — OK)

- observed event rate: **0.2341**
- Brier (forecaster): 0.190401
- Brier (baseline):   0.190401
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0514** (mean group 336.2)
- **n_eff 922.8 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 15638 (n_eff 834.4), Brier 0.185442, paired d -0.00023385 — indistinguishable from baseline
- `liq_band_v1`: n 15340 (n_eff 800.7), Brier 0.185105, paired d +0.00017360 — indistinguishable from baseline
- `liqtier_v1`: n 15638 (n_eff 834.4), Brier 0.185046, paired d +0.00016301 — indistinguishable from baseline
- `momo_v1`: n 15638 (n_eff 834.4), Brier 0.185585, paired d -0.00037692 — indistinguishable from baseline
- `momo_v2`: n 15340 (n_eff 800.7), Brier 0.184830, paired d +0.00044899 — indistinguishable from baseline
- `ownrate_v1`: n 15638 (n_eff 834.4), Brier 0.192409, paired d -0.00720029 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
