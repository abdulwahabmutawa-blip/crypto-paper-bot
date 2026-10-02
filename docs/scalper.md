# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-02T12:51:38+00:00 · runs 2351 · equity **$895.59** (-10.44%) · cash $0.00 · open 10/10 · round trips 899

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.12%/trade · realized $-105.75 · worst day $-50.94 · trades/day 32.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 779 | 53% | -0.07% | 49% | 44% | 7% |
| bottom | 120 | 46% | -0.38% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-02T09:30 | ENJUSDT | surge | TARGET | 0.2 | +2.75% | $+2.81 |
| 2026-10-02T09:14 | ENJUSDT | surge | TARGET | 0.5 | +2.75% | $+2.74 |
| 2026-10-02T08:24 | ZKUSDT | surge | TARGET | 2.0 | +2.75% | $+2.66 |
| 2026-10-02T06:45 | RESOLVUSDT | surge | STOP | 1.0 | -3.25% | $-2.80 |
| 2026-10-02T06:28 | KORUBUSDT | surge | TARGET | 3.8 | +2.75% | $+2.45 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-01T13:23 | BNCBUSDT | surge | 6.03 | 6.12 | +1.49% |
| 2026-10-01T23:36 | DYDXUSDT | surge | 0.15245 | 0.15159 | -0.56% |
| 2026-10-02T00:45 | PLUMEUSDT | bottom | 0.01859 | 0.0183 | -1.56% |
| 2026-10-02T06:28 | CVXUSDT | surge | 2.34 | 2.362 | +0.94% |
| 2026-10-02T12:13 | AXSUSDT | surge | 1.281 | 1.26 | -1.64% |
| 2026-10-02T12:13 | GALAUSDT | surge | 0.002624 | 0.002683 | +2.25% |
| 2026-10-02T12:31 | MAGICUSDT | surge | 0.0601 | 0.0602 | +0.17% |
| 2026-10-02T12:31 | CHIPUSDT | surge | 0.04492 | 0.04493 | +0.02% |
| 2026-10-02T12:49 | TRUMPUSDT | surge | 2.178 | 2.187 | +0.41% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
