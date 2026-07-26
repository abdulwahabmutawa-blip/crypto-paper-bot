# Fleet status — 2026-07-26 (UTC)

Last cycle: 2026-07-25 22:30 UTC (success). All paper accounts, $1,000 start each.

| Bot | Holds | Value | Bench | 24h change |
|---|---|---|---|---|
| trend (crypto) | SOL-USD | $1,000.43 | $998.59 | Sold DOGE; whipsawed SOL→cash→SOL on signal flips (4 fills) |
| regime (stock) | TQQQ | $902.17 | $983.54 | No change (market closed weekend) |
| congress | NVDA, META, GOOG (70% cash) | $994.58 | $983.30 | No change |
| meanrev | WMT | $1,004.31 | $984.15 | No change (market closed weekend) |
| commodity | USO | $1,145.80 | $984.15 | No change (market closed weekend) |
| allweather | 5-asset basket | $997.66 | $983.30 | No change (market closed weekend) |
| hype (sentiment) | CASH | $1,053.92 | $983.30 | No change (been in cash since SMCI sale 07-24) |
| Hunter | USO | $1,073.65 | $983.30 | No change |
| Watcher | advisory only, no position | — | — | Scanned 07-25 14:51 UTC, risk: caution |

## Changed
- trend: sold DOGE-USD, then round-tripped SOL-USD (buy→sell→cash→buy) within hours on signal flips — 4 fills, no net directional trade, now holding SOL-USD. Known defect (no hysteresis in the rank rule), already logged by the supervisor.
- No stop-outs. No bot errors — last completed run (22:30 UTC) succeeded.

## Needs a look
- No cycle commits since 2026-07-25 22:30 UTC — gap is 6.5h+ and still ongoing as of this digest (05:04 UTC). This is the same GitHub Actions cron-throttling issue flagged yesterday, and it's now the longest single gap seen (supervisor logged four gaps >90min on 07-24 alone, up to 386 min; today's is already longer). The supervisor's own operational_flag (as of 07-25 12:50 UTC) says only 26 of ~72 expected runs landed in a 24h window — worth checking the Actions tab.
- Watcher last scanned 14h ago (07-25 14:51 UTC) — consistent with its usual once-daily cadence, not confirmed as broken, but flagging alongside the cron gaps above.
