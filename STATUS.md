# Fleet Status — 2026-11-11 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | Round-tripped: SOLD (signal flip) → brief CASH → re-BOUGHT same day | $1,043.03 (11-10 $1,043.85 → now), bench $1,143.28 |
| meanrev | CASH | Unchanged, still CASH since 11-09 stop-out | $1,000.74, bench $998.91 (11-10) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen | $726.83 |
| scalper | 10/10 seats | 19 round trips closed, net -$5.28 | $507.37 (vs $505.93 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **crypto**: round-tripped BTC-USD on 11-10 — SELL "Signal flip" at $72,982.70, briefly TO CASH ($1,039.16), then re-BUY same day at $73,205.30 ("Strongest eligible coin, -5.3% 7d momentum"). Now holding BTC-USD from this new 11-10 entry, not the old 09-08/$77,700.10 position reported yesterday. Value drifted $1,043.85 → $1,043.03; bench $1,144.18 → $1,143.28.
- **scalper**: 19 round trips closed in the window — 6 TARGET, 7 STOP, 6 TIME — net -$5.28. Equity $505.93 → $507.37 (up, so open-seat marks offset the closed-trade loss). New opens include OPGUSDT, GOOGLBUSDT, BCHUSDT, OPENUSDT, ICPUSDT, AVGOBUSDT, RENDERUSDT, SKHYBUSDT, DRAMBUSDT. TVKUSDT still open since 09-12, 10/10 seats.
- **meanrev**: no new trade since the 11-09 trailing-stop exit; still CASH at $1,000.74.
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).
- GitHub Actions: checked via Actions API — every `paper-trade-cycle` run touching this window shows `success`; the current run (#1016) is still `in_progress` (started 01:29 UTC), which is normal — one run spans several hours and makes many internal cycle/lottery commits. No failed or skipped runs found.

## Needs a look
- **Watcher's Grok risk scan is still stale**: `data/sentinel_verdict.json` unchanged since 2026-10-20T16:09 UTC (~21.5 days / ~517h old). `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN, not calm — risk gate still running blind. Getting longer each digest, unresolved.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~60 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $507.37 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/carry/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path) made up most of this window's commit volume but is out of scope for this digest per CLAUDE.md.
