# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-21T05:09:34+00:00

- predictions written: **23216**
- resolved and scored: **11677**
- annulled: **46** (rate 0.4% — OK)

- observed event rate: **0.2861**
- Brier (forecaster): 0.228942
- Brier (baseline):   0.228942
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0201** (mean group 324.33)
- **n_eff 1554.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 10503 (n_eff 1311.5), Brier 0.225666, paired d -0.00014668 — indistinguishable from baseline
- `liq_band_v1`: n 10205 (n_eff 1265.9), Brier 0.226510, paired d +0.00029244 — indistinguishable from baseline
- `liqtier_v1`: n 10503 (n_eff 1311.5), Brier 0.225120, paired d +0.00039992 — indistinguishable from baseline
- `momo_v1`: n 10503 (n_eff 1311.5), Brier 0.226110, paired d -0.00059098 — indistinguishable from baseline
- `momo_v2`: n 10205 (n_eff 1265.9), Brier 0.226452, paired d +0.00035019 — indistinguishable from baseline
- `ownrate_v1`: n 10503 (n_eff 1311.5), Brier 0.232813, paired d -0.00729345 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
