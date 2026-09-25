# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-25T13:51:37+00:00 · runs 1756 · equity **$925.81** (-7.42%) · cash $0.00 · open 10/10 · round trips 616

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-69.92 · worst day $-50.94 · trades/day 29.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 518 | 53% | -0.04% | 50% | 43% | 8% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-25T13:49 | STRKUSDT | surge | STOP | 1.2 | -3.25% | $-3.16 |
| 2026-09-25T13:49 | INTCBUSDT | surge | STOP | 10.8 | -3.25% | $-3.01 |
| 2026-09-25T13:32 | MOVRUSDT | surge | TARGET | 1.0 | +2.75% | $+2.67 |
| 2026-09-25T13:32 | VTHOUSDT | surge | TARGET | 4.5 | +2.75% | $+2.52 |
| 2026-09-25T12:22 | XLMUSDT | surge | TARGET | 10.5 | +2.75% | $+2.60 |
| 2026-09-25T12:22 | CAKEUSDT | surge | TARGET | 20.2 | +2.75% | $+2.60 |
| 2026-09-25T10:21 | AXSUSDT | surge | STOP | 3.5 | -3.25% | $-2.93 |
| 2026-09-25T08:52 | MORPHOUSDT | surge | TARGET | 17.5 | +2.75% | $+2.45 |
| 2026-09-25T08:20 | LINKUSDT | surge | TARGET | 11.8 | +2.75% | $+2.68 |
| 2026-09-25T06:41 | SYNUSDT | surge | STOP | 1.0 | -3.25% | $-2.80 |
| 2026-09-25T06:41 | AXSUSDT | surge | TARGET | 4.8 | +2.75% | $+2.60 |
| 2026-09-25T05:19 | ENAUSDT | surge | STOP | 3.0 | -3.25% | $-2.90 |
| 2026-09-25T02:47 | COMPUSDT | surge | STOP | 11.8 | -3.25% | $-3.11 |
| 2026-09-25T02:01 | GIGGLEUSDT | surge | STOP | 12.2 | -3.25% | $-3.00 |
| 2026-09-25T01:44 | MANTRAUSDT | surge | STOP | 0.2 | -3.25% | $-3.28 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-24T15:34 | ENSUSDT | surge | 7.13 | 7.07 | -0.84% |
| 2026-09-24T20:01 | AMDBUSDT | surge | 629.27 | 633.5 | +0.67% |
| 2026-09-25T06:41 | BANKUSDT | surge | 0.0353 | 0.0346 | -1.98% |
| 2026-09-25T08:20 | ALICEUSDT | surge | 0.1563 | 0.1546 | -1.09% |
| 2026-09-25T10:21 | BABYUSDT | surge | 0.01287 | 0.01304 | +1.32% |
| 2026-09-25T13:32 | VTHOUSDT | surge | 0.000782 | 0.000767 | -1.92% |
| 2026-09-25T13:32 | MOVRUSDT | surge | 1.007 | 1.004 | -0.30% |
| 2026-09-25T13:49 | REZUSDT | surge | 0.004111 | 0.004113 | +0.05% |
| 2026-09-25T13:49 | JTOUSDT | surge | 0.5348 | 0.5331 | -0.32% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
