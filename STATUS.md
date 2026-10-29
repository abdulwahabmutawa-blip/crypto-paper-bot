# Fleet Status — 2026-10-29 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No position change | $1,142.95 (vs 10-28 $1,136.70) |
| meanrev | GOOGL | No position change | $1,150.41 (vs 10-28 $1,119.60) |
| sentiment (Watcher + sentinel_trader) | CASH | Still R1-frozen, unchanged | $726.83 |
| scalper | 9/10 seats | Seats 10→9; equity down | $602.74 (was $611.65 24h ago) |
| Watcher (sentinel, no capital) | — | Grok hype scan still not refreshing | n/a |

## Changed
- **scalper**: equity $611.65 → $602.74 (−1.5%); exits in the window mostly STOP (SOXLBUSDT, SNDKBUSDT, ETHFIUSDT, INJUSDT, PUMPUSDT, RAYUSDT, TIAUSDT, DRAMBUSDT, AXTIBUSDT, SKHYBUSDT each ≈−3.25%), one TIME exit (EWYBUSDT −1.65%), and 3 TARGET hits (AXTIBUSDT, BLURUSDT, TIAUSDT, MUBUSDT each ≈+2.75%); seats 10 → 9; lifetime 1,661 round trips, 48% hit rate (break-even 54%).
- **crypto**: $1,136.70 → $1,142.95 (+0.5%), no position change (holding BTC-USD since 09-08, price move only).
- **meanrev**: $1,119.60 → $1,150.41 (+2.8%), no position change (holding GOOGL since 10-22, price move only).
- **sentiment**: unchanged at $726.83 (R1-frozen since 10-12).

## Needs a look
- **Fleet cycle loop ran cleanly**: 89 `cycle:` commits in the 24h window (10-28 05:21 → 10-29 04:56 UTC), steady ~17 min cadence throughout, no gap flagged as a failure. All GitHub Actions `paper-trade-cycle` runs in the window show `success` or `cancelled` (normal queue supersession); none show `failure`. (Note: the local shallow clone initially truncated this history to 50 commits — re-fetched to confirm the full 24h window before concluding this.)
- **Watcher's Grok hype scan is still stuck**: last successful scan 2026-10-20T16:09 UTC (~9 days ago) — unchanged from prior reports, still unresolved; fleet risk gate continues running on UNKNOWN.
- **scalper** equity $602.74 remains well below the R1 hard-stop floor ($750, −25%); no retirement action taken (known open item, human call, not new this run).
- **meanrev**'s dashboard `live_ts` (10-28 19:55 UTC) trails its `generated_utc` (10-29 04:52 UTC) by ~9h — plausibly a market-hours-gated refresh, not confirmed as a fault; flagging since it's a change from crypto/sentiment, which refresh same-cycle.
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- Only 4 capital books + the no-capital Watcher are live on the Actions roster (crypto, meanrev, sentiment, scalper); congress, hunter, commodity, allweather, scholar, stock, carry, hypecrypto, analyst remain retired/frozen archives per `reports/kill_criteria.md` — no activity from them in the last 24h. (`lottery:`-prefixed commits are the separate real-money VPS book; `oracle:`-prefixed commits are an unrelated process — both excluded from this paper-fleet report per project convention.)
