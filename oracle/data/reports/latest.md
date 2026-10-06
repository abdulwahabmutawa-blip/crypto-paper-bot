# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-06T06:44:38+00:00

- predictions written: **17261**
- resolved and scored: **6535**
- annulled: **33** (rate 0.5% — OK)

- observed event rate: **0.2716**
- Brier (forecaster): 0.218807
- Brier (baseline):   0.218807
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0149** (mean group 311.17)
- **n_eff 1164.1 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 5361 (n_eff 991.2), Brier 0.210143, paired d -0.00026141 — indistinguishable from baseline
- `liq_band_v1`: n 5063 (n_eff 907.9), Brier 0.211258, paired d +0.00028814 — indistinguishable from baseline
- `liqtier_v1`: n 5361 (n_eff 991.2), Brier 0.209407, paired d +0.00047450 — indistinguishable from baseline
- `momo_v1`: n 5361 (n_eff 991.2), Brier 0.210260, paired d -0.00037857 — indistinguishable from baseline
- `momo_v2`: n 5063 (n_eff 907.9), Brier 0.211324, paired d +0.00022260 — indistinguishable from baseline
- `ownrate_v1`: n 5361 (n_eff 991.2), Brier 0.217530, paired d -0.00764812 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
