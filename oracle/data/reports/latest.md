# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-03T07:10:25+00:00

- predictions written: **28378**
- resolved and scored: **16429**
- annulled: **63** (rate 0.4% — OK)

- observed event rate: **0.2374**
- Brier (forecaster): 0.192897
- Brier (baseline):   0.192897
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0493** (mean group 335.25)
- **n_eff 940.7 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 15255 (n_eff 847.4), Brier 0.188008, paired d -0.00024165 — indistinguishable from baseline
- `liq_band_v1`: n 14957 (n_eff 812.6), Brier 0.187703, paired d +0.00018691 — indistinguishable from baseline
- `liqtier_v1`: n 15255 (n_eff 847.4), Brier 0.187591, paired d +0.00017546 — indistinguishable from baseline
- `momo_v1`: n 15255 (n_eff 847.4), Brier 0.188141, paired d -0.00037458 — indistinguishable from baseline
- `momo_v2`: n 14957 (n_eff 812.6), Brier 0.187450, paired d +0.00043973 — indistinguishable from baseline
- `ownrate_v1`: n 15255 (n_eff 847.4), Brier 0.194947, paired d -0.00717996 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
