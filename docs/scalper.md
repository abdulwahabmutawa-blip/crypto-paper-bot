# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-09T21:54:11+00:00 · runs 5622 · equity **$510.92** (-48.91%) · cash $0.00 · open 10/10 · round trips 1920

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-488.22 · worst day $-50.94 · trades/day 29.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1665 | 48% | -0.31% | 46% | 48% | 7% |
| bottom | 255 | 42% | -0.59% | 35% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-09T17:34 | ENJUSDT | surge | STOP | 3.2 | -3.25% | $-1.60 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-08T22:06 | BNBUSDT | bottom | 680.36 | 690.59 | +1.50% |
| 2026-11-08T23:31 | RWUSDUSDT | bottom | 0.9998 | 0.9999 | +0.01% |
| 2026-11-09T09:14 | DODOUSDT | surge | 0.02317 | 0.02319 | +0.09% |
| 2026-11-09T11:20 | RENDERUSDT | surge | 1.589 | 1.602 | +0.82% |
| 2026-11-09T12:45 | JSTUSDT | surge | 0.14623 | 0.14517 | -0.72% |
| 2026-11-09T14:44 | BIOUSDT | surge | 0.02039 | 0.0199 | -2.40% |
| 2026-11-09T14:44 | TUTUSDT | surge | 0.01768 | 0.01741 | -1.53% |
| 2026-11-09T16:42 | TSLABUSDT | surge | 377.77 | 378.73 | +0.25% |
| 2026-11-09T17:34 | QQQBUSDT | surge | 678.06 | 679.93 | +0.28% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
