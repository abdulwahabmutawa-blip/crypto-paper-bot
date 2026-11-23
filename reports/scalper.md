# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-23T14:26:06+00:00 · runs 6648 · equity **$501.62** (-49.84%) · cash $0.00 · open 10/10 · round trips 2171

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-503.75 · worst day $-50.94 · trades/day 27.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1870 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 301 | 44% | -0.45% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-23T12:49 | LSKUSDT | surge | TARGET | 0.2 | +2.75% | $+1.24 |
| 2026-11-23T12:16 | BLURUSDT | surge | TARGET | 1.8 | +2.75% | $+1.24 |
| 2026-11-23T12:16 | TSLABUSDT | surge | TIME | 24.0 | +0.29% | $+0.13 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-23T12:16 | LUNCUSDT | surge | 4.234e-05 | 4.294e-05 | +1.42% |
| 2026-11-23T12:16 | GOOGLBUSDT | surge | 279.77 | 283.75 | +1.42% |
| 2026-11-23T14:08 | NILUSDT | surge | 0.04992 | 0.05059 | +1.34% |
| 2026-11-23T14:08 | MORPHOUSDT | surge | 1.62 | 1.656 | +2.22% |
| 2026-11-23T14:08 | SPCXBUSDT | surge | 135.25 | 138.45 | +2.37% |
| 2026-11-23T14:24 | PENDLEUSDT | surge | 1.365 | 1.384 | +1.39% |
| 2026-11-23T14:24 | TRXUSDT | surge | 0.3103 | 0.3109 | +0.19% |
| 2026-11-23T14:24 | ADAUSDT | surge | 0.154 | 0.1546 | +0.39% |
| 2026-11-23T14:24 | SHIBUSDT | surge | 3.81e-06 | 3.85e-06 | +1.05% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
