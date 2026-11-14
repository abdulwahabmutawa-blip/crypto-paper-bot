# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-14T06:54:19+00:00

- predictions written: **32524**
- resolved and scored: **20708**
- annulled: **84** (rate 0.4% — OK)

- observed event rate: **0.2015**
- Brier (forecaster): 0.166462
- Brier (baseline):   0.166462
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0754** (mean group 345.09)
- **n_eff 768.3 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 19534 (n_eff 714.0), Brier 0.161100, paired d -0.00023283 — indistinguishable from baseline
- `liq_band_v1`: n 19236 (n_eff 689.9), Brier 0.160468, paired d +0.00007761 — indistinguishable from baseline
- `liqtier_v1`: n 19534 (n_eff 714.0), Brier 0.160757, paired d +0.00010949 — indistinguishable from baseline
- `momo_v1`: n 19534 (n_eff 714.0), Brier 0.161155, paired d -0.00028786 — indistinguishable from baseline
- `momo_v2`: n 19236 (n_eff 689.9), Brier 0.160118, paired d +0.00042766 — indistinguishable from baseline
- `ownrate_v1`: n 19534 (n_eff 714.0), Brier 0.168206, paired d -0.00733958 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
