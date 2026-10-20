# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-20T03:59:08+00:00 · runs 3862 · equity **$669.85** (-33.01%) · cash $-0.00 · open 10/10 · round trips 1416

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-332.68 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1238 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 178 | 45% | -0.36% | 39% | 42% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-19T13:37 | SKHYBUSDT | surge | TARGET | 11.5 | +2.75% | $+1.79 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-19T10:46 | ATOMUSDT | surge | 1.743 | 1.775 | +1.84% |
| 2026-10-19T13:37 | BNCBUSDT | surge | 4.7 | 4.67 | -0.64% |
| 2026-10-19T15:16 | GOOGLBUSDT | surge | 346.27 | 345.29 | -0.28% |
| 2026-10-19T19:53 | SUSDT | surge | 0.05826 | 0.0572 | -1.82% |
| 2026-10-19T19:53 | BEAMXUSDT | surge | 0.003044 | 0.00307 | +0.85% |
| 2026-10-19T20:27 | HBARUSDT | bottom | 0.08232 | 0.0837 | +1.68% |
| 2026-10-20T00:32 | NEARUSDT | bottom | 4.84 | 4.867 | +0.56% |
| 2026-10-20T00:32 | TRUMPUSDT | bottom | 1.691 | 1.703 | +0.71% |
| 2026-10-20T03:25 | SKYUSDT | surge | 0.07196 | 0.07263 | +0.93% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
