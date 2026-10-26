# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-26T14:19:56+00:00 · runs 4426 · equity **$616.21** (-38.38%) · cash $0.00 · open 10/10 · round trips 1598

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-383.07 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1392 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 206 | 43% | -0.47% | 37% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-26T02:08 | ASTERUSDT | surge | TIME | 24.0 | -2.09% | $-1.22 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-25T22:54 | MUBARAKUSDT | surge | 0.05276 | 0.05224 | -0.99% |
| 2026-10-26T01:34 | SKHYBUSDT | surge | 141.52 | 140.63 | -0.63% |
| 2026-10-26T01:51 | BNBUSDT | bottom | 735.36 | 741 | +0.77% |
| 2026-10-26T03:34 | CFGUSDT | surge | 0.1036 | 0.1027 | -0.87% |
| 2026-10-26T09:46 | CRVUSDT | surge | 0.3493 | 0.3509 | +0.46% |
| 2026-10-26T10:22 | PHAUSDT | surge | 0.0511 | 0.0509 | -0.39% |
| 2026-10-26T13:26 | CELOUSDT | surge | 0.07865 | 0.07875 | +0.13% |
| 2026-10-26T13:43 | AIUSDT | surge | 0.0196 | 0.0195 | -0.51% |
| 2026-10-26T14:00 | BEBUSDT | surge | 199.14 | 200.94 | +0.90% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
