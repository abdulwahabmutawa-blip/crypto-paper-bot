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
| **Lottery (REAL $)** | CASH | Closed AXSUSDT (+$0.44, ratcheted off a +11.8% peak), stopped ESPUSDT (−$0.44) → cash | $54.07 (08-22 13:32) |

## Changed
- commodity: whipsawed 3x between DBC and USO on signal flips, ended net long USO.
- hype (sentiment): 5 buy/sell round trips chasing Grok euphoria signals (BTC, MSTR ×2,
  CIFR), landed on MRNA.
- hype-crypto: bought/sold BTC-USD, then bought/sold PENGU-USD same day → cash.
- Hunter: sold NVDA ("outgunned" by BTC reward/risk score), went all-in BTC-USD.
- Lottery (real $): closed ZECUSDT ~breakeven and 币安人生USDT +$1.74 overnight, then exited AXSUSDT +$0.44 (RATCHET — it had been +11.8% at peak) and stopped out
  of ESPUSDT −$0.44 on volume collapse. Flat/cash since 12:04, refusing PUMPUSDT all
  afternoon as LATE (+33% off its 24h low). Book $54.07.
- crypto, congress, meanrev, allweather, Scholar, Analyst: no position changes.
- 110 paper-bot cycles + 257 lottery cycles in 24h, no gaps >15 min — cadence looks healthy.

## Needs a look
- **FIXED TODAY — the lottery's headline return was counting deposits as profit.**
  `exit_auditor.py` computed "book since inception" as live balance ÷ the $40 inception
  stake. The owner had topped the account up ~$22, so that cash was being published as
  performance: the report read **+35.2%** while the 23 closed trades summed to
  **−$7.88 (−19.7%)**. It also inverted the BTC comparison the metric was written for —
  the gap reads **−42.1pp**, not +12.8pp. Return is now computed from trading P&L over
  inception capital, which needs no deposit records and agrees with the alpha table by
  construction; balance and inferred deposits are published separately, never as return.
  Regression test: `tests/test_exit_capture.py`.
- **Deposits are still not recorded anywhere** — not in the ledger, not in the state file.
  The $21.95 above is inferred (balance − stake − P&L). Until deposits are tracked, no
  true time-weighted return is computable and position sizes silently scale with top-ups.
  This is the next thing to fix if the book keeps running past the 09-30 checkpoint.
- Lottery vs its own pre-committed criteria (`LOTTERY_CRITERIA.md`): drawdown floor **not
  breached** (−7.5% off the $58.43 peak; the line is −37.5%, i.e. $36.52 — $17.55 of
  headroom, so the book legitimately keeps trading). Success marker — a revival-sourced
  trade ratcheted past +30% — **not hit**; best ever is 币安人生USDT at +5.1%, and AXSUSDT
  peaked +11.8% and was let go at +1.3%. Win rate 8/23 (35%), avg win +$0.57 vs avg loss
  −$0.83. The exits remain the problem the auditor was built to catch: only 3 of 21 graded
  WELL_TIMED against 9 TOO_EARLY, and 12 of 23 exits are "STALLED — the pump never came."
- Analyst's cash is −$0.85 (was −$0.78 yesterday), drifting further negative — still
  looks like a fee/rounding artifact, not a real overdraft, but it's getting worse.
- sentiment and hypecrypto churned very fast (multiple full round trips within hours);
  worth checking transaction-cost drag isn't quietly eating the gains.
- A new `playbook_state.json` book ("second-account explosion-playbook bot") appeared
  today (created 08-21, flat/no trades yet) — not documented in CLAUDE.md's bot list,
  scope not verified here.
- Same as before: `oracle-bot` (1 commit) and the lottery/scout pipeline remain outside
  CLAUDE.md's documented bot list.
- The 08-21 risk/exit changes (stop→drawdown floor, exit auditor, oracle scoring): the
  exit auditor has now been reviewed — see the deposit bug above. The drawdown floor
  and oracle scoring are still code-only, not evaluated for correctness here.
