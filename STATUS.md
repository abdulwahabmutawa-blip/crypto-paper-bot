# Fleet Status — 2026-11-09 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; price drifted down with BTC | $1,066.38 (11-08 $1,081.50 → 11-09 $1,066.38), bench $1,159.50 |
| meanrev | NVDA | No trade; no new daily bar yet (weekend into Monday pre-open) | $1,061.55 (unchanged, last bar 11-06), bench $979.46 |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen | $726.83 |
| scalper | 10/10 seats | 25 round trips closed, net -$19.44 | $506.05 (vs $521.32 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still has NOT refreshed | n/a |

## Changed
- **scalper**: 25 round trips closed in the window — 6 TARGET, 17 STOP, 2 TIME — net -$19.44. Equity $521.32 → $506.05. 8 stops fired together at 22:06 UTC (MSTRBUSDT/ARBUSDT/DASHUSDT/HBARUSDT/PEPEUSDT/GRAMUSDT/SNDKBUSDT/RSRUSDT) as BTC dipped ~1.7% in the hour — correlated beta, not 8 independent signals. New opens include BNBUSDT, HYPEUSDT, RWUSDUSDT, DODOUSDT, ARBUSDT, SPCXBUSDT, RENDERUSDT, PEPEUSDT, DRAMBUSDT; TVKUSDT (stuck since 09-12) still open, still 10/10 seats.
- **crypto**: no trade, still holding BTC-USD since 09-08 (entry $77,700.1). Book $1,081.50 → $1,066.38 as BTC fell to $74,707.5; bench also down ($1,175.94 → $1,159.50).
- **meanrev**: no trade; no new 11-07→11-09 bar posted yet (weekend close, Monday session not yet reflected at 04:53 UTC run time). Value unchanged at $1,061.55.
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).
- Loop cadence: scalper's own intraday marks show one ~4h gap (23:49 UTC 11-08 → 03:46 UTC 11-09) in an otherwise ~16-20 min cadence; matches the GitHub schedule-throttling behavior `bot.yml` documents (gaps up to ~675 min expected), not a new failure.

## Needs a look
- **Watcher's Grok risk scan is still stale**: `data/sentinel_state.json` / `data/sentinel_verdict.json` unchanged — `last_scan_utc`/`ts` still 2026-10-20T16:09 UTC (~469h / ~19.5 days old). `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN, not calm — risk gate still running blind.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~58 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $506.05 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- **meanrev** has no 11-07→11-09 bar yet — weekend close into Monday pre-open, expected, not an error.
- Git history check this run was limited: this session's clone is shallow (depth 50, ~3h of commits) and an unshallow attempt failed partway through, so cycle-cadence/error checks above come from each bot's own dashboard/state timestamps rather than a full `git log` scan. No error/exception text found in the commit messages that were visible.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/carry are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path, dominant commit volume in the visible window) is out of scope for this digest per CLAUDE.md.
