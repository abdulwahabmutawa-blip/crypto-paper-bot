# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T19:02:18+00:00 · runs 3656 · equity **$689.07** (-31.09%) · cash $65.57 · open 9/10 · round trips 1348

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-311.13 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1178 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 170 | 45% | -0.43% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-17T18:28 | ALTUSDT | surge | TARGET | 0.2 | +2.75% | $+1.79 |
| 2026-10-17T17:55 | AUSDT | surge | STOP | 0.5 | -3.25% | $-2.07 |
| 2026-10-17T17:55 | ALTUSDT | surge | TARGET | 1.2 | +2.75% | $+1.81 |
| 2026-10-17T17:18 | PROMUSDT | surge | STOP | 1.8 | -3.25% | $-2.21 |
| 2026-10-17T17:01 | SANDUSDT | surge | STOP | 0.8 | -3.25% | $-2.14 |
| 2026-10-17T16:45 | ARBUSDT | bottom | STOP | 7.0 | -3.25% | $-2.20 |
| 2026-10-17T15:56 | LSKUSDT | surge | STOP | 1.0 | -3.25% | $-2.14 |
| 2026-10-17T15:23 | NMRUSDT | surge | TARGET | 7.8 | +2.75% | $+1.92 |
| 2026-10-17T14:17 | AVAUSDT | surge | STOP | 0.0 | -3.25% | $-2.16 |
| 2026-10-17T14:01 | ALTUSDT | surge | TARGET | 0.0 | +2.75% | $+1.82 |
| 2026-10-17T13:44 | ALTUSDT | surge | TARGET | 0.2 | +2.75% | $+1.82 |
| 2026-10-17T13:44 | SANDUSDT | surge | STOP | 0.2 | -3.25% | $-2.15 |
| 2026-10-17T13:44 | AXLUSDT | surge | STOP | 2.8 | -3.25% | $-2.35 |
| 2026-10-17T13:44 | EIGENUSDT | surge | STOP | 6.5 | -3.25% | $-2.08 |
| 2026-10-17T13:28 | KMNOUSDT | surge | STOP | 3.8 | -3.25% | $-2.16 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 49.01 | -0.51% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 879.09 | +0.10% |
| 2026-10-17T09:33 | XLMUSDT | bottom | 0.1791 | 0.1785 | -0.34% |
| 2026-10-17T14:17 | CAKEUSDT | surge | 2.236 | 2.215 | -0.94% |
| 2026-10-17T15:23 | NMRUSDT | surge | 12.66 | 12.62 | -0.32% |
| 2026-10-17T16:45 | UNIUSDT | bottom | 7.069 | 7.146 | +1.09% |
| 2026-10-17T18:28 | ALTUSDT | surge | 0.0091 | 0.0092 | +1.10% |
| 2026-10-17T19:00 | AXLUSDT | surge | 0.0578 | 0.0579 | +0.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
