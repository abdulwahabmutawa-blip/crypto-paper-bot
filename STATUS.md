# Fleet Status — 2026-11-03 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No position change | $1,096.85 (vs 11-02 $1,117.86), bench $1,192.63 |
| meanrev | AMZN | Unchanged (held AMZN since 10-30; 2 new daily bars posted) | $1,060.98 |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen | $726.83 |
| scalper | 8/10 seats | 27 exits; 2 seats freed | $558.94 (vs 11-02 $586.46) |
| Watcher (sentinel, no capital) | — | Grok hype scan still not refreshing | n/a |

## Changed
- **scalper**: 27 exits in the window — 6 TARGET (+2.75% each), 19 STOP (−3.25% each), 2 TIME (24h close, neither level hit); net trading P&L −$24.72. Seats 10/10 → 8/10 (two closed, not yet refilled). Round trips 1747 → 1774. Equity $586.46 → $558.94 (−4.7%).
- **crypto**: $1,117.86 → $1,096.85 (−1.9%), no position change (holding BTC-USD since 09-08, price move only).
- **meanrev**: no new trades; $1,037.71 → $1,060.98 (+2.2%, holding AMZN since 10-30). The 10-31 and 11-02 daily bars both landed this window (state's data_asof moved from 10-30 to 11-02) — price move only, not new fills.
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).

## Needs a look
- **Watcher's Grok hype scan is still stuck**: last successful scan 2026-10-20T16:09 UTC (now 14 days stale), unchanged from prior reports — fleet risk gate continues running on stale/unknown data.
- **scalper** equity $558.94 remains below the R1 hard-stop floor ($750, −25%) and dropped further this window; still no retirement action taken (known open item, human call, not new this run).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- Cycle loop ran clean this window: Actions runs #982 and #983 completed `success`; #984 is still `in_progress` (started 23:50 UTC, normal — the ~5h45m loop job). No cancelled or failed runs in this 24h window; spot-checked job logs for #982/#983 show zero `::warning::`/`::error::` lines, and no "RED FLAG" commits anywhere in repo history this window.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again described a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per `CLAUDE.md`/`reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives; `bot_carry.py` (funding-carry paper book) runs outside the Actions workflow roster entirely. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher. This report covers the real current roster; the stale scheduled-task prompt likely needs updating at the source.
