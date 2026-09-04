# Hype trader on IBKR — setup, paper first, then $300 live

The bot: `src/hype_ibkr.py` (rules) + `src/ibkr_live.py` (broker adapter).
It runs on the same VPS as the lottery book, against an **IB Gateway**
container that holds your IBKR login. Paper money by default; real money
only with two explicit flags.

Rules at $300 (why: a $1-minimum commission is 0.67% of a $300 round trip,
and a cash account cannot re-buy with unsettled proceeds): one position,
dollar-sized to settled cash, min hold 2 trading days, max 2 entries per
7 days, -10% stop, SEVERE = sell, US stocks only, regular hours only.

---

## A. IBKR account (Client Portal → Settings) — you

1. **API access**: Settings → API → Settings: enable "API" for your user.
2. **Paper account**: Settings → Paper Trading Account → note the paper
   username (your username + one letter, e.g. `abdul123` → `abdul123p`)
   and set/reset its password.
3. **Fractional shares**: Settings → Trading Permissions → United States
   (Stocks) → tick "Fractional shares". Needed for $300 in NVDA-priced names.
4. **Market data**: Settings → Market Data Subscriptions → "US Securities
   Snapshot and Futures Value Bundle" (cheap). Without it quotes are 15
   minutes delayed, which is the stale-fill problem the paper bot had.
5. Leave the live account unfunded until section D.

## B. IB Gateway on the VPS — you (paste as root over SSH)

```bash
apt-get update -qq && apt-get install -y -qq docker.io
install -m 600 /dev/null /etc/ibgateway.env
nano /etc/ibgateway.env
```
Put in the file (paper first):
```
TWS_USERID=your_paper_username
TWS_PASSWORD=your_paper_password
TRADING_MODE=paper
READ_ONLY_API=no
TWOFA_TIMEOUT_ACTION=restart
```
Then:
```bash
docker run -d --name ibgateway --restart unless-stopped \
  --env-file /etc/ibgateway.env -p 127.0.0.1:4002:4004 -p 127.0.0.1:4001:4003 \
  ghcr.io/gnzsnz/ib-gateway:stable
sleep 60; docker logs ibgateway --tail 30
```
The first login may ask for a confirmation in the **IBKR Mobile** app.
When the log shows the Gateway logged in, check the port answers:
```bash
python3 - <<'PY'
import socket; s=socket.socket(); s.settimeout(3); print("paper port:", "open" if s.connect_ex(("127.0.0.1",4002))==0 else "closed")
PY
```

## C. Bot on the VPS — you (once), then it runs itself

```bash
cd /opt/tradebot/cloud-bot && sudo -u tradebot git pull -q
pip3 install -q ib_async
install -m 600 /dev/null /etc/hype_ibkr.env
nano /etc/hype_ibkr.env
```
Contents for PAPER:
```
HYPE_IBKR_ARMED=1
IBKR_HOST=127.0.0.1
IBKR_PORT=4002
IBKR_CLIENT_ID=7
HYPE_IBKR_MAX_USD=300
XAI_API_KEY=same_key_as_in_lottery.env
```
Install the units and run one cycle by hand:
```bash
cp deploy/hype_ibkr.service deploy/hype_ibkr.timer /etc/systemd/system/
systemctl daemon-reload
systemctl start hype_ibkr.service; journalctl -u hype_ibkr.service -n 30 --no-pager
systemctl enable --now hype_ibkr.timer; systemctl list-timers hype_ibkr.timer --no-pager
```
Expected first line: `[hype-ibkr] PAPER seat=CASH net $1000000.00 ...` (IBKR
paper accounts start with fake $1M; the bot still caps each order at
HYPE_IBKR_MAX_USD so the paper record matches the $300 plan).

Watch: `tail -5 data/hype_ibkr_ledger.jsonl` and the state file; every
fill carries `"paper": true`. Any `fill_anomaly` line means the fill sat
more than 3% from the quote — read it before going live.

## D. Going live with $300 — you, after 2-4 weeks of paper

1. Fund the live account with the $300 (cash account, no margin).
2. `nano /etc/ibgateway.env`: `TWS_USERID` = live username, `TRADING_MODE=live`;
   `docker restart ibgateway`; confirm port 4001 answers.
3. `nano /etc/hype_ibkr.env`: `IBKR_PORT=4001` and add `HYPE_IBKR_REAL=1`.
   Without BOTH the adapter refuses to connect (ledger: `refused`).
4. `systemctl start hype_ibkr.service` and read the journal: the summary
   line must say `LIVE`.

## Stopping
- `touch /opt/tradebot/cloud-bot/data/KILL_SWITCH` (no orders), or
- `systemctl stop hype_ibkr.timer`, or
- remove `HYPE_IBKR_ARMED=1` from the env file, or
- disable API access in Client Portal (the wedge-proof one).

## What to judge it on
Net P&L on `pnl_usd` (commissions included) over at least 20 round trips,
against holding SPY. Two entries a week means that is roughly 10 weeks; a
$300 book that is not net positive by then does not get more money.
