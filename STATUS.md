# Fleet status — 2026-09-25 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade; roughly flat with BTC | $1,202.78 (was $1,201.32) |
| meanrev | HD | No new trade; data_asof 09-24 (normal 1-day lag, feed_delayed=false) | $1,181.55 (was $1,200.68, -1.6%) |
| sentiment | CASH | No trade — still in cash | $869.30 (unchanged) |
| scalper | 10/10 seats | 23 closed round trips (581→604), 12W/11L, net -$5.39 | $926.38 (was $932.41) |
| smallwins (lab) | 477 open seats | 88 new runs (1705→1793); open 248→477 | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STILL STUCK: 0 new scans since 09-11 15:12 UTC (~14 days) | n/a |
| social_radar | — (no capital) | Same root staleness — `last_scan_utc` unchanged since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.

## Changed
- **crypto**: no trade; BTC-USD roughly flat, $1,201.32 → $1,202.78.
- **meanrev**: no trade; HD marked down $1,200.68 → $1,181.55 (-1.6%) — a real price move (per
  supervisor's 09-24 note: HD -2.8% on a 5.11% 10-year), not a data issue.
- **sentiment**: no trade; flat in cash at $869.30.
- **scalper**: 23 closed round trips (12W/11L), net -$5.39; equity $932.41 → $926.38; open seats
  refilled 4→10.
- **smallwins**: 88 new lab runs; open seats jumped 248→477.
- Paper-fleet cron: 89 cycle commits in this 24h window, steady ~16–18 min cadence, no gap over
  20 min, no error/RED FLAG commits found.

## Needs a look
- **scalper/TVKUSDT seat**: still open, entered 2026-09-12 — now day 13. Supervisor's 2026-09-24
  log flags this as a SIM-INTEGRITY issue: priced off a dead 2023-11-27 Binance candle (delisted
  pair), so the +3%/-3%/24h rule can never fire. Supervisor recommended closing it; it is still
  open as of this digest (judgment id `2026-09-24-scalper-1`, status "open").
- **Watcher (grok_sentinel)**: no new scan — verdict timestamp still 2026-09-11T15:12:52 UTC,
  ~14 days stale. This is why sentiment stays gated in cash.
- **social_radar**: same root staleness — `last_scan_utc` unchanged since 2026-09-11T15:29:50 UTC,
  ~14 days running.
