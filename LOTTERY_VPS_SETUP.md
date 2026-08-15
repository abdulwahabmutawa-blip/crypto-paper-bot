# Lottery book on a VPS — exact steps

Why a VPS: Binance deletes a trading-enabled API key that has no IP
restriction, and GitHub Actions has no fixed IP to whitelist. A small cloud
box has exactly one permanent IP, so the key stays locked to a single
machine you control. Cost ~$4–5/month.

Split of duties, deliberately: **GitHub Actions keeps running the paper
fleet and the Watcher** (no real keys ever live there). **The VPS runs only
`lottery_live.py`** with the real key. The two talk through the git repo —
Actions publishes fresh Watcher scans, the VPS reads them and publishes its
ledger back.

The book is capped at **$20** in `src/binance_live.py`. Expected outcome of
pump-chasing at this size is loss of the stake; the cap and the ledger make
that honest rather than surprising.

---

## STEP 0 — prove the key is really Binance's (do not skip)

An API key minted on a look-alike site cannot sign a request the real
exchange accepts. `src/verify_binance_key.py` settles it. Run it on the VPS
in Step 6, after the IP is whitelisted. If it prints **KEY NOT ACCEPTED**
and the IP is definitely whitelisted, treat the issuing site as hostile:
from a trusted device, type `binance.com` by hand, change the password,
revoke all API keys, and review sessions and withdrawal whitelists.

Genuine Binance surfaces: `binance.com`, `accounts.binance.com`, and the
official mobile app. Nothing else.

---

## STEP 1 — create the server

Either provider, cheapest tier, Ubuntu 24.04 LTS:

- **Hetzner Cloud** — CX22, ~€3.79/mo. Console: <https://console.hetzner.cloud>
- **DigitalOcean** — Basic Droplet $4/mo. Console: <https://cloud.digitalocean.com>

During creation:
- Image: **Ubuntu 24.04 LTS**
- Region: closest to you (Falkenstein/Frankfurt for Hetzner, Frankfurt for
  DO — low latency to Binance's EU endpoints)
- **Add your SSH key** (both providers offer paste-a-public-key). If you
  have none, on Windows PowerShell: `ssh-keygen -t ed25519` then paste the
  contents of `C:\Users\Hobii\.ssh\id_ed25519.pub`.
- Skip backups/volumes/monitoring — nothing here is precious.

Write down the server's **IPv4 address**. That is the address you whitelist.

---

## STEP 2 — one paste does the whole install

SSH in (`ssh root@SERVER_IP` from PowerShell) and run exactly this:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/abdulwahabmutawa-blip/crypto-paper-bot/main/deploy/bootstrap.sh)
```

It patches the box, locks SSH to keys only, enables the firewall, creates
the unprivileged `tradebot` user, clones the repo, installs dependencies
and the systemd units, generates a deploy key, and prints:

- **the server's IP** (what you whitelist on the Binance key), and
- **the deploy key** to paste into GitHub → repo → Settings → Deploy keys →
  *Allow write access*.

It arms nothing: no key is written and the timer stays off. Re-running it is
safe — after you add the deploy key, run it a second time and it switches
the remote to SSH so the ledger publishes to GitHub.

Steps 3–5 below are what the script leaves for you.

---

## STEP 3 — whitelist the IP on the API key

In the Binance app or on `binance.com` → **API Management** → edit your key:

- Permissions: **Enable Reading** + **Enable Spot & Margin Trading**.
- **Enable Withdrawals: OFF.** Non-negotiable. A stolen trade-only key can
  lose the $11 on bad trades; it cannot move coins out of the account.
- Futures / Margin Loan / Universal Transfer: **OFF**.
- IP access restriction: **Restrict access to trusted IPs only** → enter the
  server's IPv4 from Step 1 → Confirm → Save.

Binance may e-mail a confirmation link; click it or the change won't apply.

---

## STEP 4 — put the keys on the server (never in git)

Keys live in one root-owned file that git has never heard of:

```bash
sudo install -m 600 /dev/null /etc/lottery.env
sudo nano /etc/lottery.env
```

Type exactly this, pasting your own values, then Ctrl+O, Enter, Ctrl+X:

```
BINANCE_LIVE_API_KEY=paste_the_api_key_here
BINANCE_LIVE_API_SECRET=paste_the_secret_here
LOTTERY_LIVE=1
```

Rules that keep this safe:
- `chmod 600`, owner root — the systemd unit reads it, humans don't.
- Never paste the secret into a chat, a commit, an issue, or a screenshot.
- `.gitignore` already excludes `.env`; `/etc/lottery.env` is outside the
  repo entirely, which is stronger.
- If a secret is ever exposed: delete the key in Binance API Management
  first, create a new one second. Rotation beats regret.

---

## STEP 5 — verify before arming

```bash
sudo -u tradebot env $(sudo cat /etc/lottery.env | xargs) \
  python3 /opt/tradebot/cloud-bot/src/verify_binance_key.py
```

Expected: `KEY IS GENUINE`, `canTrade: True`, `canWithdraw: False`, and your
~$11 USDT in the balance list. Anything else — stop and fix it before
continuing. `canWithdraw: True` makes this script exit non-zero on purpose:
turn withdrawals off and re-run.

---

## STEP 6 — go live

The units are already installed by the bootstrap; this just starts them.

```bash
sudo systemctl start lottery.service      # one manual cycle, watch it
sudo systemctl status lottery.service --no-pager
```

Read that output. A first run with no position and a fresh Watcher scan
either buys one coin or explains why it didn't. When it looks right:

```bash
sudo systemctl enable --now lottery.timer
systemctl list-timers lottery.timer --no-pager
```

Cycles now run every 10 minutes, forever, without you.

---

## Watching it

```bash
journalctl -u lottery.service -n 50 --no-pager     # recent cycles
journalctl -u lottery.service -f                   # live tail
tail -5 /opt/tradebot/cloud-bot/data/lottery_ledger.jsonl
```

The ledger also lands in the GitHub repo on every trade, so you can read the
book's whole history from your phone.

---

## Stopping it (three ways, all immediate)

```bash
sudo systemctl stop lottery.timer                  # 1. pause the schedule
```
2. Set `LOTTERY_LIVE=0` in `/etc/lottery.env` — the bot runs and refuses.
3. Create a `KILL_SWITCH` file in the repo's `data/` folder from GitHub's
   web UI — the guard blocks every order on the next pull, no SSH needed.

To end it permanently: delete the API key in Binance API Management. That
revokes the machine's power over the account no matter what the code does.

---

## What lives where (the whole security model in four lines)

| Thing | Lives | Never |
|---|---|---|
| Bot code | git, public repo | — |
| Real API key/secret | `/etc/lottery.env` on the VPS, mode 600 | git, chat, screenshots |
| Watcher scans / paper fleet | GitHub Actions → repo | touches real keys |
| Ledger + book state | VPS → repo (auditable) | contains secrets |
