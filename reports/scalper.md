# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-09T14:29:02+00:00 · runs 5601 · equity **$510.12** (-48.99%) · cash $0.00 · open 10/10 · round trips 1916

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-490.46 · worst day $-50.94 · trades/day 29.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1662 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 254 | 41% | -0.60% | 35% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-08T22:06 | SNDKBUSDT | surge | STOP | 2.2 | -3.25% | $-1.66 |
| 2026-11-08T22:06 | GRAMUSDT | bottom | STOP | 4.8 | -3.25% | $-1.51 |
| 2026-11-08T22:06 | PEPEUSDT | surge | STOP | 8.5 | -3.25% | $-1.48 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-08T22:06 | BNBUSDT | bottom | 680.36 | 684.91 | +0.67% |
| 2026-11-08T22:06 | HYPEUSDT | bottom | 74.24 | 74.35 | +0.15% |
| 2026-11-08T23:31 | RWUSDUSDT | bottom | 0.9998 | 0.9999 | +0.01% |
| 2026-11-09T02:00 | SPCXBUSDT | surge | 137.01 | 137.05 | +0.03% |
| 2026-11-09T09:14 | DODOUSDT | surge | 0.02317 | 0.02299 | -0.78% |
| 2026-11-09T11:20 | RENDERUSDT | surge | 1.589 | 1.593 | +0.25% |
| 2026-11-09T11:20 | AMDBUSDT | surge | 460.81 | 475.52 | +3.19% |
| 2026-11-09T12:45 | JSTUSDT | surge | 0.14623 | 0.14479 | -0.98% |
| 2026-11-09T14:10 | ENJUSDT | surge | 0.02405 | 0.02376 | -1.21% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
