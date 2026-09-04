# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-04T22:52:23+00:00 · runs 30 · open 311 · resolved 254 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 1 | 1 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| ignition|t5|s3|h48 | 3 | 1 | 3.0 | 67% | 41% | +2.08% | 67% | 33% | 0% | +6.2% | watch |
| ignition|t3|s3|h24 | 5 | 1 | 5.0 | 80% | 54% | +1.55% | 80% | 20% | 0% | +7.8% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| ignition|t4|s2|h24 | 7 | 1 | 7.0 | 57% | 38% | +1.18% | 57% | 43% | 0% | +8.3% | watch |
| range_bottom|t4|s2|h24 | 2 | 1 | 2.0 | 50% | 38% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| range_bottom|t5|s3|h48 | 2 | 1 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| ignition|t3|s2|h12 | 7 | 1 | 7.0 | 57% | 45% | +0.61% | 57% | 43% | 0% | +4.2% | watch |
| range_bottom|t2|s2|h8 | 3 | 1 | 3.0 | 67% | 56% | +0.42% | 67% | 33% | 0% | +1.3% | watch |
| ignition|t2|s2|h8 | 6 | 1 | 6.0 | 67% | 56% | +0.42% | 67% | 33% | 0% | +2.5% | watch |
| range_bottom|t3|s2|h12 | 2 | 1 | 2.0 | 50% | 45% | +0.25% | 50% | 50% | 0% | +0.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 6 | 1 | 6.0 | 67% | 58% | +0.25% | 67% | 33% | 0% | +1.5% | watch |
| range_bottom|t1.5|s1|h8 | 7 | 1 | 7.0 | 57% | 50% | +0.18% | 57% | 43% | 0% | +1.3% | watch |
| ignition|t1.5|s1|h8 | 9 | 1 | 9.0 | 56% | 50% | +0.14% | 56% | 44% | 0% | +1.2% | watch |
| ignition|t1.5|s1.5|h8 | 8 | 1 | 8.0 | 62% | 58% | +0.12% | 62% | 38% | 0% | +1.0% | watch |
| range_bottom|t1|s1|h6 | 9 | 1 | 9.0 | 67% | 62% | +0.08% | 67% | 33% | 0% | +0.8% | watch |
| ignition|t1|s1|h6 | 10 | 1 | 10.0 | 60% | 62% | -0.05% | 60% | 40% | 0% | -0.5% | fail |
| momentum|t1|s1|h6 | 44 | 1 | 44.0 | 57% | 62% | -0.11% | 57% | 43% | 0% | -5.0% | fail |
| momentum|t1.5|s1|h8 | 29 | 1 | 29.0 | 41% | 50% | -0.22% | 41% | 59% | 0% | -6.2% | fail |
| range_bottom|t3|s3|h24 | 2 | 1 | 2.0 | 50% | 54% | -0.25% | 50% | 50% | 0% | -0.5% | fail |
| momentum|t1.5|s1.5|h8 | 26 | 1 | 26.0 | 42% | 58% | -0.48% | 42% | 58% | 0% | -12.5% | fail |
| momentum|t2|s2|h8 | 20 | 1 | 20.0 | 40% | 56% | -0.65% | 40% | 60% | 0% | -13.0% | fail |
| momentum|t3|s4|h48 | 4 | 1 | 4.0 | 50% | 61% | -0.75% | 50% | 50% | 0% | -3.0% | fail |
| momentum|t4|s2|h24 | 12 | 1 | 12.0 | 17% | 38% | -1.25% | 17% | 83% | 0% | -15.0% | fail |
| momentum|t3|s2|h12 | 12 | 1 | 12.0 | 17% | 45% | -1.42% | 17% | 83% | 0% | -17.0% | fail |
| momentum|t3|s3|h24 | 7 | 1 | 7.0 | 29% | 54% | -1.54% | 29% | 71% | 0% | -10.8% | fail |
| momentum|t5|s3|h48 | 6 | 1 | 6.0 | 17% | 41% | -1.92% | 17% | 83% | 0% | -11.5% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
