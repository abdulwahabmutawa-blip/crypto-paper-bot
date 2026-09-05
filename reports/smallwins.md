# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T04:50:25+00:00 · runs 46 · open 304 · resolved 478 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 4 | 2 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t5|s3|h48 | 3 | 2 | 1.5 | 67% | 41% | +2.08% | 67% | 33% | 0% | +1.5% | watch |
| ignition|t5|s3|h48 | 3 | 1 | 3.0 | 67% | 41% | +2.08% | 67% | 33% | 0% | +6.2% | watch |
| ignition|t3|s3|h24 | 5 | 1 | 5.0 | 80% | 54% | +1.55% | 80% | 20% | 0% | +7.8% | watch |
| range_bottom|t3|s3|h24 | 5 | 2 | 2.5 | 80% | 54% | +1.55% | 80% | 20% | 0% | -0.5% | watch |
| momentum|t3|s4|h48 | 16 | 2 | 8.0 | 81% | 61% | +1.44% | 81% | 19% | 0% | -0.3% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| range_bottom|t4|s2|h24 | 5 | 2 | 2.5 | 60% | 38% | +1.35% | 60% | 40% | 0% | +1.5% | watch |
| ignition|t4|s2|h24 | 7 | 1 | 7.0 | 57% | 38% | +1.18% | 57% | 43% | 0% | +8.3% | watch |
| range_bottom|t3|s2|h12 | 6 | 2 | 3.0 | 67% | 45% | +1.08% | 67% | 33% | 0% | +0.5% | watch |
| ignition|t3|s2|h12 | 7 | 1 | 7.0 | 57% | 45% | +0.61% | 57% | 43% | 0% | +4.2% | watch |
| range_bottom|t2|s2|h8 | 17 | 2 | 8.5 | 59% | 56% | +0.38% | 41% | 12% | 47% | +1.3% | watch |
| ignition|t2|s2|h8 | 7 | 2 | 3.5 | 57% | 56% | +0.32% | 57% | 29% | 14% | -0.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 20 | 2 | 10.0 | 55% | 58% | +0.09% | 40% | 20% | 40% | +0.2% | fail |
| momentum|t3|s3|h24 | 18 | 2 | 9.0 | 56% | 54% | +0.08% | 56% | 44% | 0% | -11.3% | watch |
| range_bottom|t1.5|s1|h8 | 21 | 2 | 10.5 | 48% | 50% | -0.00% | 33% | 29% | 38% | -0.0% | fail |
| momentum|t1.5|s1|h8 | 52 | 2 | 26.0 | 50% | 50% | -0.02% | 44% | 46% | 10% | -6.2% | fail |
| momentum|t1|s1|h6 | 65 | 2 | 32.5 | 60% | 62% | -0.05% | 58% | 38% | 3% | -4.0% | fail |
| range_bottom|t1|s1|h6 | 26 | 2 | 13.0 | 50% | 62% | -0.05% | 42% | 27% | 31% | -1.0% | fail |
| momentum|t4|s2|h24 | 22 | 2 | 11.0 | 36% | 38% | -0.07% | 36% | 64% | 0% | -17.2% | fail |
| momentum|t2|s2|h8 | 43 | 2 | 21.5 | 53% | 56% | -0.07% | 47% | 37% | 16% | -15.7% | fail |
| ignition|t1.5|s1.5|h8 | 10 | 2 | 5.0 | 50% | 58% | -0.10% | 50% | 40% | 10% | -2.0% | fail |
| ignition|t1|s1|h6 | 15 | 2 | 7.5 | 53% | 62% | -0.12% | 53% | 40% | 7% | -1.0% | fail |
| ignition|t1.5|s1|h8 | 12 | 2 | 6.0 | 42% | 50% | -0.12% | 42% | 50% | 8% | -2.8% | fail |
| momentum|t1.5|s1.5|h8 | 48 | 2 | 24.0 | 54% | 58% | -0.14% | 48% | 42% | 10% | -11.2% | fail |
| momentum|t3|s2|h12 | 24 | 2 | 12.0 | 42% | 45% | -0.17% | 42% | 58% | 0% | -16.5% | fail |
| momentum|t5|s3|h48 | 12 | 2 | 6.0 | 33% | 41% | -0.58% | 33% | 67% | 0% | -14.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
