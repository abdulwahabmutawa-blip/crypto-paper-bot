# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-25T12:07:19+00:00 · runs 4331 · equity **$637.08** (-36.29%) · cash $61.62 · open 9/10 · round trips 1567

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-363.21 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1367 | 49% | -0.26% | 47% | 46% | 7% |
| bottom | 200 | 42% | -0.49% | 38% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-25T12:05 | POLYXUSDT | bottom | TARGET | 0.0 | +2.75% | $+1.68 |
| 2026-10-25T11:49 | ANIMEUSDT | bottom | STOP | 4.0 | -3.25% | $-2.03 |
| 2026-10-25T10:43 | POLYXUSDT | surge | TARGET | 0.2 | +2.75% | $+1.70 |
| 2026-10-25T10:43 | ANKRUSDT | surge | STOP | 0.8 | -3.25% | $-1.99 |
| 2026-10-25T10:10 | POLYXUSDT | surge | TARGET | 0.5 | +2.75% | $+1.67 |
| 2026-10-25T09:54 | ANKRUSDT | surge | TARGET | 0.2 | +2.75% | $+1.67 |
| 2026-10-25T09:54 | DODOUSDT | surge | STOP | 0.8 | -3.25% | $-2.03 |
| 2026-10-25T09:37 | STRKUSDT | bottom | STOP | 10.0 | -3.25% | $-2.02 |
| 2026-10-25T09:21 | ORCAUSDT | surge | STOP | 11.2 | -3.25% | $-2.05 |
| 2026-10-25T09:04 | NILUSDT | surge | STOP | 7.8 | -3.25% | $-1.96 |
| 2026-10-25T08:48 | POLYXUSDT | surge | TARGET | 0.0 | +2.75% | $+1.70 |
| 2026-10-25T08:48 | CVXUSDT | surge | STOP | 10.5 | -3.25% | $-2.05 |
| 2026-10-25T08:31 | POLYXUSDT | surge | TARGET | 1.2 | +2.75% | $+1.66 |
| 2026-10-25T07:42 | ZBTUSDT | bottom | STOP | 2.2 | -3.25% | $-2.09 |
| 2026-10-25T06:29 | CHIPUSDT | surge | STOP | 6.2 | -3.25% | $-2.02 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-24T16:50 | AIUSDT | bottom | 0.0193 | 0.0195 | +1.04% |
| 2026-10-24T19:52 | SOXLBUSDT | surge | 84.51 | 84.22 | -0.34% |
| 2026-10-25T01:55 | ASTERUSDT | surge | 0.712 | 0.7072 | -0.67% |
| 2026-10-25T09:37 | LUMIAUSDT | surge | 0.0798 | 0.0789 | -1.13% |
| 2026-10-25T09:37 | SUIUSDT | bottom | 0.9078 | 0.9201 | +1.35% |
| 2026-10-25T12:05 | BABYUSDT | surge | 0.01401 | 0.01394 | -0.50% |
| 2026-10-25T12:05 | MEGAUSDT | surge | 0.04689 | 0.04733 | +0.94% |
| 2026-10-25T12:05 | STEEMUSDT | bottom | 0.04973 | 0.0496 | -0.26% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
