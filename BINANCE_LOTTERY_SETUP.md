# Lottery book — arming the real money (owner-only steps)

Real money: `src/binance_live.py` spends the account's full free USDT
balance on every BUY. The original **$20 hard cap** was removed by owner
decision on 2026-08-16 after a manual top-up — every order now risks
whatever USDT actually sits in this account. This book is NOT the Track C
pilot, but with no cap it no longer stops itself from growing into one; that
line is on the owner now, not the code.

The odds, printed on the ticket: documented base rates for small-account
pump-chasing say **losing the stake is the expected outcome**. Arm it
knowing that — and know there is no ceiling on the stake anymore.

## Arm (two deliberate acts, both yours)

1. Binance app/site → **Account → API Management → Create API**:
   - Enable **Reading** and **Spot & Margin Trading** ONLY.
   - **Withdrawals: OFF** (leave unchecked — non-negotiable; with no book
     cap, a leaked trade-only key can now lose the account's FULL balance on
     bad trades — withdrawals-off is the only thing stopping it from also
     being drained outright).
   - IP whitelist: GitHub Actions has no fixed IPs; leaving it unrestricted
     is the tradeoff for a trade-only key. Never enable withdrawals on an
     unrestricted key.
2. Repo → Settings → Secrets and variables → Actions:
   - **Secrets** tab: add `BINANCE_LIVE_API_KEY` and
     `BINANCE_LIVE_API_SECRET`.
   - **Variables** tab: add `LOTTERY_LIVE` = `1`.

Missing either half = the bot logs "not armed" and does nothing.

## What runs once armed

Every ~13-min cycle: mechanical selector (Watcher's freshest euphoric
crypto, else top 24h Binance gainer >$20M volume), one entry per weekday
max, full capped balance per seat, -10% hard stop, exits on faded hype /
stale scans / SEVERE. Every fill and refusal appends to
`data/lottery_ledger.jsonl` in the repo — the public honest history.

## Disarm (either works, immediately)

- Set the `LOTTERY_LIVE` variable to `0` (or delete it), or
- Add a file named `KILL_SWITCH` inside `data/` (GitHub web UI → Add file)
  — blocks every order at the guard, including the paper pilot rails.

## Never

- Never enable withdrawals on this key.
- There is no cap left to accidentally raise (removed 2026-08-16) — the
  remaining discipline is manual: don't leave more in this account than
  you're willing to see this bot lose entirely.
