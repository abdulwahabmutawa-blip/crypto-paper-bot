# NEW-BOOK HANDOFF — ship the Explosion Playbook on a second Binance account
*Written 2026-08-21 by the PC session. For the LAPTOP Claude session: read this
top to bottom before doing anything. The owner will add their own guidelines on
the laptop — those override anything here.*

## What this is
The owner runs a live $37+ "lottery" book on this repo's `src/lottery_live.py`
(VPS, account #1). A 3-day, 245-explosion study + 29-agent verified analysis
produced THE EXPLOSION PLAYBOOK — a new entry/exit stack to be shipped as a
**separate book on a second Binance account**, so the two strategies never
touch each other's balances or records.

## Non-negotiable ground rules (owner-established, do not relax)
1. **Never mix the two accounts.** New API keys, new env file, new state files,
   new ledger. The existing lottery book and its VPS service stay untouched.
2. Claude never places manual trades or picks coins for the owner (hard line).
3. All-in %-based sizing; NO dollar amounts in any rule (owner decision 08-21:
   "amount of money should not matter"). Floor = drawdown % of book peak.
4. Real-money behavior changes need explicit owner approval. Paper first when
   in doubt. Report failures honestly — this project kills bad ideas with data.
5. API keys: spot-only permissions, withdrawals DISABLED, IP-whitelisted to
   wherever the runner lives. Owner enters keys into env files themselves —
   never paste keys into chat.
6. Owner is in Kuwait: banking rails are the sensitive part, not trading.
   Never enable anything but spot. (Context: research 08-21, Kuwait circulars.)

## The strategy to ship (distilled playbook — full evidence on the PC in
## trading-research\explosion_anatomy\PLAYBOOK_2026-08-21.md)
**Goal: catch +20%+ explosions; enter on trigger inside gates; exit on tape,
not clocks.** All thresholds carry a ONE-WAVE-WEEK calibration caveat (08-18..21,
52% of pairs moved). Expect ~+11-15% median capture per winner, NOT +21%.

### Candidate hygiene (always on, any regime)
- 24h quote volume >= ~$1M; skip movers whose gain is >70% one candle or that
  wick-retraced >80% same-candle; never rank post-crash/post-hack/delisting
  gainers as momentum (crash-low artifacts).

### Entry (gated trigger, not a bare threshold — bare volume triggers verified
### at 2.4% precision, useless)
- REGIME GATE: wave flag on (breadth >= ~3x baseline; the fleet's
  data/breadth.json) → hunt wave-beta; wave off → only calendar-class setups.
- TRIGGER: back-to-back >+4% hourly closes on >=3x baseline volume breaking a
  multi-day flat base; or 2-consecutive-rising-closes + >=1.5x vol variant.
- Late-entry guard family stays (run-up cap vs 24h low, no-room, rolled-over) —
  values per account #1's binance_live.py; proposal #6 (relax rolled-over on
  wave days) is NOT yet owner-approved.
- Sibling rotation (wave days): a vertical candle in one family member is an
  entry signal for its flat siblings (~70-min observed lag).

### Exit stack (priority order, first trigger wins)
1. CALENDAR EXPIRY: never hold toward a wallet reopen / unlock / borrow window
   end (exchange notices are public days ahead).
2. CLIMAX EXIT: red 1h close on volume >= the move's running max (fallback
   >=5x move average), close in lower half of range → out at that close.
   Holding through a vertical bar: first close below its midpoint = out.
3. TERMINAL-DIP BACKSTOP: 3h drawdown >=12% from high-water (on closes, not
   wicks) → out. (82% of such dips were terminal; resumed pullbacks median
   -6.5%, never -20%.)
4. RATCHET: arm at +10%, floor = 50% of peak gain. (+4% arm was shaken out
   240/245 times — do not use early arming.)
5. PROTECTIVE STOP: -6% from entry.
6. TIME CAP: 48h safety net (24h caps amputate wave moves — +7.2% median,
   >half-move only 10.6%).
- Volume-dead ("fuel gone") exit from account #1 is complementary (different
  top type: quiet fades, ~28% of peaks) — include it.

### Book guardrails (copy from account #1's pattern)
- Drawdown floor: no entries below 62.5% of the book's own peak value; breach
  = stop + post-mortem. 3+1 wave-day entry budget. 3h re-entry cooldown per
  coin. Exits always allowed.

## How account #1 runs (mirror this architecture)
- `src/lottery_live.py` + `src/binance_live.py`; armed ONLY when
  `LOTTERY_LIVE=1` and keys present (defense in depth in `market()`).
- VPS: systemd `deploy/lottery.service` + `lottery.timer` (~5-min cycles),
  env in `/etc/lottery.env`, repo pulled every cycle, state committed back.
- Data hosts: data-api.binance.vision FIRST (api.binance.com geo-blocks some
  runners); mainnet trading via api.binance.com signed calls.
- Ledger/state pattern: data/lottery_state.json + data/lottery_ledger.jsonl;
  exit_auditor.py grades every exit at +24h; reports/exit_timing.md carries
  alpha-by-regime. BUILD THE SAME for the new book with new filenames
  (suggest: playbook_state.json / playbook_ledger.jsonl, key "playbook").

## Laptop bring-up checklist (Claude: walk the owner through this)
1. Owner creates API keys on Binance account #2: spot trade + read ONLY,
   withdrawals off, IP whitelist. Owner keeps them out of chat.
2. Enable BNB fee payment on account #2 + hold a few USD of BNB (25% off).
3. Decide the runner: second env file + second systemd unit on the existing
   VPS (recommended; cheapest, proven) OR the laptop itself (fragile — sleeps).
4. Implement `src/playbook_live.py` per the strategy above (new module; do
   NOT modify lottery_live.py). Reuse binance_live.py helpers via a broker
   object parameterized by env-var prefix (e.g. PLAYBOOK_API_KEY...) so the
   two books cannot share keys or state. Same armed()-style hard gate:
   `PLAYBOOK_LIVE=1`.
5. Tests first (mirror tests/test_lottery_guards.py), then DRY-RUN mode
   (log-only, no orders) for at least a few cycles, then owner arms it.
6. Wire exit_auditor to also grade the new ledger; add the new book to
   reports/exit_timing.md market-capture so underperformance is visible from
   day one. Alpha-by-regime discipline applies: green-day gains are tide.
7. Never conclude from the first wins. The 08-26 review (and 09-30
   checkpoint) covers both books.

## Current live context (as of 2026-08-21 ~15:40 UTC)
- Account #1 book $37.85 + fresh owner deposits; holding AXSUSDT (ignition)
  ~+2%; entries 4/4 used; 2nd wave day running (breadth ~100+, baseline 14).
- Strategy freeze on account #1 until ~08-26 (playbook proposals #1-#10 in
  PLAYBOOK_2026-08-21.md §6 await owner approval there; hygiene #8 and
  calendar watcher #5 pre-approved as risk-free by the plan of record).
- Oracle (predict-only) first scoring 2026-09-16; SCORING_PLAN.md is
  pre-registered; feature→book promotion gate applies to BOTH books.

## Where the full evidence lives (PC only, not in this repo)
`C:\Users\a.almutawa\trading-research\` — PLAYBOOK_2026-08-21.md,
oracle_forensics_2026-08-21.md, kuwait_swing_day_research_2026-08-21.md,
daytrading_research_2026-08-21.md, exit_study\, explosion_anatomy\ (movers.json,
exit_tournament.json, entry_timing.json, shapes.json). Owner can copy the
folder to the laptop if the session needs the numbers behind any rule.
