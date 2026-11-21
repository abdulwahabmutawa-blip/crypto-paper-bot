# Fleet Status — 2026-11-21 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged, no trade since 11-12 sell | $1,027.21 |
| meanrev | **JPM** | Stopped out of NVDA (-12% trailing stop), rotated into JPM | $851.86 (live_ts 11-20 20:55 UTC) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 1/10 seats | 4 round trips closed, 0 win/4 loss, net -$4.17; 4 seats closed, none reopened | $468.17 (vs $469.86 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **meanrev**: trailing stop hit on NVDA (11-20, fell 12% from high-water $159.67) → sold at $138.95, then bought JPM at $318.25. Value $919.47 → $851.86.
- **scalper**: 4 round trips closed in the last 24h, all losses (net -$4.17). Open seats dropped 5/10 → 1/10 (only the stuck TVKUSDT seat remains); no new entries this window.
- **crypto, sentiment**: no trades, no position changes.
- `oracle/` directory had new commits (oracle-bot, daily predictions/ledger) — see Needs a look.
- Routine data refreshes (`social_radar.md`, `smallwins.md`, btc execution samples): nothing abnormal.
- GitHub Actions `paper-trade-cycle`: 76 cycle commits over the 24h window (05:11 UTC 11-20 → 05:01 UTC 11-21). Two gaps (~128min, ~125min) are within the documented GitHub schedule-throttling range, not failures. No error/fail commits found.

## Needs a look
- **meanrev now shows a trailing-stop exit** (NVDA, 11-20) — but CLAUDE.md states meanrev "deliberately keeps running without" the trailing-stop/cooldown overlay as an "uncontaminated experiment." This is the second such stop (also happened 11-09). Possible doc/code mismatch worth confirming, not something I changed.
- **Watcher's Grok risk scan still stale**: unchanged since 2026-10-20T16:09 UTC — now 31 days old.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~70 days) — past the bot's 24h hold cap; known unresolved bug.
- **scalper** equity $468.17 remains below the R1 hard-stop floor ($750); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — ~72 days stale.
- **`oracle/` system**: an oracle-bot is committing daily prediction/ledger/scoring files, but it isn't mentioned anywhere in CLAUDE.md. Flagging as an undocumented addition to the repo, not evaluated here.
- **Scheduled-task roster mismatch (recurring)**: this digest's stored instructions describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md, the active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher; the others are retired/frozen.
