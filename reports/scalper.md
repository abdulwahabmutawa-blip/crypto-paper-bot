# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-23T19:45:09+00:00 · runs 4184 · equity **$659.09** (-34.09%) · cash $0.00 · open 10/10 · round trips 1498

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-334.60 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1310 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 188 | 45% | -0.37% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-23T19:43 | ACEUSDT | surge | STOP | 11.0 | -3.25% | $-2.21 |
| 2026-10-23T17:56 | BEAMXUSDT | surge | TARGET | 10.8 | +2.75% | $+1.79 |
| 2026-10-23T15:34 | COTIUSDT | surge | STOP | 0.2 | -3.25% | $-2.11 |
| 2026-10-23T15:11 | COTIUSDT | surge | TARGET | 4.5 | +2.75% | $+1.74 |
| 2026-10-23T13:01 | ARKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.84 |
| 2026-10-23T12:44 | ARKUSDT | surge | TARGET | 1.8 | +2.75% | $+1.79 |
| 2026-10-23T11:06 | STRKUSDT | bottom | STOP | 7.5 | -3.25% | $-2.07 |
| 2026-10-23T10:50 | ARKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.74 |
| 2026-10-23T10:34 | REZUSDT | surge | STOP | 2.8 | -3.25% | $-2.13 |
| 2026-10-23T10:18 | ARKUSDT | surge | TARGET | 0.2 | +2.75% | $+1.69 |
| 2026-10-23T09:45 | DASHUSDT | surge | STOP | 7.2 | -3.25% | $-2.07 |
| 2026-10-23T08:32 | PEPEUSDT | surge | TARGET | 2.0 | +2.75% | $+1.82 |
| 2026-10-23T07:40 | DOTUSDT | surge | TARGET | 5.0 | +2.75% | $+1.75 |
| 2026-10-23T06:49 | BTCUSDT | bottom | TIME | 24.0 | -1.08% | $-0.71 |
| 2026-10-23T06:15 | REZUSDT | surge | TARGET | 2.2 | +2.75% | $+1.77 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T02:23 | ATOMUSDT | surge | 1.766 | 1.746 | -1.13% |
| 2026-10-23T02:23 | RUNEUSDT | bottom | 0.642 | 0.634 | -1.25% |
| 2026-10-23T04:15 | BCHUSDT | surge | 284.8 | 283.9 | -0.32% |
| 2026-10-23T04:32 | BNCBUSDT | surge | 5.49 | 5.35 | -2.55% |
| 2026-10-23T11:06 | BOMEUSDT | surge | 0.0006433 | 0.0006351 | -1.27% |
| 2026-10-23T13:01 | BONKUSDT | surge | 3.29e-06 | 3.27e-06 | -0.61% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 146.5 | -1.38% |
| 2026-10-23T17:56 | SENTUSDT | surge | 0.02372 | 0.02341 | -1.31% |
| 2026-10-23T19:43 | ARKMUSDT | surge | 0.1386 | 0.1385 | -0.07% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
