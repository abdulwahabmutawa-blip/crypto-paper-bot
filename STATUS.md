# Fleet Status — 2026-11-22 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged, no trade since 11-12 sell | $1,027.21 |
| meanrev | JPM | Unchanged position (US equities closed Sat/Sun) | $851.86 (11-20 close) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 10/10 seats | Seats filled 1/10 → 10/10; 7 round trips closed (4W/3L, net +$0.61) | $468.00 (vs $468.17 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **scalper**: 9 new seats opened (STXUSDT, RENDERUSDT, UNIUSDT, ETCUSDT, PYTHUSDT, ARUSDT, ICPUSDT, ERAUSDT, INJUSDT), filling the book to 10/10. 7 round trips closed: 4 wins (+$4.71), 3 losses (-$4.10), net +$0.61. Equity roughly flat.
- **crypto, meanrev, sentiment**: no trades, no position changes. meanrev's price data is still dated 2026-11-20 because US equity markets are closed over the weekend — expected, not a stall.
- Routine data refreshes (`social_radar.md`, `smallwins.md`, btc execution samples): nothing abnormal.
- GitHub Actions cycles: 49 commits in the available lookback window, ~17-18 min apart, one ~2h24m gap (13:57→16:21 UTC 11-21) consistent with previously-documented GH Actions scheduling throttling. No error or failed-cycle commits found.

## Needs a look
- **Shallow clone limit**: this session's checkout only has history back to 2026-11-21 12:49 UTC (~16h), not a full 24h — everything above covers that shorter window, not a true 24h span.
- **Watcher's Grok risk scan**: unchanged since 2026-10-20T16:09 UTC — now 33 days stale.
- **scalper seat TVKUSDT**: open since 2026-09-12 (~71 days), past the bot's 24h hold cap — known unresolved bug.
- **scalper equity** ($468.00) remains below the R1 hard-stop floor ($750); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — ~73 days stale.
- **Scheduled-task roster mismatch (recurring)**: this digest's stored instructions describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md, the active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher; the others are retired/frozen archives.
