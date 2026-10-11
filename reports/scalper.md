# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-11T21:16:16+00:00 · runs 3150 · equity **$790.40** (-20.96%) · cash $0.00 · open 10/10 · round trips 1175

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.19%/trade · realized $-209.60 · worst day $-50.94 · trades/day 31.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1032 | 51% | -0.16% | 48% | 45% | 7% |
| bottom | 143 | 45% | -0.42% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-11T20:37 | IOUSDT | surge | TARGET | 0.8 | +2.75% | $+2.29 |
| 2026-10-11T19:31 | IOUSDT | surge | TARGET | 2.5 | +2.75% | $+2.23 |
| 2026-10-11T18:25 | ATOMUSDT | surge | STOP | 3.0 | -3.25% | $-2.52 |
| 2026-10-11T17:51 | PLUMEUSDT | surge | TARGET | 3.2 | +2.75% | $+2.18 |
| 2026-10-11T16:46 | 币安人生USDT | surge | TARGET | 0.0 | +2.75% | $+2.17 |
| 2026-10-11T16:29 | MEGAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.20 |
| 2026-10-11T16:29 | ADAUSDT | bottom | TARGET | 12.5 | +2.75% | $+2.02 |
| 2026-10-11T15:40 | ALGOUSDT | surge | TARGET | 0.2 | +2.75% | $+2.13 |
| 2026-10-11T15:40 | MEGAUSDT | surge | TARGET | 1.2 | +2.75% | $+2.16 |
| 2026-10-11T15:06 | IOUSDT | surge | TARGET | 0.5 | +2.75% | $+2.16 |
| 2026-10-11T15:06 | NILUSDT | surge | STOP | 0.8 | -3.25% | $-2.51 |
| 2026-10-11T14:16 | PLUMEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.12 |
| 2026-10-11T14:00 | 币安人生USDT | surge | TARGET | 1.8 | +2.75% | $+2.23 |
| 2026-10-11T14:00 | BOMEUSDT | surge | STOP | 3.0 | -3.25% | $-2.46 |
| 2026-10-11T13:43 | ACHUSDT | surge | TARGET | 5.0 | +2.75% | $+2.11 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-10T22:49 | CAKEUSDT | surge | 2.261 | 2.315 | +2.39% |
| 2026-10-11T03:38 | TRXUSDT | bottom | 0.3303 | 0.3302 | -0.03% |
| 2026-10-11T09:49 | ARBUSDT | surge | 0.1995 | 0.1977 | -0.90% |
| 2026-10-11T09:49 | BIOUSDT | surge | 0.02956 | 0.02966 | +0.34% |
| 2026-10-11T15:40 | XLMUSDT | surge | 0.202 | 0.2022 | +0.10% |
| 2026-10-11T16:29 | TRBUSDT | surge | 19.73 | 19.3 | -2.18% |
| 2026-10-11T17:51 | MSTRBUSDT | surge | 158.04 | 156.57 | -0.93% |
| 2026-10-11T18:25 | PEPEUSDT | surge | 4.2e-06 | 4.16e-06 | -0.95% |
| 2026-10-11T20:37 | METISUSDT | surge | 3.76 | 3.84 | +2.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
