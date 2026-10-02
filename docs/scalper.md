# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-02T20:34:39+00:00 · runs 2379 · equity **$869.78** (-13.02%) · cash $251.95 · open 7/10 · round trips 917

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-131.31 · worst day $-50.94 · trades/day 32.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 794 | 52% | -0.10% | 49% | 44% | 7% |
| bottom | 123 | 45% | -0.45% | 40% | 46% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02T20:33 | NMRUSDT | surge | TARGET | 0.2 | +2.75% | $+2.29 |
| 2026-10-02T18:54 | PEPEUSDT | bottom | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | FETUSDT | bottom | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | VTHOUSDT | surge | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | CHIPUSDT | surge | STOP | 6.0 | -3.25% | $-2.90 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-02T13:07 | DODOUSDT | surge | 0.01872 | 0.01844 | -1.50% |
| 2026-10-02T15:29 | TSLABUSDT | surge | 371.22 | 370 | -0.33% |
| 2026-10-02T15:52 | SPCXBUSDT | surge | 157.12 | 158.78 | +1.06% |
| 2026-10-02T17:48 | CRCLBUSDT | bottom | 80.95 | 81.6 | +0.80% |
| 2026-10-02T18:54 | XPLUSDT | bottom | 0.09145 | 0.09202 | +0.62% |
| 2026-10-02T18:54 | BNBUSDT | bottom | 761.25 | 765.86 | +0.61% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
