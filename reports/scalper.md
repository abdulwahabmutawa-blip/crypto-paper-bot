# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-25T15:59:51+00:00 · runs 1764 · equity **$924.15** (-7.58%) · cash $0.00 · open 10/10 · round trips 620

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-74.86 · worst day $-50.94 · trades/day 29.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 522 | 53% | -0.05% | 49% | 43% | 8% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-25T15:57 | ENSUSDT | surge | TIME | 24.0 | -1.23% | $-1.16 |
| 2026-09-25T14:59 | AEROUSDT | surge | TARGET | 0.2 | +2.75% | $+2.62 |
| 2026-09-25T14:24 | MOVRUSDT | surge | STOP | 0.5 | -3.25% | $-3.15 |
| 2026-09-25T14:24 | ALICEUSDT | surge | STOP | 5.8 | -3.25% | $-3.25 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-24T20:01 | AMDBUSDT | surge | 629.27 | 627.53 | -0.28% |
| 2026-09-25T06:41 | BANKUSDT | surge | 0.0353 | 0.0346 | -1.98% |
| 2026-09-25T10:21 | BABYUSDT | surge | 0.01287 | 0.01304 | +1.32% |
| 2026-09-25T13:32 | VTHOUSDT | surge | 0.000782 | 0.000781 | -0.13% |
| 2026-09-25T13:49 | REZUSDT | surge | 0.004111 | 0.004107 | -0.10% |
| 2026-09-25T13:49 | JTOUSDT | surge | 0.5348 | 0.5354 | +0.11% |
| 2026-09-25T14:24 | NEARUSDT | surge | 5.053 | 5.11 | +1.13% |
| 2026-09-25T14:59 | SUIUSDT | surge | 1.1108 | 1.0991 | -1.05% |
| 2026-09-25T15:57 | KMNOUSDT | surge | 0.04228 | 0.04227 | -0.02% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
