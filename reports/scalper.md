# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-19T08:47:39+00:00 · runs 1209 · equity **$947.01** (-5.30%) · cash $0.00 · open 10/10 · round trips 417

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-45.02 · worst day $-50.94 · trades/day 27.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 335 | 54% | +0.00% | 50% | 42% | 8% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-19T08:45 | EPICUSDT | surge | TARGET | 1.2 | +2.75% | $+2.95 |
| 2026-09-19T08:27 | HOMEUSDT | surge | STOP | 0.5 | -3.25% | $-3.36 |
| 2026-09-19T07:34 | HOMEUSDT | surge | TARGET | 0.8 | +2.75% | $+2.77 |
| 2026-09-19T07:17 | VETUSDT | surge | TARGET | 0.0 | +2.75% | $+2.88 |
| 2026-09-19T06:59 | VETUSDT | surge | TARGET | 0.5 | +2.75% | $+2.80 |
| 2026-09-19T06:41 | POLUSDT | surge | STOP | 7.8 | -3.25% | $-3.38 |
| 2026-09-19T06:23 | ESPUSDT | surge | TARGET | 0.0 | +2.75% | $+2.72 |
| 2026-09-19T06:06 | MEGAUSDT | surge | STOP | 5.8 | -3.25% | $-3.33 |
| 2026-09-19T04:49 | WUSDT | surge | STOP | 8.5 | -3.25% | $-3.21 |
| 2026-09-19T00:05 | BCHUSDT | surge | STOP | 0.5 | -3.25% | $-3.44 |
| 2026-09-18T22:50 | ZKUSDT | surge | TARGET | 1.5 | +2.75% | $+2.83 |
| 2026-09-18T22:33 | THETAUSDT | surge | TARGET | 9.2 | +2.75% | $+2.79 |
| 2026-09-18T21:40 | ACHUSDT | surge | STOP | 2.2 | -3.25% | $-3.26 |
| 2026-09-18T21:00 | ZAMAUSDT | surge | TARGET | 1.8 | +2.75% | $+2.76 |
| 2026-09-18T20:42 | PROVEUSDT | surge | TARGET | 5.8 | +2.75% | $+2.56 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-18T10:44 | BANKUSDT | surge | 0.0298 | 0.0294 | -1.34% |
| 2026-09-18T11:16 | DODOUSDT | surge | 0.01835 | 0.01821 | -0.76% |
| 2026-09-18T16:52 | MUBUSDT | surge | 993.73 | 1006.67 | +1.30% |
| 2026-09-18T20:06 | SNDKBUSDT | surge | 1790.7 | 1780.08 | -0.59% |
| 2026-09-18T20:42 | SENTUSDT | surge | 0.01781 | 0.01754 | -1.52% |
| 2026-09-18T21:40 | SOXLBUSDT | surge | 123.48 | 120.08 | -2.75% |
| 2026-09-19T04:49 | PROVEUSDT | surge | 0.2182 | 0.2158 | -1.10% |
| 2026-09-19T08:27 | VETUSDT | surge | 0.008627 | 0.008479 | -1.72% |
| 2026-09-19T08:45 | ACEUSDT | surge | 0.1575 | 0.1576 | +0.06% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
