# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-23T22:46:08+00:00 · runs 4195 · equity **$645.32** (-35.47%) · cash $61.63 · open 9/10 · round trips 1506

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-347.71 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1318 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 188 | 45% | -0.37% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-23T22:44 | ATOMUSDT | surge | STOP | 20.2 | -3.25% | $-2.07 |
| 2026-10-23T22:26 | INITUSDT | surge | STOP | 0.8 | -3.25% | $-2.08 |
| 2026-10-23T22:26 | BNCBUSDT | surge | STOP | 17.5 | -3.25% | $-2.05 |
| 2026-10-23T21:52 | BONKUSDT | surge | STOP | 8.5 | -3.25% | $-2.23 |
| 2026-10-23T21:17 | LAUSDT | surge | STOP | 0.2 | -3.25% | $-2.13 |
| 2026-10-23T21:17 | SENTUSDT | surge | STOP | 3.2 | -3.25% | $-2.17 |
| 2026-10-23T20:53 | LAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.75 |
| 2026-10-23T20:36 | ARKMUSDT | surge | STOP | 0.8 | -3.25% | $-2.14 |
| 2026-10-23T19:43 | ACEUSDT | surge | STOP | 11.0 | -3.25% | $-2.21 |
| 2026-10-23T17:56 | BEAMXUSDT | surge | TARGET | 10.8 | +2.75% | $+1.79 |
| 2026-10-23T15:34 | COTIUSDT | surge | STOP | 0.2 | -3.25% | $-2.11 |
| 2026-10-23T15:11 | COTIUSDT | surge | TARGET | 4.5 | +2.75% | $+1.74 |
| 2026-10-23T13:01 | ARKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.84 |
| 2026-10-23T12:44 | ARKUSDT | surge | TARGET | 1.8 | +2.75% | $+1.79 |
| 2026-10-23T11:06 | STRKUSDT | bottom | STOP | 7.5 | -3.25% | $-2.07 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T02:23 | RUNEUSDT | bottom | 0.642 | 0.628 | -2.18% |
| 2026-10-23T04:15 | BCHUSDT | surge | 284.8 | 281.7 | -1.09% |
| 2026-10-23T11:06 | BOMEUSDT | surge | 0.0006433 | 0.0006368 | -1.01% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 145.95 | -1.75% |
| 2026-10-23T21:17 | WLFIUSDT | surge | 0.0548 | 0.0536 | -2.19% |
| 2026-10-23T21:52 | DOTUSDT | bottom | 1.108 | 1.088 | -1.81% |
| 2026-10-23T22:26 | KMNOUSDT | surge | 0.04211 | 0.04185 | -0.62% |
| 2026-10-23T22:26 | GRAMUSDT | bottom | 1.298 | 1.294 | -0.31% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
