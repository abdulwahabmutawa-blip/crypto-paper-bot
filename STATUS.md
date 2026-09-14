# Fleet status — 2026-09-14 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade | $1,107.78 (was $1,101.91) |
| meanrev | HD | No new trade — mkt hasn't opened yet today (Mon) | $1,248.77 (09-11 close, unchanged) |
| sentiment | CASH | No new trade — still in cash since 09-11 | $869.30 (unchanged) |
| scalper | 10 open seats | 43 round trips closed (234→277 lifetime), 22W/21L, net -$5.75 | $881.49 (was $880.45) |
| smallwins (lab) | 686 open seats | 89 new runs (740→829); resolved capped at 20,000 lifetime | n/a |
| Watcher (sentinel) | — (no capital) | STUCK: 0 new scans; last attempt 09-11 15:12 UTC still unresolved | n/a |
| carry (VPS, paper) | BTCUSDT spot+perp | 3 new funding settlements (4→7) | Net $-0.81 on $2,000 |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, stock, analyst | No state file changed in 24h | — |
| lottery — REAL MONEY | FLAT, kill-switched | Still flat, kill switch active since 09-10 | $33.15, not part of paper fleet |
| hype-ibkr — REAL MONEY | not evaluated | No update since 09-10 17:50 UTC (still stalled) | not part of paper fleet |

## Changed
- **scalper**: 43 new closed round trips (234→277 lifetime), roughly flat W/L (22W/21L), net -$5.75. Equity $881.49, up slightly from $880.45.
- **carry**: 3 new funding settlements banked (4→7). Still net negative, $-0.81 on $2,000, open BTCUSDT spot+perp unchanged since 09-11.
- **crypto**: no trade, mark up to $1,107.78 (+0.5%) with BTC price.
- **meanrev**, **sentiment**: no trades; meanrev value unchanged (market not open yet today), sentiment unchanged in cash.
- Paper-fleet cron: 89 cycle commits in 24h, steady ~17-18 min cadence, no gaps.

## Needs a look
- **Watcher/sentinel**: no new scan in the full 24h window — stuck at last_scan_utc 2026-09-11 15:12 UTC (~62h stale now, up from ~38h yesterday). Same malformed last attempt as reported previously (`risk_level: "unparsed"`). Verdicts older than 24h are treated as UNKNOWN by every risk-gated bot; this has been past that line for over two days.
- **social_radar**: same scan pipeline stuck since 2026-09-11 15:29 UTC (~62h stale), unchanged from yesterday — likely the same root cause as Watcher.
- **hype-ibkr** (real money): still hasn't logged since 09-10 17:50 UTC — flagged the last two days too, still stale.
- Bot roster mismatch persists: this digest's assumed list per the scheduled task (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter) still doesn't match what's active. Per `CLAUDE.md`, the paper fleet is crypto, meanrev, sentiment, scalper; the other 8 named remain frozen archives (0 state changes in 24h).
- Everything else: no exceptions, no failed/skipped cron cycles, no impossible states found in the data touched this window.
