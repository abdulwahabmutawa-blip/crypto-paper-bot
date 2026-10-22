# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-22T12:01:14+00:00 · runs 4070 · equity **$663.08** (-33.69%) · cash $257.59 · open 6/10 · round trips 1475

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-333.99 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1291 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 184 | 45% | -0.36% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-22T10:49 | ARKMUSDT | surge | STOP | 0.5 | -3.25% | $-2.11 |
| 2026-10-22T08:22 | RUNEUSDT | surge | STOP | 1.5 | -3.25% | $-2.13 |
| 2026-10-22T08:22 | INTCBUSDT | bottom | STOP | 8.5 | -3.25% | $-2.04 |
| 2026-10-22T07:29 | DODOUSDT | surge | TARGET | 0.5 | +2.75% | $+1.80 |
| 2026-10-22T07:29 | SOXSBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.78 |
| 2026-10-22T06:34 | PHAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.81 |
| 2026-10-22T06:34 | ZROUSDT | bottom | STOP | 4.5 | -3.25% | $-2.14 |
| 2026-10-22T05:06 | PHAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.79 |
| 2026-10-22T04:48 | PHAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.78 |
| 2026-10-22T03:34 | LUMIAUSDT | surge | STOP | 15.8 | -3.25% | $-2.19 |
| 2026-10-22T03:00 | ACEUSDT | surge | STOP | 10.2 | -3.25% | $-2.15 |
| 2026-10-22T02:43 | MSTRBUSDT | surge | STOP | 10.0 | -3.25% | $-2.15 |
| 2026-10-22T02:43 | CRCLBUSDT | surge | STOP | 11.0 | -3.25% | $-2.16 |
| 2026-10-22T01:51 | QNTUSDT | surge | STOP | 3.2 | -3.25% | $-2.12 |
| 2026-10-22T01:51 | DOGEUSDT | surge | STOP | 8.8 | -3.25% | $-2.35 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-21T23:10 | TSLABUSDT | bottom | 375.06 | 372.15 | -0.78% |
| 2026-10-22T03:00 | PROMUSDT | surge | 5.889 | 5.842 | -0.80% |
| 2026-10-22T06:34 | BTCUSDT | bottom | 82570.4 | 81760.1 | -0.98% |
| 2026-10-22T08:22 | SPCXBUSDT | bottom | 155.12 | 155.58 | +0.30% |
| 2026-10-22T10:26 | RUNEUSDT | surge | 0.701 | 0.685 | -2.28% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
