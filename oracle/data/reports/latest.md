# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-03T05:37:16+00:00

- predictions written: **16113**
- resolved and scored: **5548**
- annulled: **33** (rate 0.6% — OK)

- observed event rate: **0.2693**
- Brier (forecaster): 0.217100
- Brier (baseline):   0.217100
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0179** (mean group 308.2)
- **n_eff 852.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 4374 (n_eff 689.2), Brier 0.205866, paired d -0.00016407 — indistinguishable from baseline
- `liq_band_v1`: n 4076 (n_eff 610.0), Brier 0.207085, paired d +0.00038010 — indistinguishable from baseline
- `liqtier_v1`: n 4374 (n_eff 689.2), Brier 0.205217, paired d +0.00048572 — indistinguishable from baseline
- `momo_v1`: n 4374 (n_eff 689.2), Brier 0.206119, paired d -0.00041670 — indistinguishable from baseline
- `momo_v2`: n 4076 (n_eff 610.0), Brier 0.207075, paired d +0.00039048 — indistinguishable from baseline
- `ownrate_v1`: n 4374 (n_eff 689.2), Brier 0.212760, paired d -0.00705762 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
