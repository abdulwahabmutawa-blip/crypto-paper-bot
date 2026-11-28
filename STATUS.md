# Fleet Status — 2026-11-28 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged since 11-12, no trade | $1,027.21 |
| meanrev | JPM | No trade; price refreshed to Fri 11-27 close | $885.55 (vs $869.64 yday) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 7/10 seats | 17 round trips closed (5 TARGET, 7 STOP, 5 TIME) | $493.72 (vs $498.41 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed (~925h / ~38.5d stale) | n/a |

## Changed
- **scalper**: 17 closed round trips in the window (wins: HEIUSDT, ANTBUSDT, SKYUSDT, SNDKBUSDT, BCHUSDT; stops: DOTUSDT, TQQQBUSDT, SKHYBUSDT, GOOGLBUSDT, MAGICUSDT, NOMUSDT, ATUSDT; time-exits: TRXUSDT, THETAUSDT, WIFUSDT, QQQBUSDT, SPCXBUSDT). Equity $498.41 → $493.72 (net −$4.21). Seats dropped from 10/10 to 7/10, not yet refilled as of the last cycle.
- **meanrev**: no new trade; still holding JPM. Value moved $869.64 → $885.55 as the price feed advanced to Friday 11-27's close (previously frozen at 11-25).
- **crypto, sentiment**: no trades, no position changes.
- Routine data refreshes (`social_radar.md`, `smallwins.md`, `announcements.json`, btc execution samples): nothing abnormal.

## Needs a look
- **Cycle gaps**: ~4h24m (11:06→15:31 UTC 11-27) and ~2h50m (20:59→23:49 UTC 11-27) between cycles — above the usual ~17min cron cadence, same time-of-day pattern as yesterday's gaps. No error text in commit messages.
- **Watcher's Grok risk scan**: unchanged since 2026-10-20T16:09 UTC — now ~925h (~38.5 days) stale.
- **scalper seat TVKUSDT**: still open since 2026-09-12 (~77 days), past the bot's 24h hold cap — known unresolved bug, unchanged.
- **scalper equity** ($493.72) remains below the R1 hard-stop floor ($750); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — ~79 days stale.
- **Scheduled-task roster mismatch (recurring)**: this digest's stored instructions describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md, the active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher; the others are retired/frozen archives.
