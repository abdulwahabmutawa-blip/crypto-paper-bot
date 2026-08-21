# Pre-registered scoring plan — first official run 2026-09-16

Committed 2026-08-21, BEFORE any prediction has resolved, so the analysis
cannot bend around the results. Derived from the 08-21 forensics review
(36-agent adversarial audit; report in the owner's research folder). This
file governs how September's scoring is computed and reported; changing it
after 2026-09-15 requires an explicit owner decision recorded in the commit.

## The corrections stack (all applied through one engine)

Statistic engine: **day-block stationary bootstrap** over daily aggregated
loss differentials, run ONCE at the pre-registered date.

1. **Cluster by calendar day.** Outcomes co-move on market-wide wave days
   (measured pairwise rho ~0.38 in the 08-19..21 wave). Report n_eff via
   Kish DEFF = 1 + (m-1)*rho, never nominal rows. If wave-day clusters are
   few, use a wild cluster bootstrap.
2. **Matched-period base rate** for skill scores — the comparison baseline
   is the base rate realized over the evaluation window itself, not the
   trailing-365d climatology (which goes stale across regime shifts).
   Report the Brier reliability/resolution decomposition and
   regime-stratified results (wave vs non-wave days).
3. **Point-in-time universe.** Filters applied with information available
   at prediction date; delisted symbols retained with their outcomes.
4. **No peeking.** Every read before 2026-09-16 (including the 08-21
   forensics) is descriptive only. The significance guarantee exists only
   for the pre-registered run. Any future interim look must be
   pre-specified with alpha-spending (O'Brien-Fleming style).
5. **Multiplicity.** Holm-BH across the full comparator family
   (liqtier_v1, ownrate_v1, momo_v1, age_v1, momo_v2, liq_band_v1);
   Hansen SPA for "is the best one real"; report a Model Confidence Set if
   the window cannot crown a single winner (likely at this n_eff).
6. **Wave down-weighting.** 1/m within same-wave clusters, or
   Diebold-Mariano on daily aggregated loss differentials with
   cluster-robust errors.
7. **Window-basis stratification.** Rows predating the run-creation window
   fix (window_basis absent; runs 08-17..08-21) are scored separately: any
   hit whose 1.5x touch occurred before its run's creation time is
   look-ahead-contaminated and must be excluded from skill claims for
   those runs (kept, flagged, in calibration reporting).
8. **Hit-quality reporting.** Alongside outcomes: touch_day_index
   distribution, sustained_close fraction, retrace_48h_vs_target — a wick
   economy and a regime change must not be conflated in prose even though
   both count as outcome=1.

## Promotion gate (feature -> real-money entry-gate input)

Every condition must hold before ANY Oracle feature touches the lottery
book (owner approval required on top; the predict-only wall stays):

- The feature's comparator beats gen-0 on log-loss/Brier skill under the
  full stack above, surviving multiplicity, with day-clustered n_eff >= 100.
- Effect survives within-liquidity-bucket re-tests and wave down-weighting.
- Economics clear: full conditional return distribution (not hit rate),
  charged with per-coin realized spreads, behind a minimum-ADV floor.
  Break-even probability p_be = (L+c)/(G+L).
- Then: shadow entry gate (paper fills vs real quotes) before any staged
  real capital at fractional-Kelly sizes; judged live on calibration.

## Gen-2 (deferred until the above has run at least once)

Hierarchical random-intercept logistic regression (empirical-Bayes per-coin
intercepts + 4-6 fixed covariates, ridge, per-fold Platt recalibration);
walk-forward spanning >= two regimes; combinatorial purged CV with
purge/embargo matched to the 30d label overlap; every candidate
configuration logged from day one (MinBTL discipline). Gradient boosting
deferred until ~2,000 effective events. Resampling (SMOTE et al.) never.
