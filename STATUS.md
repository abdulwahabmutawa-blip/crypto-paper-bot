# Fleet Status — 2026-11-14 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged, no new trade since 11-12 sell | $1,027.21 |
| meanrev | CASH | Unchanged, still CASH since 11-09 stop-out | $1,000.74 |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 1/10 seats | TRXUSDT closed (TIME, -$0.44); 1 round trip | $492.06 (vs $491.82 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **scalper**: 1 round trip closed — TRXUSDT, TIME exit, -$0.44. Seats 2/10 → **1/10** (only TVKUSDT remains open). Equity $491.82 → $492.06.
- **crypto, meanrev, sentiment**: no trades, no position changes. Values flat vs yesterday.
- GitHub Actions `paper-trade-cycle`: runs #1023–#1026 all `success`; run #1027 `in_progress` since 02:18 UTC, still producing cycle commits through 05:05 — normal for a multi-hour loop run (see workflow comments on GitHub's throttled scheduler). No failed or skipped cycles found.

## Needs a look
- **Repo is a shallow clone** (50-commit depth) — visible cycle history only reaches back to 13:32 UTC yesterday, not the full 24h. Current state/value figures above are read directly from each bot's latest data file, so they're accurate regardless; only the "what happened earlier in the window" narrative is limited.
- **Watcher's Grok risk scan still stale**: `data/sentinel_verdict.json` unchanged since 2026-10-20T16:09 UTC — now ~589h (~24.5 days) old. `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN — risk gate still running blind. Unresolved, growing.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~63 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $492.06 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path) is out of scope for this digest per CLAUDE.md.
