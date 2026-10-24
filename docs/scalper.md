# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-24T15:59:28+00:00 · runs 4257 · equity **$645.02** (-35.50%) · cash $374.65 · open 4/10 · round trips 1543

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-351.94 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1351 | 49% | -0.26% | 47% | 46% | 7% |
| bottom | 192 | 44% | -0.43% | 39% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-24T15:39 | OPENUSDT | surge | STOP | 0.2 | -3.25% | $-2.06 |
| 2026-10-24T15:39 | LTCUSDT | bottom | STOP | 16.2 | -3.25% | $-1.99 |
| 2026-10-24T14:28 | MIRAUSDT | surge | STOP | 4.0 | -3.25% | $-2.19 |
| 2026-10-24T14:28 | MSTRBUSDT | surge | STOP | 22.8 | -3.25% | $-2.05 |
| 2026-10-24T13:47 | SAHARAUSDT | surge | STOP | 3.2 | -3.25% | $-2.19 |
| 2026-10-24T13:12 | WCTUSDT | surge | STOP | 0.0 | -3.25% | $-2.08 |
| 2026-10-24T12:55 | WCTUSDT | surge | TARGET | 0.2 | +2.75% | $+1.79 |
| 2026-10-24T12:55 | LUMIAUSDT | surge | STOP | 2.5 | -3.25% | $-2.05 |
| 2026-10-24T12:20 | VANAUSDT | surge | STOP | 1.8 | -3.25% | $-2.19 |
| 2026-10-24T10:19 | SAHARAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.83 |
| 2026-10-24T10:19 | VANAUSDT | surge | TARGET | 0.8 | +2.75% | $+1.87 |
| 2026-10-24T10:19 | REZUSDT | surge | STOP | 1.8 | -3.25% | $-2.16 |
| 2026-10-24T10:02 | HYPERUSDT | surge | TARGET | 9.8 | +2.75% | $+1.69 |
| 2026-10-24T09:44 | NILUSDT | surge | TARGET | 4.0 | +2.75% | $+1.78 |
| 2026-10-24T09:27 | BREVUSDT | surge | TARGET | 0.2 | +2.75% | $+1.82 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T23:01 | CRCLBUSDT | bottom | 85.12 | 83.72 | -1.64% |
| 2026-10-23T23:01 | SNDKBUSDT | bottom | 1232.71 | 1221.3 | -0.93% |
| 2026-10-24T07:22 | PARTIUSDT | surge | 0.0351 | 0.0343 | -2.28% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
