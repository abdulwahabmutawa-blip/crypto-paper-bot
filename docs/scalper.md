# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-20T06:42:11+00:00 · runs 1288 · equity **$938.16** (-6.18%) · cash $0.00 · open 10/10 · round trips 459

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-47.34 · worst day $-50.94 · trades/day 28.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 376 | 54% | -0.01% | 49% | 42% | 9% |
| bottom | 83 | 42% | -0.49% | 41% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-20T06:40 | ARKUSDT | surge | TARGET | 2.2 | +2.75% | $+2.65 |
| 2026-09-20T06:07 | STXUSDT | surge | TARGET | 2.0 | +2.75% | $+2.65 |
| 2026-09-20T05:01 | GENIUSUSDT | surge | TARGET | 0.2 | +2.75% | $+2.72 |
| 2026-09-20T04:44 | ZKUSDT | surge | TARGET | 0.5 | +2.75% | $+2.65 |
| 2026-09-20T03:50 | ACEUSDT | surge | TARGET | 18.8 | +2.75% | $+3.04 |
| 2026-09-20T03:34 | ZKUSDT | surge | TARGET | 0.0 | +2.75% | $+2.52 |
| 2026-09-20T03:01 | CTSIUSDT | surge | STOP | 0.5 | -3.25% | $-2.93 |
| 2026-09-20T03:01 | KAITOUSDT | surge | STOP | 1.0 | -3.25% | $-3.14 |
| 2026-09-20T03:01 | SEIUSDT | surge | STOP | 3.5 | -3.25% | $-2.99 |
| 2026-09-20T03:01 | VETUSDT | surge | STOP | 18.5 | -3.25% | $-3.25 |
| 2026-09-20T02:44 | ALGOUSDT | surge | STOP | 1.8 | -3.25% | $-3.24 |
| 2026-09-20T02:44 | TAOUSDT | surge | STOP | 14.2 | -3.25% | $-2.90 |
| 2026-09-20T02:28 | UNIUSDT | bottom | TARGET | 4.8 | +2.75% | $+2.42 |
| 2026-09-20T01:55 | HOMEUSDT | surge | STOP | 0.8 | -3.25% | $-3.24 |
| 2026-09-20T00:50 | ALGOUSDT | surge | TARGET | 0.2 | +2.75% | $+2.67 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-19T21:56 | SOLUSDT | bottom | 110.33 | 108.24 | -1.89% |
| 2026-09-19T21:56 | DASHUSDT | bottom | 57.97 | 56.56 | -2.43% |
| 2026-09-20T02:44 | XRPUSDT | bottom | 1.3972 | 1.3795 | -1.27% |
| 2026-09-20T03:34 | LDOUSDT | surge | 0.4205 | 0.4098 | -2.54% |
| 2026-09-20T03:50 | ACEUSDT | surge | 0.1629 | 0.1584 | -2.76% |
| 2026-09-20T03:50 | ARBUSDT | surge | 0.2148 | 0.2076 | -3.35% |
| 2026-09-20T05:01 | ZKUSDT | surge | 0.01186 | 0.01175 | -0.93% |
| 2026-09-20T06:07 | ONGUSDT | surge | 0.09185 | 0.09226 | +0.45% |
| 2026-09-20T06:40 | CAKEUSDT | surge | 2.461 | 2.449 | -0.49% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
