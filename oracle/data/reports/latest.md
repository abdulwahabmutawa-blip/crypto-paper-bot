# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-02T06:02:08+00:00

- predictions written: **15734**
- resolved and scored: **5223**
- annulled: **33** (rate 0.6% — OK)

- observed event rate: **0.2642**
- Brier (forecaster): 0.213336
- Brier (baseline):   0.213336
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0172** (mean group 307.22)
- **n_eff 834.5 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 4049 (n_eff 729.1), Brier 0.200094, paired d -0.00016161 — indistinguishable from baseline
- `liq_band_v1`: n 3751 (n_eff 632.9), Brier 0.201031, paired d +0.00035817 — indistinguishable from baseline
- `liqtier_v1`: n 4049 (n_eff 729.1), Brier 0.199521, paired d +0.00041092 — indistinguishable from baseline
- `momo_v1`: n 4049 (n_eff 729.1), Brier 0.200388, paired d -0.00045576 — indistinguishable from baseline
- `momo_v2`: n 3751 (n_eff 632.9), Brier 0.200887, paired d +0.00050294 — indistinguishable from baseline
- `ownrate_v1`: n 4049 (n_eff 729.1), Brier 0.206817, paired d -0.00688500 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
