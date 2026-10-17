# Fleet Status — 2026-10-17 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No position change (last trade 2026-09-08) | $1,162.17 |
| meanrev | JNJ | No position change (last trade 2026-10-01) | $1,113.55 (as of 2026-10-16 close; NYSE closed Sat) |
| sentiment (Watcher + sentinel_trader) | CASH | Still R1-frozen (see Needs a look) | $726.83 |
| scalper | 10/10 seats filled | 26 round trips, 7W/19L, net −$23.41 | $698.98 (−30.10%) |
| Watcher (sentinel, no capital) | — | 2 scans, latest 21:12 UTC, risk "caution" | n/a |

Cycle-commit cadence checked via git history + GitHub API across the full 24h window: steady ~17min spacing on `paper-trade-cycle`, no gaps found, no failed runs seen in the sampled window.

## Changed
- scalper: 26 round trips closed (7 wins / 19 losses), net −$23.41. Seats held steady at 10/10 throughout — no seat-count change.
- No other bot changed position.

## Needs a look
- **scalper** equity $698.98 (−30.10%) is below the R1 hard-stop floor ($750, `reports/kill_criteria.md`) — this has been true continuously since around 2026-10-12, not new today. It's still running every cycle; no retirement action has been taken (that's a human call, not made yet). Note the standing caveat: scalper fills are retrospective/candle-close, signal research rather than proven executable fills, per CLAUDE.md.
- **sentiment** remains R1-frozen in CASH at $726.83, unchanged since 2026-10-12. Un-freezing or formal retirement still undecided.
- Only 4 capital books + the no-capital Watcher are live on the Actions roster (crypto, meanrev, sentiment, scalper) — congress, hunter, analyst, hypecrypto, commodity, allweather, scholar, stock are retired/frozen archives per `kill_criteria.md`, not active bots.
- `reports/supervisor_scoreboard.json` is stale (last updated 2026-10-13) — not refreshed by the cycle loop, so not used for the numbers above.
