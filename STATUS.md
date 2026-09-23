# Fleet status — 2026-09-23 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade; marked up with BTC | $1,243.18 (was $1,222.28) |
| meanrev | HD | No new trade; data_asof now 09-22 (fresh) | $1,235.18 (was $1,202.18) |
| sentiment | CASH | No trade — still in cash | $869.30 (unchanged) |
| scalper | 10/10 seats | 39 closed round trips (519→558), net +$33.27 | $983.90 (was $953.79) |
| smallwins (lab) | 409 open seats | 90 new runs (1526→1616); open 504→409 | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STILL STUCK: 0 new scans since 09-11 15:12 UTC (now ~12 days) | n/a |
| social_radar | — (no capital) | Same root staleness — `last_scan_utc` unchanged since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.

## Changed
- **crypto**: no trade; BTC-USD marked up $1,222.28 → $1,243.18 (+1.7%).
- **meanrev**: no trade; $1,202.18 → $1,235.18 (+2.7%); HD close data_asof advanced to 09-22.
- **sentiment**: no trade; flat in cash at $869.30.
- **scalper**: 39 closed round trips (519→558, 28 wins/11 losses), net +$33.27; equity $953.79 → $983.90.
- **smallwins**: 90 new lab runs; open seats 504→409.
- Paper-fleet cron: 86 cycle commits in this 24h window, steady ~17 min cadence, no gap over 20 min, no RED FLAG/error commits found.

## Needs a look
- **Watcher (grok_sentinel)**: no new scan — verdict timestamp still 2026-09-11T15:12:52 UTC, now ~12 days stale. This is why sentiment's trading stays gated.
- **social_radar**: same root staleness — `last_scan_utc` in state hasn't moved since 2026-09-11T15:29:50 UTC either, 12 days running.
- **scalper/TVKUSDT seat**: still open, entered 2026-09-12 (now day 11) — per the 09-22 supervisor note this seat was flagged for booking against a dead/stale candle (~$86 of the book potentially mispriced). Today's dashboard `unpriced_positions` list is empty, so the flag may have cleared or may just not be firing — worth confirming which before trusting scalper's marked value.
