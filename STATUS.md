# Fleet status — 2026-10-06 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; price drift only | $1,223.24 (bench $1,330.06) |
| meanrev | JNJ | No trade; new daily mark landed (Mon close) | $1,101.96 (was $1,115.82 Fri mark) |
| sentiment | CASH | No activity — Watcher feed still down | $869.30 (flat) |
| scalper | 10/10 seats (full) | 21 round trips: 4 target / 13 stop / 4 time, net -$29.38 realized | $824.73 (was $839.32) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 (~25 days down) |

## Changed
- scalper: 21 round trips closed (4 TARGET / 13 STOP / 4 TIME), net -$29.38 realized; 10/10 seats stayed full all cycle.
- crypto: no trade; value essentially flat $1,220.48 → $1,223.24 (bench also flat, $1,330.06).
- meanrev: no trade; Monday's daily close landed, value $1,115.82 (stale Fri mark) → $1,101.96.
- sentiment: no position changes, no trades — still parked in cash.
- Cron: 80 cycle commits in the last 24h, normal ~17min cadence except one ~69min gap (10-05 17:16→18:24 UTC, one cycle skipped, no error in the commit history around it).

## Needs a look
- Watcher (sentinel) hasn't produced a scan since 2026-09-11 — ~25 days down now (pre-existing, not new today). sentiment stays idle while it's down.
- scalper's TVKUSDT seat (opened 2026-09-12) is still open 24 days later — same stuck seat flagged in prior digests, unresolved. Supervisor log (10-05) flags it as marked at a stale/dead 2023 price.
- One cycle gap of ~69 minutes on 2026-10-05 (17:16→18:24 UTC) — longer than the usual ~17min cadence but only a single missed cycle, no error visible in commit history.
- Scheduled-task note: this routine's own prompt lists a 9-bot roster (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that no longer matches the repo. Per CLAUDE.md/`reports/kill_criteria.md`, the actual active fleet is 4 paper books (crypto, meanrev, sentiment, scalper) + the non-capital Watcher; congress, allweather, commodity, hunter, hypecrypto, scholar, analyst and stock are retired frozen archives (owner overrides 2026-09-04/09-05). Reported against the real roster, not the stale prompt list.
