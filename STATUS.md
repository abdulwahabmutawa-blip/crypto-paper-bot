# Fleet status — 2026-07-27 (UTC)

Last cycle: 2026-07-27 02:52 UTC (success). All paper accounts, $1,000 start each.

| Bot | Holds | Value | Bench | 24h change |
|---|---|---|---|---|
| trend (crypto) | CASH | $1,007.42 | $1,010.22 | Sold SOL-USD on signal flip, back to cash |
| regime (stock) | TQQQ | $902.17 (asof 07-24) | $983.54 | No new mark (weekend; Mon cycle not yet run) |
| congress | NVDA, META, GOOG (+$700 cash) | $992.19 (asof 07-24) | $984.30 | No change |
| meanrev | WMT | $1,004.31 (asof 07-24) | $984.15 | No change |
| commodity | USO | $1,145.80 (asof 07-24) | $984.15 | No change |
| allweather | 5-asset basket | $997.97 (asof 07-24) | $984.30 | No change |
| hype (sentiment) | CASH | $934.33 | $984.30 (asof 07-24) | Stop-loss hit on SHIB-USD (-11.3%), sold to cash |
| Hunter | USO | $1,052.10 (asof 07-24) | $984.30 | No change |
| Watcher | advisory only, no position | — | — | Scanned 07-27 00:01 UTC, risk: caution |

## Changed
- **hype/sentiment**: bought SHIB-USD 07-26 on a Grok hype signal, stop-loss triggered 07-27 (-11.3% from entry), sold back to cash. Value fell $1,053.92 → $934.33.
- **Stale-mark fix landed** (06f1ee0, 07-26 21:03 UTC): corrected weekend marks that had overstated hunter (+$21.55), congress (+$2.39) and understated allweather (-$0.31); added a monotonic guard so no bot can write a mark behind its newest one. Values above already reflect the fix.
- **Cron cadence recovered**: cycles ran every ~13 min continuously from 20:03 UTC through 02:52 UTC (5.5h+, no gaps) — a break from the prior four days of throttling. Earlier in the 24h window there were still gaps (08:39→11:48, 12:41→15:49, 16:42→20:03 UTC).
- trend: sold SOL-USD on a signal flip, now holding cash pending next entry.
- No stop-outs beyond hype/sentiment. No bot exceptions found in the commits reviewed.

## Needs a look
- Equity bots (regime, congress, meanrev, commodity, allweather, Hunter) haven't posted a fresh mark since 2026-07-24 close — expected over the weekend, but today's (Monday) market-hours cycle hadn't landed yet as of the 02:52 UTC snapshot this digest is built from.
- No supervisor coverage/scoreboard log since 07-26 07:20 UTC (pre-fix) — can't yet confirm from supervisor data whether the recovered cadence holds over a full 24h window; the last logged stat (22/72 cycles, 31%) predates the fix and is stale.
