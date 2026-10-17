# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T18:13:11+00:00 · runs 3653 · equity **$689.04** (-31.10%) · cash $129.94 · open 8/10 · round trips 1347

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-312.92 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1177 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 170 | 45% | -0.43% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-17T13:11 | LSKUSDT | surge | TARGET | 0.5 | +2.75% | $+1.82 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 49.37 | +0.22% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 875.31 | -0.33% |
| 2026-10-17T09:33 | XLMUSDT | bottom | 0.1791 | 0.178 | -0.61% |
| 2026-10-17T14:17 | CAKEUSDT | surge | 2.236 | 2.23 | -0.27% |
| 2026-10-17T15:23 | NMRUSDT | surge | 12.66 | 12.78 | +0.95% |
| 2026-10-17T16:45 | UNIUSDT | bottom | 7.069 | 7.134 | +0.92% |
| 2026-10-17T17:55 | ALTUSDT | surge | 0.00893 | 0.00912 | +2.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
