# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-19T05:05:28+00:00

- predictions written: **22399**
- resolved and scored: **10974**
- annulled: **44** (rate 0.4% — OK)

- observed event rate: **0.2919**
- Brier (forecaster): 0.233268
- Brier (baseline):   0.233268
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0186** (mean group 322.73)
- **n_eff 1570.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 9800 (n_eff 1302.4), Brier 0.230259, paired d -0.00014097 — indistinguishable from baseline
- `liq_band_v1`: n 9502 (n_eff 1262.7), Brier 0.231361, paired d +0.00027890 — indistinguishable from baseline
- `liqtier_v1`: n 9800 (n_eff 1302.4), Brier 0.229685, paired d +0.00043329 — indistinguishable from baseline
- `momo_v1`: n 9800 (n_eff 1302.4), Brier 0.230716, paired d -0.00059847 — indistinguishable from baseline
- `momo_v2`: n 9502 (n_eff 1262.7), Brier 0.231319, paired d +0.00032095 — indistinguishable from baseline
- `ownrate_v1`: n 9800 (n_eff 1302.4), Brier 0.237677, paired d -0.00755873 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
