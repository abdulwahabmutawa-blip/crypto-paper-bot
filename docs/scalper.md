# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-11T16:30:59+00:00 · runs 3132 · equity **$789.57** (-21.04%) · cash $0.00 · open 10/10 · round trips 1170

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.20%/trade · realized $-215.95 · worst day $-50.94 · trades/day 31.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1027 | 50% | -0.17% | 48% | 45% | 7% |
| bottom | 143 | 45% | -0.42% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-11T16:29 | MEGAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.20 |
| 2026-10-11T16:29 | ADAUSDT | bottom | TARGET | 12.5 | +2.75% | $+2.02 |
| 2026-10-11T15:40 | ALGOUSDT | surge | TARGET | 0.2 | +2.75% | $+2.13 |
| 2026-10-11T15:40 | MEGAUSDT | surge | TARGET | 1.2 | +2.75% | $+2.16 |
| 2026-10-11T15:06 | IOUSDT | surge | TARGET | 0.5 | +2.75% | $+2.16 |
| 2026-10-11T15:06 | NILUSDT | surge | STOP | 0.8 | -3.25% | $-2.51 |
| 2026-10-11T14:16 | PLUMEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.12 |
| 2026-10-11T14:00 | 币安人生USDT | surge | TARGET | 1.8 | +2.75% | $+2.23 |
| 2026-10-11T14:00 | BOMEUSDT | surge | STOP | 3.0 | -3.25% | $-2.46 |
| 2026-10-11T13:43 | ACHUSDT | surge | TARGET | 5.0 | +2.75% | $+2.11 |
| 2026-10-11T13:43 | AVAXUSDT | bottom | TARGET | 9.8 | +2.75% | $+2.02 |
| 2026-10-11T12:04 | DUSKUSDT | surge | TARGET | 15.8 | +2.75% | $+2.17 |
| 2026-10-11T10:42 | NEOUSDT | surge | STOP | 1.5 | -3.25% | $-2.55 |
| 2026-10-11T09:49 | MUBARAKUSDT | surge | STOP | 0.2 | -3.25% | $-2.53 |
| 2026-10-11T09:49 | BOMEUSDT | surge | TARGET | 0.8 | +2.75% | $+2.15 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-10T22:49 | CAKEUSDT | surge | 2.261 | 2.306 | +1.99% |
| 2026-10-11T03:38 | TRXUSDT | bottom | 0.3303 | 0.3312 | +0.27% |
| 2026-10-11T09:49 | ARBUSDT | surge | 0.1995 | 0.2001 | +0.30% |
| 2026-10-11T09:49 | BIOUSDT | surge | 0.02956 | 0.03012 | +1.89% |
| 2026-10-11T14:16 | PLUMEUSDT | surge | 0.02052 | 0.02057 | +0.24% |
| 2026-10-11T15:06 | ATOMUSDT | surge | 2.017 | 2.009 | -0.40% |
| 2026-10-11T15:40 | XLMUSDT | surge | 0.202 | 0.2047 | +1.34% |
| 2026-10-11T16:29 | 币安人生USDT | surge | 0.6115 | 0.6254 | +2.27% |
| 2026-10-11T16:29 | TRBUSDT | surge | 19.73 | 19.58 | -0.76% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
