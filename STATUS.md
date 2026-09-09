# Fleet status — 2026-09-09 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | Sold ADA-USD, bought BTC-USD (09-08) | $1,128.94 (09-09 mark) |
| meanrev | HD | No new trade — mkt-hours marks only | $1,268.88 (09-08 close) |
| sentiment | DOT-USD | 4 rotations incl. a stop-loss on SOPH-USD (-12.5%); ended in DOT-USD | $980.83 (09-09 mark) |
| scalper | 10 open seats | 37 round trips closed (19W/18L), net -$8.29 | $1,005.93 |
| smallwins (lab) | 466 open seats | 394 runs, 13,323 resolved — paper study, no $ book | n/a |
| Watcher | — (no capital) | Scans at 19:13 and 03:56 UTC — risk level "caution" both times | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, stock, analyst | No state file changed in 24h | — |
| lottery — REAL MONEY | per its own state | Still active, HWM $44.27 (05:02 UTC) | not part of paper fleet |
| hype-ibkr — REAL MONEY | CASH (flat) | Logging stopped 20:01 UTC 09-08 (same as prior day — looks like a daily pattern, not a new fault) | not part of paper fleet |

## Changed
- **crypto**: sold ADA-USD ($1,114.83), bought BTC-USD ($1,109.10) on 09-08 — signal flip. Now up to $1,128.94 vs $1,119.79 yesterday.
- **sentiment**: busy day — ZEC→SOPH→ZEC→QCOM→DOT, including a stop-loss exit on SOPH-USD at -12.5%. Book down to $980.83 from $1,005.03.
- **scalper**: 37 closed round trips, 19W/18L, net -$8.29. 10 seats still open.
- **meanrev**: no trades; still holding HD, unchanged since 09-03 entry.
- Paper-fleet cron: 90 cycle commits in 24h, largest gap 22.5 min — no missed or failed cycles.
- Code change landed mid-window: PR #3 "Fix paper fleet migration, quote dates and ledger integrity" (merged 2026-09-08 13:27 UTC) touched `crypto_tracker.py`, `sentinel_trader.py`, `bot_scalper.py`, and `bot.yml`. Not evaluated here — out of scope for this digest, flagging that it landed.

## Needs a look
- This digest's brief bot list (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter) doesn't match what's actually active in this repo. Per `CLAUDE.md` and confirmed by the data, only 4 books trade daily (crypto, meanrev, sentiment, scalper); congress/commodity/allweather/hunter/hypecrypto/scholar/stock/analyst are frozen archives (0 state changes in 24h). Reporting on the real 4, not the assumed 9.
- sentiment had 4 round trips including a stop-loss in one day — worth a human glance, not necessarily a bug.
- Local clone was shallow (only ~50 commits) at the start of this run; had to unshallow to see the true 24h window. If this recurs, "last 24 hours" digests before this fix may have been silently truncated.
