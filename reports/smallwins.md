# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T09:29:47+00:00 · runs 53 · open 405 · resolved 800 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 6 | 2 | 3.0 | 83% | 41% | +3.42% | 83% | 17% | 0% | +1.5% | watch |
| range_bottom|t3|s4|h48 | 7 | 2 | 3.5 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s3|h24 | 9 | 2 | 4.5 | 89% | 54% | +2.08% | 89% | 11% | 0% | -0.5% | watch |
| range_bottom|t4|s2|h24 | 7 | 2 | 3.5 | 71% | 38% | +2.04% | 71% | 29% | 0% | +1.5% | watch |
| ignition|t3|s4|h48 | 7 | 2 | 3.5 | 86% | 61% | +1.75% | 86% | 14% | 0% | +5.5% | watch |
| momentum|t3|s4|h48 | 34 | 2 | 17.0 | 82% | 61% | +1.51% | 82% | 18% | 0% | -0.3% | watch |
| momentum|t5|s3|h48 | 27 | 2 | 13.5 | 59% | 41% | +1.49% | 59% | 41% | 0% | -14.8% | watch |
| momentum|t3|s3|h24 | 36 | 2 | 18.0 | 69% | 54% | +0.92% | 69% | 31% | 0% | -11.3% | watch |
| range_bottom|t3|s2|h12 | 17 | 2 | 8.5 | 59% | 45% | +0.87% | 35% | 12% | 53% | +0.5% | watch |
| ignition|t3|s3|h24 | 8 | 2 | 4.0 | 62% | 54% | +0.50% | 62% | 38% | 0% | -3.8% | watch |
| range_bottom|t2|s2|h8 | 24 | 2 | 12.0 | 62% | 56% | +0.45% | 38% | 8% | 54% | +1.3% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 27 | 2 | 13.5 | 59% | 58% | +0.26% | 48% | 15% | 37% | +1.5% | watch |
| momentum|t3|s2|h12 | 49 | 2 | 24.5 | 49% | 45% | +0.25% | 43% | 43% | 14% | -16.5% | watch |
| momentum|t4|s2|h24 | 39 | 2 | 19.5 | 41% | 38% | +0.21% | 41% | 59% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1|h8 | 28 | 2 | 14.0 | 54% | 50% | +0.17% | 43% | 25% | 32% | +0.0% | watch |
| momentum|t2|s2|h8 | 66 | 2 | 33.0 | 56% | 56% | +0.04% | 52% | 36% | 12% | -15.7% | fail |
| range_bottom|t1|s1|h6 | 32 | 2 | 16.0 | 53% | 62% | +0.04% | 47% | 22% | 31% | -0.4% | fail |
| momentum|t1.5|s1.5|h8 | 84 | 2 | 42.0 | 60% | 58% | +0.03% | 56% | 38% | 6% | -11.2% | watch |
| momentum|t1.5|s1|h8 | 99 | 2 | 49.5 | 48% | 50% | -0.05% | 45% | 49% | 5% | -6.2% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| ignition|t5|s3|h48 | 5 | 2 | 2.5 | 40% | 41% | -0.05% | 40% | 60% | 0% | -6.5% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t1|s1|h6 | 120 | 2 | 60.0 | 57% | 62% | -0.12% | 56% | 42% | 2% | -9.9% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |
| ignition|t1.5|s1|h8 | 14 | 2 | 7.0 | 36% | 50% | -0.29% | 36% | 57% | 7% | -5.3% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
