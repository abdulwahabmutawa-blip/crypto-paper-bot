# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T06:39:43+00:00 · runs 53 · open 305 · resolved 598 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 4 | 2 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t5|s3|h48 | 3 | 2 | 1.5 | 67% | 41% | +2.08% | 67% | 33% | 0% | +1.5% | watch |
| range_bottom|t3|s3|h24 | 5 | 2 | 2.5 | 80% | 54% | +1.55% | 80% | 20% | 0% | -0.5% | watch |
| momentum|t3|s4|h48 | 23 | 2 | 11.5 | 83% | 61% | +1.53% | 83% | 17% | 0% | -0.3% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| range_bottom|t4|s2|h24 | 5 | 2 | 2.5 | 60% | 38% | +1.35% | 60% | 40% | 0% | +1.5% | watch |
| momentum|t5|s3|h48 | 18 | 2 | 9.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | -14.8% | watch |
| ignition|t3|s3|h24 | 6 | 2 | 3.0 | 67% | 54% | +0.75% | 67% | 33% | 0% | -3.2% | watch |
| ignition|t5|s3|h48 | 4 | 2 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | -3.2% | watch |
| momentum|t3|s3|h24 | 25 | 2 | 12.5 | 64% | 54% | +0.59% | 64% | 36% | 0% | -11.3% | watch |
| range_bottom|t3|s2|h12 | 12 | 2 | 6.0 | 42% | 45% | +0.52% | 33% | 17% | 50% | +0.5% | fail |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t2|s2|h8 | 21 | 2 | 10.5 | 57% | 56% | +0.30% | 33% | 10% | 57% | +1.3% | watch |
| momentum|t3|s2|h12 | 36 | 2 | 18.0 | 50% | 45% | +0.17% | 42% | 47% | 11% | -16.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 24 | 2 | 12.0 | 54% | 58% | +0.14% | 42% | 17% | 42% | +1.5% | fail |
| momentum|t4|s2|h24 | 28 | 2 | 14.0 | 39% | 38% | +0.11% | 39% | 61% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1|h8 | 25 | 2 | 12.5 | 48% | 50% | +0.04% | 36% | 28% | 36% | +0.0% | fail |
| range_bottom|t1|s1|h6 | 30 | 2 | 15.0 | 53% | 62% | +0.02% | 47% | 23% | 30% | -0.4% | fail |
| momentum|t1.5|s1|h8 | 64 | 2 | 32.0 | 50% | 50% | -0.02% | 45% | 47% | 8% | -6.2% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t1|s1|h6 | 83 | 2 | 41.5 | 59% | 62% | -0.07% | 58% | 40% | 2% | -4.0% | fail |
| momentum|t1.5|s1.5|h8 | 58 | 2 | 29.0 | 55% | 58% | -0.10% | 50% | 41% | 9% | -11.2% | fail |
| momentum|t2|s2|h8 | 51 | 2 | 25.5 | 51% | 56% | -0.15% | 45% | 39% | 16% | -15.7% | fail |
| ignition|t1.5|s1|h8 | 13 | 2 | 6.5 | 38% | 50% | -0.21% | 38% | 54% | 8% | -4.0% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
