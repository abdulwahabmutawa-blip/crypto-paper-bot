"""Prove an API key is a REAL Binance key — run this before arming anything.

Why this exists: keys minted on a look-alike site authenticate against
nothing. This calls the genuine endpoint (api.binance.com, hardcoded) with
a signed, read-only request. Two outcomes, no ambiguity:

  * account data returns  -> the key is real, issued by Binance itself
  * 401 / signature error -> the key is NOT a Binance key. Treat the site
    that issued it as hostile: from a device you trust, go to binance.com
    directly (type the address, no links), change the password, revoke every
    API key, and check withdrawal whitelists and open sessions.

Read-only: calls /v3/account only. Places no orders, moves nothing.
Prints balances rounded — never the key, never the secret.
"""
from __future__ import annotations

import os
import sys

import binance_live

REAL_HOST = "https://api.binance.com/api"


def main() -> int:
    if binance_live.BASE != REAL_HOST:
        print(f"REFUSING: binance_live.BASE is {binance_live.BASE}, "
              f"not {REAL_HOST}")
        return 2
    if not binance_live._keys():
        print("No keys in env. Set BINANCE_LIVE_API_KEY and "
              "BINANCE_LIVE_API_SECRET, then re-run.")
        return 2

    acct = binance_live._call("GET", "/v3/account", signed=True)
    if not acct or "balances" not in acct:
        print()
        print("KEY NOT ACCEPTED by the real Binance API.")
        print("Two possible causes, in order of likelihood:")
        print("  1. This IP is not whitelisted on the key (fix: add it in")
        print("     Binance -> API Management -> Edit restrictions).")
        print("  2. The key did not come from Binance at all. If the site")
        print("     that issued it was not binance.com, assume phishing:")
        print("     from a trusted device type binance.com directly, change")
        print("     the password, revoke all API keys, review sessions and")
        print("     withdrawal whitelists.")
        return 1

    perms = acct.get("permissions", [])
    can_trade = acct.get("canTrade")
    can_withdraw = acct.get("canWithdraw")
    print()
    print("KEY IS GENUINE — the real Binance API accepted this signature.")
    print(f"  permissions : {perms}")
    print(f"  canTrade    : {can_trade}")
    print(f"  canWithdraw : {can_withdraw}"
          + ("   <-- TURN THIS OFF: a trading bot must never hold a "
             "withdrawal-enabled key" if can_withdraw else "   (correct)"))
    held = [(b["asset"], float(b["free"])) for b in acct["balances"]
            if float(b.get("free", 0) or 0) > 0]
    print(f"  assets with a free balance: {len(held)}")
    for asset, free in sorted(held, key=lambda x: -x[1])[:8]:
        print(f"    {asset:<8} {free:.8f}".rstrip("0").rstrip("."))
    if can_withdraw:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
