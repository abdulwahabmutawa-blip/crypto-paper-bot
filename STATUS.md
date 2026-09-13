# Fleet status — 2026-09-13 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade | $1,101.91 (was $1,102.40) |
| meanrev | HD | No new trade — mkt closed (weekend) | $1,248.77 (09-11 close, unchanged) |
| sentiment | CASH | No new trade — still in cash since 09-11 | $869.30 (unchanged) |
| scalper | 10 open seats | 28 round trips closed (206→234 lifetime), 9W/19L, net -$23.43 | $880.45 (was $911.32) |
| smallwins (lab) | 630 open seats | 86 new runs (654→740); resolved capped at 20,000 lifetime | n/a |
| Watcher (sentinel) | — (no capital) | STUCK: 0 new scans; last attempt 09-11 15:12 UTC failed (unparsed output) | n/a |
| carry (VPS) | BTCUSDT spot+perp | 3 new funding settlements (1→4) | Net $-1.00 on $2,000 |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, stock, analyst | No state file changed in 24h | — |
| lottery — REAL MONEY | flat, kill-switched | Still flat, kill switch active since 09-10 | $33.15, not part of paper fleet |
| hype-ibkr — REAL MONEY | not evaluated | No update since 09-10 17:50 UTC (still stalled) | not part of paper fleet |

## Changed
- **scalper**: 28 new closed round trips (206→234 lifetime), losing stretch continues (9W/19L this window, net -$23.43). Equity $880.45, down from $911.32 (-3.4%).
- **carry**: 3 new funding settlements banked (1→4). Still net negative, $-1.00 on $2,000, open BTCUSDT spot+perp unchanged.
- **crypto**, **meanrev**, **sentiment**: no trades; crypto mark roughly flat (+/-0.05%), meanrev/sentiment exactly unchanged from 24h ago (stock market closed over the weekend / sentiment idle in cash).
- Paper-fleet cron: 86 cycle commits in 24h, steady ~17-18 min cadence, no gaps >21 min.

## Needs a look
- **Watcher/sentinel**: no new scan in the full 24h window — stuck at last_scan_utc 2026-09-11 15:12 UTC (~38h stale now). That last attempt itself came back malformed: `risk_level: "unparsed"` and raw tool-call JSON leaked into the output instead of a real verdict. Per the file's own note, verdicts older than 24h are treated as UNKNOWN by every risk-gated bot — this one has been past that line for over a day.
- **social_radar**: same Grok-based scan pipeline also stuck, since 2026-09-11 15:29 UTC — likely the same root cause as Watcher (other social feeds like social_heat/coingecko are still updating fine).
- **hype-ibkr** (real money): still hasn't logged since 09-10 17:50 UTC — flagged yesterday too, still stale.
- Bot roster mismatch persists: this digest's assumed list (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter) still doesn't match what's active. Per `CLAUDE.md`, the paper fleet is crypto, meanrev, sentiment, scalper; the other 8 named remain frozen archives (0 state changes in 24h).
- Everything else: no exceptions, no failed/skipped cron cycles, no impossible states found in the data touched this window.
