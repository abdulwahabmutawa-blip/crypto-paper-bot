# Exit timing — the bot grading its own exits

updated 2026-08-25T06:32:43+00:00 · 25 exits audited · early/late line ±3% · MEASUREMENT ONLY

| verdict | n |
|---|---|
| TOO_EARLY | 11 |
| TOO_LATE | 1 |
| BOTH | 9 |
| WELL_TIMED | 4 |

| exit family | n | avg giveback | avg post-24h run | well-timed |
|---|---|---|---|---|
| FUEL GONE | 1 | +2.1% | +1.3% | 1 |
| Hype faded | 7 | +6.1% | +10.7% | 0 |
| MOMENTUM GONE | 2 | +0.6% | +12.3% | 0 |
| RATCHET | 2 | +8.9% | +6.6% | 0 |
| STALLED | 12 | +1.5% | +9.7% | 3 |
| STOP-LOSS | 1 | +15.5% | +16.3% | 0 |

## Market capture

- book since inception (08-15, $40 stake): **-23.9%** — trading P&L only (-$9.58 over 25 closed trades), deposits excluded
- account balance: $52.38 (of which **+$21.96 is deposited capital, not profit** — inferred as balance minus stake minus P&L; deposits are not tracked anywhere yet)
- BTC since inception: +28.1% (book gap **-52.0pp**) · last 24h +2.2%
- ETH since inception: +33.1% (book gap **-57.0pp**) · last 24h +0.9%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| flat | 6 | -3.03% | **-3.19pp** |
| green | 5 | -1.41% | **-6.31pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-08-16 | flat | -16.00% | -0.29% | -15.71pp |
| 2026-08-17 | green | -2.34% | +2.59% | -4.94pp |
| 2026-08-18 | flat | +3.08% | +0.30% | +2.78pp |
| 2026-08-19 | green | -8.44% | +7.12% | -15.56pp |
| 2026-08-20 | green | -1.25% | +5.32% | -6.58pp |
| 2026-08-21 | green | +5.00% | +7.27% | -2.27pp |
| 2026-08-22 | flat | -4.66% | -1.61% | -3.05pp |
| 2026-08-23 | flat | -0.66% | +0.86% | -1.52pp |
| 2026-08-24 | flat | +0.00% | +1.62% | -1.62pp |
| 2026-08-25 | green | +0.00% | +2.20% | -2.20pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
