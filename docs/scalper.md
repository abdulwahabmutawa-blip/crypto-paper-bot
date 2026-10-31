# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-31T04:22:59+00:00 · runs 4826 · equity **$586.16** (-41.38%) · cash $277.39 · open 5/10 · round trips 1691

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-414.59 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1473 | 48% | -0.28% | 46% | 47% | 7% |
| bottom | 218 | 42% | -0.54% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-31T04:05 | SPKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.52 |
| 2026-10-31T03:49 | OPUSDT | surge | STOP | 3.5 | -3.25% | $-1.81 |
| 2026-10-31T02:02 | HAEDALUSDT | surge | TARGET | 1.5 | +2.75% | $+1.53 |
| 2026-10-31T00:54 | TRXUSDT | bottom | STOP | 17.8 | -3.25% | $-1.81 |
| 2026-10-30T23:46 | OPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.52 |
| 2026-10-30T15:50 | XPLUSDT | surge | TARGET | 8.8 | +2.75% | $+1.53 |
| 2026-10-30T10:41 | WLFIUSDT | surge | STOP | 3.8 | -3.25% | $-1.81 |
| 2026-10-30T07:58 | RUNEUSDT | surge | STOP | 1.2 | -3.25% | $-1.81 |
| 2026-10-30T00:41 | BTCUSDT | bottom | STOP | 21.5 | -3.25% | $-1.85 |
| 2026-10-29T20:48 | XRPUSDT | bottom | STOP | 6.5 | -3.25% | $-1.89 |
| 2026-10-29T20:48 | 牛来USDT | surge | STOP | 7.0 | -3.25% | $-1.89 |
| 2026-10-29T20:48 | 币安人生USDT | surge | STOP | 15.2 | -3.25% | $-1.85 |
| 2026-10-29T20:48 | HBARUSDT | bottom | STOP | 18.8 | -3.25% | $-1.88 |
| 2026-10-29T20:14 | UNIUSDT | surge | STOP | 5.2 | -3.25% | $-1.85 |
| 2026-10-29T20:14 | BMNRBUSDT | surge | STOP | 5.2 | -3.25% | $-1.85 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-30T23:29 | HYPEUSDT | bottom | 89.24 | 89.41 | +0.19% |
| 2026-10-30T23:46 | PENDLEUSDT | surge | 1.848 | 1.865 | +0.92% |
| 2026-10-31T04:05 | PEPEUSDT | bottom | 4.93e-06 | 4.92e-06 | -0.20% |
| 2026-10-31T04:21 | SPKUSDT | surge | 0.020105 | 0.020195 | +0.45% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
