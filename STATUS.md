# Fleet status — 2026-10-01 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No trade; BTC drifted up, bench $1,303.98 | $1,199.26 (was $1,192.17) |
| meanrev | HD | No trade; last close down with sector, bench $1,015.56 | $1,150.41 (was $1,165.45) |
| sentiment | CASH | No activity — Watcher feed stale (see below) | $869.30 (flat) |
| scalper | 10 open seats | 30 round trips, 14 stops / 13 targets / 3 open-still | $871.07 (was ~$883.21) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 |

## Changed
- scalper: 30 round trips in 24h, net −$12.93 (14 stops vs 13 targets); no ticker list change.
- crypto, meanrev, sentiment: no position changes, no new trades.
- One cron gap: 2026-09-30 11:44→12:32 UTC (~47 min between cycles); self-recovered, cadence back to ~18 min since.

## Needs a look
- Watcher (sentinel) has not produced a scan since 2026-09-11 (~20 days). sentiment, lottery, and hype_ibkr stay idle while it's down — this is a pre-existing, known issue, not new today.
- scalper's TVKUSDT seat (stake $86.17, ~10% of book) has been open since 2026-09-12 (day 19) carrying a corrupted entry timestamp (resolves to Nov 2023) — the known dead-candle sim-integrity issue, still unresolved.
- This fleet is currently 4 active paper books (crypto, meanrev, sentiment, scalper) plus the non-capital Watcher, per CLAUDE.md/kill_criteria.md. The bots named in today's digest request (trend, regime, congress, commodity, allweather, hype, Hunter) were retired by owner overrides on 2026-09-04/09-05 and are frozen archives, not live — reporting on the actual current roster instead.
