# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-24T01:56:50+00:00 · runs 4206 · equity **$650.86** (-34.91%) · cash $64.78 · open 9/10 · round trips 1518

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-349.76 · worst day $-50.94 · trades/day 30.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1327 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 191 | 44% | -0.42% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-24T01:54 | LAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.77 |
| 2026-10-24T01:37 | LAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.72 |
| 2026-10-24T01:37 | AVAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.72 |
| 2026-10-24T01:37 | TREEUSDT | surge | TARGET | 0.5 | +2.75% | $+1.72 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 146.61 | -1.31% |
| 2026-10-23T22:26 | KMNOUSDT | surge | 0.04211 | 0.04232 | +0.50% |
| 2026-10-23T23:01 | CRCLBUSDT | bottom | 85.12 | 85.56 | +0.52% |
| 2026-10-23T23:01 | LTCUSDT | bottom | 56.84 | 57.3 | +0.81% |
| 2026-10-23T23:01 | SNDKBUSDT | bottom | 1232.71 | 1239.68 | +0.57% |
| 2026-10-24T00:11 | HYPERUSDT | surge | 0.0649 | 0.0645 | -0.62% |
| 2026-10-24T01:54 | LAUSDT | surge | 0.0647 | 0.0646 | -0.15% |
| 2026-10-24T01:54 | KATUSDT | surge | 0.00431 | 0.00434 | +0.70% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
