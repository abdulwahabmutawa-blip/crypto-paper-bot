# Crypto regime switcher lab

Kraken daily closes 2024-09-15 to 2026-09-05, 721 rows, 8 coins, decisions at close, 25 bps per side. Replay window 520 days after the 200-day warm-up. Current live rule = mom 7 / fallback CASH / rel_btc False.

| mom | TREND fallback | rel. to BTC | CAGR | vs BTC B&H | max DD | last 90d | last 90d vs BTC | switches |
|---|---|---|---|---|---|---|---|---|
| BTC-only MA200 timing |  |  | +14.5% | +26.6% | -20.5% | +14.6% | -11.1% | 9 |
| equal-weight 8 in TREND |  |  | +10.7% | +20.8% | -39.1% | +15.7% | -10.1% | 9 |
| TREND=BTC + CHOP dip brain |  |  | +9.5% | +18.9% | -48.4% | +28.6% | +2.9% | 37 |
| 14 | BTC | yes | -8.4% | -7.9% | -61.8% | +6.5% | -19.3% | 65 |
| 14 | BTC | no | -9.7% | -9.6% | -61.8% | +6.5% | -19.3% | 66 |
| 30 | BTC | no | -14.1% | -15.8% | -69.3% | +12.8% | -13.0% | 49 |
| 30 | BTC | yes | -14.1% | -15.8% | -69.3% | +12.8% | -13.0% | 49 |
| 30 | CASH | no | -17.2% | -20.2% | -69.8% | +12.8% | -13.0% | 47 |
| 30 | CASH | yes | -17.2% | -20.2% | -69.8% | +12.8% | -13.0% | 47 |
| 14 | CASH | yes | -18.2% | -21.6% | -62.4% | +6.5% | -19.3% | 64 |
| 14 | CASH | no | -19.4% | -23.2% | -62.4% | +6.5% | -19.3% | 65 |
| 7 | BTC | yes | -32.7% | -40.6% | -66.2% | +6.7% | -19.0% | 79 |
| 7 | BTC | no | -33.8% | -42.0% | -67.0% | +6.7% | -19.0% | 81 |
| 7 | CASH | yes | -37.6% | -46.6% | -69.6% | +6.7% | -19.0% | 77 |
| 7 | CASH | no | -40.1% | -49.7% | -71.4% | +6.7% | -19.0% | 79 |
| BTC buy & hold | | | -3.0% | 0 | -53.1% | +25.7% | 0 | 0 |

Read: a variant earns its place only if it beats BTC over the full window AND the last 90 days, with a drawdown no worse than the current rule. Switch counts x 50 bps are the fee bill.
