# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-27T04:41:56+00:00 · runs 4476 · equity **$611.05** (-38.89%) · cash $0.00 · open 10/10 · round trips 1608

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-385.71 · worst day $-50.94 · trades/day 30.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1401 | 49% | -0.28% | 46% | 47% | 7% |
| bottom | 207 | 43% | -0.46% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-27T04:06 | IOSTUSDT | surge | TARGET | 0.8 | +2.75% | $+1.57 |
| 2026-10-27T03:48 | CFGUSDT | surge | TIME | 24.0 | -3.05% | $-1.80 |
| 2026-10-27T03:14 | KORUBUSDT | surge | STOP | 0.8 | -3.25% | $-1.92 |
| 2026-10-27T02:06 | BNBUSDT | bottom | TIME | 24.0 | +0.91% | $+0.53 |
| 2026-10-27T01:31 | PHAUSDT | surge | STOP | 15.0 | -3.25% | $-1.95 |
| 2026-10-27T00:23 | SKHYBUSDT | surge | TARGET | 22.5 | +2.75% | $+1.68 |
| 2026-10-26T21:45 | HAEDALUSDT | surge | TARGET | 0.0 | +2.75% | $+1.62 |
| 2026-10-26T21:28 | CRVUSDT | surge | STOP | 11.2 | -3.25% | $-1.98 |
| 2026-10-26T16:54 | MUBARAKUSDT | surge | STOP | 17.8 | -3.25% | $-2.00 |
| 2026-10-26T14:52 | BEBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.60 |
| 2026-10-26T14:00 | QNTUSDT | surge | STOP | 0.2 | -3.25% | $-1.96 |
| 2026-10-26T13:43 | TSLABUSDT | surge | TARGET | 6.2 | +2.75% | $+1.69 |
| 2026-10-26T13:43 | CRCLBUSDT | bottom | STOP | 11.0 | -3.25% | $-1.92 |
| 2026-10-26T13:26 | ALTUSDT | surge | STOP | 1.8 | -3.25% | $-1.72 |
| 2026-10-26T11:15 | BEAMXUSDT | surge | STOP | 1.8 | -3.25% | $-1.78 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-26T13:26 | CELOUSDT | surge | 0.07865 | 0.07832 | -0.42% |
| 2026-10-26T13:43 | AIUSDT | surge | 0.0196 | 0.0196 | +0.00% |
| 2026-10-26T14:52 | TSLABUSDT | surge | 395.32 | 392.73 | -0.66% |
| 2026-10-26T16:54 | BEBUSDT | surge | 207.14 | 205.57 | -0.76% |
| 2026-10-26T21:45 | RWUSDUSDT | bottom | 0.9998 | 0.9999 | +0.01% |
| 2026-10-27T00:23 | TQQQBUSDT | surge | 69.3 | 68.32 | -1.41% |
| 2026-10-27T01:31 | SKHYBUSDT | surge | 148.19 | 145.94 | -1.52% |
| 2026-10-27T03:48 | TRXUSDT | bottom | 0.3292 | 0.3291 | -0.03% |
| 2026-10-27T04:06 | ZROUSDT | bottom | 1.613 | 1.602 | -0.68% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
