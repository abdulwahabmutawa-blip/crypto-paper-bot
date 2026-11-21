# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-21T07:34:51+00:00

- predictions written: **35058**
- resolved and scored: **23518**
- annulled: **105** (rate 0.4% — OK)

- observed event rate: **0.1831**
- Brier (forecaster): 0.153100
- Brier (baseline):   0.153100
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.088** (mean group 350.97)
- **n_eff 739.3 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 22344 (n_eff 697.4), Brier 0.147603, paired d -0.00009717 — indistinguishable from baseline
- `liq_band_v1`: n 22046 (n_eff 676.6), Brier 0.147012, paired d +0.00003325 — indistinguishable from baseline
- `liqtier_v1`: n 22344 (n_eff 697.4), Brier 0.147458, paired d +0.00004816 — indistinguishable from baseline
- `momo_v1`: n 22344 (n_eff 697.4), Brier 0.147787, paired d -0.00028115 — indistinguishable from baseline
- `momo_v2`: n 22046 (n_eff 676.6), Brier 0.146815, paired d +0.00023001 — indistinguishable from baseline
- `ownrate_v1`: n 22344 (n_eff 697.4), Brier 0.154755, paired d -0.00724876 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
