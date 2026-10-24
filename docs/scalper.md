# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-24T00:12:56+00:00 · runs 4200 · equity **$640.31** (-35.97%) · cash $122.68 · open 8/10 · round trips 1512

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-360.07 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1321 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 191 | 44% | -0.42% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-23T23:01 | GRAMUSDT | bottom | STOP | 0.5 | -3.25% | $-2.00 |
| 2026-10-23T23:01 | DOTUSDT | bottom | STOP | 1.0 | -3.25% | $-2.16 |
| 2026-10-23T23:01 | WLFIUSDT | surge | STOP | 1.5 | -3.25% | $-2.08 |
| 2026-10-23T23:01 | BOMEUSDT | surge | STOP | 11.8 | -3.25% | $-2.00 |
| 2026-10-23T23:01 | BCHUSDT | surge | STOP | 18.5 | -3.25% | $-2.05 |
| 2026-10-23T23:01 | RUNEUSDT | bottom | STOP | 20.5 | -3.25% | $-2.07 |
| 2026-10-23T22:44 | ATOMUSDT | surge | STOP | 20.2 | -3.25% | $-2.07 |
| 2026-10-23T22:26 | INITUSDT | surge | STOP | 0.8 | -3.25% | $-2.08 |
| 2026-10-23T22:26 | BNCBUSDT | surge | STOP | 17.5 | -3.25% | $-2.05 |
| 2026-10-23T21:52 | BONKUSDT | surge | STOP | 8.5 | -3.25% | $-2.23 |
| 2026-10-23T21:17 | LAUSDT | surge | STOP | 0.2 | -3.25% | $-2.13 |
| 2026-10-23T21:17 | SENTUSDT | surge | STOP | 3.2 | -3.25% | $-2.17 |
| 2026-10-23T20:53 | LAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.75 |
| 2026-10-23T20:36 | ARKMUSDT | surge | STOP | 0.8 | -3.25% | $-2.14 |
| 2026-10-23T19:43 | ACEUSDT | surge | STOP | 11.0 | -3.25% | $-2.21 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 146.42 | -1.43% |
| 2026-10-23T22:26 | KMNOUSDT | surge | 0.04211 | 0.04226 | +0.36% |
| 2026-10-23T23:01 | CRCLBUSDT | bottom | 85.12 | 85.6 | +0.56% |
| 2026-10-23T23:01 | LTCUSDT | bottom | 56.84 | 57.19 | +0.62% |
| 2026-10-23T23:01 | SNDKBUSDT | bottom | 1232.71 | 1242.82 | +0.82% |
| 2026-10-23T23:36 | LAUSDT | surge | 0.0606 | 0.0609 | +0.50% |
| 2026-10-24T00:11 | HYPERUSDT | surge | 0.0649 | 0.0644 | -0.77% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
