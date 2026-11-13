# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-13T07:08:16+00:00

- predictions written: **32156**
- resolved and scored: **20311**
- annulled: **82** (rate 0.4% — OK)

- observed event rate: **0.2044**
- Brier (forecaster): 0.168624
- Brier (baseline):   0.168624
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0733** (mean group 344.21)
- **n_eff 776.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 19137 (n_eff 720.3), Brier 0.163289, paired d -0.00024351 — indistinguishable from baseline
- `liq_band_v1`: n 18839 (n_eff 695.5), Brier 0.162668, paired d +0.00008426 — indistinguishable from baseline
- `liqtier_v1`: n 19137 (n_eff 720.3), Brier 0.162929, paired d +0.00011644 — indistinguishable from baseline
- `momo_v1`: n 19137 (n_eff 720.3), Brier 0.163336, paired d -0.00029101 — indistinguishable from baseline
- `momo_v2`: n 18839 (n_eff 695.5), Brier 0.162294, paired d +0.00045843 — indistinguishable from baseline
- `ownrate_v1`: n 19137 (n_eff 720.3), Brier 0.170384, paired d -0.00733901 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
