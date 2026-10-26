# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-26T10:59:42+00:00 · runs 4414 · equity **$619.20** (-38.08%) · cash $0.00 · open 10/10 · round trips 1593

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-377.39 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1388 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 205 | 43% | -0.46% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-26T10:22 | CHIPUSDT | surge | TARGET | 5.0 | +2.75% | $+1.61 |
| 2026-10-26T09:46 | SUIUSDT | bottom | TIME | 24.0 | +0.90% | $+0.54 |
| 2026-10-26T09:29 | SOXSBUSDT | surge | STOP | 1.0 | -3.25% | $-1.84 |
| 2026-10-26T08:18 | BCHUSDT | surge | STOP | 2.8 | -3.25% | $-1.90 |
| 2026-10-26T07:25 | PYTHUSDT | surge | STOP | 11.0 | -3.25% | $-2.07 |
| 2026-10-26T04:08 | AAVEUSDT | surge | STOP | 10.5 | -3.25% | $-1.94 |
| 2026-10-26T02:43 | IOSTUSDT | bottom | TARGET | 0.2 | +2.75% | $+1.57 |
| 2026-10-26T02:43 | NBISBUSDT | surge | STOP | 11.5 | -3.25% | $-1.95 |
| 2026-10-26T02:26 | ZROUSDT | surge | STOP | 9.0 | -3.25% | $-2.03 |
| 2026-10-26T02:08 | ASTERUSDT | surge | TIME | 24.0 | -2.09% | $-1.22 |
| 2026-10-26T01:51 | HOLOUSDT | surge | STOP | 1.5 | -3.25% | $-1.97 |
| 2026-10-26T01:34 | OSMOUSDT | surge | STOP | 3.0 | -3.25% | $-2.05 |
| 2026-10-26T00:08 | QNTUSDT | surge | STOP | 4.5 | -3.25% | $-2.03 |
| 2026-10-25T22:54 | PLUMEUSDT | surge | TARGET | 7.2 | +2.75% | $+1.65 |
| 2026-10-25T22:19 | ENAUSDT | surge | TARGET | 5.8 | +2.75% | $+1.69 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-25T22:54 | MUBARAKUSDT | surge | 0.05276 | 0.05163 | -2.14% |
| 2026-10-26T01:34 | SKHYBUSDT | surge | 141.52 | 139.93 | -1.12% |
| 2026-10-26T01:51 | BNBUSDT | bottom | 735.36 | 740.37 | +0.68% |
| 2026-10-26T02:43 | CRCLBUSDT | bottom | 83.2 | 83.24 | +0.05% |
| 2026-10-26T03:34 | CFGUSDT | surge | 0.1036 | 0.1012 | -2.32% |
| 2026-10-26T07:25 | TSLABUSDT | surge | 376.25 | 379.79 | +0.94% |
| 2026-10-26T09:29 | BEAMXUSDT | surge | 0.003362 | 0.003304 | -1.73% |
| 2026-10-26T09:46 | CRVUSDT | surge | 0.3493 | 0.3494 | +0.03% |
| 2026-10-26T10:22 | PHAUSDT | surge | 0.0511 | 0.051 | -0.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
