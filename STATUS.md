# Fleet status — 2026-09-27 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No trade; TREND regime intact | $1,203.75 (was $1,199.41 pre-outage) |
| meanrev | HD | No trade; data_asof 09-25 (weekend, feed_delayed=false) | $1,185.35 (unchanged since Fri close) |
| sentiment | CASH | No trade — still in cash | $869.30 (unchanged) |
| scalper | 10/10 seats | ~100 round trips settled once loop resumed | $934.32 (was $932.41 pre-outage) |
| smallwins (lab) | 578 open seats | 264 new runs (1705→1969); open 248→578 | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STILL STUCK: 0 new scans since 09-11 15:12 UTC (~16 days) | n/a |
| social_radar | — (no capital) | Same root staleness — unchanged since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No change | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) out of scope for this digest per CLAUDE.md.

## Changed
- **Paper-fleet cron outage**: zero cycle commits from 2026-09-24 05:11 UTC to 2026-09-27 01:43
  UTC — a ~68.5h gap, far beyond the workflow's own documented worst case (~11.25h). Loop resumed
  on its own at 01:43 UTC today and has run normally since (13 cycle commits, ~13-17 min apart).
- The VPS lottery process (separate, real-money, out of scope) shows the identical blackout window
  (last commit 09-24 05:11, resumed 01:45 today) on a different host.
- crypto: no trade; BTC-USD marked $1,199.41 → $1,203.75 across the gap.
- scalper: ~100 round trips settled on resume — candle-close exits are retrospective/backdated
  (per CLAUDE.md), so these reflect market moves during the outage, not live decisions made then.
  Equity $932.41 → $934.32; seats back to 10/10.
- smallwins: 264 new lab runs once resumed; open seats 248 → 578.
- meanrev, sentiment: no trades; both flat.

## Needs a look
- **Outage cause unknown**: no RED FLAG commit, no state_preflight failure recorded for the
  2026-09-24 05:11 → 2026-09-27 01:43 window. Repo data alone can't explain it — check GitHub
  Actions run history and the VPS lottery logs directly.
- **`reports/supervisor_scoreboard.json` looks stale/wrong**: its `run_note`/`loop_health` (last
  touched by the commit that ended the outage) claims "loop healthy, 175 commits/48h, max gap 34
  min" as of 2026-09-26T12:30 — a time when git shows zero commits for ~31h already. Don't trust
  that file's loop-health numbers until it's regenerated.
- **scalper/TVKUSDT seat**: still open, day 15 (entered 2026-09-12) — known SIM-INTEGRITY issue,
  priced off a dead 2023-11-27 Binance candle (delisted pair, ~$86 of book unpriced). Reported to
  owner, not yet fixed.
- **Watcher (grok_sentinel) / social_radar**: still silent since 2026-09-11 (~16 days). Sentiment
  stays gated in cash as a result.
