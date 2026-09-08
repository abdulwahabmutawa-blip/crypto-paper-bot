# Fleet status — 2026-09-08 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | ADA-USD | No new trade — marks only | $1,120.01 |
| meanrev | HD | No new trade — marks only (mkt closed Labor Day 09-07; today's session not open yet) | $1,298.52 (09-04 mark) |
| sentiment | ZEC-USD | Sold RAY-USD, bought ZEC-USD (both 09-07, hype rotation) | $1,160.42 |
| scalper | 10 open seats | 32 round trips closed (17W/15L), net +$5.36 | $1,005.61 |
| smallwins (lab) | 485 open seats | 317 runs, 10,175 resolved trades; **3 tactics hit PASS for the first time** | n/a — paper study, no $ book |
| lottery — REAL MONEY | DOTUSDT | Entered DOTUSDT 09-07 15:03 UTC (after two 09-06 stop-outs); still holding, -1.0% unrealized | $35.21 (HWM $44.27) |
| hype-ibkr — REAL MONEY ($300 live) | CASH (flat) | Never connected; stopped logging entirely after 20:01 UTC 09-07 | n/a — no position ever taken |
| Watcher | — (no capital) | New scan 09-08 01:00 UTC — caution, 4 risk alerts | n/a |
| retired (8, frozen) | commodity, allweather, scholar, congress, hunter, analyst, hypecrypto, stock | No change | — |

## Changed
- **sentiment**: sold RAY-USD (hype faded) and bought ZEC-USD, both on 09-07 — a same-day rotation.
- **scalper**: 32 round trips in 24h (17W/15L), net +$5.36, equity $1,005.61.
- **smallwins lab**: 317 runs / 10,175 resolved (up from 216 / 7,110 yesterday) — **3 tactics now show
  PASS** (`range_bottom|t3|s4|h48`, `momentum|t5|s3|h48`, `momentum|t3|s4|h48`), the first passes ever
  recorded; confirmed by diffing against yesterday's file, which had zero.
- **lottery (real money)**: entered DOTUSDT 09-07 15:03 UTC after Saturday's two stop-outs; no new
  stop-out today, currently down ~1% on the position.
- **Watcher**: fresh scan 09-08 01:00 UTC (prior one was 09-07 00:41 UTC) — risk level caution, 4 alerts
  (Treasury yield stress, Bombardier/Canada trade tension, a $320M Liquid Network BTC withdrawal, and
  low holiday-week liquidity + jobs data).
- No skipped or failed cycles for the main fleet or lottery cron: full history checked (not just the
  shallow clone), no gap over 20 min anywhere in the 24h window; GitHub Actions shows only the usual
  auto-cancelled overlapping runs, no failures.

## Needs a look
- **hype-ibkr (real $300 book, not part of the documented 9-bot roster)**: every single logged event
  since it was created on 09-05 (106/106) is a connection error to its IB Gateway on port 4001 — it has
  never successfully connected or taken a position. It stopped even attempting/logging at 20:01 UTC on
  09-07 and has been silent for 12+ hours while every other bot kept running normally. Per
  `IBKR_SETUP.md` this is meant to go live with real money; as configured it isn't trading at all.
- **lottery is real money, no hard cap** — $35.21 vs its $44.27 high-water mark; post-mortem floor
  (62.5% of peak = $27.67) not breached, but worth watching given last week's stop-outs.
- **smallwins lab**: the 3 new PASS tactics are one run's result, not yet a trend — needs another day
  or two before treating them as durable.
- CLAUDE.md's roster (trend/regime/congress/commodity/allweather/hype/Hunter) remains out of date —
  actual active books are crypto, meanrev, sentiment, scalper, lottery (real $), hype-ibkr (real $,
  currently non-functional), plus the smallwins lab.
