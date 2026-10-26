# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-26T16:38:49+00:00 · runs 4434 · equity **$614.75** (-38.52%) · cash $0.00 · open 10/10 · round trips 1599

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-381.47 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1393 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 206 | 43% | -0.47% | 37% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-26T14:52 | BEBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.60 |
| 2026-10-26T14:00 | QNTUSDT | surge | STOP | 0.2 | -3.25% | $-1.96 |
| 2026-10-26T13:43 | TSLABUSDT | surge | TARGET | 6.2 | +2.75% | $+1.69 |
| 2026-10-26T13:43 | CRCLBUSDT | bottom | STOP | 11.0 | -3.25% | $-1.92 |
| 2026-10-26T13:26 | ALTUSDT | surge | STOP | 1.8 | -3.25% | $-1.72 |
| 2026-10-26T11:15 | BEAMXUSDT | surge | STOP | 1.8 | -3.25% | $-1.78 |
| 2026-10-26T10:22 | CHIPUSDT | surge | TARGET | 5.0 | +2.75% | $+1.61 |
| 2026-10-26T09:46 | SUIUSDT | bottom | TIME | 24.0 | +0.90% | $+0.54 |
| 2026-10-26T09:29 | SOXSBUSDT | surge | STOP | 1.0 | -3.25% | $-1.84 |
| 2026-10-26T08:18 | BCHUSDT | surge | STOP | 2.8 | -3.25% | $-1.90 |
| 2026-10-26T07:25 | PYTHUSDT | surge | STOP | 11.0 | -3.25% | $-2.07 |
| 2026-10-26T04:08 | AAVEUSDT | surge | STOP | 10.5 | -3.25% | $-1.94 |
| 2026-10-26T02:43 | IOSTUSDT | bottom | TARGET | 0.2 | +2.75% | $+1.57 |
| 2026-10-26T02:43 | NBISBUSDT | surge | STOP | 11.5 | -3.25% | $-1.95 |
| 2026-10-26T02:26 | ZROUSDT | surge | STOP | 9.0 | -3.25% | $-2.03 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-25T22:54 | MUBARAKUSDT | surge | 0.05276 | 0.05131 | -2.75% |
| 2026-10-26T01:34 | SKHYBUSDT | surge | 141.52 | 141.71 | +0.13% |
| 2026-10-26T01:51 | BNBUSDT | bottom | 735.36 | 740.31 | +0.67% |
| 2026-10-26T03:34 | CFGUSDT | surge | 0.1036 | 0.1014 | -2.12% |
| 2026-10-26T09:46 | CRVUSDT | surge | 0.3493 | 0.3465 | -0.80% |
| 2026-10-26T10:22 | PHAUSDT | surge | 0.0511 | 0.0503 | -1.57% |
| 2026-10-26T13:26 | CELOUSDT | surge | 0.07865 | 0.07886 | +0.27% |
| 2026-10-26T13:43 | AIUSDT | surge | 0.0196 | 0.0196 | +0.00% |
| 2026-10-26T14:52 | TSLABUSDT | surge | 395.32 | 395.17 | -0.04% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
