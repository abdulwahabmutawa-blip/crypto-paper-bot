# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-28T05:46:15+00:00

- predictions written: **14246**
- resolved and scored: **3953**
- annulled: **25** (rate 0.6% — OK)

- observed event rate: **0.2477**
- Brier (forecaster): 0.201127
- Brier (baseline):   0.201127
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0181** (mean group 304.06)
- **n_eff 609.5 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 2779 (n_eff 1249.3), Brier 0.176536, paired d -0.00009606 — indistinguishable from baseline
- `liq_band_v1`: n 2481 (n_eff 978.3), Brier 0.175660, paired d +0.00016078 — indistinguishable from baseline
- `liqtier_v1`: n 2779 (n_eff 1249.3), Brier 0.176208, paired d +0.00023190 — indistinguishable from baseline
- `momo_v1`: n 2779 (n_eff 1249.3), Brier 0.176842, paired d -0.00040256 — indistinguishable from baseline
- `momo_v2`: n 2481 (n_eff 978.3), Brier 0.175122, paired d +0.00069896 — indistinguishable from baseline
- `ownrate_v1`: n 2779 (n_eff 1249.3), Brier 0.181548, paired d -0.00510797 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
