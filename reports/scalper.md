# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-18T20:09:02+00:00 · runs 1167 · equity **$953.87** (-4.61%) · cash $0.00 · open 10/10 · round trips 402

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.12%/trade · realized $-50.10 · worst day $-50.94 · trades/day 28.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 320 | 54% | -0.01% | 49% | 42% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-18T15:59 | INTCBUSDT | surge | TIME | 24.0 | -2.95% | $-2.73 |
| 2026-09-18T14:30 | SKYUSDT | surge | TARGET | 0.2 | +2.75% | $+2.49 |
| 2026-09-18T14:14 | AUSDT | surge | TARGET | 5.8 | +2.75% | $+2.35 |
| 2026-09-18T14:14 | BCHUSDT | surge | TARGET | 10.2 | +2.75% | $+2.50 |
| 2026-09-18T13:10 | ZAMAUSDT | surge | STOP | 0.2 | -3.25% | $-3.40 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-18T10:44 | BANKUSDT | surge | 0.0298 | 0.0297 | -0.34% |
| 2026-09-18T11:16 | DODOUSDT | surge | 0.01835 | 0.01823 | -0.65% |
| 2026-09-18T13:10 | THETAUSDT | surge | 0.2055 | 0.2079 | +1.17% |
| 2026-09-18T14:30 | PROVEUSDT | surge | 0.2039 | 0.2077 | +1.86% |
| 2026-09-18T16:52 | MUBUSDT | surge | 993.73 | 1015.49 | +2.19% |
| 2026-09-18T19:13 | ACHUSDT | surge | 0.00601 | 0.00594 | -1.16% |
| 2026-09-18T19:13 | ZAMAUSDT | surge | 0.05951 | 0.06003 | +0.87% |
| 2026-09-18T20:06 | WUSDT | surge | 0.01113 | 0.01116 | +0.27% |
| 2026-09-18T20:06 | SNDKBUSDT | surge | 1790.7 | 1787.34 | -0.19% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
