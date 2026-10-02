# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-02T16:26:45+00:00 · runs 2364 · equity **$893.87** (-10.61%) · cash $0.00 · open 10/10 · round trips 906

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-105.31 · worst day $-50.94 · trades/day 32.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 786 | 53% | -0.07% | 49% | 44% | 7% |
| bottom | 120 | 46% | -0.38% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02T16:08 | BATUSDT | surge | STOP | 0.8 | -3.25% | $-2.70 |
| 2026-10-02T15:52 | SKYUSDT | surge | TARGET | 2.2 | +2.75% | $+2.62 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-01T23:36 | DYDXUSDT | surge | 0.15245 | 0.155 | +1.67% |
| 2026-10-02T00:45 | PLUMEUSDT | bottom | 0.01859 | 0.0184 | -1.02% |
| 2026-10-02T06:28 | CVXUSDT | surge | 2.34 | 2.33 | -0.43% |
| 2026-10-02T12:31 | CHIPUSDT | surge | 0.04492 | 0.04531 | +0.87% |
| 2026-10-02T12:49 | TRUMPUSDT | surge | 2.178 | 2.136 | -1.93% |
| 2026-10-02T13:07 | DODOUSDT | surge | 0.01872 | 0.01884 | +0.64% |
| 2026-10-02T15:29 | TSLABUSDT | surge | 371.22 | 371.32 | +0.03% |
| 2026-10-02T15:52 | SPCXBUSDT | surge | 157.12 | 156.75 | -0.24% |
| 2026-10-02T16:08 | SKYUSDT | surge | 0.09432 | 0.0939 | -0.45% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
