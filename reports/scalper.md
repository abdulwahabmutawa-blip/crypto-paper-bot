# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-19T03:01:54+00:00 · runs 3772 · equity **$673.03** (-32.70%) · cash $-0.00 · open 10/10 · round trips 1397

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-331.22 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1219 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 178 | 45% | -0.36% | 39% | 42% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-19T02:24 | TQQQBUSDT | surge | TARGET | 3.8 | +2.75% | $+1.75 |
| 2026-10-19T01:49 | SKHYBUSDT | surge | TARGET | 2.5 | +2.75% | $+1.80 |
| 2026-10-19T01:49 | TRXUSDT | bottom | TIME | 24.0 | -0.61% | $-0.39 |
| 2026-10-19T01:32 | EWYBUSDT | surge | TARGET | 3.0 | +2.75% | $+1.75 |
| 2026-10-19T01:14 | INTCBUSDT | surge | TARGET | 2.8 | +2.75% | $+1.75 |
| 2026-10-19T00:21 | SOXLBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.75 |
| 2026-10-19T00:21 | KORUBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.75 |
| 2026-10-18T23:11 | RUNEUSDT | surge | TARGET | 0.5 | +2.75% | $+1.75 |
| 2026-10-18T22:18 | SANDUSDT | bottom | TARGET | 0.5 | +2.75% | $+1.75 |
| 2026-10-18T22:18 | UNIUSDT | bottom | TARGET | 1.5 | +2.75% | $+1.73 |
| 2026-10-18T22:18 | SOXSBUSDT | surge | STOP | 3.5 | -3.25% | $-2.02 |
| 2026-10-18T21:30 | ALTUSDT | bottom | TARGET | 11.0 | +2.75% | $+1.77 |
| 2026-10-18T20:37 | RWUSDUSDT | bottom | TIME | 24.0 | -0.24% | $-0.17 |
| 2026-10-18T19:44 | AMPUSDT | surge | STOP | 0.2 | -3.25% | $-2.02 |
| 2026-10-18T19:09 | NXPCUSDT | surge | STOP | 0.0 | -3.25% | $-2.02 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-18T03:05 | MSTRBUSDT | surge | 137.28 | 140.76 | +2.53% |
| 2026-10-18T22:18 | QQQBUSDT | surge | 713.34 | 719.37 | +0.85% |
| 2026-10-19T00:21 | TSLABUSDT | surge | 359.63 | 358.01 | -0.45% |
| 2026-10-19T00:21 | DRAMBUSDT | surge | 47.26 | 47.76 | +1.06% |
| 2026-10-19T01:14 | NBISBUSDT | surge | 170 | 172.36 | +1.39% |
| 2026-10-19T01:32 | EWYBUSDT | surge | 154.75 | 155.82 | +0.69% |
| 2026-10-19T01:49 | SKHYBUSDT | surge | 139.41 | 139.81 | +0.29% |
| 2026-10-19T01:49 | MUBUSDT | surge | 897.99 | 898.41 | +0.05% |
| 2026-10-19T02:24 | TQQQBUSDT | surge | 70.62 | 70.8 | +0.25% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
