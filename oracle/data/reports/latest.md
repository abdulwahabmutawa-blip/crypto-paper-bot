# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-19T07:51:04+00:00

- predictions written: **34334**
- resolved and scored: **22708**
- annulled: **99** (rate 0.4% — OK)

- observed event rate: **0.1882**
- Brier (forecaster): 0.156789
- Brier (baseline):   0.156789
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0844** (mean group 349.31)
- **n_eff 747.4 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 21534 (n_eff 702.4), Brier 0.151334, paired d -0.00014857 — indistinguishable from baseline
- `liq_band_v1`: n 21236 (n_eff 680.8), Brier 0.150710, paired d +0.00004882 — indistinguishable from baseline
- `liqtier_v1`: n 21534 (n_eff 702.4), Brier 0.151120, paired d +0.00006558 — indistinguishable from baseline
- `momo_v1`: n 21534 (n_eff 702.4), Brier 0.151456, paired d -0.00027020 — indistinguishable from baseline
- `momo_v2`: n 21236 (n_eff 680.8), Brier 0.150449, paired d +0.00031023 — indistinguishable from baseline
- `ownrate_v1`: n 21534 (n_eff 702.4), Brier 0.158472, paired d -0.00728667 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
