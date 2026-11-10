# Fleet Status — 2026-11-10 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; price drifted down with BTC | $1,065.66 (11-09 close $1,069.89 → now $1,065.66), bench $1,158.72 |
| meanrev | CASH | **SOLD NVDA** — trailing stop (-12% from $203.98 high) | $1,000.74 (11-06 $1,061.55 → now $1,000.74), bench $1,002.46 |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen | $726.83 |
| scalper | 10/10 seats | 18 round trips closed, net +$4.00 | $505.93 (vs $506.05 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **meanrev**: first position change since 11-04 — NVDA hit its 12% trailing stop at $176.18 (high-water $203.98), sold for $1,001.85, book moved TO CASH at $1,000.74. Next entry picks the most oversold mega-cap again.
- **scalper**: 18 round trips closed in the window — 10 TARGET, 6 STOP, 2 TIME — net +$4.00, equity roughly flat ($506.05 → $505.93). New opens: DODOUSDT, RENDERUSDT, JSTUSDT, TSLABUSDT, QQQBUSDT, BEBUSDT, ZROUSDT, RWUSDUSDT, AVAXUSDT. TVKUSDT still open since 09-12, still 10/10 seats.
- **crypto**: no trade, still holding BTC-USD since 09-08 (entry $77,700.1). Book $1,069.89 → $1,065.66 as BTC eased off; bench also down.
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).
- No GitHub Actions failures found for this window (checked via Actions API, all `paper-trade-cycle` runs "success"). Two cycle gaps (~102 min around 15:05→16:47 UTC, ~121 min around 22:30→00:31 UTC) — within the documented schedule-throttling range, not errors.

## Needs a look
- **Watcher's Grok risk scan is still stale**: `data/sentinel_verdict.json` unchanged since 2026-10-20T16:09 UTC (~20.6 days / ~495h old). `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN, not calm — risk gate still running blind.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~59 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $505.93 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/carry are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path) and an unrelated "oracle" bot's commits both appear in this window's commit history but are out of scope for this digest per CLAUDE.md.
