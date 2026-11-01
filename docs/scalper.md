# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-01T06:42:39+00:00 · runs 4923 · equity **$599.09** (-40.09%) · cash $0.00 · open 10/10 · round trips 1724

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-398.91 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1499 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 225 | 43% | -0.49% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-01T06:23 | FETUSDT | bottom | TARGET | 6.0 | +2.75% | $+1.53 |
| 2026-11-01T06:06 | LTCUSDT | bottom | TARGET | 21.0 | +2.75% | $+1.51 |
| 2026-11-01T05:49 | 牛来USDT | surge | TARGET | 1.8 | +2.75% | $+1.47 |
| 2026-11-01T04:58 | AAVEUSDT | surge | TARGET | 13.5 | +2.75% | $+1.70 |
| 2026-11-01T03:50 | MORPHOUSDT | surge | STOP | 8.2 | -3.25% | $-1.79 |
| 2026-11-01T00:00 | PENDLEUSDT | surge | TIME | 24.0 | -0.09% | $-0.05 |
| 2026-10-31T22:16 | BATUSDT | surge | TARGET | 1.8 | +2.75% | $+1.50 |
| 2026-10-31T22:16 | 牛来USDT | surge | TARGET | 2.0 | +2.75% | $+1.52 |
| 2026-10-31T20:25 | MARSCOINUSDT | surge | STOP | 4.0 | -3.25% | $-1.84 |
| 2026-10-31T20:09 | NMRUSDT | surge | STOP | 4.0 | -3.25% | $-1.85 |
| 2026-10-31T19:18 | STRKUSDT | surge | STOP | 3.5 | -3.25% | $-1.85 |
| 2026-10-31T18:28 | QNTUSDT | surge | TARGET | 7.5 | +2.75% | $+1.53 |
| 2026-10-31T16:14 | ZBTUSDT | surge | STOP | 1.5 | -3.25% | $-1.96 |
| 2026-10-31T16:14 | TRXUSDT | bottom | STOP | 7.8 | -3.25% | $-1.81 |
| 2026-10-31T16:14 | TIAUSDT | surge | TARGET | 8.5 | +2.75% | $+1.53 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-31T16:14 | ETHFIUSDT | surge | 0.6381 | 0.6281 | -1.57% |
| 2026-10-31T16:14 | NEARUSDT | surge | 4.479 | 4.383 | -2.14% |
| 2026-10-31T18:28 | INJUSDT | surge | 7.374 | 7.316 | -0.79% |
| 2026-10-31T22:16 | BATUSDT | surge | 0.1421 | 0.1402 | -1.34% |
| 2026-10-31T22:16 | AEROUSDT | surge | 0.6453 | 0.6419 | -0.53% |
| 2026-11-01T04:58 | RADUSDT | bottom | 0.242 | 0.243 | +0.41% |
| 2026-11-01T05:49 | KITEUSDT | surge | 0.1186 | 0.1224 | +3.20% |
| 2026-11-01T06:06 | INTWBUSDT | surge | 7.52 | 7.49 | -0.40% |
| 2026-11-01T06:23 | INTCBUSDT | surge | 66.03 | 65.81 | -0.33% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
