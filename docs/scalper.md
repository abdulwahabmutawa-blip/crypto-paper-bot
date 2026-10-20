# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-20T15:36:20+00:00 · runs 3906 · equity **$668.92** (-33.11%) · cash $0.00 · open 10/10 · round trips 1434

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-329.55 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1252 | 49% | -0.27% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-20T15:34 | ICPUSDT | surge | STOP | 0.5 | -3.25% | $-2.25 |
| 2026-10-20T15:34 | ZROUSDT | surge | STOP | 1.0 | -3.25% | $-2.17 |
| 2026-10-20T15:34 | GOOGLBUSDT | surge | TIME | 24.0 | -1.36% | $-0.83 |
| 2026-10-20T15:18 | RENDERUSDT | surge | STOP | 0.2 | -3.25% | $-2.25 |
| 2026-10-20T15:18 | TIAUSDT | surge | STOP | 2.2 | -3.25% | $-2.23 |
| 2026-10-20T14:45 | VELODROMEUSDT | surge | TARGET | 0.0 | +2.75% | $+1.83 |
| 2026-10-20T14:45 | BNCBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.87 |
| 2026-10-20T14:29 | SNDKBUSDT | bottom | TARGET | 3.2 | +2.75% | $+1.81 |
| 2026-10-20T14:29 | SKYUSDT | surge | TARGET | 11.0 | +2.75% | $+1.74 |
| 2026-10-20T14:29 | TRUMPUSDT | bottom | TARGET | 13.5 | +2.75% | $+1.77 |
| 2026-10-20T14:29 | HBARUSDT | bottom | TARGET | 17.8 | +2.75% | $+1.83 |
| 2026-10-20T13:36 | REZUSDT | surge | TARGET | 2.2 | +2.75% | $+1.82 |
| 2026-10-20T13:03 | WLDUSDT | surge | TARGET | 7.5 | +2.75% | $+1.70 |
| 2026-10-20T12:47 | BNCBUSDT | surge | TARGET | 23.0 | +2.75% | $+1.84 |
| 2026-10-20T11:09 | ATOMUSDT | surge | TIME | 24.0 | -1.40% | $-0.94 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-20T10:21 | IOUSDT | surge | 0.1632 | 0.1634 | +0.12% |
| 2026-10-20T13:03 | BEAMXUSDT | surge | 0.003193 | 0.003119 | -2.32% |
| 2026-10-20T14:29 | RSRUSDT | surge | 0.00192 | 0.00191 | -0.52% |
| 2026-10-20T14:29 | CRCLBUSDT | surge | 85.2 | 85.19 | -0.01% |
| 2026-10-20T15:18 | COMPUSDT | surge | 24.3 | 24.24 | -0.25% |
| 2026-10-20T15:18 | THETAUSDT | surge | 0.2111 | 0.2134 | +1.09% |
| 2026-10-20T15:34 | TSLABUSDT | surge | 374.56 | 373.93 | -0.17% |
| 2026-10-20T15:34 | JTOUSDT | surge | 0.4772 | 0.4748 | -0.50% |
| 2026-10-20T15:34 | CFXUSDT | surge | 0.05393 | 0.05401 | +0.15% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
