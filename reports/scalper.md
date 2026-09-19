# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-19T06:43:40+00:00 · runs 1202 · equity **$944.20** (-5.58%) · cash $0.00 · open 10/10 · round trips 412

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.12%/trade · realized $-53.05 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 330 | 54% | -0.02% | 49% | 42% | 8% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-18T20:06 | SNXXBUSDT | surge | TARGET | 1.8 | +2.75% | $+2.81 |
| 2026-09-18T20:06 | SNDKBUSDT | surge | TARGET | 4.0 | +2.75% | $+2.47 |
| 2026-09-18T19:13 | LPTUSDT | surge | STOP | 1.0 | -3.25% | $-3.32 |
| 2026-09-18T19:13 | ZKUSDT | surge | TARGET | 8.8 | +2.75% | $+2.72 |
| 2026-09-18T18:02 | ETHFIUSDT | surge | TARGET | 0.8 | +2.75% | $+2.75 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-18T10:44 | BANKUSDT | surge | 0.0298 | 0.0295 | -1.01% |
| 2026-09-18T11:16 | DODOUSDT | surge | 0.01835 | 0.01801 | -1.85% |
| 2026-09-18T16:52 | MUBUSDT | surge | 993.73 | 1006.42 | +1.28% |
| 2026-09-18T20:06 | SNDKBUSDT | surge | 1790.7 | 1781.27 | -0.53% |
| 2026-09-18T20:42 | SENTUSDT | surge | 0.01781 | 0.01786 | +0.28% |
| 2026-09-18T21:40 | SOXLBUSDT | surge | 123.48 | 120.78 | -2.19% |
| 2026-09-19T04:49 | PROVEUSDT | surge | 0.2182 | 0.2143 | -1.79% |
| 2026-09-19T06:23 | VETUSDT | surge | 0.008176 | 0.008358 | +2.23% |
| 2026-09-19T06:41 | HOMEUSDT | surge | 0.00625 | 0.00627 | +0.32% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
