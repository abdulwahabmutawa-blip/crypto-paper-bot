# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-12T07:09:07+00:00 · runs 3187 · equity **$792.63** (-20.74%) · cash $0.00 · open 10/10 · round trips 1184

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.19%/trade · realized $-205.94 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1040 | 51% | -0.16% | 48% | 45% | 7% |
| bottom | 144 | 45% | -0.42% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-12T06:35 | 币安人生USDT | surge | STOP | 2.5 | -3.25% | $-2.39 |
| 2026-10-12T05:30 | CFGUSDT | surge | TARGET | 2.8 | +2.75% | $+2.42 |
| 2026-10-12T05:14 | PEPEUSDT | surge | TARGET | 10.5 | +2.75% | $+2.06 |
| 2026-10-12T03:53 | TRXUSDT | bottom | TIME | 24.0 | +0.14% | $+0.11 |
| 2026-10-12T03:37 | DYMUSDT | surge | STOP | 0.0 | -3.25% | $-2.45 |
| 2026-10-12T03:21 | ARBUSDT | surge | STOP | 17.2 | -3.25% | $-2.53 |
| 2026-10-12T02:49 | IOUSDT | surge | TARGET | 4.2 | +2.75% | $+2.08 |
| 2026-10-12T02:33 | METISUSDT | surge | TARGET | 5.8 | +2.75% | $+2.36 |
| 2026-10-11T22:20 | CAKEUSDT | surge | TARGET | 23.2 | +2.75% | $+2.02 |
| 2026-10-11T20:37 | IOUSDT | surge | TARGET | 0.8 | +2.75% | $+2.29 |
| 2026-10-11T19:31 | IOUSDT | surge | TARGET | 2.5 | +2.75% | $+2.23 |
| 2026-10-11T18:25 | ATOMUSDT | surge | STOP | 3.0 | -3.25% | $-2.52 |
| 2026-10-11T17:51 | PLUMEUSDT | surge | TARGET | 3.2 | +2.75% | $+2.18 |
| 2026-10-11T16:46 | 币安人生USDT | surge | TARGET | 0.0 | +2.75% | $+2.17 |
| 2026-10-11T16:29 | MEGAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.20 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-11T09:49 | BIOUSDT | surge | 0.02956 | 0.0297 | +0.47% |
| 2026-10-11T15:40 | XLMUSDT | surge | 0.202 | 0.2028 | +0.40% |
| 2026-10-11T16:29 | TRBUSDT | surge | 19.73 | 19.38 | -1.77% |
| 2026-10-11T17:51 | MSTRBUSDT | surge | 158.04 | 158.85 | +0.51% |
| 2026-10-12T02:49 | MORPHOUSDT | surge | 2.469 | 2.482 | +0.53% |
| 2026-10-12T03:37 | LINEAUSDT | surge | 0.003138 | 0.003162 | +0.76% |
| 2026-10-12T05:14 | SOXLBUSDT | surge | 142.79 | 139.07 | -2.61% |
| 2026-10-12T05:30 | DASHUSDT | surge | 53.62 | 53.27 | -0.65% |
| 2026-10-12T06:35 | ALTUSDT | surge | 0.00863 | 0.00869 | +0.70% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
