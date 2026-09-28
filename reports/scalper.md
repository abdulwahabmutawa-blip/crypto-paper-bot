# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-28T23:00:21+00:00 · runs 2046 · equity **$909.69** (-9.03%) · cash $0.00 · open 10/10 · round trips 757

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-90.36 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 644 | 53% | -0.06% | 50% | 43% | 7% |
| bottom | 113 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28T21:35 | NMRUSDT | surge | STOP | 0.2 | -3.25% | $-3.01 |
| 2026-09-28T21:01 | LINEAUSDT | surge | STOP | 1.2 | -3.25% | $-3.11 |
| 2026-09-28T19:55 | WUSDT | bottom | STOP | 5.0 | -3.25% | $-2.74 |
| 2026-09-28T19:37 | ALGOUSDT | surge | TARGET | 0.8 | +2.75% | $+2.54 |
| 2026-09-28T19:37 | 牛来USDT | surge | TARGET | 0.5 | +2.75% | $+2.48 |
| 2026-09-28T19:37 | NIGHTUSDT | surge | TARGET | 4.8 | +2.75% | $+2.63 |
| 2026-09-28T19:37 | MSTRBUSDT | bottom | TARGET | 13.8 | +2.75% | $+2.60 |
| 2026-09-28T17:20 | LINKUSDT | surge | TARGET | 0.2 | +2.75% | $+2.48 |
| 2026-09-28T16:47 | LINKUSDT | surge | TARGET | 0.2 | +2.75% | $+2.37 |
| 2026-09-28T16:31 | ADAUSDT | bottom | TARGET | 1.2 | +2.75% | $+2.45 |
| 2026-09-28T15:58 | NMRUSDT | surge | STOP | 0.0 | -3.25% | $-2.90 |
| 2026-09-28T15:09 | ALGOUSDT | surge | STOP | 0.5 | -3.25% | $-2.93 |
| 2026-09-28T15:09 | IOTAUSDT | surge | STOP | 1.8 | -3.25% | $-3.03 |
| 2026-09-28T14:52 | DOTUSDT | bottom | STOP | 1.5 | -3.25% | $-3.03 |
| 2026-09-28T14:36 | HYPEUSDT | bottom | STOP | 22.5 | -3.25% | $-2.84 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-28T12:08 | NVDABUSDT | surge | 227.9 | 229.44 | +0.68% |
| 2026-09-28T12:08 | JSTUSDT | surge | 0.12933 | 0.13005 | +0.56% |
| 2026-09-28T13:14 | PROMUSDT | surge | 6.412 | 6.334 | -1.22% |
| 2026-09-28T15:42 | DODOUSDT | surge | 0.01887 | 0.01874 | -0.69% |
| 2026-09-28T19:37 | ALGOUSDT | surge | 0.1337 | 0.1342 | +0.37% |
| 2026-09-28T19:37 | XLMUSDT | surge | 0.2289 | 0.2251 | -1.66% |
| 2026-09-28T19:37 | RUNEUSDT | surge | 0.785 | 0.772 | -1.66% |
| 2026-09-28T19:55 | LINKUSDT | surge | 15.002 | 15.274 | +1.81% |
| 2026-09-28T21:35 | CRVUSDT | surge | 0.3589 | 0.3669 | +2.23% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
