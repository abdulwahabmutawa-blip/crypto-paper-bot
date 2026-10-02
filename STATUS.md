# Fleet status — 2026-10-02 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No trade; BTC drifted up, bench $1,344.40 | $1,236.43 (was $1,210.66) |
| meanrev | JNJ | Trailing-stopped out of HD, rotated into JNJ same day | $1,127.41 (was $1,150.41) |
| sentiment | CASH | No activity — Watcher feed stale (see below) | $869.30 (flat) |
| scalper | 10 open seats | 41 round trips, 21 targets / 16 stops / 4 time-exits | $882.44 (was $873.41) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 |

## Changed
- meanrev: HD hit its 12% trailing stop (high-water $321.58), sold at $280.57 (2026-10-01 ~16:05 UTC), same-day rotation into JNJ at $259.78.
- scalper: 41 round trips in 24h (21 targets / 16 stops / 4 time-exits), net +$0.62 realized; still 10 seats open.
- crypto, sentiment: no position changes, no new trades.
- No cron gaps: 85 cycle commits in 24h, steady ~17.5 min cadence, no missed runs.

## Needs a look
- Watcher (sentinel) has not produced a scan since 2026-09-11 (21 days now). sentiment, lottery, and hype_ibkr stay idle while it's down — pre-existing, known issue, not new today.
- scalper's TVKUSDT seat (stake $86.17, ~10% of book) has been open since 2026-09-12 (day 20) carrying the corrupted entry timestamp (resolves to Nov 2023). Supervisor flagged it for closure on 2026-10-01 but it is still open in bot state — unresolved.
- This fleet is currently 4 active paper books (crypto, meanrev, sentiment, scalper) plus the non-capital Watcher, per CLAUDE.md/kill_criteria.md. The bots named in today's digest request (trend, regime, congress, commodity, allweather, hype, Hunter) were retired by owner overrides on 2026-09-04/09-05 and remain frozen archives, not live — reporting on the actual current roster instead.
