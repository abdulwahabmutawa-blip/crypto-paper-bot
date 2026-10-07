# Fleet status — 2026-10-07 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; tracking BTC's decline | $1,200.97 (bench $1,305.84) |
| meanrev | JNJ | No trade; new daily mark landed | $1,110.29 (was $1,101.96) |
| sentiment | CASH | No activity — Watcher feed still down | $869.30 (flat) |
| scalper | 7/10 seats | 46 round trips: 22 target / 21 stop / 3 time, net -$7.99 realized | $815.38 (was $824.73) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 (~26 days down) |

## Changed
- scalper: 46 round trips closed (22 TARGET / 21 STOP / 3 TIME), net -$7.99 realized; seats dropped from 10/10 full to 7/10 open, cash up to $241.98 waiting to redeploy.
- crypto: no trade; value down $1,223.24 → $1,200.97, tracking BTC's broader slide (bench also down, $1,330.06 → $1,305.84).
- meanrev: no trade; daily mark landed, value $1,101.96 → $1,110.29.
- sentiment: no position changes, no trades — still parked in cash.
- Cron: 77 cycle commits in the last 24h, normal ~17min cadence with two longer gaps (52min, 88min) — within GitHub's documented scheduling variance (see bot.yml comments), no errors found in commit history or workflow run logs.

## Needs a look
- Watcher (sentinel) hasn't produced a scan since 2026-09-11 — ~26 days down now (pre-existing, not new today). sentiment stays idle while it's down.
- scalper's TVKUSDT seat (opened 2026-09-12) is still open 25 days later — same stuck seat flagged in prior digests, unresolved.
- Scheduled-task note: this routine's own prompt lists a 9-bot roster (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that no longer matches the repo. Per CLAUDE.md/`reports/kill_criteria.md`, the actual active fleet is 4 paper books (crypto, meanrev, sentiment, scalper) + the non-capital Watcher; congress, allweather, commodity, hunter, hypecrypto, scholar, analyst and stock are retired frozen archives (owner overrides 2026-09-04/09-05). Reported against the real roster, not the stale prompt list.
