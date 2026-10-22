# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-22T05:43:55+00:00 · runs 4048 · equity **$665.97** (-33.40%) · cash $262.81 · open 6/10 · round trips 1468

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-330.97 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1286 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-22T05:06 | PHAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.79 |
| 2026-10-22T04:48 | PHAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.78 |
| 2026-10-22T03:34 | LUMIAUSDT | surge | STOP | 15.8 | -3.25% | $-2.19 |
| 2026-10-22T03:00 | ACEUSDT | surge | STOP | 10.2 | -3.25% | $-2.15 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-21T23:10 | TSLABUSDT | bottom | 375.06 | 368.24 | -1.82% |
| 2026-10-21T23:33 | INTCBUSDT | bottom | 91.03 | 89.17 | -2.04% |
| 2026-10-22T01:51 | ZROUSDT | bottom | 1.942 | 1.898 | -2.27% |
| 2026-10-22T03:00 | PROMUSDT | surge | 5.889 | 5.837 | -0.88% |
| 2026-10-22T03:34 | SOXSBUSDT | surge | 47.57 | 48.6 | +2.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
