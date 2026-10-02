# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-02T11:40:26+00:00 · runs 2347 · equity **$889.15** (-11.09%) · cash $0.00 · open 10/10 · round trips 893

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.12%/trade · realized $-112.44 · worst day $-50.94 · trades/day 31.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 773 | 52% | -0.08% | 49% | 44% | 7% |
| bottom | 120 | 46% | -0.38% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02T11:20 | MAGICUSDT | surge | TARGET | 0.8 | +2.75% | $+2.22 |
| 2026-10-02T11:20 | TIAUSDT | surge | TARGET | 1.5 | +2.75% | $+2.89 |
| 2026-10-02T10:27 | WIFUSDT | surge | STOP | 3.2 | -3.25% | $-2.71 |
| 2026-10-02T10:09 | MORPHOUSDT | surge | TARGET | 9.5 | +2.75% | $+2.31 |
| 2026-10-02T09:30 | ENJUSDT | surge | TARGET | 0.2 | +2.75% | $+2.81 |
| 2026-10-02T09:14 | ENJUSDT | surge | TARGET | 0.5 | +2.75% | $+2.74 |
| 2026-10-02T08:24 | ZKUSDT | surge | TARGET | 2.0 | +2.75% | $+2.66 |
| 2026-10-02T06:45 | RESOLVUSDT | surge | STOP | 1.0 | -3.25% | $-2.80 |
| 2026-10-02T06:28 | KORUBUSDT | surge | TARGET | 3.8 | +2.75% | $+2.45 |
| 2026-10-02T06:12 | DEXEUSDT | surge | TARGET | 2.0 | +2.75% | $+2.59 |
| 2026-10-02T05:39 | SUPERUSDT | surge | STOP | 0.8 | -3.25% | $-2.89 |
| 2026-10-02T04:33 | PEPEUSDT | surge | TARGET | 12.8 | +2.75% | $+2.38 |
| 2026-10-02T03:54 | RESOLVUSDT | surge | TARGET | 0.0 | +2.75% | $+2.52 |
| 2026-10-02T03:37 | SUPERUSDT | surge | TARGET | 1.0 | +2.75% | $+2.45 |
| 2026-10-02T02:28 | LSKUSDT | surge | STOP | 0.8 | -3.25% | $-3.01 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-01T12:13 | UNIUSDT | surge | 9.062 | 9.042 | -0.22% |
| 2026-10-01T13:23 | BNCBUSDT | surge | 6.03 | 6.1 | +1.16% |
| 2026-10-01T17:36 | SKHYBUSDT | surge | 188.77 | 192.66 | +2.06% |
| 2026-10-01T23:36 | DYDXUSDT | surge | 0.15245 | 0.15066 | -1.17% |
| 2026-10-02T00:45 | PLUMEUSDT | bottom | 0.01859 | 0.01864 | +0.27% |
| 2026-10-02T06:28 | CVXUSDT | surge | 2.34 | 2.309 | -1.32% |
| 2026-10-02T10:09 | 币安人生USDT | surge | 0.523 | 0.5196 | -0.65% |
| 2026-10-02T11:20 | AXSUSDT | surge | 1.241 | 1.25 | +0.73% |
| 2026-10-02T11:20 | GALAUSDT | surge | 0.002507 | 0.002529 | +0.88% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
