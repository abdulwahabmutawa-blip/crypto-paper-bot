# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-26T05:11:50+00:00

- predictions written: **25221**
- resolved and scored: **13464**
- annulled: **51** (rate 0.4% — OK)

- observed event rate: **0.2671**
- Brier (forecaster): 0.214798
- Brier (baseline):   0.214798
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0306** (mean group 328.36)
- **n_eff 1222.8 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 12290 (n_eff 1062.7), Brier 0.210730, paired d -0.00020756 — indistinguishable from baseline
- `liq_band_v1`: n 11992 (n_eff 1016.8), Brier 0.210989, paired d +0.00025198 — indistinguishable from baseline
- `liqtier_v1`: n 12290 (n_eff 1062.7), Brier 0.210214, paired d +0.00030816 — indistinguishable from baseline
- `momo_v1`: n 12290 (n_eff 1062.7), Brier 0.211010, paired d -0.00048797 — indistinguishable from baseline
- `momo_v2`: n 11992 (n_eff 1016.8), Brier 0.210740, paired d +0.00050121 — indistinguishable from baseline
- `ownrate_v1`: n 12290 (n_eff 1062.7), Brier 0.217570, paired d -0.00704782 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
