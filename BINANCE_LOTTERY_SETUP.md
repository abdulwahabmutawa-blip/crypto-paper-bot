# Lottery book — arming the real ~$11 (owner-only steps)

Real money, deliberately tiny: `src/binance_live.py` hard-caps the managed
book at **$20**. If it ever sees more, every order halts and the ledger
red-flags. This book is NOT the Track C pilot and cannot silently become it.

The odds, printed on the ticket: documented base rates for small-account
pump-chasing say **losing the $11 is the expected outcome**. Arm it knowing
that.

## Arm (two deliberate acts, both yours)

1. Binance app/site → **Account → API Management → Create API**:
   - Enable **Reading** and **Spot & Margin Trading** ONLY.
   - **Withdrawals: OFF** (leave unchecked — non-negotiable; a leaked
     trade-only key can lose the $11 on bad trades but cannot drain the
     account).
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
- Never raise `BOOK_CAP_USD` because the book got lucky — real capital goes
  through the Track C gate (GO_LIVE_PLAN_2026-08-14.md), not through a cap
  edit on the slot machine.
