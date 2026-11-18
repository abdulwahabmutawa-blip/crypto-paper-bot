# Fleet Status — 2026-11-18 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged, no new trade since 11-12 sell | $1,027.21 |
| meanrev | **NVDA** | Held since 11-16 entry; no new trade | $979.02 (vs $983.46 11-16) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 10/10 seats (full) | 26 round trips closed (9 win/17 loss, net -$12.05) | $484.63 (vs $500.88 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **meanrev**: no new trade — still holding **NVDA** (6.2978 units) from the 11-16 entry. Marked value $983.46 → $979.02 (NVDA's own move, as-of 11-17 close, live_ts 2026-11-17T20:55 UTC).
- **scalper**: 26 round trips closed in the covered window — 9 wins, 17 losses, net -$12.05. Equity $500.88 → $484.63. Seats remain 10/10 (full); TVKUSDT (the stuck seat) still open.
- **crypto, sentiment**: no trades, no position changes. Values flat vs yesterday.
- GitHub Actions `paper-trade-cycle`: 50 cycle commits, covering 2026-11-17 11:44 UTC → 2026-11-18 05:06 UTC. One multi-hour gap inside that span (13:50→17:47 UTC, ~3h56m) matches the documented GitHub schedule-throttling behavior (see `.github/workflows/bot.yml` comments), not a failure. No error/fail commits found in that window.

## Needs a look
- This session's clone only holds the last 50 commits, so the covered window starts 2026-11-17 11:44 UTC — it does not reach back to where yesterday's digest left off (04:54 UTC on 11-17), leaving ~6h50m uninspected. Recurring clone-depth limit, not a reported bot failure.
- **Watcher's Grok risk scan still stale**: `sentinel_state.json.last_scan_utc` unchanged since 2026-10-20T16:09 UTC — now ~685h (~28.5 days) old. `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN — risk gate still running blind. Unresolved, growing.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~67 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $484.63 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — still unmoved for over two months.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path) is out of scope for this digest per CLAUDE.md.
