# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-21T04:38:49+00:00 · runs 3955 · equity **$674.95** (-32.50%) · cash $0.00 · open 10/10 · round trips 1441

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-328.74 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1259 | 49% | -0.27% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-20T14:29 | SNDKBUSDT | bottom | TARGET | 3.2 | +2.75% | $+1.81 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-20T14:29 | RSRUSDT | surge | 0.00192 | 0.001923 | +0.16% |
| 2026-10-20T14:29 | CRCLBUSDT | surge | 85.2 | 85.78 | +0.68% |
| 2026-10-20T15:34 | TSLABUSDT | surge | 374.56 | 379.77 | +1.39% |
| 2026-10-20T15:34 | JTOUSDT | surge | 0.4772 | 0.4807 | +0.73% |
| 2026-10-20T15:34 | CFXUSDT | surge | 0.05393 | 0.05502 | +2.02% |
| 2026-10-20T16:25 | BONKUSDT | surge | 3.04e-06 | 3.06e-06 | +0.66% |
| 2026-10-20T17:31 | DOGEUSDT | surge | 0.08115 | 0.08157 | +0.52% |
| 2026-10-20T20:52 | PENGUUSDT | surge | 0.00803 | 0.008009 | -0.26% |
| 2026-10-21T02:42 | SPCXBUSDT | surge | 161.76 | 161.59 | -0.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
