#!/usr/bin/env bash
# Put the Binance keys on the box without a text editor, and without the
# secret landing in shell history (it is typed at a prompt, not on the
# command line, and the secret prompt does not echo).
#
#   bash <(curl -fsSL https://raw.githubusercontent.com/abdulwahabmutawa-blip/crypto-paper-bot/main/deploy/set_keys.sh)
#
# Writes /etc/lottery.env mode 600 root-only, then immediately runs the
# read-only key verification so you learn right away whether it works.
set -uo pipefail

ENV_FILE=/etc/lottery.env
DIR=/opt/tradebot/cloud-bot

[ "$(id -u)" -eq 0 ] || { echo "run this as root (you are root if you just ssh'd in)"; exit 1; }

echo
echo "Paste your Binance API KEY and press Enter (this one IS visible):"
read -r KEY
echo
echo "Now paste your Binance API SECRET and PRESS ENTER."
echo "The screen stays blank while you paste — that is deliberate, the"
echo "characters are still going in. It will look frozen until you press"
echo "Enter, so press Enter even if nothing appeared."
read -rs SECRET
echo "  (received ${#SECRET} characters)"

KEY="${KEY//[[:space:]]/}"
SECRET="${SECRET//[[:space:]]/}"
if [ -z "$KEY" ] || [ -z "$SECRET" ]; then
  echo "One of them was empty — nothing written. Re-run when ready."
  exit 1
fi

umask 077
# DISARMED until the verification below passes (audit 08-15: writing
# LOTTERY_LIVE=1 first meant a failed verify left the box armed with a
# possibly-broken key)
printf 'BINANCE_LIVE_API_KEY=%s\nBINANCE_LIVE_API_SECRET=%s\nLOTTERY_LIVE=0\n' \
  "$KEY" "$SECRET" > "$ENV_FILE"
chmod 600 "$ENV_FILE"
chown root:root "$ENV_FILE"
echo "Saved to $ENV_FILE (readable by root only). Not armed yet."

echo
echo "== verifying the key against the real Binance API (read-only) =="
sudo -u tradebot env "BINANCE_LIVE_API_KEY=$KEY" "BINANCE_LIVE_API_SECRET=$SECRET" \
  python3 "$DIR/src/verify_binance_key.py"
rc=$?
echo
if [ $rc -eq 0 ]; then
  # verification passed — NOW arm
  sed -i 's/^LOTTERY_LIVE=0$/LOTTERY_LIVE=1/' "$ENV_FILE"
  echo "ARMED: LOTTERY_LIVE=1 written (verification passed)."
  cat <<'EOF'
All good. Next, run ONE cycle and read what it says:

    systemctl start lottery.service
    systemctl status lottery.service --no-pager

If that looks right, go live every 10 minutes:

    systemctl enable --now lottery.timer
EOF
else
  cat <<EOF
Verification did NOT pass — the box stays DISARMED (LOTTERY_LIVE=0).
The verify output above names the exact cause and fix. This server's IP
(for the whitelist) is: $(curl -fsS4 https://ifconfig.me 2>/dev/null || echo "run: curl ifconfig.me")
Fix, then re-run this same command.
EOF
fi
exit $rc
