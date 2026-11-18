# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-18T07:55:27+00:00

- predictions written: **33974**
- resolved and scored: **22303**
- annulled: **96** (rate 0.4% — OK)

- observed event rate: **0.1907**
- Brier (forecaster): 0.158625
- Brier (baseline):   0.158625
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0827** (mean group 348.44)
- **n_eff 750.1 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 21129 (n_eff 703.4), Brier 0.153192, paired d -0.00017564 — indistinguishable from baseline
- `liq_band_v1`: n 20831 (n_eff 681.3), Brier 0.152554, paired d +0.00005392 — indistinguishable from baseline
- `liqtier_v1`: n 21129 (n_eff 703.4), Brier 0.152942, paired d +0.00007425 — indistinguishable from baseline
- `momo_v1`: n 21129 (n_eff 703.4), Brier 0.153288, paired d -0.00027191 — indistinguishable from baseline
- `momo_v2`: n 20831 (n_eff 681.3), Brier 0.152262, paired d +0.00034540 — indistinguishable from baseline
- `ownrate_v1`: n 21129 (n_eff 703.4), Brier 0.160321, paired d -0.00730426 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
