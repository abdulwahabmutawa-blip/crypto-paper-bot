# Fleet status — 2026-10-13 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | BTC-USD | No trade; value tracked BTC down slightly | $1,189.32 (bench $1,293.17) |
| meanrev | JNJ | No trade; new mark printed (Mon 10-12 close) | $1,150.44 (bench $1,036.38) |
| sentiment | CASH | **Hit R1 hard stop — book FROZEN by code** | $726.83 |
| scalper | 6/10 seats | 38 round trips: 12 TARGET / 24 STOP / 2 TIME, net −$36.09 | $752.50 (was $797.04) |
| Watcher (sentinel) | — | 3 scans, normal ~8h cadence, no escalation | last scan 2026-10-12 21:39 UTC |

## Changed
- **sentiment FROZEN.** The STRK-USD stop-loss from the prior window (−15.9%, sold 2026-10-12) dropped equity to $728.95 — below the $750 R1 hard-stop floor in `reports/kill_criteria.md`. `sentinel_trader.py` auto-froze the book same day (`frozen: {date: 2026-10-12, rule: "R1 kill floor"}`); cash now $726.83. Per the rules, un-freezing is a human decision — nothing further happens automatically.
- scalper: 38 round trips closed this window (12 TARGET / 24 STOP / 2 TIME), net realized −$36.09; equity $797.04 → $752.50; open seats 10/10 → 6/10. The "币安人生USDT" ghost-symbol seat flagged yesterday is gone (closed/rolled off).
- meanrev: no trade; got its first new close since Friday (Monday 10-12 printed), value $1,139.44 → $1,150.44.
- crypto: no trade, still holding BTC-USD; value drifted $1,199.50 → $1,189.32 with BTC, still trailing bench.
- `reports/supervisor_scoreboard.json` regenerated 2026-10-12 18:58 UTC — the staleness flagged in prior digests is resolved.
- Cron: 84 cycle commits in the 24h window, one ~37-min gap, otherwise steady. All GitHub Actions runs in-window completed "success" (one loop still in_progress at report time, the current cycle).

## Needs a look
- **sentiment's R1 freeze is the fleet's key open item** — book is retired per rule, awaiting an owner decision to un-freeze or formally retire (not something this routine can decide).
- scalper's TVKUSDT seat (opened 2026-09-12, now 31 days open) is still stuck, unrealized ~0% — can't hit target/stop/time-exit; worth checking if its price feed is frozen/delisted.
- This routine's own stored prompt names a 9-bot roster (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that still doesn't match the repo. Per CLAUDE.md/`kill_criteria.md` the real active fleet is crypto, meanrev, sentiment, scalper plus the non-capital Watcher; the rest are retired frozen archives, untouched this window.
