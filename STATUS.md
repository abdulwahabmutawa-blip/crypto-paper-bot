# Fleet Status — 2026-10-21 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No position change (last trade 2026-09-08) | $1,180.20 (−$3.71 vs 10-20) |
| meanrev | JNJ | No position change (last trade 2026-10-01) | $1,130.37 (as of 2026-10-20 close) |
| sentiment (Watcher + sentinel_trader) | CASH | Still R1-frozen, unchanged | $726.83 |
| scalper | 10/10 seats filled | 25 round trips closed (14W/11L), net +$3.94 | $674.76 (−32.52%) |
| Watcher (sentinel, no capital) | — | 2 scans, both parsed cleanly | n/a |

Checked GitHub Actions runs + cycle-commit cadence for the full 24h window: 90 cycles, avg gap ~16 min, max gap ~18 min — no missed/stuck cycles. One scheduled run is `in_progress` (started 22:31 UTC, long-running loop) with the next one queued `pending` behind it — the normal overlap/cancel pattern, no failures seen.

## Changed
- scalper: 25 round trips closed this window (14W/11L), net +$3.94; equity up $669.51 → $674.76.
- No other bot changed position (crypto, meanrev, sentiment holdings unchanged).

## Needs a look
- **scalper** equity $674.76 (−32.52%) remains below the R1 hard-stop floor ($750), though it ticked up from yesterday's −33.05%. No retirement action taken (human call, not yet made). Standing caveat: scalper fills are retrospective/candle-close signal research, not proven executable fills, per CLAUDE.md.
- **sentiment** remains R1-frozen in CASH at $726.83, unchanged since 2026-10-12. Un-freezing or formal retirement still undecided.
- Only 4 capital books + the no-capital Watcher are live on the Actions roster (crypto, meanrev, sentiment, scalper) — congress, hunter, analyst, hypecrypto, commodity, allweather, scholar, stock remain retired/frozen archives per `kill_criteria.md`. The `carry` book and `oracle` forecasting project also posted updates this window (1 oracle commit) but are separate from this four-bot roster and not detailed here.
- Lottery commits in this window (256 of them) are the separate real-money VPS path, not part of the paper fleet — not reported here.
