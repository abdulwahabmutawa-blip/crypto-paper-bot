#!/usr/bin/env bash
# Health check for the lottery box: latest code, key validity, permissions,
# armed state, book value, recent decisions.
#
#   bash /opt/tradebot/cloud-bot/deploy/check.sh
#
# Reads /etc/lottery.env itself and hands the values to python via
# --preserve-env, so no secret ever appears on a command line, in shell
# history, or in `ps` output.
set -uo pipefail

DIR=/opt/tradebot/cloud-bot
[ "$(id -u)" -eq 0 ] || { echo "run as root"; exit 1; }

set -a
# shellcheck disable=SC1091
. /etc/lottery.env
set +a
# same git identity the service uses (key lives under /opt, not /home)
export GIT_SSH_COMMAND="ssh -i /opt/tradebot/.ssh/id_ed25519 -o UserKnownHostsFile=/opt/tradebot/.ssh/known_hosts -o StrictHostKeyChecking=accept-new"

echo "== updating code"
sudo -u tradebot git -C "$DIR" pull -q --rebase --autostash 2>/dev/null || \
  echo "   (pull failed — continuing on the code already here)"
echo "   $(sudo -u tradebot git -C "$DIR" log --oneline -1)"

echo
echo "== arming"
echo "   LOTTERY_LIVE=${LOTTERY_LIVE:-unset}   (1 = the bot may place orders)"
echo "   LOTTERY_EXCHANGE_STOPS=${LOTTERY_EXCHANGE_STOPS:-unset}   (1 = rest the"
echo "     protective floor AT the exchange; unset/0 = poll-only, the old path)"
if systemctl is-enabled lottery.timer >/dev/null 2>&1; then
  echo "   timer: ENABLED — cycles run every 10 minutes"
else
  echo "   timer: not enabled — the bot only runs when you start it by hand"
fi

echo
echo "== key check (read-only)"
cd "$DIR" || exit 1
sudo -u tradebot --preserve-env=BINANCE_LIVE_API_KEY,BINANCE_LIVE_API_SECRET \
  python3 src/verify_binance_key.py
rc=$?

echo
echo "== book state"
if [ -f "$DIR/data/lottery_state.json" ]; then
  python3 - "$DIR/data/lottery_state.json" <<'PY'
import json, sys
st = json.load(open(sys.argv[1]))
print(f"   seat        : {st.get('held_symbol') or 'CASH'}")
print(f"   units held  : {st.get('units', 0)}")
print(f"   entry price : {st.get('entry_price')}")
print(f"   last value  : ${st.get('last_value_usd', 0):.2f}")
print(f"   closed trades: {len(st.get('realized', []))}")
for r in st.get("realized", [])[-3:]:
    print(f"     {r.get('date')} {r.get('symbol')} "
          f"{r.get('pnl_pct')}% — {r.get('reason','')[:50]}")
PY
else
  echo "   no state file yet — the bot has not completed a cycle"
fi

echo
echo "== last 5 ledger entries"
if [ -f "$DIR/data/lottery_ledger.jsonl" ]; then
  tail -5 "$DIR/data/lottery_ledger.jsonl"
else
  echo "   ledger empty — nothing has been attempted yet"
fi

exit $rc
