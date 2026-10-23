# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-23T10:52:04+00:00 · runs 4152 · equity **$663.88** (-33.61%) · cash $0.00 · open 10/10 · round trips 1491

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-335.36 · worst day $-50.94 · trades/day 30.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1304 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 187 | 45% | -0.36% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-23T10:50 | ARKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.74 |
| 2026-10-23T10:34 | REZUSDT | surge | STOP | 2.8 | -3.25% | $-2.13 |
| 2026-10-23T10:18 | ARKUSDT | surge | TARGET | 0.2 | +2.75% | $+1.69 |
| 2026-10-23T09:45 | DASHUSDT | surge | STOP | 7.2 | -3.25% | $-2.07 |
| 2026-10-23T08:32 | PEPEUSDT | surge | TARGET | 2.0 | +2.75% | $+1.82 |
| 2026-10-23T07:40 | DOTUSDT | surge | TARGET | 5.0 | +2.75% | $+1.75 |
| 2026-10-23T06:49 | BTCUSDT | bottom | TIME | 24.0 | -1.08% | $-0.71 |
| 2026-10-23T06:15 | REZUSDT | surge | TARGET | 2.2 | +2.75% | $+1.77 |
| 2026-10-23T04:15 | KERNELUSDT | surge | STOP | 1.2 | -3.25% | $-2.07 |
| 2026-10-23T03:35 | REZUSDT | surge | TARGET | 0.8 | +2.75% | $+1.75 |
| 2026-10-23T02:59 | GTCUSDT | surge | STOP | 0.0 | -3.25% | $-2.07 |
| 2026-10-23T02:59 | KERNELUSDT | surge | TARGET | 0.2 | +2.75% | $+1.75 |
| 2026-10-22T15:10 | SPCXBUSDT | bottom | STOP | 6.5 | -3.25% | $-2.11 |
| 2026-10-22T15:10 | PROMUSDT | surge | STOP | 11.8 | -3.25% | $-2.10 |
| 2026-10-22T14:00 | TSLABUSDT | bottom | TARGET | 14.8 | +2.75% | $+1.71 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T02:23 | ATOMUSDT | surge | 1.766 | 1.779 | +0.74% |
| 2026-10-23T02:23 | RUNEUSDT | bottom | 0.642 | 0.639 | -0.47% |
| 2026-10-23T03:17 | STRKUSDT | bottom | 0.05291 | 0.05151 | -2.65% |
| 2026-10-23T04:15 | BCHUSDT | surge | 284.8 | 285.8 | +0.35% |
| 2026-10-23T04:32 | BNCBUSDT | surge | 5.49 | 5.55 | +1.09% |
| 2026-10-23T06:49 | BEAMXUSDT | surge | 0.003166 | 0.00313 | -1.14% |
| 2026-10-23T08:32 | ACEUSDT | surge | 0.1508 | 0.15 | -0.53% |
| 2026-10-23T10:18 | COTIUSDT | surge | 0.01167 | 0.01173 | +0.51% |
| 2026-10-23T10:50 | ARKUSDT | surge | 0.2015 | 0.2034 | +0.94% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
