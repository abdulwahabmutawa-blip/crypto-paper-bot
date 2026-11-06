# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-06T15:38:19+00:00 · runs 5338 · equity **$532.29** (-46.77%) · cash $0.00 · open 10/10 · round trips 1846

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-460.67 · worst day $-50.94 · trades/day 29.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1601 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 245 | 42% | -0.57% | 36% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-05T08:45 | 1000CATUSDT | surge | STOP | 0.0 | -3.25% | $-1.70 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-06T15:20 | WUSDT | surge | 0.01176 | 0.0116 | -1.36% |
| 2026-11-06T15:20 | INTWBUSDT | surge | 5.24 | 5.12 | -2.29% |
| 2026-11-06T15:20 | MUBARAKUSDT | surge | 0.04328 | 0.04269 | -1.36% |
| 2026-11-06T15:20 | SPCXBUSDT | surge | 131.8 | 130.96 | -0.64% |
| 2026-11-06T15:20 | FORMUSDT | surge | 0.2043 | 0.2006 | -1.81% |
| 2026-11-06T15:20 | RAYUSDT | surge | 1.8138 | 1.7832 | -1.69% |
| 2026-11-06T15:20 | PYTHUSDT | surge | 0.0669 | 0.06637 | -0.79% |
| 2026-11-06T15:20 | FILUSDT | surge | 0.8373 | 0.8286 | -1.04% |
| 2026-11-06T15:20 | NBISBUSDT | surge | 130.85 | 126.91 | -3.01% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
