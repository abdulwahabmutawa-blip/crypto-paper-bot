# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-23T03:19:37+00:00 · runs 4124 · equity **$662.18** (-33.78%) · cash $63.59 · open 9/10 · round trips 1481

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-338.92 · worst day $-50.94 · trades/day 30.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1295 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 186 | 45% | -0.36% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-22T05:06 | PHAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.79 |
| 2026-10-22T04:48 | PHAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.78 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-22T06:34 | BTCUSDT | bottom | 82570.4 | 81794 | -0.94% |
| 2026-10-23T02:23 | DASHUSDT | surge | 55.17 | 54.9 | -0.49% |
| 2026-10-23T02:23 | DOTUSDT | surge | 1.159 | 1.161 | +0.17% |
| 2026-10-23T02:23 | ATOMUSDT | surge | 1.766 | 1.802 | +2.04% |
| 2026-10-23T02:23 | RUNEUSDT | bottom | 0.642 | 0.647 | +0.78% |
| 2026-10-23T02:41 | REZUSDT | surge | 0.003943 | 0.003986 | +1.09% |
| 2026-10-23T02:59 | KERNELUSDT | surge | 0.0519 | 0.0514 | -0.96% |
| 2026-10-23T03:17 | STRKUSDT | bottom | 0.05291 | 0.05295 | +0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
