# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-01T16:53:52+00:00 · runs 4960 · equity **$588.19** (-41.18%) · cash $0.00 · open 10/10 · round trips 1738

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-411.04 · worst day $-50.94 · trades/day 30.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1513 | 49% | -0.28% | 46% | 47% | 7% |
| bottom | 225 | 43% | -0.49% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-01T16:51 | INJUSDT | surge | STOP | 22.2 | -3.25% | $-1.85 |
| 2026-11-01T16:34 | HEMIUSDT | surge | STOP | 1.0 | -3.25% | $-1.71 |
| 2026-11-01T15:59 | BATUSDT | surge | STOP | 17.2 | -3.25% | $-1.84 |
| 2026-11-01T15:59 | NEARUSDT | surge | STOP | 23.5 | -3.25% | $-1.84 |
| 2026-11-01T15:41 | INITUSDT | surge | STOP | 0.2 | -3.25% | $-1.81 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-31T22:16 | AEROUSDT | surge | 0.6453 | 0.6362 | -1.41% |
| 2026-11-01T04:58 | RADUSDT | bottom | 0.242 | 0.243 | +0.41% |
| 2026-11-01T06:06 | INTWBUSDT | surge | 7.52 | 7.56 | +0.53% |
| 2026-11-01T06:23 | INTCBUSDT | surge | 66.03 | 66.18 | +0.23% |
| 2026-11-01T15:41 | LDOUSDT | surge | 0.3493 | 0.344 | -1.52% |
| 2026-11-01T15:59 | PHAUSDT | surge | 0.0427 | 0.0417 | -2.34% |
| 2026-11-01T15:59 | BEAMXUSDT | bottom | 0.004721 | 0.004818 | +2.05% |
| 2026-11-01T16:34 | NIGHTUSDT | surge | 0.04234 | 0.04252 | +0.43% |
| 2026-11-01T16:51 | ONDOUSDT | bottom | 0.4048 | 0.4055 | +0.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
