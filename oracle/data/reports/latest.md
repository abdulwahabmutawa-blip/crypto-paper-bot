# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-17T08:17:22+00:00

- predictions written: **33615**
- resolved and scored: **21906**
- annulled: **93** (rate 0.4% — OK)

- observed event rate: **0.1933**
- Brier (forecaster): 0.160479
- Brier (baseline):   0.160479
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.081** (mean group 347.67)
- **n_eff 753.1 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 20732 (n_eff 704.7), Brier 0.155063, paired d -0.00019516 — indistinguishable from baseline
- `liq_band_v1`: n 20434 (n_eff 682.2), Brier 0.154420, paired d +0.00005870 — indistinguishable from baseline
- `liqtier_v1`: n 20732 (n_eff 704.7), Brier 0.154783, paired d +0.00008511 — indistinguishable from baseline
- `momo_v1`: n 20732 (n_eff 704.7), Brier 0.155142, paired d -0.00027386 — indistinguishable from baseline
- `momo_v2`: n 20434 (n_eff 682.2), Brier 0.154104, paired d +0.00037388 — indistinguishable from baseline
- `ownrate_v1`: n 20732 (n_eff 704.7), Brier 0.162186, paired d -0.00731844 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
