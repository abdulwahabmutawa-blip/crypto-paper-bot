# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-11T11:35:04+00:00 · runs 5737 · equity **$514.23** (-48.58%) · cash $0.00 · open 10/10 · round trips 1952

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-491.15 · worst day $-50.94 · trades/day 28.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1691 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 261 | 42% | -0.56% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-10T20:50 | GRAMUSDT | surge | TARGET | 4.2 | +2.75% | $+1.29 |
| 2026-11-10T17:53 | QQQBUSDT | surge | TIME | 24.0 | -1.67% | $-0.80 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-10T18:29 | GOOGLBUSDT | bottom | 285.98 | 291.07 | +1.78% |
| 2026-11-10T18:29 | BCHUSDT | bottom | 227 | 229.8 | +1.23% |
| 2026-11-11T01:37 | AVGOBUSDT | surge | 340.45 | 347.1 | +1.95% |
| 2026-11-11T06:30 | EWYBUSDT | surge | 146.03 | 147.18 | +0.79% |
| 2026-11-11T08:31 | SOXLBUSDT | surge | 63.03 | 64.81 | +2.82% |
| 2026-11-11T09:47 | PEPEUSDT | bottom | 5e-06 | 4.98e-06 | -0.40% |
| 2026-11-11T10:05 | HOMEUSDT | surge | 0.00556 | 0.00556 | +0.00% |
| 2026-11-11T10:40 | OPENUSDT | surge | 0.0932 | 0.096 | +3.00% |
| 2026-11-11T11:15 | INTCBUSDT | surge | 61.74 | 61.81 | +0.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
