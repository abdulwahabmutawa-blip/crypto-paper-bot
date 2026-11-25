# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-25T17:12:32+00:00 · runs 6759 · equity **$477.38** (-52.26%) · cash $0.00 · open 10/10 · round trips 2207

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-525.94 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1896 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 311 | 42% | -0.54% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-25T15:06 | SOLUSDT | bottom | STOP | 6.5 | -3.25% | $-1.42 |
| 2026-11-25T14:48 | ICPUSDT | bottom | STOP | 10.8 | -3.25% | $-1.43 |
| 2026-11-25T13:37 | ALICEUSDT | surge | STOP | 2.5 | -3.25% | $-1.42 |
| 2026-11-25T13:37 | ERAUSDT | surge | STOP | 4.8 | -3.25% | $-1.43 |
| 2026-11-25T13:37 | AAVEUSDT | bottom | TIME | 24.0 | -1.82% | $-0.79 |
| 2026-11-25T07:47 | TAOUSDT | bottom | STOP | 9.5 | -3.25% | $-1.43 |
| 2026-11-25T07:29 | USUALUSDT | surge | STOP | 0.2 | -3.25% | $-1.44 |
| 2026-11-25T06:21 | USUALUSDT | surge | TARGET | 1.2 | +2.75% | $+1.21 |
| 2026-11-25T04:39 | ERAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.21 |
| 2026-11-25T04:22 | INITUSDT | surge | TARGET | 0.0 | +2.75% | $+1.21 |
| 2026-11-25T04:22 | BLURUSDT | surge | STOP | 0.2 | -3.25% | $-1.43 |
| 2026-11-25T03:47 | USUALUSDT | surge | TARGET | 4.8 | +2.75% | $+1.21 |
| 2026-11-25T00:14 | ETHUSDT | bottom | TIME | 24.0 | -2.58% | $-1.14 |
| 2026-11-24T20:44 | HBARUSDT | bottom | STOP | 8.8 | -3.25% | $-1.42 |
| 2026-11-24T20:44 | SPYBUSDT | surge | TIME | 24.0 | -0.54% | $-0.24 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-25T16:17 | 牛来USDT | surge | 0.04026 | 0.04083 | +1.42% |
| 2026-11-25T16:17 | SQQQBUSDT | surge | 55.06 | 53.09 | -3.58% |
| 2026-11-25T16:17 | WLFIUSDT | surge | 0.0414 | 0.0413 | -0.24% |
| 2026-11-25T16:17 | NVDABUSDT | bottom | 142.6 | 144.24 | +1.15% |
| 2026-11-25T16:17 | QQQBUSDT | bottom | 611.59 | 619.67 | +1.32% |
| 2026-11-25T16:17 | GOOGLBUSDT | bottom | 265.1 | 268.45 | +1.26% |
| 2026-11-25T16:35 | ANTBUSDT | surge | 80.68 | 81.58 | +1.12% |
| 2026-11-25T16:35 | SENTUSDT | surge | 0.02055 | 0.0209 | +1.70% |
| 2026-11-25T16:52 | XPLUSDT | surge | 0.04528 | 0.04689 | +3.56% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
