# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-23T05:25:31+00:00 · runs 4132 · equity **$664.48** (-33.55%) · cash $0.00 · open 10/10 · round trips 1483

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-339.24 · worst day $-50.94 · trades/day 30.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1297 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 186 | 45% | -0.36% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-23T04:15 | KERNELUSDT | surge | STOP | 1.2 | -3.25% | $-2.07 |
| 2026-10-23T03:35 | REZUSDT | surge | TARGET | 0.8 | +2.75% | $+1.75 |
| 2026-10-23T02:59 | GTCUSDT | surge | STOP | 0.0 | -3.25% | $-2.07 |
| 2026-10-23T02:59 | KERNELUSDT | surge | TARGET | 0.2 | +2.75% | $+1.75 |
| 2026-10-22T15:10 | SPCXBUSDT | bottom | STOP | 6.5 | -3.25% | $-2.11 |
| 2026-10-22T15:10 | PROMUSDT | surge | STOP | 11.8 | -3.25% | $-2.10 |
| 2026-10-22T14:00 | TSLABUSDT | bottom | TARGET | 14.8 | +2.75% | $+1.71 |
| 2026-10-22T12:16 | RUNEUSDT | surge | STOP | 1.8 | -3.25% | $-2.11 |
| 2026-10-22T10:49 | ARKMUSDT | surge | STOP | 0.5 | -3.25% | $-2.11 |
| 2026-10-22T08:22 | RUNEUSDT | surge | STOP | 1.5 | -3.25% | $-2.13 |
| 2026-10-22T08:22 | INTCBUSDT | bottom | STOP | 8.5 | -3.25% | $-2.04 |
| 2026-10-22T07:29 | DODOUSDT | surge | TARGET | 0.5 | +2.75% | $+1.80 |
| 2026-10-22T07:29 | SOXSBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.78 |
| 2026-10-22T06:34 | PHAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.81 |
| 2026-10-22T06:34 | ZROUSDT | bottom | STOP | 4.5 | -3.25% | $-2.14 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-22T06:34 | BTCUSDT | bottom | 82570.4 | 81764 | -0.98% |
| 2026-10-23T02:23 | DASHUSDT | surge | 55.17 | 55.04 | -0.24% |
| 2026-10-23T02:23 | DOTUSDT | surge | 1.159 | 1.177 | +1.55% |
| 2026-10-23T02:23 | ATOMUSDT | surge | 1.766 | 1.792 | +1.47% |
| 2026-10-23T02:23 | RUNEUSDT | bottom | 0.642 | 0.65 | +1.25% |
| 2026-10-23T03:17 | STRKUSDT | bottom | 0.05291 | 0.0529 | -0.02% |
| 2026-10-23T03:35 | REZUSDT | surge | 0.004059 | 0.004137 | +1.92% |
| 2026-10-23T04:15 | BCHUSDT | surge | 284.8 | 286.3 | +0.53% |
| 2026-10-23T04:32 | BNCBUSDT | surge | 5.49 | 5.51 | +0.36% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
