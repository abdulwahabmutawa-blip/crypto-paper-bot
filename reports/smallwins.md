# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T12:45:08+00:00 · runs 66 · open 433 · resolved 1044 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 8 | 2 | 4.0 | 88% | 41% | +3.75% | 88% | 12% | 0% | +1.5% | watch |
| range_bottom|t3|s4|h48 | 9 | 2 | 4.5 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t4|s2|h24 | 9 | 2 | 4.5 | 78% | 38% | +2.42% | 78% | 22% | 0% | +1.5% | watch |
| range_bottom|t3|s3|h24 | 11 | 2 | 5.5 | 91% | 54% | +2.20% | 91% | 9% | 0% | -0.5% | watch |
| ignition|t3|s4|h48 | 7 | 2 | 3.5 | 86% | 61% | +1.75% | 86% | 14% | 0% | +5.5% | watch |
| momentum|t3|s4|h48 | 49 | 2 | 24.5 | 80% | 61% | +1.32% | 80% | 20% | 0% | -0.3% | watch |
| momentum|t5|s3|h48 | 36 | 2 | 18.0 | 53% | 41% | +0.97% | 53% | 47% | 0% | -14.8% | watch |
| momentum|t3|s3|h24 | 53 | 2 | 26.5 | 68% | 54% | +0.83% | 68% | 32% | 0% | -11.3% | watch |
| range_bottom|t3|s2|h12 | 22 | 2 | 11.0 | 55% | 45% | +0.81% | 32% | 9% | 59% | +0.5% | watch |
| ignition|t3|s3|h24 | 8 | 2 | 4.0 | 62% | 54% | +0.50% | 62% | 38% | 0% | -3.8% | watch |
| range_bottom|t2|s2|h8 | 26 | 2 | 13.0 | 62% | 56% | +0.43% | 35% | 8% | 58% | +1.3% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 28 | 2 | 14.0 | 57% | 58% | +0.24% | 46% | 14% | 39% | +1.5% | fail |
| momentum|t4|s2|h24 | 56 | 2 | 28.0 | 41% | 38% | +0.21% | 41% | 59% | 0% | -17.2% | watch |
| momentum|t3|s2|h12 | 68 | 2 | 34.0 | 47% | 45% | +0.16% | 43% | 46% | 12% | -16.5% | watch |
| range_bottom|t1.5|s1|h8 | 29 | 2 | 14.5 | 52% | 50% | +0.16% | 41% | 24% | 34% | +0.0% | watch |
| momentum|t2|s2|h8 | 91 | 2 | 45.5 | 58% | 56% | +0.12% | 55% | 36% | 9% | -15.7% | watch |
| range_bottom|t1|s1|h6 | 34 | 2 | 17.0 | 53% | 62% | +0.05% | 47% | 21% | 32% | -0.4% | fail |
| momentum|t1.5|s1.5|h8 | 121 | 2 | 60.5 | 59% | 58% | +0.01% | 56% | 40% | 4% | -11.2% | watch |
| momentum|t1.5|s1|h8 | 138 | 2 | 69.0 | 49% | 50% | -0.04% | 46% | 50% | 4% | -6.2% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| ignition|t5|s3|h48 | 5 | 2 | 2.5 | 40% | 41% | -0.05% | 40% | 60% | 0% | -6.5% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t1|s1|h6 | 166 | 2 | 83.0 | 57% | 62% | -0.12% | 56% | 43% | 1% | -15.4% | fail |
| ignition|t1.5|s1.5|h8 | 12 | 2 | 6.0 | 50% | 58% | -0.13% | 50% | 42% | 8% | -2.5% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1|h8 | 14 | 2 | 7.0 | 36% | 50% | -0.29% | 36% | 57% | 7% | -5.3% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
