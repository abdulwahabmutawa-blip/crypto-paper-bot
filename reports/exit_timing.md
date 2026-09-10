# Exit timing — the bot grading its own exits

updated 2026-09-10T11:26:18+00:00 · 45 exits audited · early/late line ±3% · MEASUREMENT ONLY

| verdict | n |
|---|---|
| TOO_EARLY | 17 |
| TOO_LATE | 9 |
| BOTH | 15 |
| WELL_TIMED | 4 |

| exit family | n | avg giveback | avg post-24h run | well-timed |
|---|---|---|---|---|
| CLIMAX | 2 | +3.0% | +13.9% | 0 |
| FUEL GONE | 6 | +3.9% | +5.0% | 1 |
| Grok scans stale | 1 | +1.6% | +3.1% | 0 |
| Hype faded | 7 | +6.1% | +10.7% | 0 |
| MOMENTUM GONE | 2 | +0.6% | +12.3% | 0 |
| PROTECTIVE STOP | 7 | +6.7% | +3.3% | 0 |
| RATCHET | 4 | +9.2% | +3.7% | 0 |
| STALLED | 12 | +1.5% | +9.7% | 3 |
| STOP-LOSS | 2 | +11.5% | +8.8% | 0 |
| TARGET | 1 | +1.9% | +13.9% | 0 |
| TURBO HOP | 1 | +0.8% | +9.8% | 0 |

## Market capture

- book since inception (08-15, $40 stake): **-66.4%** — trading P&L only (-$26.55 over 47 closed trades), deposits excluded
- account balance: $33.15 (of which **+$19.70 is deposited capital, not profit** — inferred as balance minus stake minus P&L; deposits are not tracked anywhere yet)
- BTC since inception: +23.7% (book gap **-90.1pp**) · last 24h -0.4%
- ETH since inception: +31.1% (book gap **-97.4pp**) · last 24h -0.0%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 1 | -20.08% | **-17.08pp** |
| flat | 21 | -2.79% | **-2.69pp** |
| green | 5 | -3.58% | **-9.06pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-09-01 | flat | +0.00% | -1.45% | +1.45pp |
| 2026-09-02 | flat | +0.00% | -0.13% | +0.13pp |
| 2026-09-03 | green | -10.87% | +5.08% | -15.95pp |
| 2026-09-04 | flat | -11.55% | -1.98% | -9.57pp |
| 2026-09-05 | flat | -6.35% | +0.21% | -6.56pp |
| 2026-09-06 | flat | -12.56% | +0.64% | -13.20pp |
| 2026-09-07 | flat | +0.00% | -1.53% | +1.53pp |
| 2026-09-08 | flat | +4.50% | -0.83% | +5.33pp |
| 2026-09-09 | flat | -13.39% | -0.19% | -13.20pp |
| 2026-09-10 | flat | -7.31% | -0.40% | -6.91pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
