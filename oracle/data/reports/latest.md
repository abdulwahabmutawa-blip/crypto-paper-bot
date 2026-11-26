# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-26T08:46:05+00:00

- predictions written: **36847**
- resolved and scored: **25501**
- annulled: **120** (rate 0.5% — OK)

- observed event rate: **0.1722**
- Brier (forecaster): 0.145178
- Brier (baseline):   0.145178
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0952** (mean group 354.13)
- **n_eff 736.7 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 24327 (n_eff 701.0), Brier 0.139662, paired d -0.00000393 — indistinguishable from baseline
- `liq_band_v1`: n 24029 (n_eff 681.9), Brier 0.139111, paired d +0.00002704 — indistinguishable from baseline
- `liqtier_v1`: n 24327 (n_eff 701.0), Brier 0.139650, paired d +0.00000847 — indistinguishable from baseline
- `momo_v1`: n 24327 (n_eff 701.0), Brier 0.139925, paired d -0.00026665 — indistinguishable from baseline
- `momo_v2`: n 24029 (n_eff 681.9), Brier 0.139081, paired d +0.00005750 — indistinguishable from baseline
- `ownrate_v1`: n 24327 (n_eff 701.0), Brier 0.146728, paired d -0.00706982 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
