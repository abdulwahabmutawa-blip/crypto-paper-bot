# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-20T07:42:42+00:00

- predictions written: **34694**
- resolved and scored: **23114**
- annulled: **102** (rate 0.4% — OK)

- observed event rate: **0.1856**
- Brier (forecaster): 0.154889
- Brier (baseline):   0.154889
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0863** (mean group 350.16)
- **n_eff 742.4 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 21940 (n_eff 699.0), Brier 0.149410, paired d -0.00012220 — indistinguishable from baseline
- `liq_band_v1`: n 21642 (n_eff 677.8), Brier 0.148802, paired d +0.00004154 — indistinguishable from baseline
- `liqtier_v1`: n 21940 (n_eff 699.0), Brier 0.149231, paired d +0.00005659 — indistinguishable from baseline
- `momo_v1`: n 21940 (n_eff 699.0), Brier 0.149565, paired d -0.00027681 — indistinguishable from baseline
- `momo_v2`: n 21642 (n_eff 677.8), Brier 0.148574, paired d +0.00026920 — indistinguishable from baseline
- `ownrate_v1`: n 21940 (n_eff 699.0), Brier 0.156555, paired d -0.00726745 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
