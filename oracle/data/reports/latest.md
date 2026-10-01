# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-01T06:20:34+00:00

- predictions written: **15359**
- resolved and scored: **4901**
- annulled: **31** (rate 0.6% — OK)

- observed event rate: **0.2608**
- Brier (forecaster): 0.210776
- Brier (baseline):   0.210776
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0177** (mean group 306.29)
- **n_eff 765.2 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 3727 (n_eff 703.0), Brier 0.195565, paired d -0.00015835 — indistinguishable from baseline
- `liq_band_v1`: n 3429 (n_eff 597.4), Brier 0.196319, paired d +0.00028928 — indistinguishable from baseline
- `liqtier_v1`: n 3727 (n_eff 703.0), Brier 0.195071, paired d +0.00033572 — indistinguishable from baseline
- `momo_v1`: n 3727 (n_eff 703.0), Brier 0.195830, paired d -0.00042327 — indistinguishable from baseline
- `momo_v2`: n 3429 (n_eff 597.4), Brier 0.196091, paired d +0.00051655 — indistinguishable from baseline
- `ownrate_v1`: n 3727 (n_eff 703.0), Brier 0.202218, paired d -0.00681060 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
