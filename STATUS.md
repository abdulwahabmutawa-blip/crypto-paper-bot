# Fleet Status — 2026-11-06 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No position change; tracking BTC selloff | $1,079.28 (11-04 $1,150.66 → 11-06 04:52 UTC $1,079.28), bench $1,173.52 |
| meanrev | NVDA | No trade; NVDA marked down hard on 11-05 | $1,032.64 (11-04 $1,138.92 → 11-05 $1,032.64, -9.3%), bench $976.52 |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen | $726.83 |
| scalper | 9 cash seats + 1 stuck (TVKUSDT) | 17 exits (15 STOP, 1 TARGET, 1 TIME), net -$25.31 | $539.33 (vs ~$560.94 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan has NOT refreshed; still dated 2026-10-20 | n/a |

## Changed
- **crypto**: $1,150.66 (11-04) → $1,079.28 (today, latest intraday mark), tracking the broader BTC drop; no position change (holding BTC-USD since 09-08). Gap to bench ($1,173.52) essentially unchanged in relative terms.
- **meanrev**: no trade this window, but NVDA (bought 11-04 at $202.84) marked the book down 1138.92 → 1032.64 (-9.3%) on 11-05, a sharper drop than its benchmark basket (-4.4%). No 11-06 daily bar posted yet.
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).
- **scalper**: 17 round trips closed in the window — 15 STOP, 1 TARGET, 1 TIME; net -$25.31. Equity $560.94 → $539.33.
- Loop health: 75 cycle commits in the 24h window, median cadence ~18 min (workflow is every 20 min). One gap of ~159 min (2026-11-05 ~14:58→17:36 UTC) and one of ~39 min; no error/exception/traceback text found in any commit message.

## Needs a look
- **Watcher's Grok risk scan is stale, NOT resumed**: `data/sentinel_state.json` / `data/sentinel_verdict.json` still show `last_scan_utc`/`ts` = 2026-10-20T16:09 UTC — ~17 days old, file last touched 2026-11-04 13:51, no change in the last 24h. This contradicts yesterday's digest, which reported the scan as refreshing again. `sentinel_gate.severe()` (consumed by **crypto**, among others) treats verdicts older than 24h as UNKNOWN, not calm — so the crypto bot's risk gate is currently running without a live signal.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~55 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $539.33 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- **meanrev** has no 2026-11-06 daily history bar yet as of this digest — only an intraday mark; today's close value is not yet confirmed.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again described a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher. This report covers the real current roster; the stale scheduled-task prompt likely needs updating at the source.
