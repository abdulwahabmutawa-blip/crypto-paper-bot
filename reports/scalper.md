# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-08T20:02:59+00:00 · runs 5533 · equity **$519.84** (-48.02%) · cash $0.00 · open 10/10 · round trips 1894

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-479.19 · worst day $-50.94 · trades/day 29.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1644 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 250 | 42% | -0.58% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-08T19:30 | ETHFIUSDT | surge | TIME | 24.0 | -0.69% | $-0.35 |
| 2026-11-08T17:57 | BEAMXUSDT | surge | STOP | 5.2 | -3.25% | $-1.56 |
| 2026-11-08T17:41 | RSRUSDT | surge | STOP | 0.5 | -3.25% | $-1.70 |
| 2026-11-08T17:10 | STRKUSDT | bottom | STOP | 13.5 | -3.25% | $-1.56 |
| 2026-11-08T16:54 | RSRUSDT | surge | TARGET | 1.8 | +2.75% | $+1.40 |
| 2026-11-08T14:53 | RSRUSDT | surge | TARGET | 3.2 | +2.75% | $+1.36 |
| 2026-11-08T13:15 | STXUSDT | surge | STOP | 20.5 | -3.25% | $-1.53 |
| 2026-11-08T12:25 | BMTUSDT | surge | STOP | 0.8 | -3.25% | $-1.61 |
| 2026-11-08T11:20 | RSRUSDT | surge | TARGET | 3.8 | +2.75% | $+1.34 |
| 2026-11-08T10:14 | BMTUSDT | surge | TARGET | 0.5 | +2.75% | $+1.32 |
| 2026-11-08T09:40 | BEAMXUSDT | surge | STOP | 0.8 | -3.25% | $-1.61 |
| 2026-11-08T08:38 | NIGHTUSDT | surge | TIME | 24.0 | -1.05% | $-0.52 |
| 2026-11-08T07:05 | RSRUSDT | surge | TARGET | 15.8 | +2.75% | $+1.30 |
| 2026-11-08T05:00 | XLMUSDT | bottom | TIME | 24.0 | -1.70% | $-0.83 |
| 2026-11-08T04:25 | AEROUSDT | surge | STOP | 5.8 | -3.25% | $-1.69 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-08T01:34 | MSTRBUSDT | bottom | 126.98 | 127.97 | +0.78% |
| 2026-11-08T03:23 | ARBUSDT | surge | 0.1708 | 0.1669 | -2.28% |
| 2026-11-08T04:25 | DASHUSDT | surge | 47.81 | 47.57 | -0.50% |
| 2026-11-08T05:00 | HBARUSDT | bottom | 0.06644 | 0.06698 | +0.81% |
| 2026-11-08T13:15 | PEPEUSDT | surge | 5.02e-06 | 5.07e-06 | +1.00% |
| 2026-11-08T17:10 | GRAMUSDT | bottom | 1.05 | 1.049 | -0.10% |
| 2026-11-08T17:41 | DODOUSDT | surge | 0.02233 | 0.02193 | -1.79% |
| 2026-11-08T18:44 | KORUBUSDT | surge | 7.17 | 7.2 | +0.42% |
| 2026-11-08T19:30 | SNDKBUSDT | surge | 849.18 | 847.65 | -0.18% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
