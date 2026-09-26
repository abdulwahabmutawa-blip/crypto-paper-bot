# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-26T05:19:19+00:00

- predictions written: **13515**
- resolved and scored: **3330**
- annulled: **21** (rate 0.6% — OK)

- observed event rate: **0.2457**
- Brier (forecaster): 0.199735
- Brier (baseline):   0.199735
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.022** (mean group 302.7)
- **n_eff 436.2 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 2156 (n_eff 1716.1), Brier 0.167164, paired d -0.00000712 — indistinguishable from baseline
- `liq_band_v1`: n 1858 (n_eff 1361.9), Brier 0.164684, paired d +0.00015789 — indistinguishable from baseline
- `liqtier_v1`: n 2156 (n_eff 1716.1), Brier 0.167111, paired d +0.00004611 — indistinguishable from baseline
- `momo_v1`: n 2156 (n_eff 1716.1), Brier 0.167430, paired d -0.00027364 — indistinguishable from baseline
- `momo_v2`: n 1858 (n_eff 1361.9), Brier 0.163708, paired d +0.00113405 — indistinguishable from baseline
- `ownrate_v1`: n 2156 (n_eff 1716.1), Brier 0.171269, paired d -0.00411235 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
