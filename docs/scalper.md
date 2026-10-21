# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-21T11:48:09+00:00 · runs 3982 · equity **$679.06** (-32.09%) · cash $0.00 · open 10/10 · round trips 1444

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-323.48 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1262 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-21T11:46 | BONKUSDT | surge | TARGET | 19.2 | +2.75% | $+1.69 |
| 2026-10-21T11:30 | BNCBUSDT | surge | TARGET | 3.2 | +2.75% | $+1.81 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-20T14:29 | RSRUSDT | surge | 0.00192 | 0.001932 | +0.62% |
| 2026-10-20T14:29 | CRCLBUSDT | surge | 85.2 | 87.01 | +2.12% |
| 2026-10-20T15:34 | TSLABUSDT | surge | 374.56 | 378.71 | +1.11% |
| 2026-10-20T15:34 | JTOUSDT | surge | 0.4772 | 0.479 | +0.38% |
| 2026-10-20T17:31 | DOGEUSDT | surge | 0.08115 | 0.082 | +1.05% |
| 2026-10-20T20:52 | PENGUUSDT | surge | 0.00803 | 0.008123 | +1.16% |
| 2026-10-21T02:42 | SPCXBUSDT | surge | 161.76 | 158.64 | -1.93% |
| 2026-10-21T11:30 | LUMIAUSDT | surge | 0.0894 | 0.0894 | +0.00% |
| 2026-10-21T11:46 | WUSDT | surge | 0.01426 | 0.01415 | -0.77% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
