# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T07:10:24+00:00 · runs 55 · open 302 · resolved 623 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 5 | 2 | 2.5 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t5|s3|h48 | 4 | 2 | 2.0 | 75% | 41% | +2.75% | 75% | 25% | 0% | +1.5% | watch |
| range_bottom|t3|s3|h24 | 6 | 2 | 3.0 | 83% | 54% | +1.75% | 83% | 17% | 0% | -0.5% | watch |
| momentum|t3|s4|h48 | 24 | 2 | 12.0 | 83% | 61% | +1.58% | 83% | 17% | 0% | -0.3% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| range_bottom|t4|s2|h24 | 5 | 2 | 2.5 | 60% | 38% | +1.35% | 60% | 40% | 0% | +1.5% | watch |
| momentum|t5|s3|h48 | 19 | 2 | 9.5 | 53% | 41% | +0.96% | 53% | 47% | 0% | -14.8% | watch |
| ignition|t3|s3|h24 | 6 | 2 | 3.0 | 67% | 54% | +0.75% | 67% | 33% | 0% | -3.2% | watch |
| ignition|t5|s3|h48 | 4 | 2 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | -3.2% | watch |
| range_bottom|t3|s2|h12 | 13 | 2 | 6.5 | 46% | 45% | +0.70% | 38% | 15% | 46% | +0.5% | watch |
| momentum|t3|s3|h24 | 26 | 2 | 13.0 | 65% | 54% | +0.67% | 65% | 35% | 0% | -11.3% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t2|s2|h8 | 22 | 2 | 11.0 | 59% | 56% | +0.37% | 36% | 9% | 55% | +1.3% | watch |
| momentum|t4|s2|h24 | 29 | 2 | 14.5 | 41% | 38% | +0.23% | 41% | 59% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 26 | 2 | 13.0 | 58% | 58% | +0.23% | 46% | 15% | 38% | +1.5% | fail |
| momentum|t3|s2|h12 | 39 | 2 | 19.5 | 49% | 45% | +0.19% | 41% | 44% | 15% | -16.5% | watch |
| range_bottom|t1.5|s1|h8 | 27 | 2 | 13.5 | 52% | 50% | +0.13% | 41% | 26% | 33% | +0.0% | watch |
| range_bottom|t1|s1|h6 | 31 | 2 | 15.5 | 55% | 62% | +0.04% | 48% | 23% | 29% | -0.4% | fail |
| momentum|t1.5|s1|h8 | 65 | 2 | 32.5 | 51% | 50% | +0.00% | 46% | 46% | 8% | -6.2% | watch |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| momentum|t1.5|s1.5|h8 | 60 | 2 | 30.0 | 57% | 58% | -0.06% | 52% | 40% | 8% | -11.2% | fail |
| momentum|t1|s1|h6 | 86 | 2 | 43.0 | 59% | 62% | -0.06% | 58% | 40% | 2% | -4.0% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t2|s2|h8 | 53 | 2 | 26.5 | 53% | 56% | -0.07% | 47% | 38% | 15% | -15.7% | fail |
| ignition|t1.5|s1|h8 | 13 | 2 | 6.5 | 38% | 50% | -0.21% | 38% | 54% | 8% | -4.0% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
