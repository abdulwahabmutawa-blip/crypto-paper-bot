# Fleet Status — 2026-10-22 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No position change (last trade 2026-09-08) | $1,181.41 (+$1.21 vs 10-21) |
| meanrev | JNJ | No position change (last trade 2026-10-01) | $1,122.88 (as of 2026-10-21 close, −$7.49) |
| sentiment (Watcher + sentinel_trader) | CASH | Still R1-frozen, unchanged | $726.83 |
| scalper | 6/10 seats filled | 27 round trips closed (14W/13L), net −$2.23 | $666.91 (−33.31%) |
| Watcher (sentinel, no capital) | — | Social-radar + announcements scans ran, both parsed cleanly | n/a |

Checked GitHub Actions runs + cycle-commit cadence for the full 24h window: 89 cycles, avg gap ~16 min, max gap ~18 min — no missed/stuck cycles. Workflow runs in-window: all `success`/`cancelled` (normal overlap pattern, one `in_progress` long-running loop) — no failures.

## Changed
- scalper: 27 round trips closed this window (14W/13L), net −$2.23; open seats dropped 10/10 → 6/10; equity $675.71 → $666.91.
- meanrev: equity down $1,130.37 → $1,122.88 on market move only, no position change.
- crypto: equity up $1,180.20 → $1,181.41, no position change.
- sentiment: unchanged.

## Needs a look
- **scalper** equity $666.91 (−33.31%) is now further below the R1 hard-stop floor ($750, −25%) than yesterday (−32.52%). No retirement action taken (human call, not yet made). Standing caveat: scalper fills are retrospective/candle-close signal research, not proven executable fills, per CLAUDE.md.
- **sentiment** remains R1-frozen in CASH at $726.83, unchanged since 2026-10-12. Un-freezing or formal retirement still undecided.
- **meanrev** dashboard's `live_ts` is 2026-10-21T19:55 UTC (last US market close) rather than today — expected outside trading hours, not an error, but the value above isn't live right now.
- Only 4 capital books + the no-capital Watcher are live on the Actions roster (crypto, meanrev, sentiment, scalper) — congress, hunter, analyst, hypecrypto, commodity, allweather, scholar, stock, carry remain retired/frozen archives per `kill_criteria.md`; no activity from them this window.
- Lottery commits in this window (258 of them) are the separate real-money VPS path, not part of the paper fleet — not reported here.
