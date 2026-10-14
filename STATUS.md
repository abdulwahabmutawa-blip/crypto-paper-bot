# Fleet status — 2026-10-14 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; value tracked BTC up slightly | $1,194.43 (bench $1,298.73) |
| meanrev | JNJ | No trade; sharp down mark (Mon close) | $1,083.31 (bench $1,036.34) |
| sentiment | CASH | Still R1 hard-stop FROZEN (since 2026-10-12) | $726.83 |
| scalper | 10/10 seats | 30 round trips: 15 TARGET / 13 STOP / 2 TIME, net −$3.09 | $755.66 (was $752.50) |
| Watcher (sentinel) | — | ~4 scans, normal cadence, latest flagged market caution | last scan 2026-10-13 22:03 UTC |

## Changed
- **meanrev** dropped $1,150.44 → $1,083.31 (−5.8%) in one trading-day mark while still holding JNJ — no trade fired (no stop-loss on this book by design; meanrev runs without the trailing-stop overlay per `selection_engine.py` convention). Bench barely moved, so the drop is JNJ-specific, not a data glitch.
- **crypto**: no trade, still BTC-USD; value drifted $1,187.34 → $1,194.43, still trailing bench.
- **scalper**: seats filled from 6/10 → 10/10; 30 round trips closed this window (15 TARGET / 13 STOP / 2 TIME), net realized −$3.09; equity $752.50 → $755.66.
- **sentiment**: unchanged, still frozen in cash at $726.83 since the 2026-10-12 R1 breach.
- Cron: 76 cycle commits across the 24h window, every cycle touched all bot files (no partial/skipped runs). GitHub Actions: all runs in-window completed "success" (one still in_progress at report time, the current cycle); no cancelled or failed runs. The three timing gaps seen in commit spacing (max 137 min) all line up with the boundary between one multi-hour scheduled run ending and the next starting, not missed or failed cycles.

## Needs a look
- **Scalper is $5.66 above the $750 R1 hard-stop floor** — the closest any active book has been to forced retirement. Worth a check before the next down move.
- scalper's TVKUSDT seat (opened 2026-09-12, now 32 days open) is still stuck at ~0% move — can't hit target/stop/time-exit; still looks like a frozen/delisted price feed, unchanged from prior digests.
- `reports/supervisor_scoreboard.json` last regenerated 2026-10-13 08:45 UTC (~20h stale at report time) — its own run note flags a known stale-close skew in new scalper fills (9/21 outside the fill-minute window) and the sentiment fill-rewrite alert as still open; neither is new, both remain unresolved.
- This routine's own stored prompt still names a 9-bot roster (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the repo. Per CLAUDE.md/`kill_criteria.md` the real active fleet is crypto, meanrev, sentiment, scalper plus the non-capital Watcher; the rest are retired frozen archives, untouched this window.
