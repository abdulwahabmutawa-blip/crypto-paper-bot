# Fleet Status — 2026-11-20 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged, no trade since 11-12 sell | $1,027.21 |
| meanrev | **NVDA** | Held, no new trade; value down ~3.2% day/day (post-earnings move) | $919.47 (as-of 11-19 close, live_ts 20:55 UTC) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 5/10 seats | 35 round trips closed (12 win/23 loss, net -$18.11) | $469.86 (vs $489.82 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **scalper**: 35 round trips closed in the last 24h — 12 wins, 23 losses, net -$18.11. Equity $489.82 → $469.86. Seats dropped from 10/10 full to 5/10: TVKUSDT (stuck seat) plus 4 fresh entries (RWUSDUSDT, AAVEUSDT, STRKUSDT, NIGHTUSDT).
- **meanrev**: no new trade, still holding NVDA; value fell ~3.2% on the day, consistent with a post-earnings move (per supervisor scoreboard note).
- **crypto, sentiment**: no trades, no position changes in the last 24h.
- `reports/social_radar.md`, `smallwins.md`, data/unlocks.json: routine data refreshes, nothing abnormal.
- One supervisor log committed (2026-11-19 15:42 UTC) — normal cadence. It also first-tracked several previously-untracked archive files (`data/KILL_SWITCH`, `data/exit_audit.jsonl`, `data/sentinel_state.json`, retired-bot state files) in git — their contents are historic (Sept/Oct dated), not new activity; an artifact of the shallow clone, not a fleet event.
- GitHub Actions `paper-trade-cycle`: 50 cycle commits, covering 2026-11-19 13:42 UTC → 2026-11-20 04:57 UTC. One gap inside that span (19:17→21:54 UTC, ~2h37m) matches the documented GitHub schedule-throttling behavior (see `.github/workflows/bot.yml` comments), not a failure. No error/fail commits found.

## Needs a look
- This session's clone only holds the last 50 commits, so the covered window starts 2026-11-19 13:42 UTC — it does not reach back to where yesterday's digest left off (04:53 UTC on 11-19), leaving ~8h45m uninspected. Recurring clone-depth limit, not a reported bot failure.
- **Watcher's Grok risk scan still stale**: `sentinel_state.json.last_scan_utc` unchanged since 2026-10-20T16:09 UTC — now ~31 days old. Risk gate still running blind. Unresolved, growing.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~68.5 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $469.86 remains below the R1 hard-stop floor ($750, -25%), and dropped further this run; no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — still unmoved for over two months.
- **Scheduled-task roster mismatch (recurring)**: this digest's stored instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path) is out of scope for this digest per CLAUDE.md. `data/KILL_SWITCH` surfaced in today's commits is a 2026-09-10-dated owner decision re-tracked by the supervisor log, not new activity.
