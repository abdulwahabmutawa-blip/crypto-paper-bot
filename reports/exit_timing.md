# Exit timing — the bot grading its own exits

updated 2026-09-25T03:05:42+00:00 · 47 exits audited · early/late line ±3% · MEASUREMENT ONLY

| verdict | n |
|---|---|
| TOO_EARLY | 17 |
| TOO_LATE | 9 |
| BOTH | 17 |
| WELL_TIMED | 4 |

| exit family | n | avg giveback | avg post-24h run | well-timed |
|---|---|---|---|---|
| CLIMAX | 2 | +3.0% | +13.9% | 0 |
| FUEL GONE | 6 | +3.9% | +5.0% | 1 |
| Grok scans stale | 1 | +1.6% | +3.1% | 0 |
| Hype faded | 7 | +6.1% | +10.7% | 0 |
| MOMENTUM GONE | 2 | +0.6% | +12.3% | 0 |
| PROTECTIVE STOP | 9 | +6.3% | +7.0% | 0 |
| RATCHET | 4 | +9.2% | +3.7% | 0 |
| STALLED | 12 | +1.5% | +9.7% | 3 |
| STOP-LOSS | 2 | +11.5% | +8.8% | 0 |
| TARGET | 1 | +1.9% | +13.9% | 0 |
| TURBO HOP | 1 | +0.8% | +9.8% | 0 |

## Market capture

- book since inception (08-15, $40 stake): **-66.4%** — trading P&L only (-$26.55 over 47 closed trades), deposits excluded
- account balance: $33.15 (of which **+$19.70 is deposited capital, not profit** — inferred as balance minus stake minus P&L; deposits are not tracked anywhere yet)
- BTC since inception: +33.7% (book gap **-100.1pp**) · last 24h -0.1%
- ETH since inception: +42.2% (book gap **-108.6pp**) · last 24h -0.4%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 4 | -6.85% | **-4.20pp** |
| flat | 31 | -1.65% | **-1.69pp** |
| green | 7 | -2.56% | **-8.26pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-09-16 | flat | +0.00% | +0.74% | -0.74pp |
| 2026-09-17 | flat | +0.00% | +0.28% | -0.28pp |
| 2026-09-18 | green | +0.00% | +5.85% | -5.85pp |
| 2026-09-19 | flat | +0.00% | +0.45% | -0.45pp |
| 2026-09-20 | flat | +0.00% | -0.09% | +0.09pp |
| 2026-09-21 | green | +0.00% | +6.70% | -6.70pp |
| 2026-09-22 | flat | +0.00% | -0.48% | +0.48pp |
| 2026-09-23 | red | +0.00% | -2.10% | +2.10pp |
| 2026-09-24 | flat | +0.00% | +0.01% | -0.01pp |
| 2026-09-25 | flat | +0.00% | -0.13% | +0.13pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
