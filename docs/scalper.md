# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-20T13:21:10+00:00 · runs 3897 · equity **$669.78** (-33.02%) · cash $0.00 · open 10/10 · round trips 1422

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-332.49 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1243 | 49% | -0.27% | 46% | 46% | 7% |
| bottom | 179 | 45% | -0.38% | 39% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-20T13:03 | WLDUSDT | surge | TARGET | 7.5 | +2.75% | $+1.70 |
| 2026-10-20T12:47 | BNCBUSDT | surge | TARGET | 23.0 | +2.75% | $+1.84 |
| 2026-10-20T11:09 | ATOMUSDT | surge | TIME | 24.0 | -1.40% | $-0.94 |
| 2026-10-20T10:53 | BEAMXUSDT | surge | TARGET | 14.8 | +2.75% | $+1.76 |
| 2026-10-20T10:21 | NEARUSDT | bottom | STOP | 9.5 | -3.25% | $-2.09 |
| 2026-10-20T05:18 | SUSDT | surge | STOP | 9.2 | -3.25% | $-2.08 |
| 2026-10-20T03:25 | BMTUSDT | surge | STOP | 0.5 | -3.25% | $-2.12 |
| 2026-10-20T02:36 | TQQQBUSDT | surge | TIME | 24.0 | -0.05% | $-0.03 |
| 2026-10-20T00:32 | WUSDT | surge | STOP | 1.8 | -3.25% | $-2.08 |
| 2026-10-20T00:32 | TSLABUSDT | surge | TIME | 24.0 | +1.84% | $+1.20 |
| 2026-10-19T22:33 | QQQBUSDT | surge | TIME | 24.0 | +0.75% | $+0.48 |
| 2026-10-19T20:27 | BATUSDT | surge | TARGET | 1.5 | +2.75% | $+1.78 |
| 2026-10-19T19:53 | MORPHOUSDT | surge | STOP | 3.8 | -3.25% | $-2.11 |
| 2026-10-19T19:53 | RAYUSDT | surge | STOP | 8.8 | -3.25% | $-2.18 |
| 2026-10-19T18:43 | AMDBUSDT | surge | STOP | 3.0 | -3.25% | $-2.17 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-19T15:16 | GOOGLBUSDT | surge | 346.27 | 343.24 | -0.88% |
| 2026-10-19T20:27 | HBARUSDT | bottom | 0.08232 | 0.08227 | -0.06% |
| 2026-10-20T00:32 | TRUMPUSDT | bottom | 1.691 | 1.696 | +0.30% |
| 2026-10-20T03:25 | SKYUSDT | surge | 0.07196 | 0.07211 | +0.21% |
| 2026-10-20T10:21 | IOUSDT | surge | 0.1632 | 0.1631 | -0.06% |
| 2026-10-20T10:53 | SNDKBUSDT | bottom | 1328.73 | 1341.29 | +0.95% |
| 2026-10-20T11:09 | REZUSDT | surge | 0.003595 | 0.00369 | +2.64% |
| 2026-10-20T12:47 | TIAUSDT | surge | 0.6427 | 0.6357 | -1.09% |
| 2026-10-20T13:03 | BEAMXUSDT | surge | 0.003193 | 0.00324 | +1.47% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
