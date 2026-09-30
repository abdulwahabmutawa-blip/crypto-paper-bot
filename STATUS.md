# Fleet status — 2026-09-30 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No trade; BTC drifted down | $1,188.50 (was $1,193.62) |
| meanrev | HD | No trade; last EOD print 09-29 (next print pending) | $1,165.45 (was $1,172.37 on 09-28) |
| sentiment | CASH | No trade — still gated in cash | $869.30 (unchanged) |
| scalper | 10/10 seats | 46 round trips closed (25 stop, 18 target, 3 time), net ≈ −$25.42 | $892.03 (was $908.02) |
| Watcher (grok_sentinel) | — (no capital) | Still silent, 0 scans since 09-11 15:12 UTC (~19 days) | n/a |
| social_radar | — (no capital) | Same staleness, unchanged since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state-file changes in 24h | — |

Lottery and the oracle-bot side process are separate, non-paper-fleet activity — out of scope per CLAUDE.md.

## Changed
- Cron loop healthy: 87 cycle commits in 24h (09-29 05:09 → 09-30 05:07), median gap 17 min, max
  gap 19 min. All 6 GitHub Actions runs in the window that have finished are `completed/success`;
  the two most recent are still `in_progress`/`pending`, consistent with this workflow's normal
  long-running self-looping design, not an error.
- crypto: no trade, still holding BTC-USD; value down ~0.4%.
- meanrev: no trade, still holding HD; value down ~0.6% with the market. Daily history's last
  entry is 09-29 — HD prices once/day at close, so no 09-30 print exists yet at digest time.
- scalper: 46 closes in the 24h window (25 stop, 18 target, 3 time-exit), netting ≈ −$25.42;
  seats stayed full at 10/10.
- sentiment: no trades, flat.

## Needs a look
- **scalper/TVKUSDT dead seat**: still open since 2026-09-12 (day 18+), entered off a `surge`
  shape that never closed — known issue, not yet fixed.
- **Watcher / social_radar**: silent for ~19 days (since 09-11). Sentiment stays in cash as a
  direct result.
- **`reports/supervisor_scoreboard.json` is stale**: last touched 2026-09-28T18:00 UTC (~35h
  before this digest), not regenerated since — don't trust its loop-health numbers as current.
