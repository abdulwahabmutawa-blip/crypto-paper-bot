# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-12T16:41:05+00:00 · runs 3222 · equity **$766.84** (-23.32%) · cash $78.65 · open 9/10 · round trips 1203

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-232.18 · worst day $-50.94 · trades/day 31.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1059 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 144 | 45% | -0.42% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-12T16:06 | PYTHUSDT | surge | TARGET | 1.8 | +2.75% | $+2.00 |
| 2026-10-12T15:49 | DODOUSDT | surge | TARGET | 1.0 | +2.75% | $+2.33 |
| 2026-10-12T15:49 | XLMUSDT | surge | TIME | 24.0 | -2.68% | $-2.14 |
| 2026-10-12T14:59 | RENDERUSDT | surge | STOP | 5.2 | -3.25% | $-2.17 |
| 2026-10-12T14:59 | TRBUSDT | surge | STOP | 22.5 | -3.25% | $-2.57 |
| 2026-10-12T14:42 | ZAMAUSDT | surge | STOP | 3.0 | -3.25% | $-2.84 |
| 2026-10-12T14:09 | KITEUSDT | surge | STOP | 1.8 | -3.25% | $-2.33 |
| 2026-10-12T14:09 | DODOUSDT | surge | TARGET | 3.8 | +2.75% | $+2.04 |
| 2026-10-12T13:52 | SKLUSDT | surge | STOP | 3.5 | -3.25% | $-2.41 |
| 2026-10-12T13:52 | MSTRBUSDT | surge | STOP | 19.8 | -3.25% | $-2.65 |
| 2026-10-12T12:03 | ZROUSDT | surge | STOP | 1.8 | -3.25% | $-2.41 |
| 2026-10-12T11:28 | DASHUSDT | surge | STOP | 5.5 | -3.25% | $-2.94 |
| 2026-10-12T10:01 | REDUSDT | surge | TARGET | 0.0 | +2.75% | $+1.99 |
| 2026-10-12T10:01 | LINEAUSDT | surge | STOP | 6.2 | -3.25% | $-2.37 |
| 2026-10-12T10:01 | BIOUSDT | surge | TIME | 24.0 | -0.35% | $-0.27 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T02:49 | MORPHOUSDT | surge | 2.469 | 2.45 | -0.77% |
| 2026-10-12T13:52 | HYPEUSDT | bottom | 85.05 | 84.32 | -0.86% |
| 2026-10-12T13:52 | AAVEUSDT | bottom | 164.79 | 163.2 | -0.96% |
| 2026-10-12T14:09 | SPCXBUSDT | surge | 166.2 | 164.19 | -1.21% |
| 2026-10-12T14:59 | FETUSDT | bottom | 0.2228 | 0.2241 | +0.58% |
| 2026-10-12T15:16 | STXUSDT | surge | 0.398 | 0.4064 | +2.11% |
| 2026-10-12T15:49 | JSTUSDT | surge | 0.13999 | 0.13982 | -0.12% |
| 2026-10-12T16:22 | SOXSBUSDT | surge | 36.79 | 36.82 | +0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
