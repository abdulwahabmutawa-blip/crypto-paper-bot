# Fleet status — 2026-09-11 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade | $1,100.16 (09-11 mark, was $1,117.93) |
| meanrev | HD | No new trade — mkt-hours marks only | $1,236.28 (09-10 close, was $1,255.81) |
| sentiment | USO | 1 rotation: ZEC-USD → USO (09-10 14:08, hype faded off Grok list) | $896.68 (09-10 mark, was $929.68) |
| scalper | 10 open seats | 27 round trips closed (171 lifetime), 6W/21L, net -$48.30; open seats 7→10 | $922.20 (was $971.45) |
| smallwins (lab) | 317 open seats | 88 runs, 1,456 newly resolved (20,000 lifetime) — paper study, no $ book | n/a |
| Watcher | — (no capital) | 4 scans (12:21, 14:13, 22:10, 22:11 UTC) — risk level "caution" each time | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, stock, analyst | No state file changed in 24h | — |
| lottery — REAL MONEY | flat, kill-switched | Owner stopped live entries 09-10 (surge lane -$6.13/5d, 3y backtest -34.5%); not part of paper fleet | not evaluated here |
| hype-ibkr — REAL MONEY | not evaluated | Logging stopped ~17:51 UTC 09-10 (same daily pattern) | not part of paper fleet |

## Changed
- **sentiment**: ZEC-USD → USO at 09-10 14:08, on a Grok "hype faded" signal. Book down to $896.68 from $929.68 (-3.5%).
- **scalper**: 27 new closed round trips (144→171 lifetime), open seats up 7→10, losing stretch (6W/21L, -$48.30 net). Equity $922.20, down from $971.45 (-5.1%).
- **crypto**, **meanrev**: no trades; still holding BTC-USD and HD, both drifted down slightly with the market (-1.6% each).
- **lottery** (real money, out of scope): owner pulled the kill switch 09-10 on the surge lane after a losing backtest — flagging only because it's a new file in the repo, not a paper-fleet event.
- Paper-fleet cron: 88 cycle commits in 24h, steady ~17-18 min cadence, no gaps. No error/fix/revert commit messages in the window.

## Needs a look
- Bot roster mismatch persists: this digest's assumed list (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter) still doesn't match what's active. Per `CLAUDE.md`, only 4 books trade daily (crypto, meanrev, sentiment, scalper); the other 8 remain frozen archives (0 state changes in 24h).
- This session's clone was shallow with a stale/truncated ref that made it look like the fleet had gone dark for ~44h (2026-09-09 05:02 → 2026-09-11 01:36). A full unshallow fetch showed that gap was a clone artifact, not a real outage — cycles ran continuously at normal cadence throughout. No actual fleet downtime found. Flagging in case the checkout can be fixed to always fetch full history upfront, so this doesn't need re-diagnosing daily.
- Everything else: no exceptions, no stale prices, no impossible states found in the data touched this window.
