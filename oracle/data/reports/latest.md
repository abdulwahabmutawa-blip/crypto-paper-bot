# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-16T07:00:26+00:00

- predictions written: **33252**
- resolved and scored: **21507**
- annulled: **90** (rate 0.4% — OK)

- observed event rate: **0.1959**
- Brier (forecaster): 0.162417
- Brier (baseline):   0.162417
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0792** (mean group 346.84)
- **n_eff 757.4 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 20333 (n_eff 707.2), Brier 0.157016, paired d -0.00020867 — indistinguishable from baseline
- `liq_band_v1`: n 20035 (n_eff 684.2), Brier 0.156372, paired d +0.00006702 — indistinguishable from baseline
- `liqtier_v1`: n 20333 (n_eff 707.2), Brier 0.156712, paired d +0.00009597 — indistinguishable from baseline
- `momo_v1`: n 20333 (n_eff 707.2), Brier 0.157085, paired d -0.00027800 — indistinguishable from baseline
- `momo_v2`: n 20035 (n_eff 684.2), Brier 0.156045, paired d +0.00039412 — indistinguishable from baseline
- `ownrate_v1`: n 20333 (n_eff 707.2), Brier 0.164131, paired d -0.00732398 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
