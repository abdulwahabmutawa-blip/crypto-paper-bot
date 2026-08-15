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

    print()
    print("KEY IS GENUINE — the real Binance API accepted this signature.")
    print(f"  account permissions : {acct.get('permissions', [])}")
    print(f"  account canTrade    : {acct.get('canTrade')}")

    # THE KEY's permissions, which is what actually matters here.
    # /v3/account's canWithdraw describes the ACCOUNT (is it allowed to
    # withdraw at all), not this API key — checking it flagged a correctly
    # configured key as dangerous. /sapi/v1/account/apiRestrictions is the
    # endpoint that answers "what may this key do".
    r = binance_live._call("GET", "/sapi/v1/account/apiRestrictions",
                           signed=True)
    print()
    if not isinstance(r, dict):
        print("  KEY PERMISSIONS: could not be read "
              f"({binance_live.LAST_ERROR.get('msg', 'no detail')}).")
        print("  Confirm by eye in Binance -> API Management that")
        print("  'Enable Withdrawals' is unticked before arming.")
        return 1

    withdraw = bool(r.get("enableWithdrawals"))
    spot = bool(r.get("enableSpotAndMarginTrading"))
    futures = bool(r.get("enableFutures"))
    transfer = bool(r.get("enableInternalTransfer"))
    ip_locked = bool(r.get("ipRestrict"))
    print("  KEY permissions (this is the one that matters):")
    print(f"    spot trading      : {spot}" + ("" if spot else "   <-- must be ON to trade"))
    print(f"    withdrawals       : {withdraw}"
          + ("   <-- TURN OFF: a bot key must never move coins out"
             if withdraw else "   (correct)"))
    print(f"    internal transfer : {transfer}"
          + ("   <-- turn off: also moves funds" if transfer else "   (correct)"))
    print(f"    futures           : {futures}"
          + ("   <-- turn off: not used here" if futures else "   (correct)"))
    print(f"    IP restricted     : {ip_locked}"
          + ("   (correct)" if ip_locked else "   <-- lock to this server's IP"))

    held = [(b["asset"], float(b["free"])) for b in acct["balances"]
            if float(b.get("free", 0) or 0) > 0]
    usdt = next((f for a, f in held if a == "USDT"), 0.0)
    print()
    print(f"  free USDT (what the bot can spend): {usdt:.2f}")
    if usdt < 5:
        print("    note: under Binance's ~$5 minimum order — the bot will")
        print("    refuse to buy until there is more USDT.")
    print(f"  assets with a free balance: {len(held)}")
    for asset, free in sorted(held, key=lambda x: -x[1])[:8]:
        print(f"    {asset:<8} {free:.8f}".rstrip("0").rstrip("."))

    if withdraw or transfer:
        return 1
    if not spot:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
