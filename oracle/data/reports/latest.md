# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-25T09:04:48+00:00

- predictions written: **36491**
- resolved and scored: **25104**
- annulled: **117** (rate 0.5% — OK)

- observed event rate: **0.1742**
- Brier (forecaster): 0.146601
- Brier (baseline):   0.146601
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0941** (mean group 353.53)
- **n_eff 734.5 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 23930 (n_eff 697.7), Brier 0.141074, paired d -0.00001540 — indistinguishable from baseline
- `liq_band_v1`: n 23632 (n_eff 678.3), Brier 0.140520, paired d +0.00002782 — indistinguishable from baseline
- `liqtier_v1`: n 23930 (n_eff 697.7), Brier 0.141041, paired d +0.00001772 — indistinguishable from baseline
- `momo_v1`: n 23930 (n_eff 697.7), Brier 0.141329, paired d -0.00027012 — indistinguishable from baseline
- `momo_v2`: n 23632 (n_eff 678.3), Brier 0.140462, paired d +0.00008610 — indistinguishable from baseline
- `ownrate_v1`: n 23930 (n_eff 697.7), Brier 0.148168, paired d -0.00710970 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
