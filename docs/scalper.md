# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-12T10:56:21+00:00 · runs 3201 · equity **$780.82** (-21.92%) · cash $0.00 · open 10/10 · round trips 1191

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.20%/trade · realized $-216.09 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1047 | 50% | -0.17% | 48% | 45% | 7% |
| bottom | 144 | 45% | -0.42% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-12T10:01 | REDUSDT | surge | TARGET | 0.0 | +2.75% | $+1.99 |
| 2026-10-12T10:01 | LINEAUSDT | surge | STOP | 6.2 | -3.25% | $-2.37 |
| 2026-10-12T10:01 | BIOUSDT | surge | TIME | 24.0 | -0.35% | $-0.27 |
| 2026-10-12T09:43 | PHAUSDT | surge | STOP | 0.8 | -3.25% | $-2.43 |
| 2026-10-12T09:26 | AXLUSDT | surge | STOP | 0.8 | -3.25% | $-2.24 |
| 2026-10-12T08:35 | SOXLBUSDT | surge | STOP | 3.2 | -3.25% | $-2.51 |
| 2026-10-12T08:18 | ALTUSDT | surge | STOP | 1.5 | -3.25% | $-2.32 |
| 2026-10-12T06:35 | 币安人生USDT | surge | STOP | 2.5 | -3.25% | $-2.39 |
| 2026-10-12T05:30 | CFGUSDT | surge | TARGET | 2.8 | +2.75% | $+2.42 |
| 2026-10-12T05:14 | PEPEUSDT | surge | TARGET | 10.5 | +2.75% | $+2.06 |
| 2026-10-12T03:53 | TRXUSDT | bottom | TIME | 24.0 | +0.14% | $+0.11 |
| 2026-10-12T03:37 | DYMUSDT | surge | STOP | 0.0 | -3.25% | $-2.45 |
| 2026-10-12T03:21 | ARBUSDT | surge | STOP | 17.2 | -3.25% | $-2.53 |
| 2026-10-12T02:49 | IOUSDT | surge | TARGET | 4.2 | +2.75% | $+2.08 |
| 2026-10-12T02:33 | METISUSDT | surge | TARGET | 5.8 | +2.75% | $+2.36 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-11T15:40 | XLMUSDT | surge | 0.202 | 0.2015 | -0.25% |
| 2026-10-11T16:29 | TRBUSDT | surge | 19.73 | 19.36 | -1.88% |
| 2026-10-11T17:51 | MSTRBUSDT | surge | 158.04 | 156.87 | -0.74% |
| 2026-10-12T02:49 | MORPHOUSDT | surge | 2.469 | 2.509 | +1.62% |
| 2026-10-12T05:30 | DASHUSDT | surge | 53.62 | 52.32 | -2.42% |
| 2026-10-12T09:26 | RENDERUSDT | surge | 2.092 | 2.139 | +2.25% |
| 2026-10-12T10:01 | DODOUSDT | surge | 0.01897 | 0.01903 | +0.32% |
| 2026-10-12T10:01 | SKLUSDT | surge | 0.00532 | 0.00522 | -1.88% |
| 2026-10-12T10:01 | ZROUSDT | surge | 2.429 | 2.422 | -0.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
