# Fleet status — 2026-10-03 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No trade; small BTC drift | $1,207.19 (was $1,206.91) |
| meanrev | JNJ | No trade; held since 10-01 rotation | $1,115.82 (was $1,127.41, per last daily mark 10-02) |
| sentiment | CASH | No activity — Watcher feed stale (see below) | $869.30 (flat) |
| scalper | 9 open seats | 37 round trips, 17 targets / 18 stops / 2 time-exits, net -$7.05 | $868.34 (was $882.44) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 |

## Changed
- scalper: 37 round trips in 24h (17 targets / 18 stops / 2 time-exits), net -$7.05 realized; seat count dropped 10 → 9.
- crypto, meanrev, sentiment: no position changes, no new trades.
- No cron gaps: 87 cycle commits in 24h, steady ~16.7 min cadence (max gap 18.6 min).

## Needs a look
- Watcher (sentinel) has not produced a scan since 2026-09-11 (22 days now). sentiment stays idle while it's down — pre-existing, known issue, not new today.
- scalper's TVKUSDT seat (stake $86.17, ~10% of book) has been open since 2026-09-12 (day 21) carrying the corrupted entry timestamp (resolves to Nov 2023). Flagged by supervisor on 2026-10-01 and still unresolved today.
- meanrev's 10-03 daily mark is not posted yet as of this digest (last entry in its history is 10-02); 24h change above uses the latest two marks available (10-01 → 10-02).
- This fleet is currently 4 active paper books (crypto, meanrev, sentiment, scalper) plus the non-capital Watcher, per CLAUDE.md/kill_criteria.md. Bots named in today's digest request (trend, regime, congress, commodity, allweather, hype, Hunter) were retired by owner overrides on 2026-09-04/09-05 and remain frozen archives, not live — reporting on the actual current roster instead.
