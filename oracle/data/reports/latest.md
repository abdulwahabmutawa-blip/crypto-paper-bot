# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-15T05:01:22+00:00

- predictions written: **20792**
- resolved and scored: **9578**
- annulled: **40** (rate 0.4% — OK)

- observed event rate: **0.2843**
- Brier (forecaster): 0.227933
- Brier (baseline):   0.227933
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0162** (mean group 319.24)
- **n_eff 1558.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 8404 (n_eff 1296.8), Brier 0.223761, paired d -0.00024709 — indistinguishable from baseline
- `liq_band_v1`: n 8106 (n_eff 1244.8), Brier 0.224792, paired d +0.00026283 — indistinguishable from baseline
- `liqtier_v1`: n 8404 (n_eff 1296.8), Brier 0.223107, paired d +0.00040662 — indistinguishable from baseline
- `momo_v1`: n 8404 (n_eff 1296.8), Brier 0.224130, paired d -0.00061636 — worse than baseline
- `momo_v2`: n 8106 (n_eff 1244.8), Brier 0.224908, paired d +0.00014737 — indistinguishable from baseline
- `ownrate_v1`: n 8404 (n_eff 1296.8), Brier 0.231584, paired d -0.00807046 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
