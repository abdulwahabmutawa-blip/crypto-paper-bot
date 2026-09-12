# Fleet status — 2026-09-12 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade | $1,102.40 (09-12 mark, was $1,100.16) |
| meanrev | HD | No new trade — mkt-hours marks only | $1,248.77 (09-11 close, was $1,236.28) |
| sentiment | CASH | Sold USO → cash, "hype faded" signal | $869.30 (was $896.68 holding USO) |
| scalper | 10 open seats | 35 round trips closed (206 lifetime), 17W/18L, net -$11.72 | $911.32 (was $922.20) |
| smallwins (lab) | 464 open seats | 654 runs, 20,000 resolved lifetime — paper study, no $ book | n/a |
| Watcher (sentinel) | — (no capital) | 4 scans, risk level "caution" each time | n/a |
| carry (new, VPS) | BTCUSDT spot+perp | New book, opened 09-11 21:02 UTC, 1 funding settlement | Net $-1.14 on $2,000 |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, stock, analyst | No state file changed in 24h | — |
| lottery — REAL MONEY | flat, kill-switched | Still flat since 09-10 kill switch; 260 log commits, no position | $33.15, not part of paper fleet |
| hype-ibkr — REAL MONEY | not evaluated | No update since 09-10 17:50 UTC (still stalled) | not part of paper fleet |

## Changed
- **sentiment**: sold USO → CASH, no new position yet ("hype faded off Grok's list"). Book down to $869.30 from $896.68 (-3.1%).
- **scalper**: 35 new closed round trips (171→206 lifetime), open seats steady at 10, losing stretch continues (17W/18L, -$11.72 net). Equity $911.32, down from $922.20 (-1.0%).
- **crypto**, **meanrev**: no trades; still holding BTC-USD and HD, both drifted up slightly (+0.2%, +1.0%).
- **New book**: `carry` (funding-carry, delta-neutral BTC spot+perp) appeared 09-11 in `src/bot_carry.py`/`reports/carry.md` — runs on the VPS, not GitHub Actions, $2,000 paper capital (separate from the $1,000 fleet books), 1 funding settlement banked, net -$1.14 so far.
- **New, unexplained**: an `oracle/` prediction-scoring system started logging (`oracle: ...` commits) — not documented in CLAUDE.md and not a position-holding bot; flagging rather than describing further.
- Paper-fleet cron: 87 cycle commits in 24h, steady ~17-18 min cadence, no gaps >21 min. No error/fix/revert commit messages in the window.

## Needs a look
- `carry` and `oracle` are new since yesterday's digest and aren't described in CLAUDE.md — worth the owner confirming these are intentional additions to what gets tracked here.
- `hype-ibkr` (real money) still hasn't logged since 09-10 17:50 UTC — flagged yesterday too, still stale.
- Bot roster mismatch persists: this digest's assumed list (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter) still doesn't match what's active. Per `CLAUDE.md`, the paper fleet is crypto, meanrev, sentiment, scalper; the other 8 named remain frozen archives (0 state changes in 24h).
- Everything else: no exceptions, no stale prices, no impossible states found in the data touched this window.
