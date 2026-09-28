# Fleet status — 2026-09-28 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No trade; BTC drifted down | $1,191.08 (was $1,203.75) |
| meanrev | HD | No trade; price feed stuck | $1,185.35 (history frozen at 09-25 close) |
| sentiment | CASH | No trade — still gated in cash | $869.30 (unchanged) |
| scalper | 10/10 seats | 46 round trips closed, net ≈ −$8 | $932.67 (was $934.32) |
| Watcher (grok_sentinel) | — (no capital) | Still silent, 0 scans since 09-11 15:12 UTC (~17 days) | n/a |
| social_radar | — (no capital) | Same staleness, unchanged since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state-file changes in 24h | — |

Lottery (257 commits/24h) and the oracle-bot side process are separate,
non-paper-fleet activity — out of scope per CLAUDE.md.

**Note:** the scheduled prompt for this digest names a "9-bot fleet (trend,
regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher)" —
that roster is stale. Per CLAUDE.md and the live state files, the active
paper fleet is 4 books (crypto, meanrev, sentiment, scalper) plus the
Watcher utility; the other 8 named/former bots are frozen archives.

## Changed
- Cron loop healthy for the full 24h: 88 cycle commits, ~16–17 min apart,
  no gap over 18.5 min. (Yesterday's 68.5h outage has not recurred.)
- crypto: no trade, still holding BTC-USD; value down ~1.1% with the market.
- scalper: 46 closes in the ~23h window (mostly ±$2.5–3 TARGET/STOP flips),
  netting about −$8; 10 new opens replaced them, seats stayed full at 10/10.
- meanrev, sentiment: no trades, both flat.

## Needs a look
- **meanrev price feed stuck**: `data/meanrev_state.json` history has no
  entry past 2026-09-25 even though `last_updated_utc` advances every
  cycle and `feed_delayed` reads `false`. Value shown ($1,185.35) may be
  3 days stale, not a fresh mark.
- **scalper/TVKUSDT dead seat**: still open since 2026-09-12 (day 16+),
  priced off a delisted pair's stale 2023 candle (~$86 of the book
  unpriced) — known issue, not yet fixed.
- **Watcher / social_radar**: silent for ~17 days (since 09-11). Sentiment
  stays in cash as a direct result.
- **`reports/supervisor_scoreboard.json` is stale**: last touched
  2026-09-26T12:30 UTC, not regenerated since — don't trust its loop-health
  numbers.
