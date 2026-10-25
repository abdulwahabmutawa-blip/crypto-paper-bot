# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-25T05:08:47+00:00

- predictions written: **24825**
- resolved and scored: **13102**
- annulled: **50** (rate 0.4% — OK)

- observed event rate: **0.2713**
- Brier (forecaster): 0.217944
- Brier (baseline):   0.217944
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0277** (mean group 327.52)
- **n_eff 1304.8 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 11928 (n_eff 1128.7), Brier 0.214046, paired d -0.00019843 — indistinguishable from baseline
- `liq_band_v1`: n 11630 (n_eff 1081.1), Brier 0.214410, paired d +0.00026457 — indistinguishable from baseline
- `liqtier_v1`: n 11928 (n_eff 1128.7), Brier 0.213519, paired d +0.00032901 — indistinguishable from baseline
- `momo_v1`: n 11928 (n_eff 1128.7), Brier 0.214358, paired d -0.00051086 — indistinguishable from baseline
- `momo_v2`: n 11630 (n_eff 1081.1), Brier 0.214162, paired d +0.00051245 — indistinguishable from baseline
- `ownrate_v1`: n 11928 (n_eff 1128.7), Brier 0.220822, paired d -0.00697468 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
