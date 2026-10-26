# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-26T23:51:00+00:00 · runs 4459 · equity **$616.26** (-38.37%) · cash $0.00 · open 10/10 · round trips 1602

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-383.82 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1396 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 206 | 43% | -0.47% | 37% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-26T21:45 | HAEDALUSDT | surge | TARGET | 0.0 | +2.75% | $+1.62 |
| 2026-10-26T21:28 | CRVUSDT | surge | STOP | 11.2 | -3.25% | $-1.98 |
| 2026-10-26T16:54 | MUBARAKUSDT | surge | STOP | 17.8 | -3.25% | $-2.00 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-26T01:34 | SKHYBUSDT | surge | 141.52 | 144.91 | +2.40% |
| 2026-10-26T01:51 | BNBUSDT | bottom | 735.36 | 742.47 | +0.97% |
| 2026-10-26T03:34 | CFGUSDT | surge | 0.1036 | 0.1019 | -1.64% |
| 2026-10-26T10:22 | PHAUSDT | surge | 0.0511 | 0.0501 | -1.96% |
| 2026-10-26T13:26 | CELOUSDT | surge | 0.07865 | 0.07895 | +0.38% |
| 2026-10-26T13:43 | AIUSDT | surge | 0.0196 | 0.0196 | +0.00% |
| 2026-10-26T14:52 | TSLABUSDT | surge | 395.32 | 393.32 | -0.51% |
| 2026-10-26T16:54 | BEBUSDT | surge | 207.14 | 208.14 | +0.48% |
| 2026-10-26T21:45 | RWUSDUSDT | bottom | 0.9998 | 1.0001 | +0.03% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
