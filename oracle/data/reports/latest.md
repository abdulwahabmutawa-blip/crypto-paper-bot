# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-27T05:29:21+00:00

- predictions written: **25621**
- resolved and scored: **13827**
- annulled: **52** (rate 0.4% — OK)

- observed event rate: **0.2628**
- Brier (forecaster): 0.211646
- Brier (baseline):   0.211646
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0336** (mean group 329.18)
- **n_eff 1149.8 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 12653 (n_eff 1003.8), Brier 0.207402, paired d -0.00020244 — indistinguishable from baseline
- `liq_band_v1`: n 12355 (n_eff 959.9), Brier 0.207574, paired d +0.00024394 — indistinguishable from baseline
- `liqtier_v1`: n 12653 (n_eff 1003.8), Brier 0.206905, paired d +0.00029510 — indistinguishable from baseline
- `momo_v1`: n 12653 (n_eff 1003.8), Brier 0.207653, paired d -0.00045320 — indistinguishable from baseline
- `momo_v2`: n 12355 (n_eff 959.9), Brier 0.207358, paired d +0.00045937 — indistinguishable from baseline
- `ownrate_v1`: n 12653 (n_eff 1003.8), Brier 0.214285, paired d -0.00708468 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
