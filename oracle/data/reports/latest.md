# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-04T06:14:40+00:00

- predictions written: **16492**
- resolved and scored: **5877**
- annulled: **33** (rate 0.6% — OK)

- observed event rate: **0.2699**
- Brier (forecaster): 0.217522
- Brier (baseline):   0.217522
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0167** (mean group 309.29)
- **n_eff 956.4 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 4703 (n_eff 791.6), Brier 0.207243, paired d -0.00021579 — indistinguishable from baseline
- `liq_band_v1`: n 4405 (n_eff 709.6), Brier 0.208444, paired d +0.00030449 — indistinguishable from baseline
- `liqtier_v1`: n 4703 (n_eff 791.6), Brier 0.206566, paired d +0.00046139 — indistinguishable from baseline
- `momo_v1`: n 4703 (n_eff 791.6), Brier 0.207429, paired d -0.00040110 — indistinguishable from baseline
- `momo_v2`: n 4405 (n_eff 709.6), Brier 0.208411, paired d +0.00033703 — indistinguishable from baseline
- `ownrate_v1`: n 4703 (n_eff 791.6), Brier 0.214205, paired d -0.00717786 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
