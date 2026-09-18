# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-18T23:10:08+00:00 · runs 1178 · equity **$958.05** (-4.19%) · cash $0.00 · open 10/10 · round trips 407

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-42.42 · worst day $-50.94 · trades/day 29.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 325 | 54% | +0.01% | 50% | 42% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-18T18:02 | SEIUSDT | surge | TARGET | 13.2 | +2.75% | $+2.72 |
| 2026-09-18T17:09 | LPTUSDT | surge | TARGET | 0.0 | +2.75% | $+2.67 |
| 2026-09-18T16:52 | LPTUSDT | surge | TARGET | 0.2 | +2.75% | $+2.56 |
| 2026-09-18T16:52 | AXSUSDT | surge | TARGET | 15.2 | +2.75% | $+2.65 |
| 2026-09-18T16:16 | SUSDT | surge | TARGET | 2.0 | +2.75% | $+2.49 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-18T10:44 | BANKUSDT | surge | 0.0298 | 0.0298 | +0.00% |
| 2026-09-18T11:16 | DODOUSDT | surge | 0.01835 | 0.0183 | -0.27% |
| 2026-09-18T16:52 | MUBUSDT | surge | 993.73 | 1016.28 | +2.27% |
| 2026-09-18T20:06 | WUSDT | surge | 0.01113 | 0.01098 | -1.35% |
| 2026-09-18T20:06 | SNDKBUSDT | surge | 1790.7 | 1796.35 | +0.32% |
| 2026-09-18T20:42 | SENTUSDT | surge | 0.01781 | 0.01797 | +0.90% |
| 2026-09-18T21:40 | SOXLBUSDT | surge | 123.48 | 122.78 | -0.57% |
| 2026-09-18T22:33 | POLUSDT | surge | 0.10621 | 0.10586 | -0.33% |
| 2026-09-18T22:50 | BCHUSDT | surge | 262.7 | 261.6 | -0.42% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
