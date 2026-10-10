# Fleet status — 2026-10-10 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; small bounce with BTC | $1,179.48 (bench $1,282.48) |
| meanrev | JNJ | No trade; new daily mark landed (up) | $1,139.44 (was $1,117.63) |
| sentiment | CASH | No activity — Watcher feed still down | $869.30 (flat) |
| scalper | 10/10 seats | 32 round trips: 18 target / 12 stop / 2 time, net +$7.29 realized | $770.86 (was $763.45) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 (~29 days down) |

## Changed
- scalper: 32 round trips closed (18 TARGET / 12 STOP / 2 TIME), net +$7.29 realized; value up $763.45 → $770.86; seats stayed 10/10 (fresh entries: TSLABUSDT, CRCLBUSDT, MSTRBUSDT, CAKEUSDT, BABABUSDT, ATOMUSDT, CYBERUSDT, RAYUSDT, ALTUSDT). Yesterday's garbled non-ASCII-symbol seat is gone (closed out).
- meanrev: no trade; new daily mark landed (2026-10-09), value $1,117.63 → $1,139.44, bench also up ($1,030.81 → $1,036.99).
- crypto: no trade; value up $1,178.82 → $1,179.48 (bench $1,281.76 → $1,282.48), still tracking BTC.
- sentiment: no position changes, no trades — still parked in cash at $869.30.
- Cron: 90 cycle commits in the 24h window, steady ~16-18min cadence, no gap over 18min — no missed/failed cycles.
- One scheduled bot.yml run (queued 23:32 UTC, 0 jobs) was later marked "cancelled" (~3h after queuing) — no cycle gap resulted, cadence held throughout; all other runs in the window show conclusion "success".

## Needs a look
- Watcher (sentinel) hasn't produced a scan since 2026-09-11 — ~29 days down now (pre-existing, not new today). sentiment stays idle while it's down.
- scalper's TVKUSDT seat (opened 2026-09-12) is still open 28 days later — same stuck seat flagged in prior digests, unresolved.
- Scheduled-task note (unchanged): this routine's own prompt lists a 9-bot roster (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the repo. Per CLAUDE.md/`reports/kill_criteria.md`, the actual active fleet is 4 paper books (crypto, meanrev, sentiment, scalper) + the non-capital Watcher; congress, allweather, commodity, hunter, hypecrypto, scholar, analyst and stock remain retired frozen archives, untouched in this window. Reported against the real roster, not the stale prompt list.
