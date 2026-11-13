# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-13T00:31:07+00:00 · runs 5849 · equity **$493.26** (-50.67%) · cash $318.38 · open 3/10 · round trips 1985

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-506.05 · worst day $-50.94 · trades/day 28.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1717 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 268 | 42% | -0.54% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-12T23:56 | GOOGLBUSDT | surge | TIME | 24.0 | +1.24% | $+0.57 |
| 2026-11-12T19:50 | GRAMUSDT | surge | STOP | 6.2 | -3.25% | $-1.50 |
| 2026-11-12T19:50 | QQQBUSDT | surge | TIME | 24.0 | -0.77% | $-0.35 |
| 2026-11-12T14:48 | SPCXBUSDT | bottom | TARGET | 15.5 | +2.75% | $+1.27 |
| 2026-11-12T14:31 | MSTRBUSDT | bottom | STOP | 8.5 | -3.25% | $-1.54 |
| 2026-11-12T13:56 | ERAUSDT | surge | STOP | 0.2 | -3.25% | $-1.45 |
| 2026-11-12T13:56 | ONEUSDT | surge | STOP | 1.8 | -3.25% | $-1.50 |
| 2026-11-12T13:38 | AVGOBUSDT | surge | STOP | 13.8 | -3.25% | $-1.50 |
| 2026-11-12T13:21 | TAOUSDT | bottom | STOP | 14.0 | -3.25% | $-1.50 |
| 2026-11-12T13:21 | AMDBUSDT | surge | STOP | 14.0 | -3.25% | $-1.50 |
| 2026-11-12T11:55 | SXTUSDT | surge | TARGET | 0.5 | +2.75% | $+1.30 |
| 2026-11-12T11:55 | HAEDALUSDT | surge | STOP | 4.2 | -3.25% | $-1.47 |
| 2026-11-12T10:14 | ERAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.26 |
| 2026-11-12T07:57 | KITEUSDT | surge | STOP | 1.2 | -3.25% | $-1.54 |
| 2026-11-12T06:49 | EWYBUSDT | surge | TIME | 24.0 | -0.91% | $-0.42 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-12T13:21 | OPENUSDT | surge | 0.0962 | 0.0948 | -1.46% |
| 2026-11-12T13:38 | TRXUSDT | bottom | 0.3159 | 0.3156 | -0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
