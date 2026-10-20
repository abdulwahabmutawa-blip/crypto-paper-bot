# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-20T15:19:59+00:00 · runs 3905 · equity **$671.49** (-32.85%) · cash $0.00 · open 10/10 · round trips 1431

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-324.31 · worst day $-50.94 · trades/day 31.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1249 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-20T10:53 | BEAMXUSDT | surge | TARGET | 14.8 | +2.75% | $+1.76 |
| 2026-10-20T10:21 | NEARUSDT | bottom | STOP | 9.5 | -3.25% | $-2.09 |
| 2026-10-20T05:18 | SUSDT | surge | STOP | 9.2 | -3.25% | $-2.08 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-19T15:16 | GOOGLBUSDT | surge | 346.27 | 342.5 | -1.09% |
| 2026-10-20T10:21 | IOUSDT | surge | 0.1632 | 0.1633 | +0.06% |
| 2026-10-20T13:03 | BEAMXUSDT | surge | 0.003193 | 0.003126 | -2.10% |
| 2026-10-20T14:29 | RSRUSDT | surge | 0.00192 | 0.001918 | -0.10% |
| 2026-10-20T14:29 | ZROUSDT | surge | 1.986 | 1.953 | -1.66% |
| 2026-10-20T14:29 | CRCLBUSDT | surge | 85.2 | 85.49 | +0.34% |
| 2026-10-20T14:45 | ICPUSDT | surge | 2.938 | 2.874 | -2.18% |
| 2026-10-20T15:18 | COMPUSDT | surge | 24.3 | 24.23 | -0.29% |
| 2026-10-20T15:18 | THETAUSDT | surge | 0.2111 | 0.2124 | +0.62% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
