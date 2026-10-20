# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-20T05:13:07+00:00

- predictions written: **22807**
- resolved and scored: **11324**
- annulled: **45** (rate 0.4% — OK)

- observed event rate: **0.2890**
- Brier (forecaster): 0.231130
- Brier (baseline):   0.231130
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0193** (mean group 323.51)
- **n_eff 1566.5 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 10150 (n_eff 1310.3), Brier 0.227989, paired d -0.00014759 — indistinguishable from baseline
- `liq_band_v1`: n 9852 (n_eff 1267.4), Brier 0.228949, paired d +0.00029195 — indistinguishable from baseline
- `liqtier_v1`: n 10150 (n_eff 1310.3), Brier 0.227422, paired d +0.00041949 — indistinguishable from baseline
- `momo_v1`: n 10150 (n_eff 1310.3), Brier 0.228423, paired d -0.00058201 — indistinguishable from baseline
- `momo_v2`: n 9852 (n_eff 1267.4), Brier 0.228929, paired d +0.00031160 — indistinguishable from baseline
- `ownrate_v1`: n 10150 (n_eff 1310.3), Brier 0.235209, paired d -0.00736790 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
