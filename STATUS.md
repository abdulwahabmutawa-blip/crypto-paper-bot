# Fleet status — 2026-09-15 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade | $1,107.04 (was $1,107.78) |
| meanrev | HD | No new trade — marked to Monday's close | $1,257.35 (was $1,248.77) |
| sentiment | CASH | No new trade — still in cash since 09-11 | $869.30 (unchanged) |
| scalper | 10 open seats | 28 round trips closed (277→305), 16W/12L, net +$10.57 | $889.84 (was $881.49) |
| smallwins (lab) | 611 open seats | 87 new runs (829→916); resolved capped at 20,000 lifetime | n/a |
| Watcher (sentinel) | — (no capital) | STUCK: 0 new scans; last attempt 09-11 15:12 UTC still unresolved | n/a |
| carry (VPS, paper) | BTCUSDT spot+perp | 3 new funding settlements (7→10) | Net $-0.65 on $2,000 |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, stock, analyst | No state file changed in 24h | — |
| lottery — REAL MONEY | FLAT, kill-switched | Still flat, kill switch active since 09-10 | $33.15, not part of paper fleet |
| hype-ibkr — REAL MONEY | not evaluated | No update since 09-10 17:50 UTC (still stalled) | not part of paper fleet |

## Changed
- **scalper**: 28 new closed round trips (277→305), 16W/12L, net +$10.57. Equity $889.84, up from $881.49.
- **meanrev**: no trade; marked to Monday's close, $1,257.35 (+$8.58) from $1,248.77.
- **carry**: 3 new funding settlements banked (7→10). Lifetime net $-0.65 on $2,000, open BTCUSDT spot+perp unchanged since 09-11.
- **crypto**: no trade, roughly flat at $1,107.04.
- **sentiment**: no trade; unchanged in cash.
- Paper-fleet cron: 87 cycle commits in 24h, steady cadence (no gap over ~18 min), no missed cycles.

## Needs a look
- **Watcher/sentinel**: still no new scan — stuck at last_scan_utc 2026-09-11 15:12 UTC (~90h stale now, up from ~62h yesterday). Verdicts older than 24h are treated as UNKNOWN by every risk-gated bot; this has been past that line for over three days.
- **social_radar**: same scan pipeline stuck since 2026-09-11 15:29 UTC (~90h stale), unchanged from yesterday — likely the same root cause as Watcher.
- **hype-ibkr** (real money): still hasn't logged since 09-10 17:50 UTC — flagged the last three days too, still stale.
- Bot roster mismatch persists: this digest's assumed list per the scheduled task (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter) still doesn't match what's active. Per `CLAUDE.md`, the paper fleet is crypto, meanrev, sentiment, scalper; the other 8 named remain frozen archives (0 state changes in 24h).
- Local git clone was shallow (only ~3.3h of history) at the start of this run; had to deepen against origin to cover the full 24h window before compiling this digest.
- Everything else: no exceptions, no failed/skipped cron cycles, no impossible states found in the data touched this window.
