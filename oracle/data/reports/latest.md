# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-09T06:29:35+00:00

- predictions written: **18428**
- resolved and scored: **7527**
- annulled: **34** (rate 0.4% — OK)

- observed event rate: **0.2670**
- Brier (forecaster): 0.215353
- Brier (baseline):   0.215353
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0134** (mean group 313.6)
- **n_eff 1452.7 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 6353 (n_eff 1340.7), Brier 0.207426, paired d -0.00024392 — indistinguishable from baseline
- `liq_band_v1`: n 6055 (n_eff 1243.3), Brier 0.208189, paired d +0.00025335 — indistinguishable from baseline
- `liqtier_v1`: n 6353 (n_eff 1340.7), Brier 0.206795, paired d +0.00038746 — indistinguishable from baseline
- `momo_v1`: n 6353 (n_eff 1340.7), Brier 0.207722, paired d -0.00053924 — worse than baseline
- `momo_v2`: n 6055 (n_eff 1243.3), Brier 0.208107, paired d +0.00033537 — indistinguishable from baseline
- `ownrate_v1`: n 6353 (n_eff 1340.7), Brier 0.215329, paired d -0.00814624 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
