# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-02T18:39:15+00:00 · runs 2372 · equity **$869.38** (-13.06%) · cash $84.01 · open 9/10 · round trips 912

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.13%/trade · realized $-122.44 · worst day $-50.94 · trades/day 32.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 791 | 52% | -0.09% | 49% | 44% | 7% |
| bottom | 121 | 45% | -0.40% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02T18:37 | DYDXUSDT | surge | STOP | 18.8 | -3.25% | $-2.82 |
| 2026-10-02T17:48 | WLDUSDT | surge | STOP | 0.8 | -3.25% | $-2.85 |
| 2026-10-02T17:48 | SKYUSDT | surge | STOP | 1.5 | -3.25% | $-2.62 |
| 2026-10-02T17:48 | CVXUSDT | surge | STOP | 11.2 | -3.25% | $-2.98 |
| 2026-10-02T17:48 | PLUMEUSDT | bottom | STOP | 16.8 | -3.25% | $-2.93 |
| 2026-10-02T16:58 | TRUMPUSDT | surge | STOP | 3.8 | -3.25% | $-2.94 |
| 2026-10-02T16:08 | BATUSDT | surge | STOP | 0.8 | -3.25% | $-2.70 |
| 2026-10-02T15:52 | SKYUSDT | surge | TARGET | 2.2 | +2.75% | $+2.62 |
| 2026-10-02T15:29 | MAGICUSDT | surge | TARGET | 2.5 | +2.75% | $+2.46 |
| 2026-10-02T15:11 | GALAUSDT | surge | STOP | 1.2 | -3.25% | $-2.80 |
| 2026-10-02T13:42 | BNCBUSDT | surge | TIME | 24.0 | +1.57% | $+1.33 |
| 2026-10-02T13:25 | GALAUSDT | surge | TARGET | 1.0 | +2.75% | $+2.55 |
| 2026-10-02T13:07 | AXSUSDT | surge | STOP | 0.8 | -3.25% | $-3.01 |
| 2026-10-02T12:49 | SKHYBUSDT | surge | TARGET | 19.0 | +2.75% | $+2.42 |
| 2026-10-02T12:31 | ENJUSDT | surge | TARGET | 0.0 | +2.75% | $+2.55 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-02T12:31 | CHIPUSDT | surge | 0.04492 | 0.04356 | -3.03% |
| 2026-10-02T13:07 | DODOUSDT | surge | 0.01872 | 0.01867 | -0.27% |
| 2026-10-02T15:29 | TSLABUSDT | surge | 371.22 | 370.99 | -0.06% |
| 2026-10-02T15:52 | SPCXBUSDT | surge | 157.12 | 158.68 | +0.99% |
| 2026-10-02T17:48 | VTHOUSDT | surge | 0.000686 | 0.000668 | -2.62% |
| 2026-10-02T17:48 | CRCLBUSDT | bottom | 80.95 | 80.63 | -0.40% |
| 2026-10-02T17:48 | FETUSDT | bottom | 0.2253 | 0.2194 | -2.62% |
| 2026-10-02T17:48 | PEPEUSDT | bottom | 4.29e-06 | 4.22e-06 | -1.63% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
