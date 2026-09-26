# Fleet status — 2026-09-26 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade; roughly flat with BTC | $1,198.69 (was $1,202.78) |
| meanrev | HD | No new trade; data_asof 09-25 (normal 1-day lag, feed_delayed=false) | $1,185.35 (was $1,181.55) |
| sentiment | CASH | No trade — still in cash | $869.30 (unchanged) |
| scalper | 10/10 seats | 38 closed round trips (642 total), 23W/15L, net +$19.54 | $942.71 (was $926.38) |
| smallwins (lab) | 486 open seats | 89 new runs (1793→1882); open 477→486 | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STILL STUCK: 0 new scans since 09-11 15:12 UTC (~15 days) | n/a |
| social_radar | — (no capital) | Same root staleness — `last_scan_utc` unchanged since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.

## Changed
- **crypto**: no trade; BTC-USD roughly flat, $1,202.78 → $1,198.69.
- **meanrev**: no trade; HD marked up $1,181.55 → $1,185.35.
- **sentiment**: no trade; flat in cash at $869.30.
- **scalper**: 38 closed round trips (23W/15L), net +$19.54; equity $926.38 → $942.71; open seats
  steady at 10/10 (refilled as closed).
- **smallwins**: 89 new lab runs; open seats up 477 → 486.
- Paper-fleet cron: 88 cycle commits in this 24h window, steady ~13–18 min cadence, no gap over
  25 min, no error/RED FLAG commits found.

## Needs a look
- **scalper/TVKUSDT seat**: still open, entered 2026-09-12 — now day 14. Supervisor last logged
  this 2026-09-24 (judgment `2026-09-24-scalper-1`, status "open") as a SIM-INTEGRITY issue: priced
  off a dead 2023-11-27 Binance candle (delisted pair), so the +3%/-3%/24h rule can never fire. No
  newer supervisor judgment on it found in the last 24h.
- **Watcher (grok_sentinel)**: no new scan — verdict timestamp still 2026-09-11T15:12:52 UTC,
  ~15 days stale. This is why sentiment stays gated in cash.
- **social_radar**: same root staleness — `last_scan_utc` unchanged since 2026-09-11T15:29:50 UTC,
  ~15 days running.
