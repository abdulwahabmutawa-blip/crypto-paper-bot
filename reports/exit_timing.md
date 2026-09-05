# Exit timing — the bot grading its own exits

updated 2026-09-05T21:41:21+00:00 · 39 exits audited · early/late line ±3% · MEASUREMENT ONLY

| verdict | n |
|---|---|
| TOO_EARLY | 16 |
| TOO_LATE | 6 |
| BOTH | 13 |
| WELL_TIMED | 4 |

| exit family | n | avg giveback | avg post-24h run | well-timed |
|---|---|---|---|---|
| CLIMAX | 2 | +3.0% | +13.9% | 0 |
| FUEL GONE | 6 | +3.9% | +5.0% | 1 |
| Grok scans stale | 1 | +1.6% | +3.1% | 0 |
| Hype faded | 7 | +6.1% | +10.7% | 0 |
| MOMENTUM GONE | 2 | +0.6% | +12.3% | 0 |
| PROTECTIVE STOP | 2 | +10.1% | +1.3% | 0 |
| RATCHET | 4 | +9.2% | +3.7% | 0 |
| STALLED | 12 | +1.5% | +9.7% | 3 |
| STOP-LOSS | 2 | +11.5% | +8.8% | 0 |
| TURBO HOP | 1 | +0.8% | +9.8% | 0 |

## Market capture

- book since inception (08-15, $40 stake): **-54.2%** — trading P&L only (-$21.67 over 40 closed trades), deposits excluded
- account balance: $38.17 (of which **+$19.84 is deposited capital, not profit** — inferred as balance minus stake minus P&L; deposits are not tracked anywhere yet)
- BTC since inception: +26.7% (book gap **-80.8pp**) · last 24h +0.2%
- ETH since inception: +31.9% (book gap **-86.1pp**) · last 24h +1.1%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 1 | -20.08% | **-17.08pp** |
| flat | 16 | -1.86% | **-1.88pp** |
| green | 5 | -3.58% | **-9.06pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-08-27 | flat | -2.05% | +1.55% | -3.60pp |
| 2026-08-28 | red | -20.08% | -3.00% | -17.08pp |
| 2026-08-29 | flat | -12.84% | +0.49% | -13.33pp |
| 2026-08-30 | flat | +26.83% | -0.70% | +27.53pp |
| 2026-08-31 | flat | -5.67% | +1.16% | -6.83pp |
| 2026-09-01 | flat | +0.00% | -1.45% | +1.45pp |
| 2026-09-02 | flat | +0.00% | -0.13% | +0.13pp |
| 2026-09-03 | green | -10.87% | +5.08% | -15.95pp |
| 2026-09-04 | flat | -11.55% | -1.98% | -9.57pp |
| 2026-09-05 | flat | -6.35% | +0.24% | -6.59pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
