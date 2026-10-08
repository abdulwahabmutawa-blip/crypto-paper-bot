# Fleet status — 2026-10-08 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; tracking BTC's decline | $1,178.86 (bench $1,281.81) |
| meanrev | JNJ | No trade; new daily mark landed | $1,125.80 (was $1,110.29) |
| sentiment | CASH | No activity — Watcher feed still down | $869.30 (flat) |
| scalper | 8/10 seats | 20 round trips: 6 target / 12 stop / 2 time, net -$18.35 realized | $793.07 (was $815.38) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 (~27 days down) |

## Changed
- scalper: 20 round trips closed (6 TARGET / 12 STOP / 2 TIME), net -$18.35 realized; seats 7/10 → 8/10 open (6 fresh entries in the last few hours: LINKUSDT, MSTRBUSDT, CRVUSDT, JTOUSDT, LDOUSDT, CHIPUSDT, NVDABUSDT opened, one closed), cash at $157.18.
- crypto: no trade; value down $1,200.97 → $1,178.86, tracking BTC's broader slide (bench also down, $1,305.84 → $1,281.81).
- meanrev: no trade; daily mark landed, value $1,110.29 → $1,125.80.
- sentiment: no position changes, no trades — still parked in cash.
- Cron: 86 cycle commits in the last 24h, normal ~17min median cadence with two gaps near 35min — within normal GitHub Actions scheduling variance, no error/fail commits found in the log.

## Needs a look
- Watcher (sentinel) hasn't produced a scan since 2026-09-11 — ~27 days down now (pre-existing, not new today). sentiment stays idle while it's down.
- scalper's TVKUSDT seat (opened 2026-09-12) is still open 26 days later — same stuck seat flagged in prior digests, unresolved.
- Scheduled-task note: this routine's own prompt lists a 9-bot roster (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that still doesn't match the repo. Per CLAUDE.md/`reports/kill_criteria.md`, the actual active fleet is 4 paper books (crypto, meanrev, sentiment, scalper) + the non-capital Watcher; congress, allweather, commodity, hunter, hypecrypto, scholar, analyst and stock remain retired frozen archives. Reported against the real roster, not the stale prompt list.
