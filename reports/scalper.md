# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-28T12:59:19+00:00 · runs 2017 · equity **$916.79** (-8.32%) · cash $370.30 · open 6/10 · round trips 739

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-86.41 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 631 | 53% | -0.06% | 49% | 43% | 7% |
| bottom | 108 | 44% | -0.42% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28T12:41 | ADAUSDT | bottom | TARGET | 4.8 | +2.75% | $+2.53 |
| 2026-09-28T12:25 | MARSCOINUSDT | surge | TARGET | 0.0 | +2.75% | $+2.51 |
| 2026-09-28T08:49 | PROMUSDT | surge | STOP | 2.2 | -3.25% | $-2.99 |
| 2026-09-28T08:00 | HBARUSDT | surge | STOP | 0.5 | -3.25% | $-3.07 |
| 2026-09-28T07:44 | BABYUSDT | bottom | STOP | 4.2 | -3.25% | $-2.75 |
| 2026-09-28T07:28 | MUBARAKUSDT | surge | STOP | 0.2 | -3.25% | $-3.06 |
| 2026-09-28T07:28 | HBARUSDT | surge | TARGET | 5.0 | +2.75% | $+2.66 |
| 2026-09-28T06:55 | PUMPUSDT | surge | STOP | 5.5 | -3.25% | $-3.40 |
| 2026-09-28T05:45 | ONDOUSDT | surge | STOP | 1.0 | -3.25% | $-2.97 |
| 2026-09-28T05:45 | SEIUSDT | surge | STOP | 1.8 | -3.25% | $-3.07 |
| 2026-09-28T05:45 | MMTUSDT | surge | STOP | 16.8 | -3.25% | $-3.00 |
| 2026-09-28T05:45 | JSTUSDT | surge | TIME | 24.0 | +2.60% | $+2.49 |
| 2026-09-28T04:40 | SKYUSDT | surge | STOP | 0.5 | -3.25% | $-3.07 |
| 2026-09-28T03:34 | IOTAUSDT | surge | STOP | 1.2 | -3.25% | $-3.14 |
| 2026-09-28T03:34 | IMXUSDT | surge | STOP | 1.8 | -3.25% | $-3.29 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-27T15:49 | HYPEUSDT | bottom | 91.19 | 90.3 | -0.98% |
| 2026-09-28T03:34 | MSTRBUSDT | bottom | 156.65 | 158.31 | +1.06% |
| 2026-09-28T12:08 | NVDABUSDT | surge | 227.9 | 229.72 | +0.80% |
| 2026-09-28T12:08 | JSTUSDT | surge | 0.12933 | 0.13102 | +1.31% |
| 2026-09-28T12:57 | 牛来USDT | surge | 0.11297 | 0.11434 | +1.21% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
