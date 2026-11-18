# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-18T17:12:33+00:00 · runs 6282 · equity **$481.39** (-51.86%) · cash $174.53 · open 6/10 · round trips 2077

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-517.54 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1791 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 286 | 43% | -0.48% | 37% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-18T16:38 | ZBTUSDT | surge | STOP | 1.2 | -3.25% | $-1.40 |
| 2026-11-18T16:38 | BMTUSDT | surge | STOP | 9.0 | -3.25% | $-1.39 |
| 2026-11-18T16:38 | TAOUSDT | surge | STOP | 13.2 | -3.25% | $-1.45 |
| 2026-11-18T16:38 | RENDERUSDT | surge | STOP | 14.0 | -3.25% | $-1.45 |
| 2026-11-18T16:38 | WUSDT | surge | TARGET | 16.2 | +2.75% | $+1.26 |
| 2026-11-18T16:38 | POLUSDT | surge | STOP | 21.8 | -3.25% | $-1.45 |
| 2026-11-18T16:38 | SPCXBUSDT | surge | TARGET | 21.8 | +2.75% | $+1.23 |
| 2026-11-18T12:51 | ALLOUSDT | surge | STOP | 3.2 | -3.25% | $-1.44 |
| 2026-11-18T09:23 | ENSOUSDT | surge | TARGET | 2.0 | +2.75% | $+1.19 |
| 2026-11-18T07:30 | USUALUSDT | surge | TARGET | 0.0 | +2.75% | $+1.19 |
| 2026-11-18T07:14 | PHAUSDT | bottom | STOP | 4.8 | -3.25% | $-1.45 |
| 2026-11-18T07:14 | FFUSDT | surge | STOP | 11.5 | -3.25% | $-1.45 |
| 2026-11-18T05:36 | USUALUSDT | surge | TARGET | 1.0 | +2.75% | $+1.15 |
| 2026-11-18T04:29 | ZKPUSDT | surge | STOP | 0.5 | -3.25% | $-1.40 |
| 2026-11-18T03:38 | SKYUSDT | surge | STOP | 8.8 | -3.25% | $-1.45 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-17T23:59 | AVGOBUSDT | surge | 351.62 | 349.83 | -0.51% |
| 2026-11-18T07:30 | EWYBUSDT | surge | 138.73 | 136.29 | -1.76% |
| 2026-11-18T17:11 | TLMUSDT | bottom | 0.000919 | 0.000921 | +0.22% |
| 2026-11-18T17:11 | NVDABUSDT | bottom | 151.75 | 151.68 | -0.05% |
| 2026-11-18T17:11 | ICPUSDT | bottom | 2.193 | 2.187 | -0.27% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
