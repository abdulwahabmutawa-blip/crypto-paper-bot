# Fleet status — 2026-10-05 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; price drift only | $1,220.53 (bench $1,327.11) |
| meanrev | JNJ | No trade; no new daily mark yet | $1,115.82 (last mark Fri 10-02) |
| sentiment | CASH | No activity — Watcher feed still down | $869.30 (flat) |
| scalper | 10/10 seats (full) | 28 round trips: 13 target / 12 stop / 3 time, net -$4.95 realized | $842.16 (was $853.24) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 (24 days down) |

## Changed
- scalper: 28 round trips closed (13 TARGET / 12 STOP / 3 TIME), net -$4.95 realized; 10/10 seats stayed full all cycle.
- crypto: no trade; value drifted $1,234.86 → $1,220.53 as BTC pulled back (bench also down, to $1,327.11).
- meanrev, sentiment: no position changes, no trades.
- Cron: 90 cycle commits in the last 24h, no gap over the usual ~17min cadence — no missed/failed cycles found.

## Needs a look
- Watcher (sentinel) hasn't produced a scan since 2026-09-11 — 24 days down now (pre-existing, not new today). sentiment stays idle while it's down.
- scalper's TVKUSDT seat (opened 2026-09-12) is still open 23 days later — same stuck seat flagged in prior digests, unresolved.
- meanrev's last daily mark is Fri 2026-10-02 (data_asof); today's cycle (05:12 UTC) ran before Monday's NYSE open, so no new mark yet — expected, not an error, but worth re-checking later today.
- Scheduled-task note: this routine's own prompt lists a 9-bot roster (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that no longer matches the repo. Per CLAUDE.md/`reports/kill_criteria.md`, the actual active fleet is 4 paper books (crypto, meanrev, sentiment, scalper) + the non-capital Watcher; congress, allweather, commodity, hunter, hypecrypto, scholar, analyst and stock are retired frozen archives (owner overrides 2026-09-04/09-05). Reported against the real roster, not the stale prompt list.
