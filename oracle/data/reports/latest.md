# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-06T07:12:54+00:00

- predictions written: **29542**
- resolved and scored: **17581**
- annulled: **68** (rate 0.4% — OK)

- observed event rate: **0.2271**
- Brier (forecaster): 0.185291
- Brier (baseline):   0.185291
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0562** (mean group 338.06)
- **n_eff 881.6 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 16407 (n_eff 802.5), Brier 0.180199, paired d -0.00022205 — indistinguishable from baseline
- `liq_band_v1`: n 16109 (n_eff 771.1), Brier 0.179811, paired d +0.00013620 — indistinguishable from baseline
- `liqtier_v1`: n 16407 (n_eff 802.5), Brier 0.179831, paired d +0.00014530 — indistinguishable from baseline
- `momo_v1`: n 16407 (n_eff 802.5), Brier 0.180355, paired d -0.00037806 — indistinguishable from baseline
- `momo_v2`: n 16109 (n_eff 771.1), Brier 0.179446, paired d +0.00050030 — indistinguishable from baseline
- `ownrate_v1`: n 16407 (n_eff 802.5), Brier 0.187263, paired d -0.00728669 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
