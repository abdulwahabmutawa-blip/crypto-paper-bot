# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-25T21:40:30+00:00 · runs 1784 · equity **$935.10** (-6.49%) · cash $0.00 · open 10/10 · round trips 629

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-60.02 · worst day $-50.94 · trades/day 30.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 531 | 53% | -0.02% | 50% | 42% | 8% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-25T20:25 | AMDBUSDT | surge | TIME | 24.0 | -0.02% | $-0.02 |
| 2026-09-25T19:49 | SUIUSDT | surge | TARGET | 4.8 | +2.75% | $+2.69 |
| 2026-09-25T18:38 | KMNOUSDT | surge | STOP | 2.5 | -3.25% | $-3.02 |
| 2026-09-25T18:02 | REZUSDT | surge | TARGET | 0.2 | +2.75% | $+2.59 |
| 2026-09-25T17:44 | REZUSDT | surge | TARGET | 3.5 | +2.75% | $+2.52 |
| 2026-09-25T17:08 | AEROUSDT | surge | TARGET | 0.0 | +2.75% | $+2.53 |
| 2026-09-25T16:51 | JTOUSDT | surge | TARGET | 2.8 | +2.75% | $+2.52 |
| 2026-09-25T16:51 | BABYUSDT | surge | TARGET | 6.2 | +2.75% | $+2.40 |
| 2026-09-25T16:15 | NEARUSDT | surge | TARGET | 1.8 | +2.75% | $+2.62 |
| 2026-09-25T15:57 | ENSUSDT | surge | TIME | 24.0 | -1.23% | $-1.16 |
| 2026-09-25T14:59 | AEROUSDT | surge | TARGET | 0.2 | +2.75% | $+2.62 |
| 2026-09-25T14:24 | MOVRUSDT | surge | STOP | 0.5 | -3.25% | $-3.15 |
| 2026-09-25T14:24 | ALICEUSDT | surge | STOP | 5.8 | -3.25% | $-3.25 |
| 2026-09-25T13:49 | STRKUSDT | surge | STOP | 1.2 | -3.25% | $-3.16 |
| 2026-09-25T13:49 | INTCBUSDT | surge | STOP | 10.8 | -3.25% | $-3.01 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-25T06:41 | BANKUSDT | surge | 0.0353 | 0.0343 | -2.83% |
| 2026-09-25T13:32 | VTHOUSDT | surge | 0.000782 | 0.000783 | +0.13% |
| 2026-09-25T16:15 | KORUBUSDT | surge | 21.59 | 21.55 | -0.19% |
| 2026-09-25T16:51 | SKHYBUSDT | surge | 191.35 | 191.35 | +0.00% |
| 2026-09-25T17:08 | DODOUSDT | surge | 0.01899 | 0.0187 | -1.53% |
| 2026-09-25T18:02 | REZUSDT | surge | 0.004321 | 0.004269 | -1.20% |
| 2026-09-25T18:38 | ZKUSDT | surge | 0.01278 | 0.0126 | -1.41% |
| 2026-09-25T19:49 | MUBARAKUSDT | surge | 0.05443 | 0.05374 | -1.27% |
| 2026-09-25T20:25 | AEROUSDT | surge | 0.8239 | 0.849 | +3.05% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
