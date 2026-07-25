# Fleet status — 2026-07-25 (UTC)

Last cycle: 2026-07-24 22:40 UTC (run completed 22:53, success). All paper accounts, $1,000 start each.

| Bot | Holds | Value | Bench | 24h change |
|---|---|---|---|---|
| trend (crypto) | DOGE-USD | $978.62 | $995.29 | No change |
| regime (stock) | TQQQ | $902.17 | $983.54 | No change |
| congress | NVDA, META, GOOG (70% cash) | $992.19 | $984.30 | No change |
| meanrev | WMT | $1,004.31 | $984.15 | No change |
| commodity | USO | $1,145.80 | $984.15 | No change |
| allweather | 5-asset basket | $997.97 | $984.30 | No change |
| hype (sentiment) | CASH | $1,053.92 | $984.30 | Sold SMCI 07-24 (hype faded) |
| Hunter | USO | $1,052.10 | $984.30 | No change |
| Watcher | advisory only, no position | — | — | Scanned 07-24 17:57 UTC, risk: caution |

## Changed
- hype: sold SMCI 07-24 → CASH ($1,053.92); "hype faded — symbol dropped off Grok's euphoric list."
- No stop-outs. No bot errors — the last completed Actions run (finished 22:53 UTC) had every step succeed.

## Needs a look
- No cycle commits since 2026-07-24 22:40 UTC — a 6h+ gap, still ongoing as of this digest (05:03 UTC). No newer GitHub Actions run has started. This matches the known scheduler-queue throttling the self-looping workflow (added 07-24) was built to survive, but the gap already exceeds a normal hourly landing — worth a look at the Actions tab if it hasn't resumed on its own.
- reports/supervisor_scoreboard.json still shows updated_utc 07-24T07:20 — the supervisor log hasn't refreshed since this morning; likely just its own separate cadence, not confirmed.
