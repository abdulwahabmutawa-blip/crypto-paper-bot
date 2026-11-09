# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-09T17:19:19+00:00 · runs 5606 · equity **$511.64** (-48.84%) · cash $0.00 · open 10/10 · round trips 1919

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-486.62 · worst day $-50.94 · trades/day 29.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1664 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 255 | 42% | -0.59% | 35% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-09T16:42 | HYPEUSDT | bottom | TARGET | 17.0 | +2.75% | $+1.28 |
| 2026-11-09T14:44 | AMDBUSDT | surge | TARGET | 3.0 | +2.75% | $+1.29 |
| 2026-11-09T14:44 | SPCXBUSDT | surge | TARGET | 12.5 | +2.75% | $+1.28 |
| 2026-11-09T14:10 | BIOUSDT | surge | TARGET | 1.0 | +2.75% | $+1.32 |
| 2026-11-09T12:45 | CHIPUSDT | surge | TARGET | 1.2 | +2.75% | $+1.29 |
| 2026-11-09T12:45 | ARBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.29 |
| 2026-11-09T10:29 | PORTALUSDT | surge | TARGET | 1.2 | +2.75% | $+1.28 |
| 2026-11-09T09:14 | DODOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.26 |
| 2026-11-09T09:14 | ARBUSDT | surge | TARGET | 8.0 | +2.75% | $+1.28 |
| 2026-11-09T08:39 | DODOUSDT | surge | TARGET | 8.2 | +2.75% | $+1.28 |
| 2026-11-09T07:29 | PEPEUSDT | surge | STOP | 5.0 | -3.25% | $-1.51 |
| 2026-11-09T07:29 | RENDERUSDT | surge | STOP | 5.0 | -3.25% | $-1.51 |
| 2026-11-09T07:12 | DRAMBUSDT | surge | STOP | 4.5 | -3.25% | $-1.51 |
| 2026-11-08T23:31 | QNTUSDT | bottom | TARGET | 1.2 | +2.75% | $+1.28 |
| 2026-11-08T22:06 | RSRUSDT | surge | STOP | 0.2 | -3.25% | $-1.41 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-08T22:06 | BNBUSDT | bottom | 680.36 | 687.6 | +1.06% |
| 2026-11-08T23:31 | RWUSDUSDT | bottom | 0.9998 | 0.9997 | -0.01% |
| 2026-11-09T09:14 | DODOUSDT | surge | 0.02317 | 0.02319 | +0.09% |
| 2026-11-09T11:20 | RENDERUSDT | surge | 1.589 | 1.603 | +0.88% |
| 2026-11-09T12:45 | JSTUSDT | surge | 0.14623 | 0.14519 | -0.71% |
| 2026-11-09T14:10 | ENJUSDT | surge | 0.02405 | 0.02343 | -2.58% |
| 2026-11-09T14:44 | BIOUSDT | surge | 0.02039 | 0.02016 | -1.13% |
| 2026-11-09T14:44 | TUTUSDT | surge | 0.01768 | 0.01748 | -1.13% |
| 2026-11-09T16:42 | TSLABUSDT | surge | 377.77 | 377.9 | +0.03% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
