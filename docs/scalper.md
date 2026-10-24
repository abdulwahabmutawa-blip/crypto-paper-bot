# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-24T01:39:29+00:00 · runs 4205 · equity **$649.15** (-35.09%) · cash $128.38 · open 8/10 · round trips 1517

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-351.53 · worst day $-50.94 · trades/day 30.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1326 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 191 | 44% | -0.42% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-23T21:52 | BONKUSDT | surge | STOP | 8.5 | -3.25% | $-2.23 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 145.71 | -1.91% |
| 2026-10-23T22:26 | KMNOUSDT | surge | 0.04211 | 0.04211 | +0.00% |
| 2026-10-23T23:01 | CRCLBUSDT | bottom | 85.12 | 85.32 | +0.23% |
| 2026-10-23T23:01 | LTCUSDT | bottom | 56.84 | 57.07 | +0.40% |
| 2026-10-23T23:01 | SNDKBUSDT | bottom | 1232.71 | 1235.8 | +0.25% |
| 2026-10-24T00:11 | HYPERUSDT | surge | 0.0649 | 0.0649 | +0.00% |
| 2026-10-24T01:37 | LAUSDT | surge | 0.0628 | 0.0641 | +2.07% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
