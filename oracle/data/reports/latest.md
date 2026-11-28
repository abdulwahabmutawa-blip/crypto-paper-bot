# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-28T08:17:59+00:00

- predictions written: **37556**
- resolved and scored: **26293**
- annulled: **122** (rate 0.5% — OK)

- observed event rate: **0.1682**
- Brier (forecaster): 0.142309
- Brier (baseline):   0.142309
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0977** (mean group 355.26)
- **n_eff 738.6 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 25119 (n_eff 705.0), Brier 0.136810, paired d +0.00001807 — indistinguishable from baseline
- `liq_band_v1`: n 24821 (n_eff 686.4), Brier 0.136261, paired d +0.00002978 — indistinguishable from baseline
- `liqtier_v1`: n 25119 (n_eff 705.0), Brier 0.136836, paired d -0.00000704 — indistinguishable from baseline
- `momo_v1`: n 25119 (n_eff 705.0), Brier 0.137081, paired d -0.00025265 — indistinguishable from baseline
- `momo_v2`: n 24821 (n_eff 686.4), Brier 0.136274, paired d +0.00001684 — indistinguishable from baseline
- `ownrate_v1`: n 25119 (n_eff 705.0), Brier 0.143825, paired d -0.00699645 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
