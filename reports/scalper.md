# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-15T10:33:26+00:00 · runs 867 · equity **$881.81** (-11.82%) · cash $85.80 · open 9/10 · round trips 311

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.38%/trade · realized $-113.56 · worst day $-50.94 · trades/day 28.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 239 | 47% | -0.36% | 44% | 48% | 8% |
| bottom | 72 | 43% | -0.42% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-15T09:59 | COTIUSDT | surge | STOP | 0.5 | -3.25% | $-2.83 |
| 2026-09-15T09:09 | COTIUSDT | surge | TARGET | 1.5 | +2.75% | $+2.22 |
| 2026-09-15T08:36 | SAGAUSDT | surge | STOP | 0.0 | -3.25% | $-3.07 |
| 2026-09-15T08:03 | VANAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.53 |
| 2026-09-15T07:59 | XLMUSDT | surge | STOP | 13.8 | -3.25% | $-3.09 |
| 2026-09-15T07:26 | CAKEUSDT | surge | STOP | 18.0 | -3.25% | $-2.71 |
| 2026-09-15T04:26 | REDUSDT | surge | TARGET | 0.5 | +2.75% | $+2.32 |
| 2026-09-15T04:09 | MSTRBUSDT | surge | STOP | 10.0 | -3.25% | $-3.11 |
| 2026-09-15T03:37 | LAUSDT | surge | STOP | 0.0 | -3.25% | $-2.91 |
| 2026-09-15T03:37 | UNIUSDT | surge | STOP | 1.2 | -3.25% | $-2.79 |
| 2026-09-15T03:37 | SAGAUSDT | surge | STOP | 3.0 | -3.25% | $-2.81 |
| 2026-09-15T03:20 | TREEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.38 |
| 2026-09-15T03:20 | OPUSDT | surge | STOP | 7.2 | -3.25% | $-3.02 |
| 2026-09-15T02:31 | AEROUSDT | surge | TIME | 24.0 | -1.63% | $-1.44 |
| 2026-09-15T02:09 | FLOKIUSDT | surge | STOP | 5.2 | -3.25% | $-2.88 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-14T16:03 | SPCXBUSDT | surge | 150.77 | 148.76 | -1.33% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 660.6 | -0.47% |
| 2026-09-15T03:20 | JSTUSDT | surge | 0.11522 | 0.11531 | +0.08% |
| 2026-09-15T03:37 | BANKUSDT | bottom | 0.0274 | 0.0275 | +0.36% |
| 2026-09-15T03:37 | GRAMUSDT | bottom | 1.341 | 1.341 | +0.00% |
| 2026-09-15T04:09 | DODOUSDT | surge | 0.01822 | 0.01806 | -0.88% |
| 2026-09-15T04:26 | FETUSDT | bottom | 0.1619 | 0.1579 | -2.47% |
| 2026-09-15T10:31 | TUTUSDT | surge | 0.01948 | 0.01941 | -0.36% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
