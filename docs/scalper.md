# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-12T16:02:20+00:00 · runs 623 · equity **$904.89** (-9.51%) · cash $0.00 · open 10/10 · round trips 214

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.43%/trade · realized $-89.74 · worst day $-50.94 · trades/day 26.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 149 | 46% | -0.46% | 42% | 50% | 8% |
| bottom | 65 | 45% | -0.35% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-12T16:00 | GOOGLBUSDT | surge | TIME | 24.0 | -0.75% | $-0.68 |
| 2026-09-12T14:13 | THEUSDT | surge | STOP | 2.8 | -3.25% | $-2.81 |
| 2026-09-12T14:13 | BTCUSDT | surge | TIME | 24.0 | -0.91% | $-0.82 |
| 2026-09-12T14:13 | AAPLBUSDT | surge | TIME | 24.0 | -0.21% | $-0.19 |
| 2026-09-12T13:55 | REZUSDT | surge | TARGET | 0.2 | +2.75% | $+2.53 |
| 2026-09-12T13:20 | POLUSDT | surge | TIME | 24.0 | +0.60% | $+0.55 |
| 2026-09-12T11:28 | ACEUSDT | surge | STOP | 8.8 | -3.25% | $-2.91 |
| 2026-09-12T10:53 | CAKEUSDT | surge | TARGET | 18.0 | +2.75% | $+2.57 |
| 2026-09-12T02:18 | KAVAUSDT | surge | TARGET | 17.8 | +2.75% | $+2.39 |
| 2026-09-11T20:35 | HOLOUSDT | surge | STOP | 2.8 | -3.25% | $-3.02 |
| 2026-09-11T17:44 | DOGSUSDT | surge | TARGET | 1.2 | +2.75% | $+2.49 |
| 2026-09-11T16:38 | HOLOUSDT | surge | TARGET | 2.0 | +2.75% | $+2.59 |
| 2026-09-11T16:38 | CRCLBUSDT | surge | STOP | 2.2 | -3.25% | $-3.04 |
| 2026-09-11T16:04 | MORPHOUSDT | surge | STOP | 1.8 | -3.25% | $-3.04 |
| 2026-09-11T16:04 | ADAUSDT | surge | STOP | 1.8 | -3.25% | $-3.04 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-11T16:04 | SOXLBUSDT | surge | 123.42 | 122.62 | -0.65% |
| 2026-09-11T16:04 | PLUMEUSDT | surge | 0.01336 | 0.01339 | +0.22% |
| 2026-09-11T16:38 | KAITOUSDT | surge | 0.3105 | 0.3104 | -0.03% |
| 2026-09-11T20:35 | SPCXBUSDT | surge | 150.6 | 150.11 | -0.33% |
| 2026-09-12T10:53 | PROMUSDT | surge | 5.762 | 5.709 | -0.92% |
| 2026-09-12T14:31 | KAVAUSDT | surge | 0.07024 | 0.07031 | +0.10% |
| 2026-09-12T14:31 | NEIROUSDT | surge | 8.935e-05 | 8.919e-05 | -0.18% |
| 2026-09-12T14:31 | CFGUSDT | surge | 0.1115 | 0.1091 | -2.15% |
| 2026-09-12T14:31 | ETHFIUSDT | surge | 0.7646 | 0.7483 | -2.13% |
| 2026-09-12T16:00 | ORDIUSDT | surge | 4.305 | 4.312 | +0.16% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
