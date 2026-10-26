# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-26T08:38:26+00:00 · runs 4406 · equity **$618.46** (-38.15%) · cash $0.00 · open 10/10 · round trips 1590

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-377.70 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1386 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 204 | 43% | -0.46% | 38% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-25T20:01 | SOXLBUSDT | surge | TIME | 24.0 | +1.37% | $+0.86 |
| 2026-10-25T19:26 | DODOUSDT | surge | TARGET | 5.2 | +2.75% | $+1.67 |
| 2026-10-25T17:23 | DASHUSDT | surge | STOP | 3.8 | -3.25% | $-2.01 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-25T09:37 | SUIUSDT | bottom | 0.9078 | 0.9154 | +0.84% |
| 2026-10-25T22:54 | MUBARAKUSDT | surge | 0.05276 | 0.05172 | -1.97% |
| 2026-10-26T01:34 | SKHYBUSDT | surge | 141.52 | 139.3 | -1.57% |
| 2026-10-26T01:51 | BNBUSDT | bottom | 735.36 | 737.38 | +0.27% |
| 2026-10-26T02:43 | CRCLBUSDT | bottom | 83.2 | 83.69 | +0.59% |
| 2026-10-26T03:34 | CFGUSDT | surge | 0.1036 | 0.1021 | -1.45% |
| 2026-10-26T05:00 | CHIPUSDT | surge | 0.04604 | 0.04518 | -1.87% |
| 2026-10-26T07:25 | TSLABUSDT | surge | 376.25 | 378.75 | +0.66% |
| 2026-10-26T08:18 | SOXSBUSDT | surge | 53.74 | 52.65 | -2.03% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
