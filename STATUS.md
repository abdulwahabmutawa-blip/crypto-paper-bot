# Fleet status — 2026-09-24 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade; marked down with BTC | $1,199.41 (was $1,204.73) |
| meanrev | HD | No new trade; data_asof 09-23 (normal 1-day lag, feed_delayed=false) | $1,200.68 (unchanged) |
| sentiment | CASH | No trade — still in cash | $869.30 (unchanged) |
| scalper | 4/10 seats | 23 closed round trips (558→581), net -$47.42 | $932.41 (was $983.90) |
| smallwins (lab) | 248 open seats | 89 new runs (1616→1705); open 409→248 | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STILL STUCK: 0 new scans since 09-11 15:12 UTC (~13 days) | n/a |
| social_radar | — (no capital) | Same root staleness — `last_scan_utc` unchanged since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.
An `oracle/` prediction system also committed today (ledger/predictions/scores); it isn't described in
CLAUDE.md's fleet list, so it's noted here but left out of scope for this digest.

## Changed
- **crypto**: no trade; BTC-USD marked down $1,204.73 → $1,199.41 (-0.4%).
- **meanrev**: no trade; flat at $1,200.68 (HD close data still dated 09-23).
- **sentiment**: no trade; flat in cash at $869.30.
- **scalper**: rough stretch — 23 closed round trips (558→581, 4 wins/19 losses), net -$47.42; equity
  $983.90 → $932.41; open seats dropped 10→4.
- **smallwins**: 89 new lab runs; open seats 409→248.
- Paper-fleet cron: 89 cycle commits in this 24h window, steady ~16–18 min cadence, no gap over 20 min,
  no error/RED FLAG commits found.

## Needs a look
- **scalper**: net -$47.42 over 23 closes (4W/19L, 17% win rate) — worst 24h stretch seen in recent
  digests. Worth checking if this is normal variance or a regime shift.
- **scalper/TVKUSDT seat**: still open, entered 2026-09-12 — now day 12 (flagged yesterday too).
  `unpriced_positions` is still empty, so it's still unclear whether the stale-candle flag from the
  09-22 supervisor note ever cleared.
- **Watcher (grok_sentinel)**: no new scan — verdict timestamp still 2026-09-11T15:12:52 UTC, ~13 days
  stale. This is why sentiment stays gated in cash.
- **social_radar**: same root staleness — `last_scan_utc` unchanged since 2026-09-11T15:29:50 UTC,
  ~13 days running.
