# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-16T04:52:12+00:00

- predictions written: **21195**
- resolved and scored: **9926**
- annulled: **41** (rate 0.4% — OK)

- observed event rate: **0.2888**
- Brier (forecaster): 0.231228
- Brier (baseline):   0.231228
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0182** (mean group 320.16)
- **n_eff 1460.6 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 8752 (n_eff 1196.6), Brier 0.227641, paired d -0.00021447 — indistinguishable from baseline
- `liq_band_v1`: n 8454 (n_eff 1152.4), Brier 0.228782, paired d +0.00026035 — indistinguishable from baseline
- `liqtier_v1`: n 8752 (n_eff 1196.6), Brier 0.226987, paired d +0.00043965 — indistinguishable from baseline
- `momo_v1`: n 8752 (n_eff 1196.6), Brier 0.228050, paired d -0.00062334 — indistinguishable from baseline
- `momo_v2`: n 8454 (n_eff 1152.4), Brier 0.228926, paired d +0.00011668 — indistinguishable from baseline
- `ownrate_v1`: n 8752 (n_eff 1196.6), Brier 0.235339, paired d -0.00791199 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
