# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-14T05:11:39+00:00

- predictions written: **20393**
- resolved and scored: **9234**
- annulled: **39** (rate 0.4% — OK)

- observed event rate: **0.2821**
- Brier (forecaster): 0.226362
- Brier (baseline):   0.226362
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0163** (mean group 318.39)
- **n_eff 1495.1 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 8060 (n_eff 1243.6), Brier 0.221773, paired d -0.00024697 — indistinguishable from baseline
- `liq_band_v1`: n 7762 (n_eff 1188.0), Brier 0.222797, paired d +0.00026180 — indistinguishable from baseline
- `liqtier_v1`: n 8060 (n_eff 1243.6), Brier 0.221133, paired d +0.00039338 — indistinguishable from baseline
- `momo_v1`: n 8060 (n_eff 1243.6), Brier 0.222118, paired d -0.00059239 — indistinguishable from baseline
- `momo_v2`: n 7762 (n_eff 1188.0), Brier 0.222888, paired d +0.00017128 — indistinguishable from baseline
- `ownrate_v1`: n 8060 (n_eff 1243.6), Brier 0.229770, paired d -0.00824360 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
