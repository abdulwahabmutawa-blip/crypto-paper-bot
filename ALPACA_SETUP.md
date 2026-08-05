# Alpaca paper-trading shadow — setup (owner steps)

The meanrev bot mirrors every trade to an Alpaca **paper** account (fake
money, free) and records the real fill price beside the sim's assumed fill
(`broker_fill` + `fill_gap_bps` in the trade ledger). Until keys exist,
everything is a silent no-op.

Only you can do these steps (account creation + credentials):

1. Create an account at <https://alpaca.markets> (choose the free
   individual account; no funding needed — paper trading is separate fake
   money).
2. In the dashboard, switch to **Paper** (toggle top-left), then generate
   API keys: *Home → API Keys → Generate*. You get a Key ID and a Secret.
3. Add both as GitHub secrets in the `crypto-paper-bot` repo:
   *Settings → Secrets and variables → Actions → New repository secret*
   - `ALPACA_API_KEY_ID` = the Key ID
   - `ALPACA_API_SECRET_KEY` = the Secret
4. Done. Next cycle picks them up automatically.

Safety notes:
- `src/alpaca_broker.py` hardcodes the **paper** endpoint
  (`paper-api.alpaca.markets`) — a live key pasted by mistake cannot trade
  real money through this code path.
- Shadow only: the sim's books stay the source of truth; a broker outage
  or rejected order never blocks a bot.
- Rollout: meanrev first (fewest trades). Widen to other equity bots by
  adding `"broker_shadow": True` to their SPEC once the fill-gap data
  looks sane for a week.
