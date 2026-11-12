# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-12T15:42:01+00:00 · runs 5825 · equity **$495.20** (-50.48%) · cash $181.49 · open 6/10 · round trips 1982

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-504.77 · worst day $-50.94 · trades/day 28.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1714 | 48% | -0.33% | 46% | 48% | 7% |
| bottom | 268 | 42% | -0.54% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-12T05:57 | WLFIUSDT | bottom | TARGET | 8.2 | +2.75% | $+1.29 |
| 2026-11-12T05:23 | BNCBUSDT | surge | STOP | 12.2 | -3.25% | $-1.57 |
| 2026-11-11T23:23 | HOMEUSDT | surge | STOP | 13.0 | -3.25% | $-1.55 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-11T19:19 | QQQBUSDT | surge | 693.04 | 687.25 | -0.84% |
| 2026-11-11T23:39 | GOOGLBUSDT | surge | 297.09 | 296.17 | -0.31% |
| 2026-11-12T11:55 | GRAMUSDT | surge | 1.253 | 1.26 | +0.56% |
| 2026-11-12T13:21 | OPENUSDT | surge | 0.0962 | 0.0968 | +0.62% |
| 2026-11-12T13:38 | TRXUSDT | bottom | 0.3159 | 0.3156 | -0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
