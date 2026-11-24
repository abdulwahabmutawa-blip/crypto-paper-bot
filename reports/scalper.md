# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-24T05:50:21+00:00 · runs 6683 · equity **$488.87** (-51.11%) · cash $0.00 · open 10/10 · round trips 2185

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-513.62 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1882 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 303 | 43% | -0.47% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-24T04:44 | BABYUSDT | surge | TARGET | 2.5 | +2.75% | $+1.22 |
| 2026-11-24T03:23 | PUMPUSDT | bottom | STOP | 3.0 | -3.25% | $-1.44 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-23T12:16 | GOOGLBUSDT | surge | 279.77 | 285.93 | +2.20% |
| 2026-11-23T14:24 | TRXUSDT | surge | 0.3103 | 0.3091 | -0.39% |
| 2026-11-23T17:56 | METABUSDT | surge | 594.66 | 602.93 | +1.39% |
| 2026-11-23T17:56 | SPYBUSDT | surge | 722.28 | 724.9 | +0.36% |
| 2026-11-24T00:09 | ETHUSDT | bottom | 1710.65 | 1707.91 | -0.16% |
| 2026-11-24T01:14 | BEBUSDT | surge | 171.8 | 169.18 | -1.53% |
| 2026-11-24T02:51 | ZROUSDT | bottom | 1.127 | 1.146 | +1.69% |
| 2026-11-24T03:39 | INJUSDT | bottom | 6.169 | 6.337 | +2.72% |
| 2026-11-24T04:44 | BABYUSDT | surge | 0.00892 | 0.00887 | -0.56% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
