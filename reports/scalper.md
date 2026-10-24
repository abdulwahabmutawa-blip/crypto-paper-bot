# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-24T01:22:11+00:00 · runs 4204 · equity **$647.90** (-35.21%) · cash $0.00 · open 10/10 · round trips 1514

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-356.68 · worst day $-50.94 · trades/day 30.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1323 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 191 | 44% | -0.42% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-24T00:45 | LAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.70 |
| 2026-10-24T00:28 | LAUSDT | surge | TARGET | 0.8 | +2.75% | $+1.69 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 145.93 | -1.76% |
| 2026-10-23T22:26 | KMNOUSDT | surge | 0.04211 | 0.04197 | -0.33% |
| 2026-10-23T23:01 | CRCLBUSDT | bottom | 85.12 | 85.32 | +0.23% |
| 2026-10-23T23:01 | LTCUSDT | bottom | 56.84 | 57.27 | +0.76% |
| 2026-10-23T23:01 | SNDKBUSDT | bottom | 1232.71 | 1238.8 | +0.49% |
| 2026-10-24T00:11 | HYPERUSDT | surge | 0.0649 | 0.0657 | +1.23% |
| 2026-10-24T00:45 | TREEUSDT | surge | 0.0427 | 0.0439 | +2.81% |
| 2026-10-24T00:45 | AVAUSDT | surge | 0.428 | 0.4352 | +1.68% |
| 2026-10-24T01:02 | LAUSDT | surge | 0.0617 | 0.0631 | +2.27% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
