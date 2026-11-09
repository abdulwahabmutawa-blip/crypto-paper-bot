# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-09T07:49:17+00:00 · runs 5577 · equity **$498.62** (-50.14%) · cash $135.22 · open 7/10 · round trips 1909

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.37%/trade · realized $-499.45 · worst day $-50.94 · trades/day 28.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1655 | 48% | -0.33% | 46% | 48% | 7% |
| bottom | 254 | 41% | -0.60% | 35% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-08T22:06 | MSTRBUSDT | bottom | STOP | 20.2 | -3.25% | $-1.57 |
| 2026-11-08T21:50 | DODOUSDT | surge | STOP | 4.0 | -3.25% | $-1.65 |
| 2026-11-08T21:35 | NEIROUSDT | surge | STOP | 0.5 | -3.25% | $-1.46 |
| 2026-11-08T20:48 | KORUBUSDT | surge | STOP | 2.0 | -3.25% | $-1.51 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-08T22:06 | BNBUSDT | bottom | 680.36 | 673.86 | -0.96% |
| 2026-11-08T22:06 | HYPEUSDT | bottom | 74.24 | 73.06 | -1.59% |
| 2026-11-08T23:31 | RWUSDUSDT | bottom | 0.9998 | 1.0001 | +0.03% |
| 2026-11-09T00:04 | DODOUSDT | surge | 0.02221 | 0.02238 | +0.77% |
| 2026-11-09T01:11 | ARBUSDT | surge | 0.1709 | 0.1703 | -0.35% |
| 2026-11-09T02:00 | SPCXBUSDT | surge | 137.01 | 134.19 | -2.06% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
