# Fleet Status — 2026-11-12 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No new trade; still holding the 11-10 re-entry | $1,043.41, bench $1,143.70 |
| meanrev | CASH | Unchanged, still CASH since 11-09 stop-out | $1,000.74, bench $1,012.03 (11-11) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83, bench $1,012.11 |
| scalper | 10/10 seats | 25 round trips closed, net +$0.30 | $501.71 (vs $507.37 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **scalper**: 25 round trips closed in the window — 13 TARGET, 11 STOP, 1 TIME — net +$0.30. Equity $507.37 → $501.71 (down despite near-flat closed PnL, so open-seat marks dragged it). New opens include EWYBUSDT, BNCBUSDT, QQQBUSDT, WLFIUSDT, AMDBUSDT, SPCXBUSDT, TAOUSDT, GOOGLBUSDT, AVGOBUSDT. TVKUSDT still open since 09-12, 10/10 seats.
- **crypto**: no new trade since the 11-10 round-trip (SELL "Signal flip" → brief TO CASH → re-BUY BTC-USD at $73,205.30). Value drifted $1,047.09 (11-11) → $1,043.41; bench $1,147.73 → $1,143.70.
- **meanrev**: no new trade since the 11-09 trailing-stop exit on NVDA; still CASH at $1,000.74.
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).
- GitHub Actions: checked via Actions API — runs #1016–#1019 all `success`; current run #1020 is `in_progress` (started 03:46 UTC), normal for a multi-hour run. No failed or skipped cycles found.

## Needs a look
- **Watcher's Grok risk scan is still stale**: `data/sentinel_verdict.json` unchanged since 2026-10-20T16:09 UTC (~22.5 days / ~538h old). `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN, not calm — risk gate still running blind. Getting longer each digest, unresolved.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~61 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $501.71 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path, 37 commits this window) made up most of this window's commit volume but is out of scope for this digest per CLAUDE.md.
