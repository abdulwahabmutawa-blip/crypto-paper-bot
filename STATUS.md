# Fleet status — 2026-09-07 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | ADA-USD | No new trade — marks only | $1,133.47 |
| meanrev | HD | No new trade — marks only (US mkt closed, Labor Day) | $1,298.52 (09-04 mark) |
| sentiment | RAY-USD | Sold to CASH 09-04, re-bought RAY-USD 09-07 00:41 UTC | unclear — see below |
| scalper | 10 open seats | 31 round trips closed (16W/15L), net -$1.57 | $1,011.38 |
| smallwins (lab) | 557 open seats | 216 runs, 7,110 resolved total; still no tactic at "pass" | n/a — paper study, no $ book |
| lottery — REAL MONEY | CASH (flat) | Stopped BNBUSDT -3.0% and PROMUSDT -3.1%, circuit breaker halted new entries; no re-entry found yet today | $35.57 |
| Watcher | — (no capital) | New scan 09-07 00:41 UTC — caution, 2 risk alerts (Iran tensions, Fed pressure) | n/a |
| retired (8, frozen) | commodity, allweather, scholar, congress, hunter, analyst, hypecrypto, stock | No change | — |

## Changed
- **scalper**: 31 round trips in the last 24h (16W/15L), net -$1.57, equity down slightly to $1,011.38.
- **lottery (real money)**: two more stop-outs (BNBUSDT -3.0%, PROMUSDT -3.1%, combined -$2.30), which
  tripped its own circuit breaker (2 losing exits/day) and halted new entries for the rest of 09-06.
  Back to scanning today but found no eligible pair yet; currently flat.
- **sentiment**: bought RAY-USD again (trade log timestamp 09-07 00:41 UTC).
- **Watcher**: first fresh scan since 09-05 22:14 UTC — risk level caution, 2 alerts.
- No skipped or failed cycles: paper-fleet ran every ~15-20 min, lottery every ~5-8 min — no gap
  over 20 min anywhere in the window.
- Not part of this fleet but new in the repo's last 24h: an "oracle" forecasting system
  (oracle-bot commits) unrelated to the 9-bot roster — not covered by this digest.

## Needs a look
- **sentiment data inconsistency**: daily history already shows it holding RAY-USD on 2026-09-05,
  but the trade log's only RAY-USD BUY is dated 2026-09-07 — no SELL/BUY pair bridges 09-04 (CASH)
  to 09-05 (RAY-USD shown). History also has no entries for 09-06 or 09-07 despite the bot running.
  Current equity for sentiment is not reliably known from the data — treat $1,221.07 (09-05) as stale.
- **lottery is real money, no cap** — $35.57 vs its $44.27 high-water mark (post-mortem floor at
  62.5% of peak = $27.67, not yet breached, but two stop-outs in one day is worth a look).
- **smallwins lab**: still zero tactics at "pass" after 216 runs / 7,110 resolved trades.
- CLAUDE.md's roster list (trend/regime/congress/commodity/allweather/hype/Hunter) is out of date —
  actual active books are crypto, meanrev, sentiment, scalper (+ smallwins lab, + lottery real-money).
