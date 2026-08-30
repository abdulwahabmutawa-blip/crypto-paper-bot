# Exit timing — the bot grading its own exits

updated 2026-08-30T04:26:43+00:00 · 29 exits audited · early/late line ±3% · MEASUREMENT ONLY

| verdict | n |
|---|---|
| TOO_EARLY | 13 |
| TOO_LATE | 2 |
| BOTH | 10 |
| WELL_TIMED | 4 |

| exit family | n | avg giveback | avg post-24h run | well-timed |
|---|---|---|---|---|
| FUEL GONE | 2 | +3.9% | +2.4% | 1 |
| Grok scans stale | 1 | +1.6% | +3.1% | 0 |
| Hype faded | 7 | +6.1% | +10.7% | 0 |
| MOMENTUM GONE | 2 | +0.6% | +12.3% | 0 |
| RATCHET | 2 | +8.9% | +6.6% | 0 |
| STALLED | 12 | +1.5% | +9.7% | 3 |
| STOP-LOSS | 2 | +11.5% | +8.8% | 0 |
| TURBO HOP | 1 | +0.8% | +9.8% | 0 |

## Market capture

- book since inception (08-15, $40 stake): **-48.1%** — trading P&L only (-$19.24 over 32 closed trades), deposits excluded
- account balance: $46.41 (of which **+$25.65 is deposited capital, not profit** — inferred as balance minus stake minus P&L; deposits are not tracked anywhere yet)
- BTC since inception: +23.9% (book gap **-72.0pp**) · last 24h -0.1%
- ETH since inception: +30.5% (book gap **-78.6pp**) · last 24h -0.1%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 1 | -20.08% | **-17.08pp** |
| flat | 11 | -3.01% | **-3.27pp** |
| green | 4 | -1.76% | **-7.34pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-08-21 | green | +5.00% | +7.27% | -2.27pp |
| 2026-08-22 | flat | -4.66% | -1.61% | -3.05pp |
| 2026-08-23 | flat | -0.66% | +0.86% | -1.52pp |
| 2026-08-24 | flat | +0.00% | +1.62% | -1.62pp |
| 2026-08-25 | flat | +0.00% | -0.57% | +0.57pp |
| 2026-08-26 | flat | +0.00% | +0.62% | -0.62pp |
| 2026-08-27 | flat | -2.05% | +1.55% | -3.60pp |
| 2026-08-28 | red | -20.08% | -3.00% | -17.08pp |
| 2026-08-29 | flat | -12.84% | +0.49% | -13.33pp |
| 2026-08-30 | flat | +0.00% | -0.13% | +0.13pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
