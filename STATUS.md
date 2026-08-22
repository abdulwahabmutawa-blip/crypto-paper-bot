# Fleet status — 2026-08-22 (UTC)

10 paper books ($1,000 each, no real money) + 1 REAL-MONEY book (Lottery, VPS-run) + 1 new unverified book (playbook).

| Bot | Holds | 24h change | Value (asof) |
|---|---|---|---|
| crypto (trend) | XRP-USD | No trade; XRP up hard (+14.8% mark-to-market) | $1,346.04 (08-22) |
| congress | 10 positions | No trade | $990.44 (08-21) |
| meanrev | UNH | No trade | $1,196.26 (08-21) |
| commodity | USO | 3 round trips (DBC↔USO, signal flip) → USO | $1,049.33 (08-21) |
| allweather | 5-asset basket | No trade | $1,026.58 (08-21) |
| hype (sentiment) | MRNA | 5 round trips (BTC, MSTR×2, CIFR) → MRNA | $1,518.86 (08-21) |
| hype-crypto | CASH | Round-tripped BTC-USD, then PENGU-USD → cash | $997.44 (08-22) |
| Hunter | BTC-USD | SOLD NVDA → BUY BTC-USD, all-in | $955.21 (08-22) |
| Scholar | SPY | No trade | $1,014.39 (08-21) |
| Analyst | SPY | No trade | $1,019.97 (08-21) |
| **Lottery (REAL $)** | AXSUSDT | Closed ZECUSDT (−$0.02), 币安人生USDT (+$1.74) → entered AXSUSDT (+$4.17 unrl.) | $58.21 (08-22 05:02) |

## Changed
- commodity: whipsawed 3x between DBC and USO on signal flips, ended net long USO.
- hype (sentiment): 5 buy/sell round trips chasing Grok euphoria signals (BTC, MSTR ×2,
  CIFR), landed on MRNA.
- hype-crypto: bought/sold BTC-USD, then bought/sold PENGU-USD same day → cash.
- Hunter: sold NVDA ("outgunned" by BTC reward/risk score), went all-in BTC-USD.
- Lottery (real $): closed ZECUSDT ~breakeven, closed 币安人生USDT +$1.74, entered AXSUSDT.
- crypto, congress, meanrev, allweather, Scholar, Analyst: no position changes.
- 110 paper-bot cycles + 257 lottery cycles in 24h, no gaps >15 min — cadence looks healthy.

## Needs a look
- Analyst's cash is −$0.85 (was −$0.78 yesterday), drifting further negative — still
  looks like a fee/rounding artifact, not a real overdraft, but it's getting worse.
- sentiment and hypecrypto churned very fast (multiple full round trips within hours);
  worth checking transaction-cost drag isn't quietly eating the gains.
- A new `playbook_state.json` book ("second-account explosion-playbook bot") appeared
  today (created 08-21, flat/no trades yet) — not documented in CLAUDE.md's bot list,
  scope not verified here.
- Same as before: `oracle-bot` (1 commit) and the lottery/scout pipeline remain outside
  CLAUDE.md's documented bot list.
- Several human commits today touched risk/exit logic (stop→drawdown floor, exit
  auditor, oracle scoring) — code changes only, not evaluated for correctness here.
