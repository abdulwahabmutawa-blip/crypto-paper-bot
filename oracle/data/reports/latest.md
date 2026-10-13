# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-13T07:05:51+00:00

- predictions written: **19997**
- resolved and scored: **8889**
- annulled: **38** (rate 0.4% — OK)

- observed event rate: **0.2790**
- Brier (forecaster): 0.224092
- Brier (baseline):   0.224092
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0159** (mean group 317.44)
- **n_eff 1475.6 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 7715 (n_eff 1238.2), Brier 0.218937, paired d -0.00024295 — indistinguishable from baseline
- `liq_band_v1`: n 7417 (n_eff 1176.6), Brier 0.219937, paired d +0.00024818 — indistinguishable from baseline
- `liqtier_v1`: n 7715 (n_eff 1238.2), Brier 0.218332, paired d +0.00036182 — indistinguishable from baseline
- `momo_v1`: n 7715 (n_eff 1238.2), Brier 0.219296, paired d -0.00060247 — worse than baseline
- `momo_v2`: n 7417 (n_eff 1176.6), Brier 0.219904, paired d +0.00028064 — indistinguishable from baseline
- `ownrate_v1`: n 7715 (n_eff 1238.2), Brier 0.227088, paired d -0.00839450 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
