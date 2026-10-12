# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-12T18:21:29+00:00 · runs 3228 · equity **$766.00** (-23.40%) · cash $76.86 · open 9/10 · round trips 1204

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.22%/trade · realized $-234.70 · worst day $-50.94 · trades/day 31.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1060 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 144 | 45% | -0.42% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-12T17:12 | MORPHOUSDT | surge | STOP | 14.0 | -3.25% | $-2.52 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T13:52 | HYPEUSDT | bottom | 85.05 | 83.48 | -1.85% |
| 2026-10-12T13:52 | AAVEUSDT | bottom | 164.79 | 160.78 | -2.43% |
| 2026-10-12T14:09 | SPCXBUSDT | surge | 166.2 | 164.41 | -1.08% |
| 2026-10-12T14:59 | FETUSDT | bottom | 0.2228 | 0.2223 | -0.22% |
| 2026-10-12T15:16 | STXUSDT | surge | 0.398 | 0.4068 | +2.21% |
| 2026-10-12T15:49 | JSTUSDT | surge | 0.13999 | 0.14015 | +0.11% |
| 2026-10-12T16:22 | SOXSBUSDT | surge | 36.79 | 37.33 | +1.47% |
| 2026-10-12T18:03 | BEAMXUSDT | surge | 0.00277 | 0.002844 | +2.67% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
