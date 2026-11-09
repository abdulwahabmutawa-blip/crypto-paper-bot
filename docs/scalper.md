# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-09T12:29:55+00:00 · runs 5594 · equity **$508.91** (-49.11%) · cash $0.00 · open 10/10 · round trips 1913

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-494.35 · worst day $-50.94 · trades/day 29.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1659 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 254 | 41% | -0.60% | 35% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-08T22:06 | HBARUSDT | bottom | STOP | 16.8 | -3.25% | $-1.56 |
| 2026-11-08T22:06 | DASHUSDT | surge | STOP | 17.5 | -3.25% | $-1.63 |
| 2026-11-08T22:06 | ARBUSDT | surge | STOP | 18.5 | -3.25% | $-1.56 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-08T22:06 | BNBUSDT | bottom | 680.36 | 686.64 | +0.92% |
| 2026-11-08T22:06 | HYPEUSDT | bottom | 74.24 | 73.65 | -0.79% |
| 2026-11-08T23:31 | RWUSDUSDT | bottom | 0.9998 | 0.9997 | -0.01% |
| 2026-11-09T02:00 | SPCXBUSDT | surge | 137.01 | 137.49 | +0.35% |
| 2026-11-09T09:14 | DODOUSDT | surge | 0.02317 | 0.02285 | -1.38% |
| 2026-11-09T11:20 | RENDERUSDT | surge | 1.589 | 1.616 | +1.70% |
| 2026-11-09T11:20 | ARBUSDT | surge | 0.1773 | 0.1824 | +2.88% |
| 2026-11-09T11:20 | CHIPUSDT | surge | 0.03422 | 0.03481 | +1.72% |
| 2026-11-09T11:20 | AMDBUSDT | surge | 460.81 | 468.11 | +1.58% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
