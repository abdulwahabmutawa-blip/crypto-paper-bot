# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-30T21:48:51+00:00 · runs 4802 · equity **$583.62** (-41.64%) · cash $442.69 · open 2/10 · round trips 1686

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-415.55 · worst day $-50.94 · trades/day 30.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1469 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 217 | 42% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-29T20:14 | INJUSDT | surge | STOP | 5.5 | -3.25% | $-1.85 |
| 2026-10-29T20:14 | BEBUSDT | surge | STOP | 6.0 | -3.25% | $-1.89 |
| 2026-10-29T14:31 | SOXSBUSDT | surge | STOP | 12.5 | -3.25% | $-1.88 |
| 2026-10-29T14:13 | LSKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.60 |
| 2026-10-29T14:13 | AVAUSDT | surge | STOP | 1.0 | -3.25% | $-1.87 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-30T06:48 | TRXUSDT | bottom | 0.3341 | 0.3291 | -1.50% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
