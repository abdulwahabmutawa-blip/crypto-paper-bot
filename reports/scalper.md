# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-24T02:52:48+00:00 · runs 6672 · equity **$485.47** (-51.45%) · cash $0.00 · open 10/10 · round trips 2183

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-513.40 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1881 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 302 | 43% | -0.46% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-24T02:51 | ZECUSDT | bottom | STOP | 2.5 | -3.25% | $-1.44 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-23T12:16 | GOOGLBUSDT | surge | 279.77 | 284.49 | +1.69% |
| 2026-11-23T14:24 | TRXUSDT | surge | 0.3103 | 0.3094 | -0.29% |
| 2026-11-23T17:56 | METABUSDT | surge | 594.66 | 599.41 | +0.80% |
| 2026-11-23T17:56 | SPYBUSDT | surge | 722.28 | 723.89 | +0.22% |
| 2026-11-24T00:09 | ETHUSDT | bottom | 1710.65 | 1686.88 | -1.39% |
| 2026-11-24T00:09 | PUMPUSDT | bottom | 0.002534 | 0.00249 | -1.74% |
| 2026-11-24T01:14 | BEBUSDT | surge | 171.8 | 169.16 | -1.54% |
| 2026-11-24T01:47 | BABYUSDT | surge | 0.00856 | 0.00853 | -0.35% |
| 2026-11-24T02:51 | ZROUSDT | bottom | 1.127 | 1.127 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
