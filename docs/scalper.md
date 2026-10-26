# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-26T03:02:07+00:00 · runs 4386 · equity **$625.09** (-37.49%) · cash $118.05 · open 8/10 · round trips 1587

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-371.78 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1383 | 49% | -0.26% | 46% | 47% | 7% |
| bottom | 204 | 43% | -0.46% | 38% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-25T17:06 | AIUSDT | bottom | TIME | 24.0 | +0.27% | $+0.17 |
| 2026-10-25T16:17 | POLYXUSDT | bottom | TARGET | 1.5 | +2.75% | $+1.65 |
| 2026-10-25T14:38 | CHIPUSDT | surge | STOP | 1.8 | -3.25% | $-1.99 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-25T09:37 | SUIUSDT | bottom | 0.9078 | 0.912 | +0.46% |
| 2026-10-25T17:23 | AAVEUSDT | surge | 137.88 | 134.65 | -2.34% |
| 2026-10-25T20:01 | PYTHUSDT | surge | 0.0754 | 0.0742 | -1.59% |
| 2026-10-25T22:54 | MUBARAKUSDT | surge | 0.05276 | 0.05263 | -0.25% |
| 2026-10-26T01:34 | SKHYBUSDT | surge | 141.52 | 139.34 | -1.54% |
| 2026-10-26T01:51 | BNBUSDT | bottom | 735.36 | 735.52 | +0.02% |
| 2026-10-26T02:43 | CRCLBUSDT | bottom | 83.2 | 83.32 | +0.14% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
