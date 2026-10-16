# Exit timing — the bot grading its own exits

updated 2026-10-16T00:32:15+00:00 · 47 exits audited · early/late line ±3% · MEASUREMENT ONLY

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
- BTC since inception: +30.7% (book gap **-97.1pp**) · last 24h +0.2%
- ETH since inception: +29.8% (book gap **-96.2pp**) · last 24h +0.1%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 6 | -4.56% | **-1.99pp** |
| flat | 49 | -1.05% | **-1.08pp** |
| green | 8 | -2.24% | **-7.49pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-10-07 | red | +0.00% | -2.60% | +2.60pp |
| 2026-10-08 | flat | +0.00% | -1.88% | +1.88pp |
| 2026-10-09 | flat | +0.00% | +1.08% | -1.08pp |
| 2026-10-10 | flat | +0.00% | +0.43% | -0.43pp |
| 2026-10-11 | flat | +0.00% | +0.95% | -0.95pp |
| 2026-10-12 | red | +0.00% | -2.30% | +2.30pp |
| 2026-10-13 | flat | +0.00% | +1.61% | -1.61pp |
| 2026-10-14 | flat | +0.00% | -1.79% | +1.79pp |
| 2026-10-15 | flat | +0.00% | +0.69% | -0.69pp |
| 2026-10-16 | flat | +0.00% | +0.17% | -0.17pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
