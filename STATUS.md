# Fleet status — 2026-08-21 (UTC)

10 paper books ($1,000 each, no real money) + 1 REAL-MONEY book (Lottery, VPS-run).

| Bot | Holds | 24h change | Value (asof) |
|---|---|---|---|
| crypto (trend) | XRP-USD | SELL LINK-USD (signal flip) → BUY XRP-USD (+25% 7d momentum) | $1,064.83 (08-21) |
| congress | 10 positions | No trade | $982.01 (08-20) |
| meanrev | UNH | No trade | $1,180.65 (08-20) |
| commodity | DBC | No trade | $1,057.25 (08-20) |
| allweather | 5-asset basket | No trade (not rebalance week) | $1,023.08 (08-20) |
| hype (sentiment) | CASH | BUY XRP-USD → STOP-LOSS hit (-16.1%) → CASH | $1,394.45 (08-20) |
| hype-crypto | CASH | BUY BTC-USD → SELL (hype faded) → CASH | $990.19 (08-21) |
| Hunter | NVDA | No trade (still stopped out of SLV since 08-18) | $945.03 (08-20) |
| Scholar | SPY | No trade | $1,010.40 (08-20) |
| Analyst | SPY | No trade | $1,016.03 (08-20) |
| **Lottery (REAL $)** | ZECUSDT | 2 closes: CFGUSDT +$0.05, MEGAUSDT -$0.19 → entered ZECUSDT | $35.50 (08-21 05:06) |

## Changed
- crypto: SELL LINK-USD (signal flip) → BUY XRP-USD.
- hype (sentiment): XRP-USD stop-loss hit at -16.1%, cutting a $1,667.85 position down
  to $1,398.51 → sits in cash.
- hype-crypto: round-tripped BTC-USD (bought on Grok euphoria, sold ~4h later "hype
  faded") → cash.
- Lottery (real $): MEGAUSDT stopped out -$0.19, CFGUSDT closed +$0.05, then entered
  ZECUSDT (currently +$0.09 unrealized).
- No position changes on congress, meanrev, commodity, allweather, Hunter, Scholar, or
  Analyst.

## Needs a look
- Analyst's cash is -$0.78 (should be ≥0) — likely a fee/rounding artifact, not a real
  overdraft, but flagging since it's technically an impossible state.
- All 109 paper-bot cycle commits in the last 24h landed on a steady ~13–14 min cadence
  (max gap 14.6 min) — no missed cron windows, no frozen bots.
- Two extra systems are committing to this repo alongside the 10-bot fleet: an
  `oracle-bot` (1 commit, 02:07 UTC) and the lottery/scout pipeline — neither is
  documented in CLAUDE.md's bot list, so their scope wasn't verified here.
