# Fleet Status — 2026-11-27 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged since 11-12, no trade | $1,027.21 |
| meanrev | JPM | Unchanged position; price frozen at 11-25 close (pre-market Fri) | $869.64 |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 10/10 seats | 15 round trips closed (11 TARGET, 2 STOP, 2 TIME); seats stayed full | $498.41 (vs $490.22 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed (~901h / ~37.5d stale) | n/a |

## Changed
- **scalper**: 15 closed round trips in the window (wins: KORUBUSDT, SENTUSDT x2, SNDKBUSDT, TRUMPUSDT, TIAUSDT, SKYUSDT, FETUSDT, SAGAUSDT, SEIUSDT, WIFUSDT; losses: SOPHUSDT stop, SAGAUSDT stop, EWYBUSDT time, SUPERUSDT time). Equity $490.22 → $498.41 (net +$8.19). Seats stayed full (10/10) throughout.
- **crypto, sentiment**: no trades, no position changes.
- **meanrev**: no new trade; still holding JPM. Value unchanged from yesterday's report ($869.64) — US market has not opened yet for Friday as of this run.
- Routine data refreshes (`social_radar.md`, `smallwins.md`, `announcements.json`, `unlocks.json`, btc execution samples): nothing abnormal.

## Needs a look
- **Cycle gaps**: ~4h35m (10:30→15:05 UTC 11-26) and ~3h07m (20:42→23:49 UTC 11-26) between cycles — above the usual ~17min cron cadence. No error text in commit messages explaining them.
- **Watcher's Grok risk scan**: unchanged since 2026-10-20T16:09 UTC — now ~901h (~37.5 days) stale.
- **scalper seat TVKUSDT**: still open since 2026-09-12 (~76 days), past the bot's 24h hold cap — known unresolved bug, unchanged.
- **scalper equity** ($498.41) remains below the R1 hard-stop floor ($750); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — ~78 days stale.
- **Scheduled-task roster mismatch (recurring)**: this digest's stored instructions describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md, the active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher; the others are retired/frozen archives.
