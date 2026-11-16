# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-16T01:09:51+00:00 · runs 6103 · equity **$493.27** (-50.67%) · cash $0.00 · open 10/10 · round trips 2009

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-499.52 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1736 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 273 | 42% | -0.54% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-16T00:02 | KORUBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.29 |
| 2026-11-16T00:02 | PROMUSDT | surge | TARGET | 7.5 | +2.75% | $+1.24 |
| 2026-11-15T23:29 | TQQQBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.27 |
| 2026-11-15T23:29 | KORUBUSDT | surge | TARGET | 2.2 | +2.75% | $+1.24 |
| 2026-11-15T23:29 | NBISBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.25 |
| 2026-11-15T23:29 | SOXLBUSDT | surge | TARGET | 6.5 | +2.75% | $+1.24 |
| 2026-11-15T22:40 | LSKUSDT | surge | TARGET | 7.8 | +2.75% | $+1.24 |
| 2026-11-15T21:02 | WINUSDT | surge | STOP | 1.5 | -3.25% | $-1.48 |
| 2026-11-15T20:25 | PARTIUSDT | surge | STOP | 3.5 | -3.25% | $-1.47 |
| 2026-11-15T20:25 | KITEUSDT | surge | TARGET | 6.5 | +2.75% | $+1.24 |
| 2026-11-15T19:20 | FFUSDT | surge | STOP | 0.2 | -3.25% | $-1.50 |
| 2026-11-15T17:58 | SHELLUSDT | bottom | TARGET | 1.0 | +2.75% | $+1.24 |
| 2026-11-15T17:26 | FFUSDT | surge | TARGET | 0.8 | +2.75% | $+1.24 |
| 2026-11-15T16:20 | PROMUSDT | surge | TARGET | 0.0 | +2.75% | $+1.23 |
| 2026-11-15T16:20 | FFUSDT | surge | TARGET | 3.0 | +2.75% | $+1.24 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-15T14:58 | TRXUSDT | bottom | 0.3057 | 0.3033 | -0.79% |
| 2026-11-15T19:20 | NVDABUSDT | surge | 164.87 | 163 | -1.13% |
| 2026-11-15T20:25 | SENTUSDT | surge | 0.01694 | 0.01688 | -0.35% |
| 2026-11-15T21:02 | SAGAUSDT | surge | 0.01416 | 0.01407 | -0.64% |
| 2026-11-15T23:29 | TQQQBUSDT | surge | 58.28 | 57.47 | -1.39% |
| 2026-11-15T23:29 | SKHYBUSDT | surge | 132.44 | 129.05 | -2.56% |
| 2026-11-15T23:29 | NBISBUSDT | surge | 117.77 | 113.22 | -3.86% |
| 2026-11-16T00:02 | DRAMBUSDT | surge | 42.65 | 41.55 | -2.58% |
| 2026-11-16T00:02 | MUBUSDT | surge | 780.37 | 763.36 | -2.18% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
