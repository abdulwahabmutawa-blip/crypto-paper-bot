# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-23T16:03:44+00:00 · runs 6654 · equity **$496.30** (-50.37%) · cash $0.00 · open 10/10 · round trips 2175

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-501.52 · worst day $-50.94 · trades/day 27.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1874 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 301 | 44% | -0.45% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-23T15:29 | LUNCUSDT | surge | TARGET | 3.0 | +2.75% | $+1.24 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-23T12:16 | GOOGLBUSDT | surge | 279.77 | 281.47 | +0.61% |
| 2026-11-23T14:08 | NILUSDT | surge | 0.04992 | 0.0496 | -0.64% |
| 2026-11-23T14:24 | PENDLEUSDT | surge | 1.365 | 1.361 | -0.29% |
| 2026-11-23T14:24 | TRXUSDT | surge | 0.3103 | 0.3107 | +0.13% |
| 2026-11-23T14:24 | ADAUSDT | surge | 0.154 | 0.1538 | -0.13% |
| 2026-11-23T14:24 | SHIBUSDT | surge | 3.81e-06 | 3.76e-06 | -1.31% |
| 2026-11-23T14:40 | SPCXBUSDT | surge | 140.07 | 136.21 | -2.76% |
| 2026-11-23T14:57 | MORPHOUSDT | surge | 1.66 | 1.653 | -0.42% |
| 2026-11-23T15:29 | ALGOUSDT | surge | 0.0852 | 0.0853 | +0.12% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
