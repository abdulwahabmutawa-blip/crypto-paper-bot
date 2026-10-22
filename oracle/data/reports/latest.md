# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-10-22T05:15:35+00:00

- predictions written: **23623**
- resolved and scored: **12030**
- annulled: **47** (rate 0.4% — OK)

- observed event rate: **0.2825**
- Brier (forecaster): 0.226277
- Brier (baseline):   0.226277
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0218** (mean group 325.1)
- **n_eff 1493.9 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 10856 (n_eff 1268.9), Brier 0.222839, paired d -0.00016233 — indistinguishable from baseline
- `liq_band_v1`: n 10558 (n_eff 1221.4), Brier 0.223539, paired d +0.00029761 — indistinguishable from baseline
- `liqtier_v1`: n 10856 (n_eff 1268.9), Brier 0.222295, paired d +0.00038236 — indistinguishable from baseline
- `momo_v1`: n 10856 (n_eff 1268.9), Brier 0.223234, paired d -0.00055697 — indistinguishable from baseline
- `momo_v2`: n 10558 (n_eff 1221.4), Brier 0.223453, paired d +0.00038324 — indistinguishable from baseline
- `ownrate_v1`: n 10856 (n_eff 1268.9), Brier 0.229870, paired d -0.00719296 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
