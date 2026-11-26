# Fleet Status — 2026-11-26 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged since 11-12, no trade | $1,027.21 |
| meanrev | JPM | Unchanged position; price drifted | $869.64 (vs $870.35 11-25) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 10/10 seats | 9 seats opened in window; seats 6/10 → 10/10 | $490.22 (vs $482.40 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed (~36.5d stale) | n/a |

## Changed
- **scalper**: 9 new entries opened (SENTUSDT, STXUSDT, STRKUSDT, SUPERUSDT, RAYUSDT, NEARUSDT, EWYBUSDT, SKHYBUSDT, PUMPUSDT); seats 6/10 → 10/10 (full); equity $482.40 → $490.22 (net +$7.82). Round-trip counter 2201 → 2225 (+24 closed).
- **crypto, sentiment**: no trades, no position changes.
- **meanrev**: no new trade; still holding JPM (2.7432 units). Value moved $870.35 → $869.64 on price action; dashboard timestamp stuck at 11-25 20:55 — US market holiday (Thanksgiving) today, so expected.
- Routine data refreshes (`social_radar.md`, `smallwins.md`, `announcements.json`, `unlocks.json`, btc execution samples): nothing abnormal.

## Needs a look
- **Cycle gaps**: ~4h08m (09:33→13:41 UTC 11-25) and ~3h34m (19:18→22:53 UTC 11-25) between cycles — well above the usual ~20min cron cadence. No error text in commit messages explaining them.
- **Watcher's Grok risk scan**: unchanged since 2026-10-20T16:09 UTC — now ~36.5 days stale (877h per dashboard).
- **scalper seat TVKUSDT**: still open since 2026-09-12 (~75 days), past the bot's 24h hold cap — known unresolved bug, unchanged.
- **scalper equity** ($490.22) remains below the R1 hard-stop floor ($750); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — ~77 days stale.
- **Scheduled-task roster mismatch (recurring)**: this digest's stored instructions describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md, the active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher; the others are retired/frozen archives.
