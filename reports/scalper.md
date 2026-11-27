# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-27T03:10:07+00:00 · runs 6840 · equity **$496.04** (-50.40%) · cash $0.00 · open 10/10 · round trips 2247

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-506.81 · worst day $-50.94 · trades/day 26.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1929 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 318 | 43% | -0.46% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-27T02:34 | TRUMPUSDT | bottom | TARGET | 2.5 | +2.75% | $+1.21 |
| 2026-11-27T02:34 | TIAUSDT | bottom | TARGET | 2.5 | +2.75% | $+1.21 |
| 2026-11-27T02:34 | SKYUSDT | surge | TARGET | 11.0 | +2.75% | $+1.20 |
| 2026-11-27T01:44 | SOPHUSDT | surge | STOP | 0.5 | -3.25% | $-1.46 |
| 2026-11-27T00:54 | EWYBUSDT | surge | TIME | 24.0 | -1.35% | $-0.61 |
| 2026-11-26T23:46 | SAGAUSDT | surge | STOP | 4.5 | -3.25% | $-1.47 |
| 2026-11-26T23:46 | SUPERUSDT | surge | TIME | 24.0 | -1.10% | $-0.49 |
| 2026-11-26T19:32 | FETUSDT | surge | TARGET | 1.0 | +2.75% | $+1.26 |
| 2026-11-26T18:58 | SENTUSDT | surge | TARGET | 3.0 | +2.75% | $+1.25 |
| 2026-11-26T18:42 | SAGAUSDT | surge | TARGET | 3.2 | +2.75% | $+1.21 |
| 2026-11-26T18:25 | SEIUSDT | surge | TARGET | 0.0 | +2.75% | $+1.21 |
| 2026-11-26T18:25 | WIFUSDT | surge | TARGET | 2.0 | +2.75% | $+1.24 |
| 2026-11-26T18:08 | STXUSDT | surge | TIME | 24.0 | -0.86% | $-0.38 |
| 2026-11-26T17:51 | MANTRAUSDT | bottom | TARGET | 2.2 | +2.75% | $+1.20 |
| 2026-11-26T16:10 | ZECUSDT | bottom | TARGET | 0.5 | +2.75% | $+1.20 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-26T15:19 | TRXUSDT | bottom | 0.3026 | 0.3052 | +0.86% |
| 2026-11-26T17:51 | THETAUSDT | surge | 0.1357 | 0.136 | +0.22% |
| 2026-11-26T18:25 | WIFUSDT | surge | 0.1387 | 0.1388 | +0.07% |
| 2026-11-26T18:58 | SENTUSDT | surge | 0.02178 | 0.0218 | +0.09% |
| 2026-11-26T19:32 | DOTUSDT | surge | 0.676 | 0.691 | +2.22% |
| 2026-11-27T01:44 | SNDKBUSDT | surge | 77.37 | 78.91 | +1.99% |
| 2026-11-27T02:34 | KORUBUSDT | surge | 5.65 | 5.68 | +0.53% |
| 2026-11-27T02:34 | QQQBUSDT | surge | 647.34 | 647.72 | +0.06% |
| 2026-11-27T02:34 | TQQQBUSDT | surge | 48.01 | 48.15 | +0.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
