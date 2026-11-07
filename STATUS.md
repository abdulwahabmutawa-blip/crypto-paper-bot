# Fleet Status — 2026-11-07 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No position change; roughly flat | $1,082.04 (11-06 $1,083.00 → 11-07 $1,082.04), bench $1,176.53 |
| meanrev | NVDA | No trade; recovered some of Wed's drop | $1,061.55 (11-05 $1,032.64 → 11-06 $1,061.55, +2.8%); no 11-07 bar yet (market closed, Sat) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen | $726.83 |
| scalper | 7/10 seats open (was 1/10) | 6 new entries, several exits, net -$9.55 | $529.78 (vs $539.33 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still has NOT refreshed | n/a |

## Changed
- **crypto**: $1,083.00 (11-06) → $1,082.04 (today), essentially flat; still holding BTC-USD since 09-08. Bench also flat.
- **meanrev**: no trade; book moved $1,032.64 → $1,061.55 (+2.8%) on the 11-06 close, partly recovering Wed's drop. No 11-07 daily bar yet (US equities closed Saturday); last intraday mark repeats the 11-06 close.
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).
- **scalper**: opened 6 new seats (RAYUSDT, DASHUSDT, BABABUSDT, XRPUSDT, FETUSDT, XLMUSDT) alongside the old stuck TVKUSDT seat — now 7/10 open vs 1/10 yesterday. At least 12 round trips visible in the log within the window (4 TARGET, 8 STOP); the on-disk log only keeps the last 15, so the true count may be higher. Equity $539.33 → $529.78 (-$9.55).
- Loop health: 84 cycle commits in the 24h window (cron fires every 20 min). Two cadence gaps — ~43 min (11-06 10:36→11:18) and ~71 min (11-06 17:01→18:12) — matching gaps between GitHub Actions runs, not failures. The last 15 `paper-trade-cycle` workflow runs on GitHub Actions all show `conclusion: success`; none failed in this window. No error/exception text in any commit message.

## Needs a look
- **Watcher's Grok risk scan is still stale**: `data/sentinel_state.json` / `data/sentinel_verdict.json` unchanged in the last 24h — `last_scan_utc`/`ts` still 2026-10-20T16:09 UTC (~421h / ~17.5 days old per the dashboard). `sentinel_gate.severe()` (consumed by crypto, among others) treats verdicts older than 24h as UNKNOWN, not calm — the risk gate is still running blind.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~56 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $529.78 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- **meanrev** has no 2026-11-07 daily bar — market closed for the weekend, expected, not an error.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again described a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher. This report covers the real current roster; the stale scheduled-task prompt likely needs updating at the source.
- Lottery/IBKR activity (257 commits in this window) and the separate `oracle/` system (1 commit) are real-money/non-fleet paths per CLAUDE.md and are out of scope for this digest.
