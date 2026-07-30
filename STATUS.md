# Fleet status — 2026-07-30 (UTC)

Last cycle: 2026-07-30 04:58 UTC (success). All paper accounts, $1,000 start each.

| Bot | Holds | Value | Bench | 24h change |
|---|---|---|---|---|
| trend (crypto) | SOL-USD | $1,023.74 (asof 07-30) | $992.20 | 8 trades / 3 cash round-trips (XRP→SOL→cash→SOL→cash→SOL), all "signal flip" |
| regime (stock) | TQQQ | $814.07 (asof 07-29) | $970.93 | No trade; mark -6.2% day on Nasdaq/semis selloff |
| congress | NVDA, META, GOOG (+$700 cash) | $987.74 (asof 07-29) | $971.68 | No change |
| meanrev | AMZN | $1,027.88 (asof 07-29) | $971.74 | No trade; mark -1.8% day |
| commodity | USO | $1,084.26 (asof 07-29) | $971.74 | No trade; mark +7.3% day on oil surge |
| allweather | 5-asset basket | $990.18 (asof 07-29) | $971.68 | No change |
| hype (sentiment) | CASH | $896.16 (asof 07-29) | $971.68 | No trade, flat |
| Hunter | USO | $920.47 (asof 07-29) | $971.68 | ETH-USD → USO (07-29), "Oil now scores >1.25x better" |
| Watcher | advisory only, no position | — | — | Scanned 2026-07-30 04:04 UTC, risk: caution |

## Changed
- **trend/crypto**: churned hard — 8 trades, 3 full round-trips into cash and back into SOL-USD, all "signal flip" / "strongest eligible coin." Net roughly flat-to-up ($1,017.75 → $1,023.74).
- **Hunter**: sold ETH-USD, bought USO (07-29) — reward/risk board flipped back to Oil.
- **regime/stock**: no trade, but TQQQ mark dropped -6.2% ($867.78 → $814.07) — matches Watcher's "Dow -1,000pts on AI spend worries" scan.
- **commodity**: no trade, but USO mark jumped +7.3% ($1,010.15 → $1,084.26) — matches Watcher's "oil surges" after Iran strikes.
- congress, meanrev, allweather, hype: no trades, marks only.
- No stop-loss trips, no failed cycles, no exceptions found in the 50 commits reviewed.

## Needs a look
- **Supervisor/judgment pipeline still stuck**: `reports/judgments.jsonl`, `trade_attributions.jsonl`, `supervisor_scoreboard.json` unchanged since 2026-07-29 12:18 UTC, even though ~38 trading cycles have committed since. Same defect flagged in yesterday's digest, not resolved.
- **trend/crypto churn getting worse, not better**: 3 cash round-trips in this window alone (same signal-flip whipsaw noted yesterday).
- **regime/stock (TQQQ)**: down to $814.07, worst book in the fleet (~-18.6% since inception), no stop-loss by design.
- One cron gap of 6h07m (07-29 21:58 → 07-30 04:05 UTC) — within the range the workflow's own comments document as expected GitHub-throttling behavior, not a failure.
