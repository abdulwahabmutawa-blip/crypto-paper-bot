# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T01:11:58+00:00 · runs 39 · open 300 · resolved 323 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 3 | 2 | 1.5 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| ignition|t5|s3|h48 | 3 | 1 | 3.0 | 67% | 41% | +2.08% | 67% | 33% | 0% | +6.2% | watch |
| ignition|t3|s3|h24 | 5 | 1 | 5.0 | 80% | 54% | +1.55% | 80% | 20% | 0% | +7.8% | watch |
| range_bottom|t3|s2|h12 | 4 | 2 | 2.0 | 75% | 45% | +1.50% | 75% | 25% | 0% | +0.5% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| range_bottom|t3|s3|h24 | 4 | 2 | 2.0 | 75% | 54% | +1.25% | 75% | 25% | 0% | -0.5% | watch |
| ignition|t4|s2|h24 | 7 | 1 | 7.0 | 57% | 38% | +1.18% | 57% | 43% | 0% | +8.3% | watch |
| range_bottom|t2|s2|h8 | 6 | 2 | 3.0 | 83% | 56% | +1.08% | 83% | 17% | 0% | +1.3% | watch |
| range_bottom|t4|s2|h24 | 2 | 1 | 2.0 | 50% | 38% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| range_bottom|t5|s3|h48 | 2 | 1 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| momentum|t3|s4|h48 | 7 | 2 | 3.5 | 71% | 61% | +0.75% | 71% | 29% | 0% | -0.3% | watch |
| ignition|t3|s2|h12 | 7 | 1 | 7.0 | 57% | 45% | +0.61% | 57% | 43% | 0% | +4.2% | watch |
| ignition|t2|s2|h8 | 6 | 1 | 6.0 | 67% | 56% | +0.42% | 67% | 33% | 0% | +2.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 9 | 2 | 4.5 | 67% | 58% | +0.25% | 67% | 33% | 0% | +0.8% | watch |
| ignition|t1.5|s1|h8 | 9 | 1 | 9.0 | 56% | 50% | +0.14% | 56% | 44% | 0% | +1.2% | watch |
| ignition|t1.5|s1.5|h8 | 8 | 1 | 8.0 | 62% | 58% | +0.12% | 62% | 38% | 0% | +1.0% | watch |
| range_bottom|t1|s1|h6 | 21 | 2 | 10.5 | 57% | 62% | +0.06% | 52% | 24% | 24% | -0.4% | fail |
| range_bottom|t1.5|s1|h8 | 10 | 2 | 5.0 | 50% | 50% | +0.00% | 50% | 50% | 0% | +0.0% | fail |
| momentum|t1|s1|h6 | 51 | 2 | 25.5 | 61% | 62% | -0.03% | 61% | 39% | 0% | -4.0% | fail |
| momentum|t1.5|s1|h8 | 35 | 2 | 17.5 | 49% | 50% | -0.04% | 49% | 51% | 0% | -6.2% | fail |
| ignition|t1|s1|h6 | 11 | 1 | 11.0 | 55% | 62% | -0.07% | 55% | 36% | 9% | -0.8% | fail |
| momentum|t1.5|s1.5|h8 | 32 | 2 | 16.0 | 50% | 58% | -0.25% | 50% | 50% | 0% | -11.2% | fail |
| momentum|t2|s2|h8 | 26 | 2 | 13.0 | 46% | 56% | -0.40% | 46% | 54% | 0% | -15.7% | fail |
| momentum|t3|s2|h12 | 16 | 2 | 8.0 | 31% | 45% | -0.69% | 31% | 69% | 0% | -16.5% | fail |
| momentum|t3|s3|h24 | 12 | 2 | 6.0 | 42% | 54% | -0.75% | 42% | 58% | 0% | -11.3% | fail |
| momentum|t4|s2|h24 | 14 | 2 | 7.0 | 21% | 38% | -0.96% | 21% | 79% | 0% | -17.2% | fail |
| momentum|t5|s3|h48 | 8 | 2 | 4.0 | 12% | 41% | -2.25% | 12% | 88% | 0% | -14.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
