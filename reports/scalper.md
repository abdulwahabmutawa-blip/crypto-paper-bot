# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-11T17:21:50+00:00 · runs 5751 · equity **$518.02** (-48.20%) · cash $0.00 · open 10/10 · round trips 1957

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-484.47 · worst day $-50.94 · trades/day 28.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1696 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 261 | 42% | -0.56% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-11T16:45 | INTCBUSDT | surge | TARGET | 5.2 | +2.75% | $+1.29 |
| 2026-11-11T16:28 | INTWBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.41 |
| 2026-11-11T14:29 | AVGOBUSDT | surge | TARGET | 12.8 | +2.75% | $+1.30 |
| 2026-11-11T12:25 | SOXLBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.37 |
| 2026-11-11T11:50 | OPENUSDT | surge | TARGET | 1.0 | +2.75% | $+1.30 |
| 2026-11-11T11:15 | INTWBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.26 |
| 2026-11-11T10:40 | OPENUSDT | surge | TARGET | 14.5 | +2.75% | $+1.27 |
| 2026-11-11T10:05 | SKHYBUSDT | surge | TARGET | 8.0 | +2.75% | $+1.27 |
| 2026-11-11T09:47 | PHAUSDT | surge | STOP | 1.5 | -3.25% | $-1.47 |
| 2026-11-11T09:47 | DRAMBUSDT | surge | TARGET | 7.8 | +2.75% | $+1.27 |
| 2026-11-11T08:31 | CRWVBUSDT | surge | TARGET | 2.8 | +2.75% | $+1.33 |
| 2026-11-11T08:14 | OPGUSDT | surge | TIME | 24.0 | +0.76% | $+0.34 |
| 2026-11-11T06:30 | RENDERUSDT | surge | STOP | 4.8 | -3.25% | $-1.54 |
| 2026-11-11T05:38 | ICPUSDT | surge | TARGET | 5.8 | +2.75% | $+1.30 |
| 2026-11-11T01:53 | ERAUSDT | surge | STOP | 1.0 | -3.25% | $-1.52 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-10T18:29 | GOOGLBUSDT | bottom | 285.98 | 293.57 | +2.65% |
| 2026-11-10T18:29 | BCHUSDT | bottom | 227 | 233.6 | +2.91% |
| 2026-11-11T06:30 | EWYBUSDT | surge | 146.03 | 149.7 | +2.51% |
| 2026-11-11T09:47 | PEPEUSDT | bottom | 5e-06 | 4.99e-06 | -0.20% |
| 2026-11-11T10:05 | HOMEUSDT | surge | 0.00556 | 0.00548 | -1.44% |
| 2026-11-11T11:50 | OPENUSDT | surge | 0.0961 | 0.0949 | -1.25% |
| 2026-11-11T14:29 | KITEUSDT | surge | 0.1264 | 0.1256 | -0.63% |
| 2026-11-11T16:28 | 0GUSDT | surge | 0.156 | 0.1562 | +0.13% |
| 2026-11-11T16:45 | BNCBUSDT | surge | 4.71 | 4.75 | +0.85% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
