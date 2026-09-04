# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-04T22:05:54+00:00 · runs 27 · open 306 · resolved 209 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| range_bottom|t4|s2|h24 | 1 | 1 | 1.0 | 100% | 38% | +3.75% | 100% | 0% | 0% | +3.8% | watch |
| range_bottom|t3|s2|h12 | 1 | 1 | 1.0 | 100% | 45% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s3|h24 | 1 | 1 | 1.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s4|h48 | 1 | 1 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t2|s2|h8 | 2 | 1 | 2.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +3.5% | watch |
| ignition|t4|s2|h24 | 5 | 1 | 5.0 | 60% | 38% | +1.35% | 60% | 40% | 0% | +6.8% | watch |
| ignition|t3|s3|h24 | 4 | 1 | 4.0 | 75% | 54% | +1.25% | 75% | 25% | 0% | +5.0% | watch |
| ignition|t3|s4|h48 | 4 | 1 | 4.0 | 75% | 61% | +1.00% | 75% | 25% | 0% | +4.0% | watch |
| ignition|t2|s2|h8 | 4 | 1 | 4.0 | 75% | 56% | +0.75% | 75% | 25% | 0% | +3.0% | watch |
| range_bottom|t1.5|s1|h8 | 5 | 1 | 5.0 | 80% | 50% | +0.75% | 80% | 20% | 0% | +3.8% | watch |
| ignition|t3|s2|h12 | 5 | 1 | 5.0 | 60% | 45% | +0.75% | 60% | 40% | 0% | +3.8% | watch |
| ignition|t5|s3|h48 | 2 | 1 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 5 | 1 | 5.0 | 80% | 58% | +0.65% | 80% | 20% | 0% | +3.2% | watch |
| range_bottom|t1|s1|h6 | 7 | 1 | 7.0 | 86% | 62% | +0.46% | 86% | 14% | 0% | +3.2% | watch |
| momentum|t3|s4|h48 | 3 | 1 | 3.0 | 67% | 61% | +0.42% | 67% | 33% | 0% | +1.2% | watch |
| ignition|t1.5|s1.5|h8 | 6 | 1 | 6.0 | 67% | 58% | +0.25% | 67% | 33% | 0% | +1.5% | watch |
| momentum|t1|s1|h6 | 38 | 1 | 38.0 | 63% | 62% | +0.01% | 63% | 37% | 0% | +0.5% | watch |
| ignition|t1.5|s1|h8 | 8 | 1 | 8.0 | 50% | 50% | +0.00% | 50% | 50% | 0% | +0.0% | fail |
| momentum|t1.5|s1|h8 | 26 | 1 | 26.0 | 46% | 50% | -0.10% | 46% | 54% | 0% | -2.5% | fail |
| ignition|t1|s1|h6 | 9 | 1 | 9.0 | 56% | 62% | -0.14% | 56% | 44% | 0% | -1.3% | fail |
| momentum|t1.5|s1.5|h8 | 23 | 1 | 23.0 | 48% | 58% | -0.32% | 48% | 52% | 0% | -7.3% | fail |
| momentum|t2|s2|h8 | 17 | 1 | 17.0 | 47% | 56% | -0.37% | 47% | 53% | 0% | -6.2% | fail |
| momentum|t4|s2|h24 | 10 | 1 | 10.0 | 20% | 38% | -1.05% | 20% | 80% | 0% | -10.5% | fail |
| momentum|t3|s2|h12 | 10 | 1 | 10.0 | 20% | 45% | -1.25% | 20% | 80% | 0% | -12.5% | fail |
| momentum|t3|s3|h24 | 6 | 1 | 6.0 | 33% | 54% | -1.25% | 33% | 67% | 0% | -7.5% | fail |
| momentum|t5|s3|h48 | 5 | 1 | 5.0 | 20% | 41% | -1.65% | 20% | 80% | 0% | -8.2% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
