# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-25T20:55:10+00:00 · runs 4364 · equity **$635.27** (-36.47%) · cash $0.00 · open 10/10 · round trips 1578

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-365.44 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1375 | 49% | -0.26% | 47% | 46% | 7% |
| bottom | 203 | 43% | -0.48% | 37% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-25T20:01 | SOXLBUSDT | surge | TIME | 24.0 | +1.37% | $+0.86 |
| 2026-10-25T19:26 | DODOUSDT | surge | TARGET | 5.2 | +2.75% | $+1.67 |
| 2026-10-25T17:23 | DASHUSDT | surge | STOP | 3.8 | -3.25% | $-2.01 |
| 2026-10-25T17:06 | AIUSDT | bottom | TIME | 24.0 | +0.27% | $+0.17 |
| 2026-10-25T16:17 | POLYXUSDT | bottom | TARGET | 1.5 | +2.75% | $+1.65 |
| 2026-10-25T14:38 | CHIPUSDT | surge | STOP | 1.8 | -3.25% | $-1.99 |
| 2026-10-25T14:38 | STEEMUSDT | bottom | STOP | 2.2 | -3.25% | $-2.00 |
| 2026-10-25T13:32 | REUSDT | surge | STOP | 0.0 | -3.25% | $-2.01 |
| 2026-10-25T12:59 | BABYUSDT | surge | TARGET | 0.8 | +2.75% | $+1.69 |
| 2026-10-25T12:38 | LUMIAUSDT | surge | STOP | 2.8 | -3.25% | $-1.96 |
| 2026-10-25T12:22 | MEGAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.69 |
| 2026-10-25T12:05 | POLYXUSDT | bottom | TARGET | 0.0 | +2.75% | $+1.68 |
| 2026-10-25T11:49 | ANIMEUSDT | bottom | STOP | 4.0 | -3.25% | $-2.03 |
| 2026-10-25T10:43 | POLYXUSDT | surge | TARGET | 0.2 | +2.75% | $+1.70 |
| 2026-10-25T10:43 | ANKRUSDT | surge | STOP | 0.8 | -3.25% | $-1.99 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-25T01:55 | ASTERUSDT | surge | 0.712 | 0.703 | -1.26% |
| 2026-10-25T09:37 | SUIUSDT | bottom | 0.9078 | 0.9245 | +1.84% |
| 2026-10-25T15:11 | NBISBUSDT | surge | 158.74 | 160.22 | +0.93% |
| 2026-10-25T15:28 | PLUMEUSDT | surge | 0.01585 | 0.01603 | +1.14% |
| 2026-10-25T16:17 | ENAUSDT | surge | 0.2045 | 0.2061 | +0.78% |
| 2026-10-25T17:06 | ZROUSDT | surge | 1.766 | 1.773 | +0.40% |
| 2026-10-25T17:23 | AAVEUSDT | surge | 137.88 | 137.7 | -0.13% |
| 2026-10-25T19:26 | QNTUSDT | surge | 194.2 | 192.98 | -0.63% |
| 2026-10-25T20:01 | PYTHUSDT | surge | 0.0754 | 0.07403 | -1.82% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
