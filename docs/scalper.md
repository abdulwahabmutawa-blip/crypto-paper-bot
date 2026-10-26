# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-26T00:45:00+00:00 · runs 4378 · equity **$632.27** (-36.77%) · cash $0.00 · open 10/10 · round trips 1581

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-364.14 · worst day $-50.94 · trades/day 30.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1378 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 203 | 43% | -0.48% | 37% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-26T00:08 | QNTUSDT | surge | STOP | 4.5 | -3.25% | $-2.03 |
| 2026-10-25T22:54 | PLUMEUSDT | surge | TARGET | 7.2 | +2.75% | $+1.65 |
| 2026-10-25T22:19 | ENAUSDT | surge | TARGET | 5.8 | +2.75% | $+1.69 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-25T01:55 | ASTERUSDT | surge | 0.712 | 0.7018 | -1.43% |
| 2026-10-25T09:37 | SUIUSDT | bottom | 0.9078 | 0.9214 | +1.50% |
| 2026-10-25T15:11 | NBISBUSDT | surge | 158.74 | 157.92 | -0.52% |
| 2026-10-25T17:06 | ZROUSDT | surge | 1.766 | 1.758 | -0.45% |
| 2026-10-25T17:23 | AAVEUSDT | surge | 137.88 | 136.07 | -1.31% |
| 2026-10-25T20:01 | PYTHUSDT | surge | 0.0754 | 0.07532 | -0.11% |
| 2026-10-25T22:19 | OSMOUSDT | surge | 0.051 | 0.0504 | -1.18% |
| 2026-10-25T22:54 | MUBARAKUSDT | surge | 0.05276 | 0.05269 | -0.13% |
| 2026-10-26T00:08 | HOLOUSDT | surge | 0.0606 | 0.0592 | -2.31% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
