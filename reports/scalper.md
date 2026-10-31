# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-31T23:45:14+00:00 · runs 4898 · equity **$593.20** (-40.68%) · cash $0.00 · open 10/10 · round trips 1718

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-403.28 · worst day $-50.94 · trades/day 30.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1495 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 223 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-31T22:16 | BATUSDT | surge | TARGET | 1.8 | +2.75% | $+1.50 |
| 2026-10-31T22:16 | 牛来USDT | surge | TARGET | 2.0 | +2.75% | $+1.52 |
| 2026-10-31T20:25 | MARSCOINUSDT | surge | STOP | 4.0 | -3.25% | $-1.84 |
| 2026-10-31T20:09 | NMRUSDT | surge | STOP | 4.0 | -3.25% | $-1.85 |
| 2026-10-31T19:18 | STRKUSDT | surge | STOP | 3.5 | -3.25% | $-1.85 |
| 2026-10-31T18:28 | QNTUSDT | surge | TARGET | 7.5 | +2.75% | $+1.53 |
| 2026-10-31T16:14 | ZBTUSDT | surge | STOP | 1.5 | -3.25% | $-1.96 |
| 2026-10-31T16:14 | TRXUSDT | bottom | STOP | 7.8 | -3.25% | $-1.81 |
| 2026-10-31T16:14 | TIAUSDT | surge | TARGET | 8.5 | +2.75% | $+1.53 |
| 2026-10-31T15:57 | ZROUSDT | surge | TARGET | 6.0 | +2.75% | $+1.53 |
| 2026-10-31T15:41 | ARBUSDT | bottom | TARGET | 10.5 | +2.75% | $+1.53 |
| 2026-10-31T15:24 | MORPHOUSDT | surge | TARGET | 0.0 | +2.75% | $+1.66 |
| 2026-10-31T15:07 | MORPHOUSDT | surge | TARGET | 2.0 | +2.75% | $+1.61 |
| 2026-10-31T14:30 | ZBTUSDT | surge | TARGET | 0.5 | +2.75% | $+1.61 |
| 2026-10-31T13:57 | EDENUSDT | surge | TARGET | 1.5 | +2.75% | $+1.57 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-30T23:46 | PENDLEUSDT | surge | 1.848 | 1.854 | +0.32% |
| 2026-10-31T08:58 | LTCUSDT | bottom | 54.62 | 55.71 | +2.00% |
| 2026-10-31T15:24 | AAVEUSDT | surge | 135.29 | 134.09 | -0.89% |
| 2026-10-31T16:14 | ETHFIUSDT | surge | 0.6381 | 0.6249 | -2.07% |
| 2026-10-31T16:14 | NEARUSDT | surge | 4.479 | 4.438 | -0.92% |
| 2026-10-31T18:28 | INJUSDT | surge | 7.374 | 7.195 | -2.43% |
| 2026-10-31T19:18 | MORPHOUSDT | surge | 2.401 | 2.37 | -1.29% |
| 2026-10-31T22:16 | BATUSDT | surge | 0.1421 | 0.1415 | -0.42% |
| 2026-10-31T22:16 | AEROUSDT | surge | 0.6453 | 0.6427 | -0.40% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
