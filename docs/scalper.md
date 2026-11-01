# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-01T15:25:57+00:00 · runs 4955 · equity **$590.60** (-40.94%) · cash $0.00 · open 10/10 · round trips 1733

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-401.99 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1508 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 225 | 43% | -0.49% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-01T15:23 | BIOUSDT | surge | STOP | 0.5 | -3.25% | $-1.76 |
| 2026-11-01T15:06 | TRUMPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.49 |
| 2026-11-01T14:31 | TRUMPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.45 |
| 2026-11-01T14:31 | BIOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.45 |
| 2026-11-01T14:13 | ERAUSDT | surge | STOP | 1.5 | -3.25% | $-1.77 |
| 2026-11-01T14:13 | MARSCOINUSDT | surge | STOP | 4.2 | -3.25% | $-1.78 |
| 2026-11-01T12:41 | AVAXUSDT | surge | STOP | 5.5 | -3.25% | $-1.83 |
| 2026-11-01T09:51 | ETHFIUSDT | surge | STOP | 17.5 | -3.25% | $-1.84 |
| 2026-11-01T06:57 | KITEUSDT | surge | TARGET | 0.8 | +2.75% | $+1.51 |
| 2026-11-01T06:23 | FETUSDT | bottom | TARGET | 6.0 | +2.75% | $+1.53 |
| 2026-11-01T06:06 | LTCUSDT | bottom | TARGET | 21.0 | +2.75% | $+1.51 |
| 2026-11-01T05:49 | 牛来USDT | surge | TARGET | 1.8 | +2.75% | $+1.47 |
| 2026-11-01T04:58 | AAVEUSDT | surge | TARGET | 13.5 | +2.75% | $+1.70 |
| 2026-11-01T03:50 | MORPHOUSDT | surge | STOP | 8.2 | -3.25% | $-1.79 |
| 2026-11-01T00:00 | PENDLEUSDT | surge | TIME | 24.0 | -0.09% | $-0.05 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-31T16:14 | NEARUSDT | surge | 4.479 | 4.361 | -2.63% |
| 2026-10-31T18:28 | INJUSDT | surge | 7.374 | 7.223 | -2.05% |
| 2026-10-31T22:16 | BATUSDT | surge | 0.1421 | 0.1387 | -2.39% |
| 2026-10-31T22:16 | AEROUSDT | surge | 0.6453 | 0.6358 | -1.47% |
| 2026-11-01T04:58 | RADUSDT | bottom | 0.242 | 0.242 | +0.00% |
| 2026-11-01T06:06 | INTWBUSDT | surge | 7.52 | 7.51 | -0.13% |
| 2026-11-01T06:23 | INTCBUSDT | surge | 66.03 | 65.83 | -0.30% |
| 2026-11-01T15:06 | INITUSDT | surge | 0.19352 | 0.18658 | -3.59% |
| 2026-11-01T15:23 | HEMIUSDT | surge | 0.00498 | 0.00495 | -0.60% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
