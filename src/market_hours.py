"""US equity market-hours gate.

Fills must use prices that can actually be traded. Yahoo's last daily bar is
near-live during regular trading hours but silently serves the PRIOR close on
nights/weekends/premarket — which let bots buy news-driven surges at
pre-surge prices (found 2026-07-22: hype bot filled SMCI at the prior close
during a premarket rip). Every bot now defers stock fills to regular hours;
crypto (-USD) trades 24/7 and is exempt.

Not holiday-aware by design: on a market holiday the last close IS the
freshest price and nothing moves, so a stale-close fill is harmless.
"""
from datetime import datetime, timedelta, timezone


def _et_now(now=None):
    now = now or datetime.now(timezone.utc)
    try:
        from zoneinfo import ZoneInfo
        return now.astimezone(ZoneInfo("America/New_York"))
    except Exception:  # tzdata unavailable — approximate with EDT
        return now.astimezone(timezone(timedelta(hours=-4)))


def us_equities_open(now=None) -> bool:
    """True during regular US session: Mon-Fri 9:30-16:00 America/New_York."""
    et = _et_now(now)
    if et.weekday() >= 5:
        return False
    minutes = et.hour * 60 + et.minute
    return 9 * 60 + 30 <= minutes < 16 * 60


def can_fill(ticker: str, now=None) -> bool:
    """Crypto fills any time; equities only while the market is open."""
    return ticker.endswith("-USD") or us_equities_open(now)
