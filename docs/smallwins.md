# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T05:05:44+00:00 · runs 47 · open 304 · resolved 490 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 4 | 2 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t5|s3|h48 | 3 | 2 | 1.5 | 67% | 41% | +2.08% | 67% | 33% | 0% | +1.5% | watch |
| ignition|t5|s3|h48 | 3 | 1 | 3.0 | 67% | 41% | +2.08% | 67% | 33% | 0% | +6.2% | watch |
| ignition|t3|s3|h24 | 5 | 1 | 5.0 | 80% | 54% | +1.55% | 80% | 20% | 0% | +7.8% | watch |
| range_bottom|t3|s3|h24 | 5 | 2 | 2.5 | 80% | 54% | +1.55% | 80% | 20% | 0% | -0.5% | watch |
| momentum|t3|s4|h48 | 17 | 2 | 8.5 | 82% | 61% | +1.51% | 82% | 18% | 0% | -0.3% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| range_bottom|t4|s2|h24 | 5 | 2 | 2.5 | 60% | 38% | +1.35% | 60% | 40% | 0% | +1.5% | watch |
| ignition|t4|s2|h24 | 7 | 1 | 7.0 | 57% | 38% | +1.18% | 57% | 43% | 0% | +8.3% | watch |
| range_bottom|t3|s2|h12 | 6 | 2 | 3.0 | 67% | 45% | +1.08% | 67% | 33% | 0% | +0.5% | watch |
| ignition|t3|s2|h12 | 7 | 1 | 7.0 | 57% | 45% | +0.61% | 57% | 43% | 0% | +4.2% | watch |
| range_bottom|t2|s2|h8 | 18 | 2 | 9.0 | 61% | 56% | +0.37% | 39% | 11% | 50% | +1.3% | watch |
| ignition|t2|s2|h8 | 7 | 2 | 3.5 | 57% | 56% | +0.32% | 57% | 29% | 14% | -0.2% | watch |
| momentum|t3|s3|h24 | 19 | 2 | 9.5 | 58% | 54% | +0.22% | 58% | 42% | 0% | -11.3% | watch |
| momentum|t5|s3|h48 | 14 | 2 | 7.0 | 43% | 41% | +0.18% | 43% | 57% | 0% | -14.8% | watch |
| momentum|t4|s2|h24 | 23 | 2 | 11.5 | 39% | 38% | +0.10% | 39% | 61% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 20 | 2 | 10.0 | 55% | 58% | +0.09% | 40% | 20% | 40% | +0.2% | fail |
| momentum|t1.5|s1|h8 | 53 | 2 | 26.5 | 51% | 50% | +0.00% | 45% | 45% | 9% | -6.2% | watch |
| range_bottom|t1.5|s1|h8 | 21 | 2 | 10.5 | 48% | 50% | -0.00% | 33% | 29% | 38% | -0.0% | fail |
| momentum|t1|s1|h6 | 66 | 2 | 33.0 | 61% | 62% | -0.04% | 59% | 38% | 3% | -4.0% | fail |
| momentum|t3|s2|h12 | 25 | 2 | 12.5 | 44% | 45% | -0.05% | 44% | 56% | 0% | -16.5% | fail |
| range_bottom|t1|s1|h6 | 26 | 2 | 13.0 | 50% | 62% | -0.05% | 42% | 27% | 31% | -1.0% | fail |
| momentum|t2|s2|h8 | 43 | 2 | 21.5 | 53% | 56% | -0.07% | 47% | 37% | 16% | -15.7% | fail |
| momentum|t1.5|s1.5|h8 | 49 | 2 | 24.5 | 55% | 58% | -0.11% | 49% | 41% | 10% | -11.2% | fail |
| ignition|t1|s1|h6 | 15 | 2 | 7.5 | 53% | 62% | -0.12% | 53% | 40% | 7% | -1.0% | fail |
| ignition|t1.5|s1|h8 | 13 | 2 | 6.5 | 38% | 50% | -0.21% | 38% | 54% | 8% | -4.0% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
