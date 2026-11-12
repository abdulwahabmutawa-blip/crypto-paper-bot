# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-12T07:33:58+00:00

- predictions written: **31788**
- resolved and scored: **19917**
- annulled: **80** (rate 0.4% — OK)

- observed event rate: **0.2077**
- Brier (forecaster): 0.171032
- Brier (baseline):   0.171032
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0704** (mean group 343.35)
- **n_eff 793.2 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 18743 (n_eff 734.0), Brier 0.165734, paired d -0.00024816 — indistinguishable from baseline
- `liq_band_v1`: n 18445 (n_eff 708.3), Brier 0.165141, paired d +0.00008532 — indistinguishable from baseline
- `liqtier_v1`: n 18743 (n_eff 734.0), Brier 0.165365, paired d +0.00012102 — indistinguishable from baseline
- `momo_v1`: n 18743 (n_eff 734.0), Brier 0.165794, paired d -0.00030780 — indistinguishable from baseline
- `momo_v2`: n 18445 (n_eff 708.3), Brier 0.164758, paired d +0.00046857 — indistinguishable from baseline
- `ownrate_v1`: n 18743 (n_eff 734.0), Brier 0.172834, paired d -0.00734810 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
