# Fleet Status — 2026-11-13 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | SOLD BTC-USD (signal flip), now CASH | $1,027.21, bench $1,066.04 |
| meanrev | CASH | Unchanged, still CASH since 11-09 stop-out | $1,000.74, bench $1,008.58 (11-12) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83, bench $1,008.53 (asof 11-12) |
| scalper | 2/10 seats | 11 round trips closed, net -$10.47 | $491.82 (vs $501.71 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **crypto**: SOLD BTC-USD at $72,727.00 (2026-11-12, "Signal flip") → TO CASH. First position change since the 11-10 re-entry. Value $1,043.41 (11-12) → $1,027.21; bench $1,143.70 → $1,066.04.
- **scalper**: 11 round trips closed in the window — 1 TARGET, 8 STOP, 2 TIME — net -$10.47. Equity $501.71 → $491.82. Open seats dropped from 10/10 to **2/10**: TVKUSDT (stuck since 09-12) and TRXUSDT (opened 11-12 13:38). 8 seats sitting unfilled — not just a quiet period, a real drop from full occupancy.
- **meanrev**: no new trade since the 11-09 trailing-stop exit on NVDA; still CASH at $1,000.74.
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).
- GitHub Actions: run #1023 `in_progress` (started 2026-11-13 00:59 UTC, still producing cycle commits through 04:58 — normal for a multi-hour run). Runs #1016–#1022 all `success`. No failed or skipped cycles found.

## Needs a look
- **scalper seat occupancy dropped to 2/10** (was 10/10 yesterday) — 8 seats empty/unfilled this window. Not confirmed whether this is the scanner finding fewer setups or something not opening new positions; worth a look if it doesn't refill next digest.
- **Watcher's Grok risk scan is still stale**: `data/sentinel_verdict.json` unchanged since 2026-10-20T16:09 UTC (~23.5 days old). `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN — risk gate still running blind. Getting longer each digest, unresolved.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~62 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $491.82 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path) is out of scope for this digest per CLAUDE.md.
