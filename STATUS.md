# Fleet status — 2026-07-29 (UTC)

Last cycle: 2026-07-29 05:06 UTC (success). All paper accounts, $1,000 start each.

| Bot | Holds | Value | Bench | 24h change |
|---|---|---|---|---|
| trend (crypto) | SOL-USD | $1,014.79 (asof 07-29) | $991.60 | 4 round-trips (ADA→XRP→SOL→XRP→SOL), all "signal flip" |
| regime (stock) | TQQQ | $867.78 (asof 07-28) | $986.10 | No trade; mark keeps sliding, no stop by design |
| congress | NVDA, META, GOOG (+$700 cash) | $991.36 (asof 07-28) | $986.87 | No change |
| meanrev | AMZN | $1,046.88 (asof 07-28) | $986.68 | WMT → AMZN (07-28), signal flip, banked +$46.33 |
| commodity | USO | $1,010.15 (asof 07-28) | $986.68 | No trade; mark down further, no stop by design |
| allweather | 5-asset basket | $998.47 (asof 07-28) | $986.87 | No change |
| hype (sentiment) | CASH | $896.16 (asof 07-28) | $986.87 | RKLB → CASH (07-28), "hype faded" |
| Hunter | ETH-USD | $924.04 (asof 07-28) | $986.87 | USO → ETH-USD (07-28), "outgunned on reward/risk" |
| Watcher | advisory only, no position | — | — | Scanned 2026-07-29 03:47 UTC, risk: caution |

## Changed
- **trend/crypto**: unusually high turnover — 4 flips in ~24h (ADA→XRP→SOL→XRP→SOL), each logged as "signal flip"/"strongest eligible coin." Net effect roughly flat-to-up ($982.08 → $1,014.79).
- **meanrev**: sold WMT for +$46.33 gain, rotated into AMZN (both "oversold mega-cap" signal), 07-28.
- **Hunter**: sold USO, bought ETH-USD (07-28) — reward/risk board re-picked Ethereum over Oil.
- **hype/sentiment**: exited RKLB (07-28, "hype faded off Grok's list"), back to 100% cash.
- No stop-loss trips, no failed cycles, no exceptions found in the 50 commits reviewed.

## Needs a look
- **Supervisor/judgment pipeline stale**: `reports/judgments.jsonl`, `trade_attributions.jsonl`, and `supervisor_scoreboard.json` have no entries newer than 2026-07-26, even though trading cycles are committing normally through today. That side process (not the trading bots themselves) looks stuck.
- **regime/stock (TQQQ)**: down to $867.78, worst book in the fleet (~-13% since inception), no risk overlay by design — flagging in case that's meant to change.
- **commodity (USO)**: down from its 07-24 peak of $1,145.80 to $1,010.15 with no stop-loss trade — same "no risk overlay by design" as above, not new.
- Two cron gaps this window (2h25m on 07-28, 6h07m 07-28→07-29) — both within the range the workflow's own comments document as expected GitHub-throttling behavior, not treated as a failure.
