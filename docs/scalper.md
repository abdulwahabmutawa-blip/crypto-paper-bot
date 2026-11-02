# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-02T19:11:59+00:00 · runs 5040 · equity **$565.40** (-43.46%) · cash $54.11 · open 9/10 · round trips 1763

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-429.10 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1533 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 230 | 43% | -0.51% | 37% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-02T19:10 | HOTUSDT | surge | TARGET | 0.2 | +2.75% | $+1.49 |
| 2026-11-02T19:10 | BEAMXUSDT | bottom | STOP | 0.8 | -3.25% | $-1.76 |
| 2026-11-02T18:05 | SOXSBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.54 |
| 2026-11-02T18:05 | SEIUSDT | surge | STOP | 18.5 | -3.25% | $-1.71 |
| 2026-11-02T17:16 | DRAMBUSDT | surge | STOP | 15.5 | -3.25% | $-1.88 |
| 2026-11-02T16:59 | MEGAUSDT | surge | STOP | 0.8 | -3.25% | $-1.60 |
| 2026-11-02T16:59 | MITOUSDT | surge | TARGET | 2.2 | +2.75% | $+1.47 |
| 2026-11-02T16:59 | KORUBUSDT | surge | STOP | 8.0 | -3.25% | $-1.86 |
| 2026-11-02T16:59 | CRCLBUSDT | surge | STOP | 9.5 | -3.25% | $-2.05 |
| 2026-11-02T16:59 | SKHYBUSDT | surge | STOP | 15.2 | -3.25% | $-1.81 |
| 2026-11-02T16:59 | CELOUSDT | bottom | STOP | 22.8 | -3.25% | $-1.83 |
| 2026-11-02T12:26 | SOXLBUSDT | surge | STOP | 7.2 | -3.25% | $-1.66 |
| 2026-11-02T10:13 | ONDOUSDT | bottom | STOP | 17.2 | -3.25% | $-1.79 |
| 2026-11-02T07:11 | NIGHTUSDT | surge | STOP | 14.2 | -3.25% | $-1.65 |
| 2026-11-02T06:35 | INTCBUSDT | surge | TIME | 24.0 | +0.51% | $+0.29 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-02T07:11 | PROMUSDT | bottom | 5.468 | 5.426 | -0.77% |
| 2026-11-02T16:59 | TSLABUSDT | surge | 410.69 | 406.79 | -0.95% |
| 2026-11-02T16:59 | BABABUSDT | surge | 103.32 | 102.66 | -0.64% |
| 2026-11-02T16:59 | MSTRBUSDT | surge | 136.3 | 132.57 | -2.74% |
| 2026-11-02T16:59 | SPCXBUSDT | surge | 140.88 | 138.53 | -1.67% |
| 2026-11-02T16:59 | COWUSDT | surge | 0.1187 | 0.1174 | -1.10% |
| 2026-11-02T16:59 | MUBUSDT | bottom | 861.83 | 844.69 | -1.99% |
| 2026-11-02T19:10 | TQQQBUSDT | bottom | 61.48 | 61.29 | -0.31% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
