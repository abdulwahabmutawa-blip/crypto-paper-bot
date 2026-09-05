# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T05:23:07+00:00 · runs 48 · open 283 · resolved 513 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 4 | 2 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t5|s3|h48 | 3 | 2 | 1.5 | 67% | 41% | +2.08% | 67% | 33% | 0% | +1.5% | watch |
| momentum|t3|s4|h48 | 18 | 2 | 9.0 | 83% | 61% | +1.58% | 83% | 17% | 0% | -0.3% | watch |
| range_bottom|t3|s3|h24 | 5 | 2 | 2.5 | 80% | 54% | +1.55% | 80% | 20% | 0% | -0.5% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| range_bottom|t4|s2|h24 | 5 | 2 | 2.5 | 60% | 38% | +1.35% | 60% | 40% | 0% | +1.5% | watch |
| range_bottom|t3|s2|h12 | 7 | 2 | 3.5 | 57% | 45% | +0.91% | 57% | 29% | 14% | +0.5% | watch |
| ignition|t3|s3|h24 | 6 | 2 | 3.0 | 67% | 54% | +0.75% | 67% | 33% | 0% | -3.2% | watch |
| ignition|t5|s3|h48 | 4 | 2 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | -3.2% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t2|s2|h8 | 18 | 2 | 9.0 | 61% | 56% | +0.37% | 39% | 11% | 50% | +1.3% | watch |
| momentum|t3|s3|h24 | 20 | 2 | 10.0 | 60% | 54% | +0.35% | 60% | 40% | 0% | -11.3% | watch |
| momentum|t5|s3|h48 | 14 | 2 | 7.0 | 43% | 41% | +0.18% | 43% | 57% | 0% | -14.8% | watch |
| momentum|t4|s2|h24 | 23 | 2 | 11.5 | 39% | 38% | +0.10% | 39% | 61% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 20 | 2 | 10.0 | 55% | 58% | +0.09% | 40% | 20% | 40% | +0.2% | fail |
| momentum|t3|s2|h12 | 28 | 2 | 14.0 | 46% | 45% | +0.08% | 43% | 50% | 7% | -16.5% | watch |
| momentum|t1.5|s1|h8 | 54 | 2 | 27.0 | 50% | 50% | -0.02% | 44% | 46% | 9% | -6.2% | fail |
| momentum|t1|s1|h6 | 69 | 2 | 34.5 | 61% | 62% | -0.03% | 59% | 38% | 3% | -4.0% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| range_bottom|t1|s1|h6 | 26 | 2 | 13.0 | 50% | 62% | -0.05% | 42% | 27% | 31% | -1.0% | fail |
| range_bottom|t1.5|s1|h8 | 22 | 2 | 11.0 | 45% | 50% | -0.06% | 32% | 32% | 36% | -1.3% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t2|s2|h8 | 45 | 2 | 22.5 | 53% | 56% | -0.08% | 47% | 38% | 16% | -15.7% | fail |
| momentum|t1.5|s1.5|h8 | 49 | 2 | 24.5 | 55% | 58% | -0.11% | 49% | 41% | 10% | -11.2% | fail |
| ignition|t1.5|s1|h8 | 13 | 2 | 6.5 | 38% | 50% | -0.21% | 38% | 54% | 8% | -4.0% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
