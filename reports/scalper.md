# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-01T03:17:47+00:00 · runs 4911 · equity **$595.90** (-40.41%) · cash $0.00 · open 10/10 · round trips 1719

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-403.32 · worst day $-50.94 · trades/day 29.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1496 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 223 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-31T15:41 | ARBUSDT | bottom | TARGET | 10.5 | +2.75% | $+1.53 |
| 2026-10-31T15:24 | MORPHOUSDT | surge | TARGET | 0.0 | +2.75% | $+1.66 |
| 2026-10-31T15:07 | MORPHOUSDT | surge | TARGET | 2.0 | +2.75% | $+1.61 |
| 2026-10-31T14:30 | ZBTUSDT | surge | TARGET | 0.5 | +2.75% | $+1.61 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-31T08:58 | LTCUSDT | bottom | 54.62 | 55.83 | +2.22% |
| 2026-10-31T15:24 | AAVEUSDT | surge | 135.29 | 137.69 | +1.77% |
| 2026-10-31T16:14 | ETHFIUSDT | surge | 0.6381 | 0.627 | -1.74% |
| 2026-10-31T16:14 | NEARUSDT | surge | 4.479 | 4.447 | -0.71% |
| 2026-10-31T18:28 | INJUSDT | surge | 7.374 | 7.265 | -1.48% |
| 2026-10-31T19:18 | MORPHOUSDT | surge | 2.401 | 2.343 | -2.42% |
| 2026-10-31T22:16 | BATUSDT | surge | 0.1421 | 0.141 | -0.77% |
| 2026-10-31T22:16 | AEROUSDT | surge | 0.6453 | 0.6466 | +0.20% |
| 2026-11-01T00:00 | FETUSDT | bottom | 0.1596 | 0.1619 | +1.44% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
