# Fleet Status — 2026-10-25 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No position change | $1,153.26 (≈flat vs 10-24 $1,153.20) |
| meanrev | GOOGL | No position change | $1,131.47 (dashboard still dated 10-23 — stale over weekend, expected) |
| sentiment (Watcher + sentinel_trader) | CASH | Still R1-frozen, unchanged | $726.83 |
| scalper | 10/10 seats filled | Seats 9/10 → 10/10 (8 new entries since 10-24 16:50 UTC); equity down | $644.09 (was $653.46) |
| Watcher (sentinel, no capital) | — | Grok hype scan still not refreshing | n/a |

## Changed
- **scalper**: open seats 9/10 → 10/10 (AIUSDT, SOXLBUSDT, ORCAUSDT, CVXUSDT, STRKUSDT, CHIPUSDT, NILUSDT, ASTERUSDT, ZBTUSDT entries); equity $653.46 → $644.09.
- **crypto**: equity $1,153.20 → $1,153.26, no position change (BTC price move only, still holding BTC-USD).
- **meanrev**: unchanged at $1,131.47; underlying data is Friday's close, not refreshed over the weekend.
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).

## Needs a look
- **Fleet cycle loop ran cleanly all 24h** — 88 `cycle:` commits from 10-24 05:10 UTC to 10-25 05:08 UTC, max gap ~19 min (median ~17 min). No tracebacks/ERROR/CRITICAL strings found in any of today's commit diffs.
- **Watcher's Grok hype scan has stopped producing new scans and the gap is widening**: last successful scan is still 2026-10-20T16:09 UTC. The sentinel board itself now says "WATCHER OFFLINE 109h — scans are failing (key/credits/API)", so the likely cause (API key/credits) is named in the data itself, not something to re-derive. Fleet risk gate is running on UNKNOWN as a result. Trading is already suspended (R1-frozen since 10-12) so no live exposure, but the feed outage itself is unresolved.
- **scalper** equity $644.09 (≈−36%) remains below the R1 hard-stop floor ($750); no retirement action taken (known open item, human call, not new this run).
- **sentiment** remains R1-frozen in CASH at $726.83, unchanged since 2026-10-12; un-freeze or formal retirement still undecided.
- Only 4 capital books + the no-capital Watcher are live on the Actions roster (crypto, meanrev, sentiment, scalper); congress, hunter, commodity, allweather, scholar, stock, carry remain retired/frozen archives per `reports/kill_criteria.md` — no activity from them in the last 24h (the only `carry_state.json` writes seen came from separate `lottery:` commits, not the paper fleet).
