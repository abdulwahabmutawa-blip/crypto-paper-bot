# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-09-21T05:19:25+00:00

- predictions written: **11723**
- resolved and scored: **1773**
- annulled: **11** (rate 0.6% — OK)

- observed event rate: **0.2786**
- Brier (forecaster): 0.224501
- Brier (baseline):   0.224501
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0293** (mean group 295.49)
- **n_eff 184.0 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 599 (n_eff 130.0), Brier 0.156748, paired d -0.00096956 — indistinguishable from baseline
- `liq_band_v1`: n 301 (n_eff 301.0), Brier 0.130166, paired d +0.00005865 — indistinguishable from baseline
- `liqtier_v1`: n 599 (n_eff 130.0), Brier 0.156061, paired d -0.00028260 — indistinguishable from baseline
- `momo_v1`: n 599 (n_eff 130.0), Brier 0.156575, paired d -0.00079573 — indistinguishable from baseline
- `momo_v2`: n 301 (n_eff 301.0), Brier 0.128862, paired d +0.00136259 — indistinguishable from baseline
- `ownrate_v1`: n 599 (n_eff 130.0), Brier 0.161323, paired d -0.00554444 — indistinguishable from baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
