# Fleet status — 2026-07-28 (UTC)

Last cycle: 2026-07-27 23:45 UTC (success). None since (see Needs a look). All paper accounts, $1,000 start each.

| Bot | Holds | Value | Bench | 24h change |
|---|---|---|---|---|
| trend (crypto) | ADA-USD | $982.08 | $987.52 | CASH → ADA-USD (07-27), strongest eligible coin |
| regime (stock) | TQQQ | $893.71 (asof 07-27) | $983.75 | No change |
| congress | NVDA, META, GOOG (+$700 cash) | $989.31 (asof 07-27) | $984.51 | No change |
| meanrev | WMT | $1,025.23 (asof 07-27) | $984.36 | No change |
| commodity | USO | $1,044.52 (asof 07-27) | $984.36 | No change (value down ~8.8% on the mark, no trade) |
| allweather | 5-asset basket | $998.67 (asof 07-27) | $984.51 | No change |
| hype (sentiment) | RKLB | $946.35 | $984.51 | CASH → RKLB (07-27), Grok hype signal |
| Hunter | USO | $960.28 | $984.51 | Trailing stop hit, then immediately re-bought USO |
| Watcher | advisory only, no position | — | — | Scanned 07-27 20:13 UTC, risk: caution |

## Changed
- **trend/crypto**: rotated CASH → ADA-USD (07-27), "strongest eligible coin" signal (-6.3% 7d momentum).
- **hype/sentiment**: bought RKLB (07-27) on a Grok hype signal (space-contract buzz, retail frenzy), following yesterday's SHIB-USD stop-loss exit.
- **Hunter**: trailing stop tripped on USO (-8% from high-water mark), then the reward/risk board immediately re-picked USO as the top score — sold and re-bought the same ticker at the same price ($128.04), same value ($985.52). Net position unchanged, just a round-trip in the trade log.
- No other position changes. No exceptions found in the commits reviewed.

## Needs a look
- **Cron gap, ongoing**: last cycle was 2026-07-27 23:45 UTC; none since — 5h20m+ with no cycle as of this digest (2026-07-28 05:06 UTC).
- **Earlier gap same window**: 2026-07-27 05:07 → 12:02 UTC (~6h55m, no cycles). Once running, cadence was solid every ~13 min from 12:02 to 23:45 with no gaps.
- **commodity**: value dropped $1,145.80 → $1,044.52 (~-8.8%) with no stop-loss trade recorded — worth confirming this bot has no risk overlay by design (only Hunter appears to carry a trailing stop).
- **Watcher**: last scan 20:13 UTC 07-27 (~9h stale as of this digest), consistent with the cron gap above rather than a Watcher-specific failure.
