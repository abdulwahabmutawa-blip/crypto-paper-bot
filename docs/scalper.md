# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-20T18:05:25+00:00 · runs 3915 · equity **$674.82** (-32.52%) · cash $0.00 · open 10/10 · round trips 1438

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-326.24 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1256 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-20T17:31 | IOUSDT | surge | TARGET | 7.0 | +2.75% | $+1.71 |
| 2026-10-20T17:14 | THETAUSDT | surge | TARGET | 1.8 | +2.75% | $+1.83 |
| 2026-10-20T16:41 | COMPUSDT | surge | TARGET | 1.0 | +2.75% | $+1.83 |
| 2026-10-20T16:25 | BEAMXUSDT | surge | STOP | 3.0 | -3.25% | $-2.06 |
| 2026-10-20T15:34 | ICPUSDT | surge | STOP | 0.5 | -3.25% | $-2.25 |
| 2026-10-20T15:34 | ZROUSDT | surge | STOP | 1.0 | -3.25% | $-2.17 |
| 2026-10-20T15:34 | GOOGLBUSDT | surge | TIME | 24.0 | -1.36% | $-0.83 |
| 2026-10-20T15:18 | RENDERUSDT | surge | STOP | 0.2 | -3.25% | $-2.25 |
| 2026-10-20T15:18 | TIAUSDT | surge | STOP | 2.2 | -3.25% | $-2.23 |
| 2026-10-20T14:45 | VELODROMEUSDT | surge | TARGET | 0.0 | +2.75% | $+1.83 |
| 2026-10-20T14:45 | BNCBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.87 |
| 2026-10-20T14:29 | SNDKBUSDT | bottom | TARGET | 3.2 | +2.75% | $+1.81 |
| 2026-10-20T14:29 | SKYUSDT | surge | TARGET | 11.0 | +2.75% | $+1.74 |
| 2026-10-20T14:29 | TRUMPUSDT | bottom | TARGET | 13.5 | +2.75% | $+1.77 |
| 2026-10-20T14:29 | HBARUSDT | bottom | TARGET | 17.8 | +2.75% | $+1.83 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-20T14:29 | RSRUSDT | surge | 0.00192 | 0.001927 | +0.36% |
| 2026-10-20T14:29 | CRCLBUSDT | surge | 85.2 | 86.1 | +1.06% |
| 2026-10-20T15:34 | TSLABUSDT | surge | 374.56 | 374.47 | -0.02% |
| 2026-10-20T15:34 | JTOUSDT | surge | 0.4772 | 0.4808 | +0.75% |
| 2026-10-20T15:34 | CFXUSDT | surge | 0.05393 | 0.05416 | +0.43% |
| 2026-10-20T16:25 | BONKUSDT | surge | 3.04e-06 | 3.06e-06 | +0.66% |
| 2026-10-20T16:41 | REZUSDT | surge | 0.003796 | 0.003811 | +0.40% |
| 2026-10-20T17:14 | ACEUSDT | surge | 0.1539 | 0.151 | -1.88% |
| 2026-10-20T17:31 | DOGEUSDT | surge | 0.08115 | 0.08114 | -0.01% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
