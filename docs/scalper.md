# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T20:47:08+00:00 · runs 3662 · equity **$683.87** (-31.61%) · cash $0.00 · open 10/10 · round trips 1353

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-314.05 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1182 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 171 | 44% | -0.43% | 39% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-17T20:29 | MUBUSDT | bottom | TIME | 24.0 | -0.29% | $-0.20 |
| 2026-10-17T20:29 | SOXSBUSDT | surge | TIME | 24.0 | -0.29% | $-0.20 |
| 2026-10-17T20:06 | OGNUSDT | surge | STOP | 0.5 | -3.25% | $-2.16 |
| 2026-10-17T20:06 | LSKUSDT | surge | STOP | 0.5 | -3.25% | $-2.16 |
| 2026-10-17T19:17 | ALTUSDT | surge | TARGET | 0.8 | +2.75% | $+1.80 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-17T09:33 | XLMUSDT | bottom | 0.1791 | 0.1791 | +0.00% |
| 2026-10-17T14:17 | CAKEUSDT | surge | 2.236 | 2.218 | -0.81% |
| 2026-10-17T15:23 | NMRUSDT | surge | 12.66 | 12.37 | -2.29% |
| 2026-10-17T16:45 | UNIUSDT | bottom | 7.069 | 7.186 | +1.66% |
| 2026-10-17T19:00 | AXLUSDT | surge | 0.0578 | 0.0578 | +0.00% |
| 2026-10-17T20:06 | AUSDT | surge | 0.114 | 0.1121 | -1.67% |
| 2026-10-17T20:06 | CRVUSDT | surge | 0.3485 | 0.3476 | -0.26% |
| 2026-10-17T20:29 | HBARUSDT | surge | 0.0849 | 0.0851 | +0.24% |
| 2026-10-17T20:29 | RWUSDUSDT | bottom | 1 | 1 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
