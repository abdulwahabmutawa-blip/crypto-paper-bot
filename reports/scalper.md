# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-15T23:19:02+00:00 · runs 914 · equity **$877.35** (-12.27%) · cash $618.08 · open 3/10 · round trips 324

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.39%/trade · realized $-121.95 · worst day $-50.94 · trades/day 29.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 249 | 47% | -0.35% | 44% | 47% | 8% |
| bottom | 75 | 41% | -0.53% | 40% | 47% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-15T19:04 | BANKUSDT | bottom | STOP | 15.2 | -3.25% | $-2.74 |
| 2026-09-15T18:29 | DODOUSDT | surge | STOP | 14.2 | -3.25% | $-3.01 |
| 2026-09-15T17:38 | METABUSDT | surge | TIME | 24.0 | +0.08% | $+0.07 |
| 2026-09-15T16:12 | SKHYBUSDT | surge | STOP | 2.2 | -3.25% | $-2.79 |
| 2026-09-15T15:03 | TUTUSDT | surge | TARGET | 1.2 | +2.75% | $+2.36 |
| 2026-09-15T15:03 | INJUSDT | bottom | STOP | 2.5 | -3.25% | $-2.94 |
| 2026-09-15T14:12 | SPCXBUSDT | surge | STOP | 21.8 | -3.25% | $-3.17 |
| 2026-09-15T13:33 | TUTUSDT | surge | TARGET | 2.8 | +2.75% | $+2.36 |
| 2026-09-15T13:16 | MINAUSDT | surge | STOP | 0.5 | -3.25% | $-2.80 |
| 2026-09-15T12:43 | SAGAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.31 |
| 2026-09-15T12:27 | VTHOUSDT | surge | TARGET | 0.0 | +2.75% | $+2.42 |
| 2026-09-15T12:10 | MINAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.36 |
| 2026-09-15T11:54 | FETUSDT | bottom | STOP | 7.2 | -3.25% | $-2.82 |
| 2026-09-15T09:59 | COTIUSDT | surge | STOP | 0.5 | -3.25% | $-2.83 |
| 2026-09-15T09:09 | COTIUSDT | surge | TARGET | 1.5 | +2.75% | $+2.22 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-15T03:20 | JSTUSDT | surge | 0.11522 | 0.11553 | +0.27% |
| 2026-09-15T03:37 | GRAMUSDT | bottom | 1.341 | 1.326 | -1.12% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
