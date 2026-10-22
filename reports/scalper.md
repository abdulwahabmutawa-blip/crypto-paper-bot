# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-22T02:44:55+00:00 · runs 4037 · equity **$663.79** (-33.62%) · cash $259.52 · open 6/10 · round trips 1464

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-330.20 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1282 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-22T02:43 | MSTRBUSDT | surge | STOP | 10.0 | -3.25% | $-2.15 |
| 2026-10-22T02:43 | CRCLBUSDT | surge | STOP | 11.0 | -3.25% | $-2.16 |
| 2026-10-22T01:51 | QNTUSDT | surge | STOP | 3.2 | -3.25% | $-2.12 |
| 2026-10-22T01:51 | DOGEUSDT | surge | STOP | 8.8 | -3.25% | $-2.35 |
| 2026-10-22T01:51 | AAVEUSDT | surge | STOP | 9.2 | -3.25% | $-2.15 |
| 2026-10-21T23:33 | SCUSDT | surge | STOP | 10.2 | -3.25% | $-2.11 |
| 2026-10-21T23:10 | SPCXBUSDT | surge | STOP | 20.2 | -3.25% | $-2.09 |
| 2026-10-21T22:19 | DASHUSDT | surge | STOP | 6.5 | -3.25% | $-2.19 |
| 2026-10-21T16:48 | PENGUUSDT | surge | TARGET | 19.8 | +2.75% | $+1.94 |
| 2026-10-21T16:15 | OPNUSDT | surge | STOP | 0.2 | -3.25% | $-2.13 |
| 2026-10-21T16:15 | MAGICUSDT | surge | STOP | 0.8 | -3.25% | $-2.16 |
| 2026-10-21T16:15 | PROMUSDT | surge | TARGET | 2.0 | +2.75% | $+1.88 |
| 2026-10-21T15:59 | JTOUSDT | surge | TARGET | 24.0 | +2.75% | $+1.76 |
| 2026-10-21T15:42 | DASHUSDT | surge | TARGET | 1.5 | +2.75% | $+1.81 |
| 2026-10-21T15:25 | WUSDT | surge | TARGET | 0.5 | +2.75% | $+1.80 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-21T11:30 | LUMIAUSDT | surge | 0.0894 | 0.0871 | -2.57% |
| 2026-10-21T16:15 | ACEUSDT | surge | 0.1574 | 0.1531 | -2.73% |
| 2026-10-21T23:10 | TSLABUSDT | bottom | 375.06 | 369.64 | -1.45% |
| 2026-10-21T23:33 | INTCBUSDT | bottom | 91.03 | 89.79 | -1.36% |
| 2026-10-22T01:51 | ZROUSDT | bottom | 1.942 | 1.921 | -1.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
