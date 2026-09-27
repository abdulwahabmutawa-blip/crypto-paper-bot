# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-27T05:35:14+00:00

- predictions written: **13879**
- resolved and scored: **3641**
- annulled: **23** (rate 0.6% — OK)

- observed event rate: **0.2450**
- Brier (forecaster): 0.199192
- Brier (baseline):   0.199192
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0197** (mean group 303.39)
- **n_eff 522.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 2467 (n_eff 1812.2), Brier 0.170479, paired d -0.00001802 — indistinguishable from baseline
- `liq_band_v1`: n 2169 (n_eff 1423.1), Brier 0.168768, paired d +0.00016377 — indistinguishable from baseline
- `liqtier_v1`: n 2467 (n_eff 1812.2), Brier 0.170273, paired d +0.00018801 — indistinguishable from baseline
- `momo_v1`: n 2467 (n_eff 1812.2), Brier 0.170815, paired d -0.00035374 — indistinguishable from baseline
- `momo_v2`: n 2169 (n_eff 1423.1), Brier 0.168021, paired d +0.00091079 — indistinguishable from baseline
- `ownrate_v1`: n 2467 (n_eff 1812.2), Brier 0.175025, paired d -0.00456390 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
