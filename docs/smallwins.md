# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T01:58:21+00:00 · runs 42 · open 288 · resolved 361 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 3 | 2 | 1.5 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| ignition|t5|s3|h48 | 3 | 1 | 3.0 | 67% | 41% | +2.08% | 67% | 33% | 0% | +6.2% | watch |
| range_bottom|t4|s2|h24 | 3 | 2 | 1.5 | 67% | 38% | +1.75% | 67% | 33% | 0% | +1.5% | watch |
| ignition|t3|s3|h24 | 5 | 1 | 5.0 | 80% | 54% | +1.55% | 80% | 20% | 0% | +7.8% | watch |
| range_bottom|t3|s2|h12 | 4 | 2 | 2.0 | 75% | 45% | +1.50% | 75% | 25% | 0% | +0.5% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| range_bottom|t3|s3|h24 | 4 | 2 | 2.0 | 75% | 54% | +1.25% | 75% | 25% | 0% | -0.5% | watch |
| ignition|t4|s2|h24 | 7 | 1 | 7.0 | 57% | 38% | +1.18% | 57% | 43% | 0% | +8.3% | watch |
| momentum|t3|s4|h48 | 8 | 2 | 4.0 | 75% | 61% | +1.00% | 75% | 25% | 0% | -0.3% | watch |
| range_bottom|t5|s3|h48 | 2 | 1 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| range_bottom|t2|s2|h8 | 12 | 2 | 6.0 | 67% | 56% | +0.66% | 50% | 8% | 42% | +1.3% | watch |
| ignition|t3|s2|h12 | 7 | 1 | 7.0 | 57% | 45% | +0.61% | 57% | 43% | 0% | +4.2% | watch |
| ignition|t2|s2|h8 | 7 | 2 | 3.5 | 57% | 56% | +0.32% | 57% | 29% | 14% | -0.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 15 | 2 | 7.5 | 60% | 58% | +0.21% | 47% | 20% | 33% | +1.5% | watch |
| ignition|t1.5|s1|h8 | 10 | 2 | 5.0 | 50% | 50% | +0.10% | 50% | 40% | 10% | -0.2% | watch |
| range_bottom|t1|s1|h6 | 22 | 2 | 11.0 | 59% | 62% | +0.10% | 55% | 23% | 23% | -0.4% | fail |
| ignition|t1.5|s1.5|h8 | 9 | 2 | 4.5 | 56% | 58% | +0.08% | 56% | 33% | 11% | -0.2% | fail |
| range_bottom|t1.5|s1|h8 | 16 | 2 | 8.0 | 50% | 50% | +0.06% | 38% | 31% | 31% | +0.0% | watch |
| momentum|t1.5|s1|h8 | 38 | 2 | 19.0 | 53% | 50% | +0.01% | 47% | 47% | 5% | -6.2% | watch |
| momentum|t1|s1|h6 | 53 | 2 | 26.5 | 62% | 62% | -0.02% | 60% | 38% | 2% | -4.0% | fail |
| ignition|t1|s1|h6 | 11 | 1 | 11.0 | 55% | 62% | -0.07% | 55% | 36% | 9% | -0.8% | fail |
| momentum|t1.5|s1.5|h8 | 34 | 2 | 17.0 | 53% | 58% | -0.20% | 50% | 47% | 3% | -11.2% | fail |
| momentum|t2|s2|h8 | 30 | 2 | 15.0 | 50% | 56% | -0.25% | 47% | 47% | 7% | -15.7% | fail |
| momentum|t3|s3|h24 | 13 | 2 | 6.5 | 46% | 54% | -0.48% | 46% | 54% | 0% | -11.3% | fail |
| momentum|t3|s2|h12 | 17 | 2 | 8.5 | 35% | 45% | -0.49% | 35% | 65% | 0% | -16.5% | fail |
| momentum|t4|s2|h24 | 15 | 2 | 7.5 | 27% | 38% | -0.65% | 27% | 73% | 0% | -17.2% | fail |
| momentum|t5|s3|h48 | 8 | 2 | 4.0 | 12% | 41% | -2.25% | 12% | 88% | 0% | -14.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
