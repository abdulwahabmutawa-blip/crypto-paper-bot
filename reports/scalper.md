# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-29T02:00:31+00:00 · runs 4644 · equity **$604.97** (-39.50%) · cash $115.54 · open 8/10 · round trips 1659

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-391.20 · worst day $-50.94 · trades/day 30.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1447 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 212 | 43% | -0.47% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-29T01:59 | ETHFIUSDT | surge | STOP | 1.2 | -3.25% | $-1.95 |
| 2026-10-29T01:59 | INJUSDT | surge | STOP | 1.5 | -3.25% | $-1.91 |
| 2026-10-29T01:59 | PUMPUSDT | surge | STOP | 3.0 | -3.25% | $-1.84 |
| 2026-10-29T01:59 | RAYUSDT | surge | STOP | 4.8 | -3.25% | $-1.88 |
| 2026-10-29T01:59 | EWYBUSDT | surge | TIME | 24.0 | -1.65% | $-1.06 |
| 2026-10-29T00:37 | TIAUSDT | surge | STOP | 4.0 | -3.25% | $-2.02 |
| 2026-10-29T00:04 | DRAMBUSDT | surge | STOP | 5.0 | -3.25% | $-1.97 |
| 2026-10-28T22:59 | AXTIBUSDT | surge | STOP | 0.5 | -3.25% | $-1.91 |
| 2026-10-28T22:10 | AXTIBUSDT | surge | TARGET | 0.2 | +2.75% | $+1.57 |
| 2026-10-28T21:37 | SKHYBUSDT | surge | STOP | 4.8 | -3.25% | $-1.92 |
| 2026-10-28T20:59 | BLURUSDT | surge | TARGET | 2.0 | +2.75% | $+1.55 |
| 2026-10-28T20:24 | TIAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.66 |
| 2026-10-28T19:50 | MUBUSDT | surge | TARGET | 18.0 | +2.75% | $+1.62 |
| 2026-10-28T18:58 | SNXXBUSDT | surge | TARGET | 2.0 | +2.75% | $+1.62 |
| 2026-10-28T18:41 | TUTUSDT | surge | STOP | 4.0 | -3.25% | $-1.89 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-28T12:27 | BNBUSDT | surge | 756.74 | 744.62 | -1.60% |
| 2026-10-28T13:49 | SNDKBUSDT | surge | 1381.1 | 1347.36 | -2.44% |
| 2026-10-28T13:49 | SPCXBUSDT | bottom | 144.87 | 142.99 | -1.30% |
| 2026-10-28T16:23 | LTCUSDT | surge | 58.66 | 58.64 | -0.03% |
| 2026-10-29T01:59 | SOXSBUSDT | surge | 42.98 | 43.33 | +0.81% |
| 2026-10-29T01:59 | SOXLBUSDT | bottom | 99.18 | 98.26 | -0.93% |
| 2026-10-29T01:59 | HBARUSDT | bottom | 0.07428 | 0.07354 | -1.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
