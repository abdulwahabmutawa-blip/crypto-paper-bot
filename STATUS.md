# Fleet status — 2026-10-09 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; small bounce with BTC | $1,173.13 (bench $1,275.57) |
| meanrev | JNJ | No trade; new daily mark landed (down) | $1,117.63 (was $1,125.80) |
| sentiment | CASH | No activity — Watcher feed still down | $869.30 (flat) |
| scalper | 10/10 seats | 36 round trips: 13 target / 22 stop / 1 time, net -$29.48 realized | $763.45 (was $793.07) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 (~28 days down) |

## Changed
- scalper: 36 round trips closed (13 TARGET / 22 STOP / 1 TIME), net -$29.48 realized; seats filled 8/10 → 10/10 (fresh entries: FILUSDT, TRXUSDT, MUBARAKUSDT, ALGOUSDT, ONTUSDT, ONEUSDT, AEROUSDT, a non-ASCII-symbol pair, METUSDT); cash down to $0 (fully deployed).
- crypto: no trade; value up $1,165.55 → $1,173.13, tracking BTC's small bounce (bench also up, $1,267.33 → $1,275.57).
- meanrev: no trade; new daily mark landed (for 2026-10-08, feed not delayed), value $1,125.80 → $1,117.63.
- sentiment: no position changes, no trades — still parked in cash.
- Cron: 90 cycle commits in the last 24h, steady ~17min median cadence, no gap over 18min — no missed/failed cycles. GitHub Actions runs in this window (bot.yml) all show conclusion "success".

## Needs a look
- Watcher (sentinel) hasn't produced a scan since 2026-09-11 — ~28 days down now (pre-existing, not new today). sentiment stays idle while it's down.
- scalper's TVKUSDT seat (opened 2026-09-12) is still open 27 days later — same stuck seat flagged in prior digests, unresolved.
- scalper opened a seat today with a garbled/non-ASCII symbol name (CJK characters + "USDT") — looks like a data/encoding glitch in the scan feed, not a real market symbol; worth a look at the feed parser.
- Scheduled-task note (unchanged from yesterday): this routine's own prompt lists a 9-bot roster (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the repo. Per CLAUDE.md/`reports/kill_criteria.md`, the actual active fleet is 4 paper books (crypto, meanrev, sentiment, scalper) + the non-capital Watcher; congress, allweather, commodity, hunter, hypecrypto, scholar, analyst and stock remain retired frozen archives. Reported against the real roster, not the stale prompt list.
