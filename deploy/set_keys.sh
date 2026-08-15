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
printf 'BINANCE_LIVE_API_KEY=%s\nBINANCE_LIVE_API_SECRET=%s\nLOTTERY_LIVE=1\n' \
  "$KEY" "$SECRET" > "$ENV_FILE"
chmod 600 "$ENV_FILE"
chown root:root "$ENV_FILE"
echo "Saved to $ENV_FILE (readable by root only). LOTTERY_LIVE=1."

echo
echo "== verifying the key against the real Binance API (read-only) =="
sudo -u tradebot env "BINANCE_LIVE_API_KEY=$KEY" "BINANCE_LIVE_API_SECRET=$SECRET" \
  python3 "$DIR/src/verify_binance_key.py"
rc=$?
echo
if [ $rc -eq 0 ]; then
  cat <<'EOF'
All good. Next, run ONE cycle and read what it says:

    systemctl start lottery.service
    systemctl status lottery.service --no-pager

If that looks right, go live every 10 minutes:

    systemctl enable --now lottery.timer
EOF
else
  cat <<'EOF'
Verification did NOT pass — do not arm yet. Most likely causes:
  * this server's IP is not on the key's whitelist (add 168.119.103.198
    under Binance -> API Management -> Edit restrictions), or
  * withdrawals are still enabled (turn them OFF and re-run this), or
  * the key/secret was pasted with a character missing.
Fix, then re-run this same command.
EOF
fi
exit $rc
