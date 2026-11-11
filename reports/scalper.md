# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-11T09:14:18+00:00 · runs 5729 · equity **$508.96** (-49.10%) · cash $0.00 · open 10/10 · round trips 1947

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-494.75 · worst day $-50.94 · trades/day 28.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1686 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 261 | 42% | -0.56% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-10T17:18 | MEGAUSDT | surge | STOP | 0.8 | -3.25% | $-1.52 |
| 2026-11-10T17:00 | AMDBUSDT | surge | STOP | 0.5 | -3.25% | $-1.52 |
| 2026-11-10T17:00 | SOPHUSDT | surge | STOP | 0.5 | -3.25% | $-1.52 |
| 2026-11-10T17:00 | TSLABUSDT | surge | TIME | 24.0 | -0.63% | $-0.30 |
| 2026-11-10T15:48 | XLMUSDT | bottom | STOP | 2.5 | -3.25% | $-1.53 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-10T18:29 | GOOGLBUSDT | bottom | 285.98 | 290.62 | +1.62% |
| 2026-11-10T18:29 | BCHUSDT | bottom | 227 | 228.6 | +0.70% |
| 2026-11-10T19:57 | OPENUSDT | surge | 0.0915 | 0.0927 | +1.31% |
| 2026-11-11T01:37 | AVGOBUSDT | surge | 340.45 | 344.05 | +1.06% |
| 2026-11-11T01:53 | SKHYBUSDT | surge | 136.27 | 139.49 | +2.36% |
| 2026-11-11T01:53 | DRAMBUSDT | surge | 42.39 | 43.52 | +2.67% |
| 2026-11-11T06:30 | EWYBUSDT | surge | 146.03 | 146.06 | +0.02% |
| 2026-11-11T08:14 | PHAUSDT | surge | 0.0356 | 0.0347 | -2.53% |
| 2026-11-11T08:31 | SOXLBUSDT | surge | 63.03 | 63.46 | +0.68% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
