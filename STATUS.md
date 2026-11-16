# Fleet Status — 2026-11-16 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged, no new trade since 11-12 sell | $1,027.21 |
| meanrev | CASH | Unchanged, still CASH since 11-09 stop-out | $1,000.74 |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 10/10 seats (full) | 25 round trips closed (15 win/10 loss, net +$3.73); seats filled 3→10 | $493.13 (vs $490.43 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **scalper**: 25 round trips closed in the last 24h — 15 wins (+$17.60), 10 losses (-$13.87), net +$3.73. Equity $490.43 → $493.13. Seats went from 3/10 to **10/10 (full)**: GOOGLBUSDT and SPCXBUSDT (open yesterday) closed; 9 new entries opened — TRXUSDT, NVDABUSDT, SENTUSDT, SAGAUSDT, PROMUSDT, ZROUSDT, MSTRBUSDT, BMNRBUSDT, NIGHTUSDT. TVKUSDT (the stuck seat) still open.
- **crypto, meanrev, sentiment**: no trades, no position changes. Values flat vs yesterday.
- `announcements.json` (listings/delistings) refreshed normally this cycle (current as of 04:56 UTC).
- GitHub Actions `paper-trade-cycle`: run #1034 `success`; run #1035 `in_progress` since 23:55 UTC yesterday, still producing cycle commits through 04:58 UTC today — normal for the multi-hour loop. No failed or skipped cycles found in the last 24h.

## Needs a look
- **Watcher's Grok risk scan still stale**: `data/sentinel_verdict.json` and `social_radar` card inputs both unchanged since 2026-10-20T16:09 UTC — now ~637h (~26.5 days) old. `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN — risk gate still running blind. Unresolved, growing.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~64 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $493.13 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-11 — likely just no fresh exits to audit yet, but flagging since it hasn't moved in over two months.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path) is out of scope for this digest per CLAUDE.md.
