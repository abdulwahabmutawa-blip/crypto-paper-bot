# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-02T15:36:27+00:00 · runs 2361 · equity **$894.13** (-10.59%) · cash $0.00 · open 10/10 · round trips 904

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-105.22 · worst day $-50.94 · trades/day 32.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 784 | 53% | -0.07% | 49% | 44% | 7% |
| bottom | 120 | 46% | -0.38% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02T15:29 | MAGICUSDT | surge | TARGET | 2.5 | +2.75% | $+2.46 |
| 2026-10-02T15:11 | GALAUSDT | surge | STOP | 1.2 | -3.25% | $-2.80 |
| 2026-10-02T13:42 | BNCBUSDT | surge | TIME | 24.0 | +1.57% | $+1.33 |
| 2026-10-02T13:25 | GALAUSDT | surge | TARGET | 1.0 | +2.75% | $+2.55 |
| 2026-10-02T13:07 | AXSUSDT | surge | STOP | 0.8 | -3.25% | $-3.01 |
| 2026-10-02T12:49 | SKHYBUSDT | surge | TARGET | 19.0 | +2.75% | $+2.42 |
| 2026-10-02T12:31 | ENJUSDT | surge | TARGET | 0.0 | +2.75% | $+2.55 |
| 2026-10-02T12:31 | 币安人生USDT | surge | STOP | 2.2 | -3.25% | $-2.80 |
| 2026-10-02T12:13 | GALAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.62 |
| 2026-10-02T12:13 | AXSUSDT | surge | TARGET | 0.5 | +2.75% | $+2.62 |
| 2026-10-02T12:13 | UNIUSDT | surge | TIME | 24.0 | -0.88% | $-0.73 |
| 2026-10-02T11:20 | MAGICUSDT | surge | TARGET | 0.8 | +2.75% | $+2.22 |
| 2026-10-02T11:20 | TIAUSDT | surge | TARGET | 1.5 | +2.75% | $+2.89 |
| 2026-10-02T10:27 | WIFUSDT | surge | STOP | 3.2 | -3.25% | $-2.71 |
| 2026-10-02T10:09 | MORPHOUSDT | surge | TARGET | 9.5 | +2.75% | $+2.31 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-01T23:36 | DYDXUSDT | surge | 0.15245 | 0.15215 | -0.20% |
| 2026-10-02T00:45 | PLUMEUSDT | bottom | 0.01859 | 0.01841 | -0.97% |
| 2026-10-02T06:28 | CVXUSDT | surge | 2.34 | 2.346 | +0.26% |
| 2026-10-02T12:31 | CHIPUSDT | surge | 0.04492 | 0.045 | +0.18% |
| 2026-10-02T12:49 | TRUMPUSDT | surge | 2.178 | 2.138 | -1.84% |
| 2026-10-02T13:07 | DODOUSDT | surge | 0.01872 | 0.01875 | +0.16% |
| 2026-10-02T13:25 | SKYUSDT | surge | 0.09134 | 0.09305 | +1.87% |
| 2026-10-02T15:11 | BATUSDT | surge | 0.1012 | 0.1003 | -0.89% |
| 2026-10-02T15:29 | TSLABUSDT | surge | 371.22 | 373.14 | +0.52% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
