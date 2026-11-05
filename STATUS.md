# Fleet Status — 2026-11-05 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No position change | $1,148.71 (vs 11-04 $1,096.64), bench $1,249.02 |
| meanrev | NVDA | Sold AMZN (signal flip, +$152), briefly cash, bought NVDA — all 11-04 | $1,138.89 (11-04 mark; no 11-05 bar posted yet) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen | $726.83 |
| scalper | 10/10 seats | 26 exits (20 TARGET, 5 STOP, 1 TIME), net +$19.93 | $560.94 (vs ~$546.56 yday) |
| Watcher (sentinel, no capital) | — | Grok hype scan resumed refreshing (was 15d stale) | n/a |

## Changed
- **meanrev**: AMZN sold on signal flip ($1,003.53 → $1,155.94), briefly to cash, then bought NVDA — all on 2026-11-04.
- **scalper**: 26 round trips closed in the window — 20 TARGET, 5 STOP, 1 TIME; net +$19.93. Equity $546.56 → $560.94.
- **crypto**: $1,096.64 → $1,148.71 (+4.7%), no position change (holding BTC-USD since 07-16), still trailing bench ($1,249.02).
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).
- **Watcher**: Grok hype scan is refreshing again every cycle (last scan 2026-11-05 05:02 UTC) — resolves the prior 15-day-stale flag.
- Loop health: 80 cycle commits in the window, continuous ~16–17 min cadence except one 115-min gap (11-04 13:52→15:47 UTC, within the workflow's own documented normal range). No error/exception/traceback found in cycle commit history.

## Needs a look
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~54 days) — past the bot's 24h hold cap; unresolved known bug, not new this run.
- **scalper** equity $560.94 remains below the R1 hard-stop floor ($750, −25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
