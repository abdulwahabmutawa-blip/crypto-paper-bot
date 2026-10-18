# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-18T04:54:33+00:00

- predictions written: **21999**
- resolved and scored: **10624**
- annulled: **43** (rate 0.4% — OK)

- observed event rate: **0.2939**
- Brier (forecaster): 0.234790
- Brier (baseline):   0.234790
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0186** (mean group 321.91)
- **n_eff 1522.8 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 9450 (n_eff 1250.1), Brier 0.231865, paired d -0.00015240 — indistinguishable from baseline
- `liq_band_v1`: n 9152 (n_eff 1212.9), Brier 0.233073, paired d +0.00027081 — indistinguishable from baseline
- `liqtier_v1`: n 9450 (n_eff 1250.1), Brier 0.231258, paired d +0.00045444 — indistinguishable from baseline
- `momo_v1`: n 9450 (n_eff 1250.1), Brier 0.232367, paired d -0.00065448 — indistinguishable from baseline
- `momo_v2`: n 9152 (n_eff 1212.9), Brier 0.233056, paired d +0.00028830 — indistinguishable from baseline
- `ownrate_v1`: n 9450 (n_eff 1250.1), Brier 0.239529, paired d -0.00781711 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
