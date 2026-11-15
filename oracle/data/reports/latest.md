# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-15T07:02:24+00:00

- predictions written: **32890**
- resolved and scored: **21108**
- annulled: **87** (rate 0.4% — OK)

- observed event rate: **0.1986**
- Brier (forecaster): 0.164362
- Brier (baseline):   0.164362
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0775** (mean group 345.99)
- **n_eff 761.1 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 19934 (n_eff 709.0), Brier 0.158977, paired d -0.00022185 — indistinguishable from baseline
- `liq_band_v1`: n 19636 (n_eff 685.5), Brier 0.158338, paired d +0.00007101 — indistinguishable from baseline
- `liqtier_v1`: n 19934 (n_eff 709.0), Brier 0.158651, paired d +0.00010445 — indistinguishable from baseline
- `momo_v1`: n 19934 (n_eff 709.0), Brier 0.159039, paired d -0.00028377 — indistinguishable from baseline
- `momo_v2`: n 19636 (n_eff 685.5), Brier 0.157998, paired d +0.00041025 — indistinguishable from baseline
- `ownrate_v1`: n 19934 (n_eff 709.0), Brier 0.166093, paired d -0.00733795 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
