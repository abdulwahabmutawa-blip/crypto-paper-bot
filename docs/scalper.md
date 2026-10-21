# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-21T10:42:50+00:00 · runs 3978 · equity **$679.08** (-32.09%) · cash $0.00 · open 10/10 · round trips 1442

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-326.98 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1260 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-21T08:14 | CFXUSDT | surge | TARGET | 16.2 | +2.75% | $+1.76 |
| 2026-10-21T02:42 | RAYUSDT | surge | STOP | 7.8 | -3.25% | $-2.16 |
| 2026-10-20T20:52 | REZUSDT | surge | TARGET | 4.0 | +2.75% | $+1.89 |
| 2026-10-20T18:36 | ACEUSDT | surge | STOP | 1.2 | -3.25% | $-2.23 |
| 2026-10-20T17:31 | IOUSDT | surge | TARGET | 7.0 | +2.75% | $+1.71 |
| 2026-10-20T17:14 | THETAUSDT | surge | TARGET | 1.8 | +2.75% | $+1.83 |
| 2026-10-20T16:41 | COMPUSDT | surge | TARGET | 1.0 | +2.75% | $+1.83 |
| 2026-10-20T16:25 | BEAMXUSDT | surge | STOP | 3.0 | -3.25% | $-2.06 |
| 2026-10-20T15:34 | ICPUSDT | surge | STOP | 0.5 | -3.25% | $-2.25 |
| 2026-10-20T15:34 | ZROUSDT | surge | STOP | 1.0 | -3.25% | $-2.17 |
| 2026-10-20T15:34 | GOOGLBUSDT | surge | TIME | 24.0 | -1.36% | $-0.83 |
| 2026-10-20T15:18 | RENDERUSDT | surge | STOP | 0.2 | -3.25% | $-2.25 |
| 2026-10-20T15:18 | TIAUSDT | surge | STOP | 2.2 | -3.25% | $-2.23 |
| 2026-10-20T14:45 | VELODROMEUSDT | surge | TARGET | 0.0 | +2.75% | $+1.83 |
| 2026-10-20T14:45 | BNCBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.87 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-20T14:29 | RSRUSDT | surge | 0.00192 | 0.001945 | +1.30% |
| 2026-10-20T14:29 | CRCLBUSDT | surge | 85.2 | 86.67 | +1.73% |
| 2026-10-20T15:34 | TSLABUSDT | surge | 374.56 | 379.72 | +1.38% |
| 2026-10-20T15:34 | JTOUSDT | surge | 0.4772 | 0.4782 | +0.21% |
| 2026-10-20T16:25 | BONKUSDT | surge | 3.04e-06 | 3.1e-06 | +1.97% |
| 2026-10-20T17:31 | DOGEUSDT | surge | 0.08115 | 0.08196 | +1.00% |
| 2026-10-20T20:52 | PENGUUSDT | surge | 0.00803 | 0.008149 | +1.48% |
| 2026-10-21T02:42 | SPCXBUSDT | surge | 161.76 | 160.26 | -0.93% |
| 2026-10-21T08:14 | BNCBUSDT | surge | 5.44 | 5.5 | +1.10% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
