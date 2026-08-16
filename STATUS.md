# Fleet status — 2026-08-16 (UTC)

Last paper-fleet cycle: 2026-08-16 01:09 UTC (~4h before this digest — see below).
Fleet has grown past the "9-bot" baseline: 10 paper books ($1,000 each, no real
money) + 1 REAL-MONEY book (Lottery, $20 hard cap, added 08-15).

| Bot | Holds | 24h change | Value (asof) |
|---|---|---|---|
| crypto (trend) | XRP-USD | No trade | $1,007.44 (08-16) |
| congress | 10 positions (NVDA/META/GOOG/TSM/ADBE/PYPL/CSCO/PLTR/AVGO/MSFT) | No trade | $1,005.63 (08-14) |
| meanrev | UNH | No trade | $1,232.58 (08-14) |
| commodity | DBC | No trade | $1,019.53 (08-14) |
| allweather | 5-asset basket | No trade | $1,018.60 (08-14) |
| hype (sentiment) | CASH | No trade | $1,326.92 (08-14) |
| hype-crypto | CASH | No trade | $1,000.00 (08-15) |
| Hunter | PLTR | No trade | $990.45 (08-14) |
| Scholar | IWM | No trade | $1,040.22 (08-14) |
| Analyst | SPY | No trade | $1,034.53 (08-14) |
| **Lottery (REAL $)** | CASH (flat) | Stop-out + 5 failed buys | **$9.30** (08-16) |

## Changed
- **Lottery (real money)**: stop-loss exit on COWUSDT −11.2% (−$1.19) at 02:02
  UTC; book now flat at $9.30 vs a ~$11 stake. Since 04:10 UTC, 5 straight BUY
  attempts (JSTUSDT ×2, HEIUSDT, ZAMAUSDT ×2) failed "insufficient balance"
  (Binance error -2010), each paired with an "order MAY have filled —
  reconcile next cycle" warning.
- Scout: 2 "Invalid symbol" errors scanning candidates (02:41/02:46 UTC), no
  trade impact — cosmetic.
- Main paper fleet: 89 cycles landed in 24h, one 28-min gap (07:22→07:50 UTC
  on 08-15), otherwise normal ~13-min cadence. No position changes on the 10
  paper books — stock market closed for the weekend, crypto bot unchanged too.

## Needs a look
- **Lottery real-money book**: 5 failed BUY orders in the last hour, each
  flagged as possibly-filled-but-unconfirmed. Worth manually checking the
  actual Binance balance against `data/lottery_state.json`. At $9.30 the book
  may now be under Binance's per-pair minimum order size, which would explain
  the run of failures continuing indefinitely.
- Main paper-fleet: no "cycle" commit since 01:09 UTC (~4h as of this run).
  Plausibly GitHub Actions' documented low accept-rate for this schedule
  (bot.yml notes ~6% of requested starts land), not confirmed broken — noting
  the gap since it's real.
- Nothing else abnormal: no exceptions found in the other 9 state files;
  Watcher/Sentinel scanning normally (last scan 08-15 23:48 UTC, risk_level
  "caution" on Strait of Hormuz / oil-reserve headlines).
