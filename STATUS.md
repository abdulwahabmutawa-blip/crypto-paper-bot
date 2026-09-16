# Fleet status — 2026-09-16 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade | $1,082.08 (was $1,107.04) |
| meanrev | HD | No new trade — marked to Tue's close (today not closed yet) | $1,235.51 (was $1,257.35) |
| sentiment | CASH | No new trade — still in cash since 09-11 | $869.30 (unchanged) |
| scalper | 10 open seats | 21 round trips closed (305→326), 9W/12L, net -$17.25 | $876.15 (was $889.84) |
| smallwins (lab) | 272 open seats | 89 new runs (916→1005); resolved capped at 20,000 lifetime | n/a |
| Watcher (sentinel) | — (no capital) | STUCK: 0 new scans; last attempt 09-11 15:12 UTC still unresolved | n/a |
| carry (VPS, paper) | BTCUSDT spot+perp | 3 new funding settlements (10→13) | Net $-0.45 on $2,000 |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, stock, analyst | No state file changed in 24h | — |
| lottery — REAL MONEY | FLAT, kill-switched | Still flat, kill switch active since 09-10 | $33.15, not part of paper fleet |
| hype-ibkr — REAL MONEY | not evaluated | No update since 09-10 17:50 UTC (still stalled) | not part of paper fleet |

## Changed
- **scalper**: 21 new closed round trips (305→326), 9W/12L, net -$17.25. Equity $876.15, down from $889.84.
- **crypto**: no trade; drifted down to $1,082.08 (-2.3%) from $1,107.04 with BTC price.
- **meanrev**: no trade; marked to Tuesday's close, $1,235.51 (-$21.84) from $1,257.35.
- **carry**: 3 new funding settlements banked (10→13). Lifetime net improved to $-0.45 (was $-0.65) on $2,000, open BTCUSDT spot+perp unchanged since 09-11.
- **sentiment**: no trade; unchanged in cash.
- Paper-fleet cron: 89 cycle commits in 24h, steady cadence (max gap ~18 min), no missed cycles. GitHub Actions history shows only `success`/`cancelled` runs (the cancels are the usual concurrent-run supersede pattern, not new) — no `failure` runs in the window.

## Needs a look
- **Watcher/sentinel**: still no new scan — stuck at last_scan_utc 2026-09-11 15:12 UTC (~110h stale now, up from ~90h yesterday). Verdicts older than 24h are treated as UNKNOWN by every risk-gated bot; this is now past that line by over four days.
- **social_radar**: same scan pipeline stuck since 2026-09-11 15:29 UTC (~109h stale), unchanged from yesterday — likely the same root cause as Watcher.
- **hype-ibkr** (real money): still hasn't logged since 09-10 17:50 UTC (~131h stale) — flagged the last four days too, still stale.
- Bot roster mismatch persists: this digest's assumed list per the scheduled task (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter) still doesn't match what's active. Per `CLAUDE.md`, the paper fleet is crypto, meanrev, sentiment, scalper; the other 8 named remain frozen archives (0 state changes in 24h).
- Local git clone was shallow again at the start of this run; had to deepen against origin (~500 commits) to cover the full 24h window before compiling this digest.
- Everything else: no exceptions, no failed/skipped cron cycles, no impossible states found in the data touched this window.
