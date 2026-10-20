# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-20T09:01:47+00:00 · runs 3881 · equity **$663.43** (-33.66%) · cash $0.00 · open 10/10 · round trips 1417

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-334.76 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1239 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 178 | 45% | -0.36% | 39% | 42% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-19T15:50 | MRVLBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.74 |
| 2026-10-19T15:33 | MUBUSDT | surge | TARGET | 13.5 | +2.75% | $+1.79 |
| 2026-10-19T15:16 | KATUSDT | surge | STOP | 1.0 | -3.25% | $-2.05 |
| 2026-10-19T13:54 | NBISBUSDT | surge | STOP | 1.8 | -3.25% | $-2.18 |
| 2026-10-19T13:54 | AAOIBUSDT | surge | STOP | 10.2 | -3.25% | $-2.07 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-19T10:46 | ATOMUSDT | surge | 1.743 | 1.73 | -0.75% |
| 2026-10-19T13:37 | BNCBUSDT | surge | 4.7 | 4.72 | +0.43% |
| 2026-10-19T15:16 | GOOGLBUSDT | surge | 346.27 | 344.07 | -0.64% |
| 2026-10-19T19:53 | BEAMXUSDT | surge | 0.003044 | 0.003086 | +1.38% |
| 2026-10-19T20:27 | HBARUSDT | bottom | 0.08232 | 0.08278 | +0.56% |
| 2026-10-20T00:32 | NEARUSDT | bottom | 4.84 | 4.742 | -2.02% |
| 2026-10-20T00:32 | TRUMPUSDT | bottom | 1.691 | 1.685 | -0.35% |
| 2026-10-20T03:25 | SKYUSDT | surge | 0.07196 | 0.07153 | -0.60% |
| 2026-10-20T05:18 | WLDUSDT | surge | 0.5424 | 0.5375 | -0.90% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
