# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-01T06:36:13+00:00

- predictions written: **27601**
- resolved and scored: **15675**
- annulled: **59** (rate 0.4% — OK)

- observed event rate: **0.2442**
- Brier (forecaster): 0.197892
- Brier (baseline):   0.197892
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0452** (mean group 333.47)
- **n_eff 977.3 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 14501 (n_eff 873.1), Brier 0.193125, paired d -0.00022566 — indistinguishable from baseline
- `liq_band_v1`: n 14203 (n_eff 836.2), Brier 0.192922, paired d +0.00021445 — indistinguishable from baseline
- `liqtier_v1`: n 14501 (n_eff 873.1), Brier 0.192683, paired d +0.00021653 — indistinguishable from baseline
- `momo_v1`: n 14501 (n_eff 873.1), Brier 0.193305, paired d -0.00040602 — indistinguishable from baseline
- `momo_v2`: n 14203 (n_eff 836.2), Brier 0.192711, paired d +0.00042569 — indistinguishable from baseline
- `ownrate_v1`: n 14501 (n_eff 873.1), Brier 0.200059, paired d -0.00715975 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
