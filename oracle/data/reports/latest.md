# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-09T07:04:18+00:00

- predictions written: **30672**
- resolved and scored: **18745**
- annulled: **74** (rate 0.4% — OK)

- observed event rate: **0.2178**
- Brier (forecaster): 0.178398
- Brier (baseline):   0.178398
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0621** (mean group 340.78)
- **n_eff 848.1 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 17571 (n_eff 779.5), Brier 0.173215, paired d -0.00023957 — indistinguishable from baseline
- `liq_band_v1`: n 17273 (n_eff 750.6), Brier 0.172734, paired d +0.00009232 — indistinguishable from baseline
- `liqtier_v1`: n 17571 (n_eff 779.5), Brier 0.172845, paired d +0.00013020 — indistinguishable from baseline
- `momo_v1`: n 17571 (n_eff 779.5), Brier 0.173325, paired d -0.00034982 — indistinguishable from baseline
- `momo_v2`: n 17273 (n_eff 750.6), Brier 0.172300, paired d +0.00052670 — indistinguishable from baseline
- `ownrate_v1`: n 17571 (n_eff 779.5), Brier 0.180293, paired d -0.00731755 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
