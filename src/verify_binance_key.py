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
        err = binance_live.LAST_ERROR
        code = err.get("code")
        print()
        print("KEY NOT ACCEPTED by the real Binance API.")
        print(f"Binance said: code {code} — {err.get('msg', '(no message)')}")
        print()
        if code == -1022:
            print("DIAGNOSIS: the API key was recognised, but the SECRET does")
            print("not match it. The key itself is genuine and registered.")
            print()
            print("Binance shows a key's Secret ONLY ONCE, on the screen where")
            print("you create it — revisiting API Management never shows it")
            print("again. If that screen is gone, the secret cannot be")
            print("recovered.")
            print()
            print("FIX: create a NEW API key, and copy the Secret immediately")
            print("while it is on screen. Then re-run this setup. Delete the")
            print("old key afterwards so nothing unused stays enabled.")
        elif code in (-2015, -2014):
            print("DIAGNOSIS: the key/IP/permission combination was rejected.")
            print("  * add this server's IP to the key's trusted-IP list, and")
            print("  * make sure 'Enable Spot & Margin Trading' is ticked.")
            print("  * a brand-new whitelist entry can take a minute to apply.")
        elif code == -1021:
            print("DIAGNOSIS: this server's clock drifted outside Binance's")
            print("accepted window. Fix: timedatectl set-ntp true")
        elif code == -2008:
            print("DIAGNOSIS: Binance does not recognise this API key at all.")
            print("If the site that issued it was not binance.com, treat it as")
            print("phishing: from a trusted device type binance.com directly,")
            print("change the password, revoke all keys, review sessions and")
            print("withdrawal whitelists.")
        else:
            print("Check the key's permissions, the IP whitelist, and that the")
            print("secret was pasted whole.")
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
