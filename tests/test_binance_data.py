"""binance_data host fallback — offline, no network.

Pins the fix for the 2026-08-15 hype-crypto freeze: api.binance.com answers
HTTP 451 to US IPs, GitHub's runners are US-hosted, so every spot call from
Actions returned None and the bot skipped every cycle in silence for two
days. A geo-block must fall through to the mirror, not be retried.
"""
import sys
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import binance_data as bd  # noqa: E402

# the non-geo-blocked mirror must lead
assert bd.HOSTS[0] == "https://data-api.binance.vision", bd.HOSTS
assert "api.binance.com" in bd.HOSTS[1]

calls = []


def fake_urlopen(req, timeout=20):
    calls.append(req.full_url)
    if "data-api.binance.vision" in req.full_url:
        raise urllib.error.HTTPError(req.full_url, 451, "blocked", None, None)

    class R:
        headers = {}

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    return R()


orig_open, orig_load, orig_throttle = (bd.urllib.request.urlopen,
                                       bd.json.load, bd._throttle)
try:
    bd.urllib.request.urlopen = fake_urlopen
    bd.json.load = lambda r: {"ok": True}
    bd._throttle = lambda w: None

    out = bd._get("/api/v3/ticker/price", {"symbol": "BTCUSDT"})
    assert out == {"ok": True}, out
    assert len(calls) == 2, f"a 451 must not be retried: {calls}"
    assert "data-api.binance.vision" in calls[0]
    assert "api.binance.com" in calls[1]

    # a 418 ban still stops the cycle dead on the first host — retrying or
    # rotating hosts after a ban only lengthens it
    calls.clear()

    def banned(req, timeout=20):
        calls.append(req.full_url)
        raise urllib.error.HTTPError(req.full_url, 418, "banned", None, None)

    bd.urllib.request.urlopen = banned
    assert bd._get("/api/v3/ticker/price") is None
    assert len(calls) == 1, f"418 must not rotate hosts: {calls}"
finally:
    bd.urllib.request.urlopen = orig_open
    bd.json.load = orig_load
    bd._throttle = orig_throttle

print("test_binance_data: ALL PASS")
