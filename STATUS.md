# Fleet status — 2026-08-05 (UTC)

Last cycle: 2026-08-04 22:09 UTC. $1,000 paper start/bot. 50 cycle commits in shallow-clone window (08-04 09:47 → 22:09).

| Bot | Holds | Value (asof) | 24h change |
|---|---|---|---|
| trend (crypto) | CASH | $1,078.77 (08-04) | Churn: BUY→SELL→CASH on LINK-USD, 3x in a row (signal flip each time) |
| congress | NVDA, META, GOOG, TSM (+$600 cash) | $1,015.65 (08-04) | No new trade (positions unchanged since 08-03) |
| meanrev | UNH | $1,250.62 (08-04) | SELL PG → BUY UNH (signal flip, new most-oversold pick) |
| commodity | USO | $970.49 (08-04) | No trade |
| allweather | 5-asset basket | $1,004.95 (08-04) | No trade |
| hype (sentiment) | PLTR | $1,125.10 (08-04) | SELL CRWV → BUY PLTR (hype rotation on Grok scan) |
| Hunter | PLTR | $948.17 (08-04) | SELL UPRO → BUY PLTR ("outgunned" reward/risk switch) |
| Scholar | IWM | $1,028.73 (08-04) | No trade |
| Analyst | SPY | $1,028.27 (08-04) | No trade |
| Watcher | advisory, no position | — | Last scan 08-04 16:24 UTC: risk "caution" (crypto extreme fear, Amazon antitrust suit/Bezos share sale) |

## Changed
- **crypto/trend**: three round trips into LINK-USD and back to cash on repeated signal flips; ended in cash.
- **meanrev**: rotated PG → UNH on a fresh oversold signal.
- **hype/sentiment**: CRWV faded off Grok's euphoric list, rotated into PLTR.
- **Hunter**: exited UPRO into PLTR after PLTR scored >1.25x better reward/risk.
- congress, commodity, allweather, Scholar, Analyst: no position changes, values just marked to market.
- No stop-outs, no exceptions found in state files for this window.

## Needs a look
- No cycle commit since 08-04 22:09 UTC — ~7h stale as of this digest (now 08-05 05:06 UTC). The workflow's own docs say GitHub queue-throttles scheduled starts hard (measured max gap 675 min ≈ 11.25h), so this is within known/expected range — flagging as a stale mark, not a confirmed failure. Worth checking if it's still stale next digest.
- Repo is a shallow clone (50-commit window) — history before 08-04 09:47 UTC wasn't inspectable this run.
