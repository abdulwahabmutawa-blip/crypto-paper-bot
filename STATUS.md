# Fleet status — 2026-09-06 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | ADA-USD | No new trade — marks only | $1,148.49 |
| meanrev | HD | No new trade — marks only (US mkt closed, weekend) | $1,298.52 |
| sentiment | CASH | No new trade — marks only | $1,323.05 |
| scalper | 10 open seats | 15 round trips closed (12W/3L), net +$23.37 | $1,024.79 |
| smallwins (lab) | 540 open seats | 2,909 of 3,387 resolved fell in this window | n/a — paper study, no $ book |
| lottery — REAL MONEY | BNBUSDT | Stopped ASTERUSDT -3.1%, re-entered BNBUSDT | $37.76 |
| Watcher | — (no capital) | Last scan 09-05 22:14 UTC — caution, 3 risk alerts | n/a |
| retired (8, frozen) | commodity, allweather, scholar, congress, hunter, analyst, hypecrypto, stock | No change | — |

## Changed
- **Roster reshuffle (09-05, owner decision):** commodity, allweather, scholar retired to
  frozen archive; scalper (10-seat small-wins bot) added; crypto reinstated hours later as
  v4 BTC tide gauge. Active paper books now: crypto, meanrev, sentiment, scalper (+ smallwins lab).
- **sentiment** restated $2,453.00 → $1,323.05 after a fill-audit found 5 stale/mismatched
  price fills and 4 bad ARB legs; no new trade since.
- **scalper**: first full day live — 10 seats, 15 closed round trips (12W/3L), net +$23.37,
  equity $1,024.79.
- **lottery (real money)**: stopped out of ASTERUSDT at -3.1% (-$1.24, 13:47 UTC); re-entered
  BNBUSDT at 13:49 UTC, currently -0.15%. No circuit-breaker or tape-gate halt active.
- No skipped or failed cycles: paper-fleet ran every ~15-16 min, lottery every ~5-8 min — no
  gap over 20 min anywhere in the window.

## Needs a look
- **lottery is real money, no cap** — currently $37.76 vs its $44.27 high-water mark
  (post-mortem floor triggers at 62.5% of peak = $27.67, not yet breached).
- **smallwins lab**: no tactic has hit "pass" yet in reports/smallwins.md (needs ≥60 trades,
  hit ≥ break-even+5pts, mean>0, worst day > -3 units) — all still "watch" or "fail".
- CLAUDE.md's roster list predates the 09-05 crypto reinstatement — doc, not data, out of sync.
