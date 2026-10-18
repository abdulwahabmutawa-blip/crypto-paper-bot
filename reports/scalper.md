# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-18T20:56:40+00:00 · runs 3751 · equity **$651.49** (-34.85%) · cash $252.19 · open 6/10 · round trips 1385

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-346.36 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1211 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 174 | 44% | -0.41% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-18T20:37 | RWUSDUSDT | bottom | TIME | 24.0 | -0.24% | $-0.17 |
| 2026-10-18T19:44 | AMPUSDT | surge | STOP | 0.2 | -3.25% | $-2.02 |
| 2026-10-18T19:09 | NXPCUSDT | surge | STOP | 0.0 | -3.25% | $-2.02 |
| 2026-10-18T19:09 | AMPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.71 |
| 2026-10-18T18:16 | NXPCUSDT | surge | TARGET | 0.2 | +2.75% | $+1.70 |
| 2026-10-18T17:59 | HBARUSDT | surge | STOP | 10.8 | -3.25% | $-2.12 |
| 2026-10-18T16:31 | AMPUSDT | surge | STOP | 1.0 | -3.25% | $-2.01 |
| 2026-10-18T14:14 | OGNUSDT | surge | STOP | 0.8 | -3.25% | $-2.05 |
| 2026-10-18T14:14 | MORPHOUSDT | surge | STOP | 10.8 | -3.25% | $-2.02 |
| 2026-10-18T13:57 | SUSDT | surge | STOP | 1.2 | -3.25% | $-2.12 |
| 2026-10-18T13:24 | MEGAUSDT | surge | STOP | 3.5 | -3.25% | $-2.13 |
| 2026-10-18T12:50 | ERAUSDT | surge | STOP | 0.8 | -3.25% | $-2.12 |
| 2026-10-18T11:45 | ERAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.77 |
| 2026-10-18T11:28 | AMPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.75 |
| 2026-10-18T10:34 | SENTUSDT | surge | STOP | 0.2 | -3.25% | $-2.10 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-18T01:44 | TRXUSDT | bottom | 0.3338 | 0.3321 | -0.51% |
| 2026-10-18T03:05 | MSTRBUSDT | surge | 137.28 | 134.47 | -2.05% |
| 2026-10-18T10:17 | ALTUSDT | bottom | 0.00843 | 0.00841 | -0.24% |
| 2026-10-18T18:16 | SOXSBUSDT | surge | 52.08 | 51.97 | -0.21% |
| 2026-10-18T20:37 | UNIUSDT | bottom | 6.862 | 6.833 | -0.42% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
