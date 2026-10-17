# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T16:47:00+00:00 · runs 3647 · equity **$685.88** (-31.41%) · cash $0.00 · open 10/10 · round trips 1343

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-308.31 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1173 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 170 | 45% | -0.43% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-17T09:33 | NILUSDT | surge | STOP | 1.2 | -3.25% | $-2.18 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 49.25 | -0.02% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 875.93 | -0.26% |
| 2026-10-17T09:33 | XLMUSDT | bottom | 0.1791 | 0.1764 | -1.51% |
| 2026-10-17T14:17 | CAKEUSDT | surge | 2.236 | 2.215 | -0.94% |
| 2026-10-17T15:23 | NMRUSDT | surge | 12.66 | 12.46 | -1.58% |
| 2026-10-17T15:23 | PROMUSDT | surge | 5.061 | 4.922 | -2.75% |
| 2026-10-17T16:12 | SANDUSDT | surge | 0.06313 | 0.06263 | -0.79% |
| 2026-10-17T16:29 | ALTUSDT | surge | 0.00869 | 0.00863 | -0.69% |
| 2026-10-17T16:45 | UNIUSDT | bottom | 7.069 | 7.063 | -0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
