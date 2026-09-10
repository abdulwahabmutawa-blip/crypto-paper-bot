# Fleet status — 2026-09-10 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade | $1,117.94 (09-10 mark) |
| meanrev | HD | No new trade — mkt-hours marks only | $1,255.81 (09-09 close) |
| sentiment | ZEC-USD | 1 rotation: DOT-USD → ZEC-USD (09-09 11:58, hype faded off Grok list) | $929.68 (09-10 mark) |
| scalper | 7 open seats | 34 round trips closed since yesterday (144 lifetime), open seats 10→7 | $971.45 (-2.85% lifetime) |
| smallwins (lab) | 622 open seats | 479 runs, 18,544 resolved — paper study, no $ book | n/a |
| Watcher | — (no capital) | 3 scans (11:58, 20:06, 04:16 UTC) — risk level "caution" each time | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, stock, analyst | No state file changed in 24h | — |
| lottery — REAL MONEY | flat (last stopped NEWTUSDT 04:26 UTC) | Still active; per its own state, not part of paper fleet | not evaluated here |
| hype-ibkr — REAL MONEY | CASH (flat) | Logging stopped 20:02 UTC (connect errors, port 4001) — same daily pattern as prior day | not part of paper fleet |

## Changed
- **sentiment**: DOT-USD → ZEC-USD at 09-09 11:58, on a Grok "hype faded" signal. One rotation, no stop-loss this cycle. Book at $929.68, down from $980.83.
- **scalper**: 34 new closed round trips (110→144 lifetime), open seats down 10→7, cash built up to $287.23. Equity $971.45, down from $1,005.93.
- **crypto**, **meanrev**: no trades; holding BTC-USD and HD respectively, unchanged since their last entries.
- Paper-fleet cron: 84 cycle commits in 24h, largest gap ~20 min — no missed or failed cycles. No error/fix/revert commit messages in the window.

## Needs a look
- Bot roster mismatch persists: this digest's assumed list (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter) still doesn't match what's active. Per `CLAUDE.md`, only 4 books trade daily (crypto, meanrev, sentiment, scalper); congress/commodity/allweather/hunter/hypecrypto/scholar/stock/analyst remain frozen archives (0 state changes in 24h).
- Local clone starts shallow each run; had to unshallow again to see the true 24h window. Confirming this each day adds overhead — flagging in case the checkout can be fixed to fetch full history upfront.
- Everything else: no exceptions, no stale prices, no impossible states found in the data touched this window.
