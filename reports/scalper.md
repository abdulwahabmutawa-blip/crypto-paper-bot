# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-23T14:58:30+00:00 · runs 6650 · equity **$497.73** (-50.23%) · cash $0.00 · open 10/10 · round trips 2174

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-502.76 · worst day $-50.94 · trades/day 27.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1873 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 301 | 44% | -0.45% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-23T14:57 | AMZNBUSDT | surge | STOP | 0.0 | -3.25% | $-1.52 |
| 2026-11-23T14:40 | SPCXBUSDT | surge | TARGET | 0.2 | +2.75% | $+1.25 |
| 2026-11-23T14:40 | MORPHOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.25 |
| 2026-11-23T14:24 | MRVLBUSDT | surge | TARGET | 0.0 | +2.75% | $+1.25 |
| 2026-11-23T14:24 | DRAMBUSDT | surge | TARGET | 0.0 | +2.75% | $+1.25 |
| 2026-11-23T14:24 | TSMBUSDT | surge | TARGET | 0.0 | +2.75% | $+1.25 |
| 2026-11-23T14:24 | COINBUSDT | surge | TARGET | 7.8 | +2.75% | $+1.12 |
| 2026-11-23T14:08 | ALGOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.31 |
| 2026-11-23T14:08 | QNTUSDT | surge | TARGET | 0.8 | +2.75% | $+1.18 |
| 2026-11-23T14:08 | DRAMBUSDT | surge | TARGET | 4.8 | +2.75% | $+1.22 |
| 2026-11-23T14:08 | XLMUSDT | bottom | TARGET | 11.5 | +2.75% | $+1.19 |
| 2026-11-23T14:08 | SKHYBUSDT | surge | TARGET | 12.0 | +2.75% | $+1.20 |
| 2026-11-23T14:08 | CAKEUSDT | surge | TARGET | 20.8 | +2.75% | $+1.23 |
| 2026-11-23T13:37 | ALGOUSDT | surge | TARGET | 0.5 | +2.75% | $+1.28 |
| 2026-11-23T13:05 | AMDBUSDT | surge | STOP | 3.8 | -3.25% | $-1.44 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-23T12:16 | LUNCUSDT | surge | 4.234e-05 | 4.261e-05 | +0.64% |
| 2026-11-23T12:16 | GOOGLBUSDT | surge | 279.77 | 280.08 | +0.11% |
| 2026-11-23T14:08 | NILUSDT | surge | 0.04992 | 0.05022 | +0.60% |
| 2026-11-23T14:24 | PENDLEUSDT | surge | 1.365 | 1.372 | +0.51% |
| 2026-11-23T14:24 | TRXUSDT | surge | 0.3103 | 0.311 | +0.23% |
| 2026-11-23T14:24 | ADAUSDT | surge | 0.154 | 0.1539 | -0.06% |
| 2026-11-23T14:24 | SHIBUSDT | surge | 3.81e-06 | 3.8e-06 | -0.26% |
| 2026-11-23T14:40 | SPCXBUSDT | surge | 140.07 | 140.06 | -0.01% |
| 2026-11-23T14:57 | MORPHOUSDT | surge | 1.66 | 1.649 | -0.66% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
