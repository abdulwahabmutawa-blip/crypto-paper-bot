# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-19T15:23:00+00:00 · runs 1232 · equity **$952.86** (-4.71%) · cash $0.00 · open 10/10 · round trips 427

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-44.56 · worst day $-50.94 · trades/day 28.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 345 | 54% | +0.01% | 50% | 41% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-19T15:20 | BANKUSDT | surge | TARGET | 0.0 | +2.75% | $+2.34 |
| 2026-09-19T15:20 | AVAXUSDT | surge | TARGET | 2.2 | +2.75% | $+2.55 |
| 2026-09-19T15:03 | HOMEUSDT | surge | STOP | 4.0 | -3.25% | $-2.86 |
| 2026-09-19T12:59 | AVAXUSDT | surge | TARGET | 0.2 | +2.75% | $+2.48 |
| 2026-09-19T12:41 | INJUSDT | surge | TARGET | 1.5 | +2.75% | $+2.42 |
| 2026-09-19T12:23 | ENAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.38 |
| 2026-09-19T11:30 | DODOUSDT | surge | TIME | 24.0 | -0.80% | $-0.69 |
| 2026-09-19T10:49 | ACHUSDT | surge | STOP | 1.0 | -3.25% | $-3.05 |
| 2026-09-19T10:49 | BANKUSDT | surge | TIME | 24.0 | -2.26% | $-1.97 |
| 2026-09-19T09:38 | SOXLBUSDT | surge | STOP | 11.8 | -3.25% | $-3.15 |
| 2026-09-19T08:45 | EPICUSDT | surge | TARGET | 1.2 | +2.75% | $+2.95 |
| 2026-09-19T08:27 | HOMEUSDT | surge | STOP | 0.5 | -3.25% | $-3.36 |
| 2026-09-19T07:34 | HOMEUSDT | surge | TARGET | 0.8 | +2.75% | $+2.77 |
| 2026-09-19T07:17 | VETUSDT | surge | TARGET | 0.0 | +2.75% | $+2.88 |
| 2026-09-19T06:59 | VETUSDT | surge | TARGET | 0.5 | +2.75% | $+2.80 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-18T16:52 | MUBUSDT | surge | 993.73 | 1006.76 | +1.31% |
| 2026-09-18T20:06 | SNDKBUSDT | surge | 1790.7 | 1781.61 | -0.51% |
| 2026-09-18T20:42 | SENTUSDT | surge | 0.01781 | 0.01796 | +0.84% |
| 2026-09-19T04:49 | PROVEUSDT | surge | 0.2182 | 0.2156 | -1.19% |
| 2026-09-19T08:27 | VETUSDT | surge | 0.008627 | 0.008389 | -2.76% |
| 2026-09-19T08:45 | ACEUSDT | surge | 0.1575 | 0.1548 | -1.71% |
| 2026-09-19T12:23 | TAOUSDT | surge | 267.9 | 272.3 | +1.64% |
| 2026-09-19T15:20 | ALLOUSDT | surge | 0.2431 | 0.2433 | +0.08% |
| 2026-09-19T15:20 | IOSTUSDT | surge | 0.00089 | 0.000891 | +0.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
