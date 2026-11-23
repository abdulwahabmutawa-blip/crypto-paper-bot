# Fleet Status — 2026-11-23 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged, CHOP regime, no trade | $1,027.21 |
| meanrev | JPM | Unchanged position (US equities closed Sat/Sun, Monday not yet closed) | $851.86 (11-20 close) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 10/10 seats | Seats stayed 10/10; 21 round trips closed (16W/5L, net +$11.24) | $480.79 (vs $468.00 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed (805h stale) | n/a |

## Changed
- **scalper**: 21 round trips closed in the window (16 wins, 5 losses, net +$11.24); equity up from $468.00 to $480.79. Seat count held at 10/10 — same coins rotating through as seats free up.
- **crypto, meanrev, sentiment**: no trades, no position changes. meanrev's price data is still dated 2026-11-20 — expected, Monday's US close hadn't happened yet as of this cycle.
- Routine data refreshes (`social_radar.md`, `smallwins.md`, `announcements.json`, btc execution samples): nothing abnormal.
- GitHub Actions cycles: 50 commits in the available lookback window, ~17-18 min apart, one ~116min gap (15:11→17:07 UTC 11-22) consistent with previously-documented GH Actions scheduling throttling. No error or failed-cycle commits found.

## Needs a look
- **Shallow clone limit (recurring)**: this session's checkout only has history back to 2026-11-22 14:03 UTC (~15h), not a full 24h — everything above covers that shorter window.
- **Watcher's Grok risk scan**: unchanged since 2026-10-20T16:09 UTC — now ~34 days stale.
- **scalper seat TVKUSDT**: still open since 2026-09-12 (~72 days), past the bot's 24h hold cap — known unresolved bug, unchanged.
- **scalper equity** ($480.79) remains below the R1 hard-stop floor ($750); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — ~74 days stale.
- **Scheduled-task roster mismatch (recurring)**: this digest's stored instructions describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md, the active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher; the others are retired/frozen archives.
