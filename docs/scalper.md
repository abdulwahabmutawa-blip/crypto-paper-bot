# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-24T00:27:40+00:00 · runs 6663 · equity **$489.30** (-51.07%) · cash $88.56 · open 8/10 · round trips 2182

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-511.96 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1881 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 301 | 44% | -0.45% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-24T00:09 | ALGOUSDT | surge | STOP | 4.2 | -3.25% | $-1.51 |
| 2026-11-24T00:09 | MORPHOUSDT | surge | STOP | 6.0 | -3.25% | $-1.47 |
| 2026-11-24T00:09 | ADAUSDT | surge | STOP | 5.0 | -3.25% | $-1.48 |
| 2026-11-24T00:09 | PENDLEUSDT | surge | STOP | 5.0 | -3.25% | $-1.48 |
| 2026-11-24T00:09 | NILUSDT | surge | STOP | 5.2 | -3.25% | $-1.48 |
| 2026-11-23T17:56 | SPCXBUSDT | surge | STOP | 3.0 | -3.25% | $-1.52 |
| 2026-11-23T17:56 | SHIBUSDT | surge | STOP | 3.2 | -3.25% | $-1.48 |
| 2026-11-23T15:29 | LUNCUSDT | surge | TARGET | 3.0 | +2.75% | $+1.24 |
| 2026-11-23T14:57 | AMZNBUSDT | surge | STOP | 0.0 | -3.25% | $-1.52 |
| 2026-11-23T14:40 | SPCXBUSDT | surge | TARGET | 0.2 | +2.75% | $+1.25 |
| 2026-11-23T14:40 | MORPHOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.25 |
| 2026-11-23T14:24 | MRVLBUSDT | surge | TARGET | 0.0 | +2.75% | $+1.25 |
| 2026-11-23T14:24 | DRAMBUSDT | surge | TARGET | 0.0 | +2.75% | $+1.25 |
| 2026-11-23T14:24 | TSMBUSDT | surge | TARGET | 0.0 | +2.75% | $+1.25 |
| 2026-11-23T14:24 | COINBUSDT | surge | TARGET | 7.8 | +2.75% | $+1.12 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-23T12:16 | GOOGLBUSDT | surge | 279.77 | 284.31 | +1.62% |
| 2026-11-23T14:24 | TRXUSDT | surge | 0.3103 | 0.3109 | +0.19% |
| 2026-11-23T17:56 | METABUSDT | surge | 594.66 | 599.2 | +0.76% |
| 2026-11-23T17:56 | SPYBUSDT | surge | 722.28 | 724.09 | +0.25% |
| 2026-11-24T00:09 | ZECUSDT | bottom | 776.93 | 773.75 | -0.41% |
| 2026-11-24T00:09 | ETHUSDT | bottom | 1710.65 | 1710.29 | -0.02% |
| 2026-11-24T00:09 | PUMPUSDT | bottom | 0.002534 | 0.002544 | +0.39% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
