# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T00:56:28+00:00 · runs 38 · open 309 · resolved 313 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 2 | 2 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| ignition|t5|s3|h48 | 3 | 1 | 3.0 | 67% | 41% | +2.08% | 67% | 33% | 0% | +6.2% | watch |
| ignition|t3|s3|h24 | 5 | 1 | 5.0 | 80% | 54% | +1.55% | 80% | 20% | 0% | +7.8% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| ignition|t4|s2|h24 | 7 | 1 | 7.0 | 57% | 38% | +1.18% | 57% | 43% | 0% | +8.3% | watch |
| range_bottom|t2|s2|h8 | 6 | 2 | 3.0 | 83% | 56% | +1.08% | 83% | 17% | 0% | +1.3% | watch |
| range_bottom|t3|s2|h12 | 3 | 2 | 1.5 | 67% | 45% | +1.08% | 67% | 33% | 0% | +0.5% | watch |
| range_bottom|t3|s3|h24 | 3 | 2 | 1.5 | 67% | 54% | +0.75% | 67% | 33% | 0% | -0.5% | watch |
| range_bottom|t4|s2|h24 | 2 | 1 | 2.0 | 50% | 38% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| range_bottom|t5|s3|h48 | 2 | 1 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| ignition|t3|s2|h12 | 7 | 1 | 7.0 | 57% | 45% | +0.61% | 57% | 43% | 0% | +4.2% | watch |
| ignition|t2|s2|h8 | 6 | 1 | 6.0 | 67% | 56% | +0.42% | 67% | 33% | 0% | +2.5% | watch |
| momentum|t3|s4|h48 | 6 | 2 | 3.0 | 67% | 61% | +0.42% | 67% | 33% | 0% | -0.3% | watch |
| range_bottom|t1.5|s1.5|h8 | 9 | 2 | 4.5 | 67% | 58% | +0.25% | 67% | 33% | 0% | +0.8% | watch |
| ignition|t1.5|s1|h8 | 9 | 1 | 9.0 | 56% | 50% | +0.14% | 56% | 44% | 0% | +1.2% | watch |
| ignition|t1.5|s1.5|h8 | 8 | 1 | 8.0 | 62% | 58% | +0.12% | 62% | 38% | 0% | +1.0% | watch |
| range_bottom|t1|s1|h6 | 21 | 2 | 10.5 | 57% | 62% | +0.06% | 52% | 24% | 24% | -0.4% | fail |
| range_bottom|t1.5|s1|h8 | 10 | 2 | 5.0 | 50% | 50% | +0.00% | 50% | 50% | 0% | +0.0% | fail |
| momentum|t1|s1|h6 | 51 | 2 | 25.5 | 61% | 62% | -0.03% | 61% | 39% | 0% | -4.0% | fail |
| ignition|t1|s1|h6 | 11 | 1 | 11.0 | 55% | 62% | -0.07% | 55% | 36% | 9% | -0.8% | fail |
| momentum|t1.5|s1|h8 | 34 | 2 | 17.0 | 47% | 50% | -0.07% | 47% | 53% | 0% | -6.2% | fail |
| momentum|t1.5|s1.5|h8 | 31 | 2 | 15.5 | 48% | 58% | -0.30% | 48% | 52% | 0% | -11.2% | fail |
| momentum|t2|s2|h8 | 25 | 2 | 12.5 | 44% | 56% | -0.49% | 44% | 56% | 0% | -15.7% | fail |
| momentum|t3|s2|h12 | 15 | 2 | 7.5 | 27% | 45% | -0.92% | 27% | 73% | 0% | -16.5% | fail |
| momentum|t3|s3|h24 | 11 | 2 | 5.5 | 36% | 54% | -1.07% | 36% | 64% | 0% | -11.3% | fail |
| momentum|t4|s2|h24 | 13 | 1 | 13.0 | 15% | 38% | -1.33% | 15% | 85% | 0% | -17.2% | fail |
| momentum|t5|s3|h48 | 8 | 2 | 4.0 | 12% | 41% | -2.25% | 12% | 88% | 0% | -14.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
