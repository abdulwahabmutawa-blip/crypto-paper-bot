# Fleet status — 2026-09-22 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade (last: 09-08); marked up with BTC | $1,220.40 (was $1,161.98) |
| meanrev | HD | No new trade (last: 09-03); fresh close landed (data_asof 09-21) | $1,202.18 (was $1,213.18) |
| sentiment | CASH | No trade — still in cash, feed stuck since 09-11 | $869.30 (unchanged) |
| scalper | 10/10 seats | Routine churn: closed trips 497→521 (24 round trips), net +$18.42 | $942.34 (was $923.92) |
| smallwins (lab) | 492 open seats | 13 new runs (1516→1529); open 464→492; resolved capped at 20,000 | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STILL STUCK: 0 new scans since 09-11 15:12 UTC (now ~11 days) | n/a |
| social_radar | — (no capital) | Same root staleness — `last_scan_utc` unchanged since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.

## Changed
- **crypto**: no trade; BTC-USD marked up to $1,220.40 from $1,161.98 (+5.0%).
- **meanrev**: no trade; $1,213.18 → $1,202.18 (-0.9%); daily close is no longer stale (now dated 09-21).
- **sentiment**: no trade; flat in cash at $869.30.
- **scalper**: 24 closed round trips (497→521, e.g. FLOKIUSDT +$2.60, DOGEUSDT +$2.75), equity up $923.92 → $942.34.
- **smallwins**: 13 new lab runs; open seats 464→492.
- Paper-fleet cron: 94 cycle commits in this 24h window, steady ~16-17 min cadence, no gaps over 20 min.
- BTC execution watch: still collecting (ACCEPTED quotes, NO_TRADE, ~25bps est. cost) — no strategy qualified, nothing changed.

## Needs a look
- **Watcher (grok_sentinel)**: no new scan — verdict timestamp still 2026-09-11T15:12:52 UTC, now ~11 days stale. This is why sentiment's trading stays suspended.
- **social_radar**: same root staleness — `last_scan_utc` in state hasn't moved since 2026-09-11T15:29:50 UTC either, despite the dashboard file re-rendering each cycle. Same underlying cause as the Watcher (both consume Grok scans); unresolved 11 days running.
- No error/exception text found in any cycle commit message across the 24h window; no cron gaps beyond normal cadence.
