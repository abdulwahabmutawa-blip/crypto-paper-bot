# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-07T00:10:17+00:00 · runs 5367 · equity **$531.08** (-46.89%) · cash $0.00 · open 10/10 · round trips 1852

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-464.44 · worst day $-50.94 · trades/day 29.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1607 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 245 | 42% | -0.57% | 36% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-06T23:16 | FORMUSDT | surge | STOP | 7.8 | -3.25% | $-1.64 |
| 2026-11-06T21:23 | SPCXBUSDT | surge | TARGET | 5.8 | +2.75% | $+1.38 |
| 2026-11-06T21:07 | MRNABUSDT | surge | STOP | 2.0 | -3.25% | $-1.63 |
| 2026-11-06T18:58 | INTWBUSDT | surge | TARGET | 3.2 | +2.75% | $+1.38 |
| 2026-11-06T18:58 | WUSDT | surge | STOP | 3.2 | -3.25% | $-1.64 |
| 2026-11-06T15:53 | NBISBUSDT | surge | STOP | 0.2 | -3.25% | $-1.64 |
| 2026-11-05T17:31 | SUIUSDT | bottom | STOP | 0.2 | -3.25% | $-1.63 |
| 2026-11-05T17:31 | HYPEUSDT | bottom | STOP | 2.2 | -3.25% | $-1.66 |
| 2026-11-05T17:31 | NEARUSDT | bottom | STOP | 2.2 | -3.25% | $-1.66 |
| 2026-11-05T17:31 | BABABUSDT | surge | STOP | 12.8 | -3.25% | $-1.77 |
| 2026-11-05T17:31 | AMZNBUSDT | surge | STOP | 23.5 | -3.25% | $-1.72 |
| 2026-11-05T17:31 | MSFTBUSDT | surge | TIME | 24.0 | -2.50% | $-1.32 |
| 2026-11-05T14:53 | NILUSDT | surge | STOP | 1.2 | -3.25% | $-1.66 |
| 2026-11-05T14:53 | INJUSDT | surge | STOP | 2.8 | -3.25% | $-1.61 |
| 2026-11-05T14:53 | NVDABUSDT | bottom | STOP | 13.2 | -3.25% | $-1.76 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-06T15:20 | MUBARAKUSDT | surge | 0.04328 | 0.04264 | -1.48% |
| 2026-11-06T15:20 | RAYUSDT | surge | 1.8138 | 1.794 | -1.09% |
| 2026-11-06T15:20 | PYTHUSDT | surge | 0.0669 | 0.06639 | -0.76% |
| 2026-11-06T15:20 | FILUSDT | surge | 0.8373 | 0.8181 | -2.29% |
| 2026-11-06T15:53 | DASHUSDT | surge | 47.87 | 46.82 | -2.19% |
| 2026-11-06T18:58 | BABABUSDT | surge | 109.38 | 109.47 | +0.08% |
| 2026-11-06T21:07 | XTZUSDT | surge | 0.2777 | 0.2755 | -0.79% |
| 2026-11-06T21:23 | XRPUSDT | bottom | 1.1787 | 1.1819 | +0.27% |
| 2026-11-06T23:16 | ACTUSDT | surge | 0.01048 | 0.0104 | -0.76% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
