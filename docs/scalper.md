# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-06T18:10:52+00:00 · runs 5344 · equity **$535.35** (-46.46%) · cash $0.00 · open 10/10 · round trips 1847

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-462.30 · worst day $-50.94 · trades/day 29.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1602 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 245 | 42% | -0.57% | 36% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-05T14:53 | LUNCUSDT | surge | STOP | 23.0 | -3.25% | $-1.72 |
| 2026-11-05T12:51 | AEROUSDT | surge | STOP | 3.8 | -3.25% | $-1.65 |
| 2026-11-05T12:51 | CAKEUSDT | surge | STOP | 17.8 | -3.25% | $-1.77 |
| 2026-11-05T12:51 | BNCBUSDT | surge | STOP | 21.0 | -3.25% | $-1.72 |
| 2026-11-05T11:59 | PENDLEUSDT | surge | STOP | 19.5 | -3.25% | $-1.66 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-06T15:20 | WUSDT | surge | 0.01176 | 0.01153 | -1.96% |
| 2026-11-06T15:20 | INTWBUSDT | surge | 5.24 | 5.27 | +0.57% |
| 2026-11-06T15:20 | MUBARAKUSDT | surge | 0.04328 | 0.0435 | +0.51% |
| 2026-11-06T15:20 | SPCXBUSDT | surge | 131.8 | 131.93 | +0.10% |
| 2026-11-06T15:20 | FORMUSDT | surge | 0.2043 | 0.2007 | -1.76% |
| 2026-11-06T15:20 | RAYUSDT | surge | 1.8138 | 1.8252 | +0.63% |
| 2026-11-06T15:20 | PYTHUSDT | surge | 0.0669 | 0.06602 | -1.32% |
| 2026-11-06T15:20 | FILUSDT | surge | 0.8373 | 0.826 | -1.35% |
| 2026-11-06T15:53 | DASHUSDT | surge | 47.87 | 47.83 | -0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
