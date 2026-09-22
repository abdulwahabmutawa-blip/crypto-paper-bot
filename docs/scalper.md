# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-22T18:02:55+00:00 · runs 1506 · equity **$963.34** (-3.67%) · cash $0.00 · open 10/10 · round trips 550

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.07%/trade · realized $-42.23 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 459 | 54% | +0.02% | 50% | 42% | 8% |
| bottom | 91 | 42% | -0.53% | 40% | 46% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-22T17:43 | QQQBUSDT | surge | TIME | 24.0 | +0.62% | $+0.58 |
| 2026-09-22T16:49 | GIGGLEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.63 |
| 2026-09-22T16:13 | PROVEUSDT | bottom | STOP | 9.5 | -3.25% | $-3.21 |
| 2026-09-22T16:13 | AMDBUSDT | surge | TIME | 24.0 | +1.08% | $+1.02 |
| 2026-09-22T15:56 | ETCUSDT | surge | TARGET | 0.2 | +2.75% | $+2.65 |
| 2026-09-22T15:56 | TSLABUSDT | surge | TIME | 24.0 | +0.19% | $+0.16 |
| 2026-09-22T15:20 | KITEUSDT | surge | TARGET | 4.5 | +2.75% | $+2.58 |
| 2026-09-22T15:02 | MARSCOINUSDT | surge | STOP | 0.0 | -3.25% | $-3.22 |
| 2026-09-22T14:44 | TSTUSDT | surge | STOP | 1.0 | -3.25% | $-3.38 |
| 2026-09-22T14:44 | TUTUSDT | surge | STOP | 1.5 | -3.25% | $-3.29 |
| 2026-09-22T13:15 | MARSCOINUSDT | surge | TARGET | 0.2 | +2.75% | $+2.78 |
| 2026-09-22T12:53 | UNIUSDT | bottom | TARGET | 0.5 | +2.75% | $+2.72 |
| 2026-09-22T12:53 | QNTUSDT | surge | TARGET | 0.5 | +2.75% | $+2.72 |
| 2026-09-22T12:53 | AVAUSDT | surge | TARGET | 1.0 | +2.75% | $+2.73 |
| 2026-09-22T12:53 | BCHUSDT | surge | TARGET | 22.2 | +2.75% | $+2.65 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-22T12:53 | SPCXBUSDT | bottom | 152.07 | 153.55 | +0.97% |
| 2026-09-22T12:53 | ONDOUSDT | bottom | 0.4304 | 0.4316 | +0.28% |
| 2026-09-22T14:44 | SKHYBUSDT | surge | 194.89 | 193.74 | -0.59% |
| 2026-09-22T15:02 | SNDKBUSDT | surge | 1858.77 | 1884.3 | +1.37% |
| 2026-09-22T15:56 | MUBUSDT | surge | 1074.98 | 1081.53 | +0.61% |
| 2026-09-22T15:56 | QNTUSDT | surge | 72.87 | 72.83 | -0.05% |
| 2026-09-22T16:13 | KORUBUSDT | surge | 22.87 | 23.53 | +2.89% |
| 2026-09-22T16:49 | ETCUSDT | surge | 9.15 | 9.23 | +0.87% |
| 2026-09-22T17:43 | TRBUSDT | surge | 20.11 | 19.99 | -0.60% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
