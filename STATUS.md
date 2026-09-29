# Fleet status — 2026-09-29 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No trade; BTC drifted down | $1,185.52 (was $1,192.10) |
| meanrev | HD | No trade; feed advanced normally over the weekend | $1,172.37 (was $1,185.35 on 09-25) |
| sentiment | CASH | No trade — still gated in cash | $869.30 (unchanged) |
| scalper | 10/10 seats | 38 round trips closed (20 stop, 17 target, 1 time), net ≈ −$14.68 | $908.02 (was $932.67) |
| Watcher (grok_sentinel) | — (no capital) | Still silent, 0 scans since 09-11 15:12 UTC (~18 days) | n/a |
| social_radar | — (no capital) | Same staleness, unchanged since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state-file changes in 24h | — |

Lottery and the oracle-bot side process are separate, non-paper-fleet activity — out of scope per CLAUDE.md.

**Note:** the scheduled prompt for this digest names a stale "9-bot" roster (trend, regime,
congress, meanrev, commodity, allweather, hype, Hunter, Watcher). Per CLAUDE.md and the live
state files, the active paper fleet is 4 books (crypto, meanrev, sentiment, scalper) plus the
Watcher utility; the other 8 named/former bots are frozen archives.

## Changed
- Cron loop healthy: 70 cycle commits in 24h, median gap ~16 min; one gap of ~2h18min
  (17:24–19:42 UTC on 09-28), otherwise no gap over ~19 min. No failed Actions runs in the window
  (all `completed/success`; one run still `in_progress` since 23:57 UTC 09-28, consistent with
  this workflow's normal long-running/self-looping design, not an error).
- crypto: no trade, still holding BTC-USD; value down ~0.6%.
- meanrev: last flagged as "feed stuck" — resolved; history advanced 09-25 → 09-28 as expected
  over the weekend (HD only trades weekdays). No trade, value down with the market.
- scalper: 38 closes in the ~23h window (mix of stop/target flips), netting ≈ −$14.68; seats
  stayed full at 10/10.
- sentiment: no trades, flat.

## Needs a look
- **scalper/TVKUSDT dead seat**: still open since 2026-09-12 (day 17+), priced off a delisted
  pair's stale candle — known issue, not yet fixed.
- **Watcher / social_radar**: silent for ~18 days (since 09-11). Sentiment stays in cash as a
  direct result.
- **`reports/supervisor_scoreboard.json` is stale**: last touched 2026-09-28T18:00 UTC (~11h
  before this digest), not regenerated since — don't trust its loop-health numbers as current.
