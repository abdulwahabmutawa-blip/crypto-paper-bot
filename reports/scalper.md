# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-01T06:08:29+00:00 · runs 4921 · equity **$600.97** (-39.90%) · cash $0.00 · open 10/10 · round trips 1723

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-400.44 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1499 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 224 | 43% | -0.50% | 37% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-31T15:57 | ZROUSDT | surge | TARGET | 6.0 | +2.75% | $+1.53 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-31T16:14 | ETHFIUSDT | surge | 0.6381 | 0.6336 | -0.71% |
| 2026-10-31T16:14 | NEARUSDT | surge | 4.479 | 4.395 | -1.88% |
| 2026-10-31T18:28 | INJUSDT | surge | 7.374 | 7.402 | +0.38% |
| 2026-10-31T22:16 | BATUSDT | surge | 0.1421 | 0.1411 | -0.70% |
| 2026-10-31T22:16 | AEROUSDT | surge | 0.6453 | 0.6473 | +0.31% |
| 2026-11-01T00:00 | FETUSDT | bottom | 0.1596 | 0.1644 | +3.01% |
| 2026-11-01T04:58 | RADUSDT | bottom | 0.242 | 0.243 | +0.41% |
| 2026-11-01T05:49 | KITEUSDT | surge | 0.1186 | 0.12 | +1.18% |
| 2026-11-01T06:06 | INTWBUSDT | surge | 7.52 | 7.56 | +0.53% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
