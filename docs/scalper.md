# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-18T22:20:33+00:00 · runs 3756 · equity **$657.76** (-34.22%) · cash $0.00 · open 10/10 · round trips 1389

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-343.12 · worst day $-50.94 · trades/day 31.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1212 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 177 | 45% | -0.36% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-18T22:18 | SANDUSDT | bottom | TARGET | 0.5 | +2.75% | $+1.75 |
| 2026-10-18T22:18 | UNIUSDT | bottom | TARGET | 1.5 | +2.75% | $+1.73 |
| 2026-10-18T22:18 | SOXSBUSDT | surge | STOP | 3.5 | -3.25% | $-2.02 |
| 2026-10-18T21:30 | ALTUSDT | bottom | TARGET | 11.0 | +2.75% | $+1.77 |
| 2026-10-18T20:37 | RWUSDUSDT | bottom | TIME | 24.0 | -0.24% | $-0.17 |
| 2026-10-18T19:44 | AMPUSDT | surge | STOP | 0.2 | -3.25% | $-2.02 |
| 2026-10-18T19:09 | NXPCUSDT | surge | STOP | 0.0 | -3.25% | $-2.02 |
| 2026-10-18T19:09 | AMPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.71 |
| 2026-10-18T18:16 | NXPCUSDT | surge | TARGET | 0.2 | +2.75% | $+1.70 |
| 2026-10-18T17:59 | HBARUSDT | surge | STOP | 10.8 | -3.25% | $-2.12 |
| 2026-10-18T16:31 | AMPUSDT | surge | STOP | 1.0 | -3.25% | $-2.01 |
| 2026-10-18T14:14 | OGNUSDT | surge | STOP | 0.8 | -3.25% | $-2.05 |
| 2026-10-18T14:14 | MORPHOUSDT | surge | STOP | 10.8 | -3.25% | $-2.02 |
| 2026-10-18T13:57 | SUSDT | surge | STOP | 1.2 | -3.25% | $-2.12 |
| 2026-10-18T13:24 | MEGAUSDT | surge | STOP | 3.5 | -3.25% | $-2.13 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-18T01:44 | TRXUSDT | bottom | 0.3338 | 0.3331 | -0.21% |
| 2026-10-18T03:05 | MSTRBUSDT | surge | 137.28 | 136.5 | -0.57% |
| 2026-10-18T22:18 | TQQQBUSDT | surge | 68.58 | 68.62 | +0.06% |
| 2026-10-18T22:18 | RUNEUSDT | surge | 0.643 | 0.649 | +0.93% |
| 2026-10-18T22:18 | EWYBUSDT | surge | 149.99 | 150.2 | +0.14% |
| 2026-10-18T22:18 | INTCBUSDT | surge | 89.15 | 89.2 | +0.06% |
| 2026-10-18T22:18 | KORUBUSDT | surge | 10.56 | 10.64 | +0.76% |
| 2026-10-18T22:18 | QQQBUSDT | surge | 713.34 | 713.72 | +0.05% |
| 2026-10-18T22:18 | SOXLBUSDT | surge | 93.74 | 93.89 | +0.16% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
