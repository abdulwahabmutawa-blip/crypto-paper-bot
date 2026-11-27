# Oracle scoreboard

generation `gen-000-baserate` · forecaster `baserate_v1` · 2026-11-27T08:56:58+00:00

- predictions written: **37200**
- resolved and scored: **25897**
- annulled: **121** (rate 0.5% — OK)

- observed event rate: **0.1702**
- Brier (forecaster): 0.143722
- Brier (baseline):   0.143722
- paired mean d: 0.00000000 (sd 0.000000)
- cluster rho: **0.0965** (mean group 354.71)
- **n_eff 737.4 / 100 required**

> **verdict: indistinguishable from baseline** (90% CI [0.0, 0.0])

## Comparators (phase 1 — paired vs baseline on shared resolutions)

- `age_v1`: n 24723 (n_eff 702.8), Brier 0.138214, paired d +0.00000715 — indistinguishable from baseline
- `liq_band_v1`: n 24425 (n_eff 683.9), Brier 0.137662, paired d +0.00002959 — indistinguishable from baseline
- `liqtier_v1`: n 24723 (n_eff 702.8), Brier 0.138218, paired d +0.00000245 — indistinguishable from baseline
- `momo_v1`: n 24723 (n_eff 702.8), Brier 0.138481, paired d -0.00026000 — indistinguishable from baseline
- `momo_v2`: n 24425 (n_eff 683.9), Brier 0.137658, paired d +0.00003372 — indistinguishable from baseline
- `ownrate_v1`: n 24723 (n_eff 702.8), Brier 0.145256, paired d -0.00703532 — worse than baseline

_AUC, precision, recall and hit rate are deliberately absent — see oracle/README.md._
