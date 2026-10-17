# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T17:03:22+00:00 · runs 3648 · equity **$682.34** (-31.77%) · cash $0.00 · open 10/10 · round trips 1344

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-310.45 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1174 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 170 | 45% | -0.43% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-17T13:11 | LSKUSDT | surge | TARGET | 0.5 | +2.75% | $+1.82 |
| 2026-10-17T12:22 | SENTUSDT | surge | STOP | 20.5 | -3.25% | $-2.23 |
| 2026-10-17T10:37 | MINAUSDT | surge | TARGET | 7.2 | +2.75% | $+1.94 |
| 2026-10-17T09:33 | RSRUSDT | surge | TARGET | 0.5 | +2.75% | $+1.89 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 49.61 | +0.71% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 872.14 | -0.69% |
| 2026-10-17T09:33 | XLMUSDT | bottom | 0.1791 | 0.1762 | -1.62% |
| 2026-10-17T14:17 | CAKEUSDT | surge | 2.236 | 2.215 | -0.94% |
| 2026-10-17T15:23 | NMRUSDT | surge | 12.66 | 12.53 | -1.03% |
| 2026-10-17T15:23 | PROMUSDT | surge | 5.061 | 4.916 | -2.87% |
| 2026-10-17T16:29 | ALTUSDT | surge | 0.00869 | 0.00847 | -2.53% |
| 2026-10-17T16:45 | UNIUSDT | bottom | 7.069 | 7.031 | -0.54% |
| 2026-10-17T17:01 | AUSDT | surge | 0.1134 | 0.1119 | -1.32% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
