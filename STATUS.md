# Fleet Status — 2026-11-15 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged, no new trade since 11-12 sell | $1,027.21 |
| meanrev | CASH | Unchanged, still CASH since 11-09 stop-out | $1,000.74 |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 3/10 seats | 3 closed (+$1.24, -$1.47, -$1.47), 2 opened | $490.43 (vs $492.06 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **scalper**: 3 round trips closed — DODOUSDT (TARGET, +$1.24), FETUSDT (STOP, -$1.47), WLFIUSDT (STOP, -$1.47). 2 new seats opened — GOOGLBUSDT, SPCXBUSDT (both 11-14 05:52). Seats now **3/10** (TVKUSDT, GOOGLBUSDT, SPCXBUSDT open). Equity $492.06 → $490.43.
- **crypto, meanrev, sentiment**: no trades, no position changes. Values flat vs yesterday.
- `announcement_watch` and `unlock_watch` data refreshed normally this cycle (listings/unlocks current as of 05:03 UTC).
- GitHub Actions `paper-trade-cycle`: runs #1029–#1030 `success`; run #1031 `in_progress` since 03:21 UTC, still producing cycle commits through 05:04 — normal for the multi-hour loop. No failed or skipped cycles found in the last 24h.

## Needs a look
- **Watcher's Grok risk scan still stale**: `data/sentinel_verdict.json` and `social_radar` both unchanged since 2026-10-20T16:09 UTC — now ~613h (~25.5 days) old. `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN — risk gate still running blind. Unresolved, growing.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~64 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $490.43 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-11 — likely just no fresh exits to audit yet, but flagging since it hasn't moved in two months.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path) is out of scope for this digest per CLAUDE.md.
