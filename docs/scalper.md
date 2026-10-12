# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-12T15:00:57+00:00 · runs 3216 · equity **$758.41** (-24.16%) · cash $70.46 · open 9/10 · round trips 1200

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.22%/trade · realized $-234.36 · worst day $-50.94 · trades/day 31.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1056 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 144 | 45% | -0.42% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-12T09:43 | PHAUSDT | surge | STOP | 0.8 | -3.25% | $-2.43 |
| 2026-10-12T09:26 | AXLUSDT | surge | STOP | 0.8 | -3.25% | $-2.24 |
| 2026-10-12T08:35 | SOXLBUSDT | surge | STOP | 3.2 | -3.25% | $-2.51 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-11T15:40 | XLMUSDT | surge | 0.202 | 0.1968 | -2.57% |
| 2026-10-12T02:49 | MORPHOUSDT | surge | 2.469 | 2.454 | -0.61% |
| 2026-10-12T13:52 | HYPEUSDT | bottom | 85.05 | 84.46 | -0.69% |
| 2026-10-12T13:52 | AAVEUSDT | bottom | 164.79 | 162.65 | -1.30% |
| 2026-10-12T14:09 | SPCXBUSDT | surge | 166.2 | 164.77 | -0.86% |
| 2026-10-12T14:09 | PYTHUSDT | surge | 0.08655 | 0.08541 | -1.32% |
| 2026-10-12T14:42 | DODOUSDT | surge | 0.01961 | 0.01931 | -1.53% |
| 2026-10-12T14:59 | FETUSDT | bottom | 0.2228 | 0.2218 | -0.45% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
