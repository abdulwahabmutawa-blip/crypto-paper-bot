# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-25T15:13:05+00:00 · runs 4343 · equity **$633.57** (-36.64%) · cash $59.86 · open 9/10 · round trips 1573

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-367.78 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1372 | 49% | -0.26% | 47% | 47% | 7% |
| bottom | 201 | 42% | -0.50% | 37% | 45% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-25T10:10 | POLYXUSDT | surge | TARGET | 0.5 | +2.75% | $+1.67 |
| 2026-10-25T09:54 | ANKRUSDT | surge | TARGET | 0.2 | +2.75% | $+1.67 |
| 2026-10-25T09:54 | DODOUSDT | surge | STOP | 0.8 | -3.25% | $-2.03 |
| 2026-10-25T09:37 | STRKUSDT | bottom | STOP | 10.0 | -3.25% | $-2.02 |
| 2026-10-25T09:21 | ORCAUSDT | surge | STOP | 11.2 | -3.25% | $-2.05 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-24T16:50 | AIUSDT | bottom | 0.0193 | 0.0194 | +0.52% |
| 2026-10-24T19:52 | SOXLBUSDT | surge | 84.51 | 85.25 | +0.88% |
| 2026-10-25T01:55 | ASTERUSDT | surge | 0.712 | 0.7071 | -0.69% |
| 2026-10-25T09:37 | SUIUSDT | bottom | 0.9078 | 0.9174 | +1.06% |
| 2026-10-25T13:16 | DASHUSDT | surge | 53.63 | 53.08 | -1.03% |
| 2026-10-25T13:49 | DODOUSDT | surge | 0.02286 | 0.02276 | -0.44% |
| 2026-10-25T14:38 | POLYXUSDT | bottom | 0.0331 | 0.0337 | +1.81% |
| 2026-10-25T15:11 | NBISBUSDT | surge | 158.74 | 158.89 | +0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
