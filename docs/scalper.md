# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-19T04:15:20+00:00 · runs 6321 · equity **$490.21** (-50.98%) · cash $0.00 · open 10/10 · round trips 2083

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-510.83 · worst day $-50.94 · trades/day 27.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1795 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 288 | 43% | -0.46% | 37% | 43% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-19T04:14 | LUNCUSDT | surge | TARGET | 0.2 | +2.75% | $+1.25 |
| 2026-11-19T03:57 | CHIPUSDT | surge | TARGET | 10.2 | +2.75% | $+1.20 |
| 2026-11-19T02:37 | ICPUSDT | bottom | TARGET | 9.2 | +2.75% | $+1.20 |
| 2026-11-19T01:01 | TLMUSDT | bottom | TARGET | 7.8 | +2.75% | $+1.20 |
| 2026-11-19T00:45 | AMDBUSDT | surge | TARGET | 7.0 | +2.75% | $+1.20 |
| 2026-11-19T00:14 | AVGOBUSDT | surge | TIME | 24.0 | +1.44% | $+0.67 |
| 2026-11-18T16:38 | ZBTUSDT | surge | STOP | 1.2 | -3.25% | $-1.40 |
| 2026-11-18T16:38 | BMTUSDT | surge | STOP | 9.0 | -3.25% | $-1.39 |
| 2026-11-18T16:38 | TAOUSDT | surge | STOP | 13.2 | -3.25% | $-1.45 |
| 2026-11-18T16:38 | RENDERUSDT | surge | STOP | 14.0 | -3.25% | $-1.45 |
| 2026-11-18T16:38 | WUSDT | surge | TARGET | 16.2 | +2.75% | $+1.26 |
| 2026-11-18T16:38 | POLUSDT | surge | STOP | 21.8 | -3.25% | $-1.45 |
| 2026-11-18T16:38 | SPCXBUSDT | surge | TARGET | 21.8 | +2.75% | $+1.23 |
| 2026-11-18T12:51 | ALLOUSDT | surge | STOP | 3.2 | -3.25% | $-1.44 |
| 2026-11-18T09:23 | ENSOUSDT | surge | TARGET | 2.0 | +2.75% | $+1.19 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-18T07:30 | EWYBUSDT | surge | 138.73 | 139.51 | +0.56% |
| 2026-11-18T17:11 | NVDABUSDT | bottom | 151.75 | 152.44 | +0.45% |
| 2026-11-18T17:27 | PROMUSDT | surge | 5.559 | 5.596 | +0.67% |
| 2026-11-18T17:43 | WCTUSDT | surge | 0.02981 | 0.02951 | -1.01% |
| 2026-11-19T03:57 | MEGAUSDT | surge | 0.05716 | 0.05707 | -0.16% |
| 2026-11-19T03:57 | CHIPUSDT | surge | 0.03013 | 0.0303 | +0.56% |
| 2026-11-19T03:57 | ZKPUSDT | bottom | 0.0321 | 0.0321 | +0.00% |
| 2026-11-19T03:57 | ZILUSDT | bottom | 0.001006 | 0.000998 | -0.80% |
| 2026-11-19T04:14 | LUNCUSDT | surge | 4.519e-05 | 4.608e-05 | +1.97% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
