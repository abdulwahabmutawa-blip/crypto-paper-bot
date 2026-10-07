# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-07T06:24:30+00:00

- predictions written: **17649**
- resolved and scored: **6864**
- annulled: **33** (rate 0.5% — OK)

- observed event rate: **0.2704**
- Brier (forecaster): 0.217883
- Brier (baseline):   0.217883
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0142** (mean group 311.98)
- **n_eff 1268.6 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 5690 (n_eff 1111.6), Brier 0.209535, paired d -0.00025272 — indistinguishable from baseline
- `liq_band_v1`: n 5392 (n_eff 1023.8), Brier 0.210526, paired d +0.00028653 — indistinguishable from baseline
- `liqtier_v1`: n 5690 (n_eff 1111.6), Brier 0.208826, paired d +0.00045611 — indistinguishable from baseline
- `momo_v1`: n 5690 (n_eff 1111.6), Brier 0.209738, paired d -0.00045559 — indistinguishable from baseline
- `momo_v2`: n 5392 (n_eff 1023.8), Brier 0.210541, paired d +0.00027210 — indistinguishable from baseline
- `ownrate_v1`: n 5690 (n_eff 1111.6), Brier 0.217181, paired d -0.00789860 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
