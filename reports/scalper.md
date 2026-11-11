# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-11T13:20:47+00:00 · runs 5743 · equity **$513.31** (-48.67%) · cash $0.00 · open 10/10 · round trips 1954

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-488.47 · worst day $-50.94 · trades/day 28.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1693 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 261 | 42% | -0.56% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-11T01:04 | AVGOBUSDT | surge | TARGET | 8.5 | +2.75% | $+1.29 |
| 2026-11-11T00:31 | RWUSDUSDT | bottom | TIME | 24.0 | -0.25% | $-0.12 |
| 2026-11-10T23:09 | ICPUSDT | surge | TARGET | 2.5 | +2.75% | $+1.27 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-10T18:29 | GOOGLBUSDT | bottom | 285.98 | 291.02 | +1.76% |
| 2026-11-10T18:29 | BCHUSDT | bottom | 227 | 229.3 | +1.01% |
| 2026-11-11T01:37 | AVGOBUSDT | surge | 340.45 | 346.42 | +1.75% |
| 2026-11-11T06:30 | EWYBUSDT | surge | 146.03 | 147.16 | +0.77% |
| 2026-11-11T09:47 | PEPEUSDT | bottom | 5e-06 | 4.98e-06 | -0.40% |
| 2026-11-11T10:05 | HOMEUSDT | surge | 0.00556 | 0.00554 | -0.36% |
| 2026-11-11T11:15 | INTCBUSDT | surge | 61.74 | 61.92 | +0.29% |
| 2026-11-11T11:50 | OPENUSDT | surge | 0.0961 | 0.0944 | -1.77% |
| 2026-11-11T12:25 | INTWBUSDT | surge | 6.39 | 6.44 | +0.78% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
