# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-08T06:32:31+00:00

- predictions written: **30300**
- resolved and scored: **18356**
- annulled: **72** (rate 0.4% — OK)

- observed event rate: **0.2209**
- Brier (forecaster): 0.180712
- Brier (baseline):   0.180712
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.06** (mean group 339.88)
- **n_eff 860.6 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 17182 (n_eff 788.6), Brier 0.175554, paired d -0.00022956 — indistinguishable from baseline
- `liq_band_v1`: n 16884 (n_eff 758.8), Brier 0.175110, paired d +0.00010388 — indistinguishable from baseline
- `liqtier_v1`: n 17182 (n_eff 788.6), Brier 0.175190, paired d +0.00013478 — indistinguishable from baseline
- `momo_v1`: n 17182 (n_eff 788.6), Brier 0.175687, paired d -0.00036197 — indistinguishable from baseline
- `momo_v2`: n 16884 (n_eff 758.8), Brier 0.174685, paired d +0.00052938 — indistinguishable from baseline
- `ownrate_v1`: n 17182 (n_eff 788.6), Brier 0.182649, paired d -0.00732404 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
