# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-03T13:46:17+00:00 · runs 2442 · equity **$862.72** (-13.73%) · cash $167.25 · open 8/10 · round trips 924

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-139.11 · worst day $-50.94 · trades/day 31.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 800 | 52% | -0.11% | 49% | 44% | 7% |
| bottom | 124 | 45% | -0.42% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-03T13:27 | SYNUSDT | surge | STOP | 5.2 | -3.25% | $-2.65 |
| 2026-10-03T13:27 | DODOUSDT | surge | TIME | 24.0 | -1.64% | $-1.47 |
| 2026-10-03T12:00 | RAYUSDT | surge | TARGET | 3.0 | +2.75% | $+2.17 |
| 2026-10-03T08:31 | LPTUSDT | surge | STOP | 2.8 | -3.25% | $-2.65 |
| 2026-10-03T07:54 | AXSUSDT | surge | STOP | 4.0 | -3.25% | $-2.74 |
| 2026-10-03T04:21 | PYTHUSDT | surge | STOP | 2.8 | -3.25% | $-2.74 |
| 2026-10-03T01:28 | XPLUSDT | bottom | TARGET | 6.2 | +2.75% | $+2.29 |
| 2026-10-02T20:33 | NMRUSDT | surge | TARGET | 0.2 | +2.75% | $+2.29 |
| 2026-10-02T18:54 | PEPEUSDT | bottom | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | FETUSDT | bottom | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | VTHOUSDT | surge | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | CHIPUSDT | surge | STOP | 6.0 | -3.25% | $-2.90 |
| 2026-10-02T18:37 | DYDXUSDT | surge | STOP | 18.8 | -3.25% | $-2.82 |
| 2026-10-02T17:48 | WLDUSDT | surge | STOP | 0.8 | -3.25% | $-2.85 |
| 2026-10-02T17:48 | SKYUSDT | surge | STOP | 1.5 | -3.25% | $-2.62 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-02T15:29 | TSLABUSDT | surge | 371.22 | 370.94 | -0.08% |
| 2026-10-02T15:52 | SPCXBUSDT | surge | 157.12 | 159.11 | +1.27% |
| 2026-10-02T17:48 | CRCLBUSDT | bottom | 80.95 | 82.17 | +1.51% |
| 2026-10-02T18:54 | BNBUSDT | bottom | 761.25 | 773.54 | +1.61% |
| 2026-10-03T01:28 | SNDKBUSDT | bottom | 1718.8 | 1717.26 | -0.09% |
| 2026-10-03T03:31 | INJUSDT | surge | 7.685 | 7.615 | -0.91% |
| 2026-10-03T12:34 | ARUSDT | surge | 4.646 | 4.582 | -1.38% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
