#!/usr/bin/env bash
# One-paste VPS setup for the lottery book. Run as root on a fresh
# Ubuntu 24.04 box:
#
#   bash <(curl -fsSL https://raw.githubusercontent.com/abdulwahabmutawa-blip/crypto-paper-bot/main/deploy/bootstrap.sh)
#
# Safe to re-run: every step checks before acting. Re-run it after adding
# the deploy key to GitHub and it upgrades the remote to SSH so the ledger
# can publish.
#
# What it does NOT do, on purpose: write your API keys (you do that in
# /etc/lottery.env), and enable the timer (you enable it after the key
# verification passes). Arming stays a human act.
set -uo pipefail

REPO_HTTPS="https://github.com/abdulwahabmutawa-blip/crypto-paper-bot.git"
REPO_SSH="git@github.com:abdulwahabmutawa-blip/crypto-paper-bot.git"
DIR=/opt/tradebot/cloud-bot
USER_NAME=tradebot

[ "$(id -u)" -eq 0 ] || { echo "run as root"; exit 1; }
say() { printf '\n\033[1;36m== %s\033[0m\n' "$1"; }

say "packages"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get -y -qq upgrade
apt-get -y -qq install python3-pip python3-venv git ufw unattended-upgrades curl

say "user + firewall + ssh hardening"
id "$USER_NAME" &>/dev/null || adduser --disabled-password --gecos "" "$USER_NAME"
install -d -o "$USER_NAME" -g "$USER_NAME" /opt/tradebot
ufw allow OpenSSH >/dev/null 2>&1
ufw --force enable >/dev/null 2>&1
systemctl enable --now unattended-upgrades >/dev/null 2>&1
sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin prohibit-password/; s/^#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart ssh

say "deploy key"
KEYFILE=/home/$USER_NAME/.ssh/id_ed25519
if [ ! -f "$KEYFILE" ]; then
  sudo -u "$USER_NAME" install -d -m 700 "/home/$USER_NAME/.ssh"
  sudo -u "$USER_NAME" ssh-keygen -t ed25519 -N "" -q -f "$KEYFILE"
fi

say "repo"
if [ ! -d "$DIR/.git" ]; then
  # public repo: HTTPS clone needs no key, so the bot can run today and the
  # deploy key becomes an optional upgrade for publishing its ledger
  sudo -u "$USER_NAME" git clone -q "$REPO_HTTPS" "$DIR"
else
  sudo -u "$USER_NAME" git -C "$DIR" pull --rebase --autostash -q || true
fi
sudo -u "$USER_NAME" git -C "$DIR" config user.name "lottery-bot"
sudo -u "$USER_NAME" git -C "$DIR" config user.email "bot@users.noreply.github.com"
chmod +x "$DIR/deploy/lottery_runner.sh"

# If the deploy key is already registered on GitHub, publish over SSH.
# Capture first, grep second: `ssh -T git@github.com` ALWAYS exits 1 (GitHub
# grants no shell), and under `set -o pipefail` that non-zero status wins the
# pipeline even when grep matches — which silently kept this on HTTPS.
GH_PROBE=$(sudo -u "$USER_NAME" ssh -o StrictHostKeyChecking=accept-new \
             -o BatchMode=yes -T git@github.com 2>&1 || true)
if printf '%s' "$GH_PROBE" | grep -q "successfully authenticated"; then
  sudo -u "$USER_NAME" git -C "$DIR" remote set-url origin "$REPO_SSH"
  PUBLISH="yes — deploy key active, the ledger will push to GitHub"
else
  PUBLISH="not yet — add the deploy key below, then re-run this script"
fi

say "python deps"
pip3 install -q --break-system-packages -r "$DIR/requirements.txt"

say "systemd units"
cp "$DIR/deploy/lottery.service" "$DIR/deploy/lottery.timer" /etc/systemd/system/
systemctl daemon-reload
[ -f /etc/lottery.env ] || {
  install -m 600 /dev/null /etc/lottery.env
  cat > /etc/lottery.env <<'EOF'
BINANCE_LIVE_API_KEY=
BINANCE_LIVE_API_SECRET=
LOTTERY_LIVE=0
EOF
}

IP=$(curl -fsS4 https://ifconfig.me 2>/dev/null || echo "unknown")
cat <<EOF

========================================================================
 READY. Nothing is armed yet — no order can be placed.

 THIS SERVER'S IP (whitelist this on the Binance API key):
     $IP

 Ledger publishing: $PUBLISH

 Deploy key (GitHub -> repo -> Settings -> Deploy keys -> Add,
 tick "Allow write access"):
$(cat "$KEYFILE.pub")

 REMAINING STEPS
   1. Binance -> API Management -> your key:
        Reading ON, Spot & Margin Trading ON,
        Withdrawals OFF, Futures OFF,
        Restrict access to trusted IPs -> $IP -> Confirm.
   2. nano /etc/lottery.env
        paste the key and secret, set LOTTERY_LIVE=1
   3. Verify (read-only, places nothing):
        sudo -u $USER_NAME env \$(cat /etc/lottery.env | xargs) \\
          python3 $DIR/src/verify_binance_key.py
      Expect: KEY IS GENUINE / canTrade True / canWithdraw False
   4. One manual cycle, then read it:
        systemctl start lottery.service
        systemctl status lottery.service --no-pager
   5. Go live every 10 minutes:
        systemctl enable --now lottery.timer

 STOP ANYTIME
   systemctl stop lottery.timer        (pause)
   LOTTERY_LIVE=0 in /etc/lottery.env  (refuse)
   KILL_SWITCH file in the repo data/  (block, no SSH needed)
========================================================================
EOF
