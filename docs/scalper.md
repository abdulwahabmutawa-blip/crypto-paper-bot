# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-23T14:10:01+00:00 · runs 6647 · equity **$498.45** (-50.16%) · cash $0.00 · open 10/10 · round trips 2167

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-508.64 · worst day $-50.94 · trades/day 27.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1866 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 301 | 44% | -0.45% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-23T14:08 | ALGOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.31 |
| 2026-11-23T14:08 | QNTUSDT | surge | TARGET | 0.8 | +2.75% | $+1.18 |
| 2026-11-23T14:08 | DRAMBUSDT | surge | TARGET | 4.8 | +2.75% | $+1.22 |
| 2026-11-23T14:08 | XLMUSDT | bottom | TARGET | 11.5 | +2.75% | $+1.19 |
| 2026-11-23T14:08 | SKHYBUSDT | surge | TARGET | 12.0 | +2.75% | $+1.20 |
| 2026-11-23T14:08 | CAKEUSDT | surge | TARGET | 20.8 | +2.75% | $+1.23 |
| 2026-11-23T13:37 | ALGOUSDT | surge | TARGET | 0.5 | +2.75% | $+1.28 |
| 2026-11-23T13:05 | AMDBUSDT | surge | STOP | 3.8 | -3.25% | $-1.44 |
| 2026-11-23T12:49 | LSKUSDT | surge | TARGET | 0.2 | +2.75% | $+1.24 |
| 2026-11-23T12:16 | BLURUSDT | surge | TARGET | 1.8 | +2.75% | $+1.24 |
| 2026-11-23T12:16 | TSLABUSDT | surge | TIME | 24.0 | +0.29% | $+0.13 |
| 2026-11-23T12:16 | EWYBUSDT | surge | TIME | 24.0 | +0.94% | $+0.41 |
| 2026-11-23T09:14 | NVDABUSDT | surge | TARGET | 22.8 | +2.75% | $+1.20 |
| 2026-11-23T09:14 | RENDERUSDT | surge | TIME | 24.0 | +0.27% | $+0.12 |
| 2026-11-23T08:24 | BONKUSDT | surge | TARGET | 22.0 | +2.75% | $+1.21 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-23T06:26 | COINBUSDT | surge | 107.54 | 109.63 | +1.94% |
| 2026-11-23T12:16 | LUNCUSDT | surge | 4.234e-05 | 4.235e-05 | +0.02% |
| 2026-11-23T12:16 | GOOGLBUSDT | surge | 279.77 | 282.12 | +0.84% |
| 2026-11-23T14:08 | NILUSDT | surge | 0.04992 | 0.0502 | +0.56% |
| 2026-11-23T14:08 | MORPHOUSDT | surge | 1.62 | 1.62 | +0.00% |
| 2026-11-23T14:08 | TSMBUSDT | surge | 352.63 | 366.43 | +3.91% |
| 2026-11-23T14:08 | DRAMBUSDT | surge | 38.21 | 39.33 | +2.93% |
| 2026-11-23T14:08 | SPCXBUSDT | surge | 135.25 | 136.47 | +0.90% |
| 2026-11-23T14:08 | MRVLBUSDT | surge | 136.92 | 143.24 | +4.62% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
