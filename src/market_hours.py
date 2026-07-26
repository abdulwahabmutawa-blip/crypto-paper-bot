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


def trim_incomplete_bars(close):
    """Drop trailing rows the feed has not actually delivered yet.

    Companion to the fill gate, but for MARKS and SIGNALS (found 2026-07-26).
    Yahoo sometimes returns a row for a weekday whose equity columns are all
    NaN — the date exists but the data has not landed. Every bot then calls
    .ffill(), which fabricates that bar out of the PRIOR day's close. A mark
    computed off it is a full session stale while looking current; this is
    what marked hunter's USO at Thursday's 139.49 on a Friday bar and
    overstated the fleet by $21.55.

    Kept deliberately: crypto-only weekend rows. When the equity market is
    shut, an equity's last close IS its correct mark, so forward-filling it
    beside a live crypto bar is honest. Only a weekday with no equity data
    means "not in yet".

    Must be called BEFORE .ffill() — afterwards nothing is NaN to detect.

    This fully handles the pure-equity bots. A MIXED frame (equities beside
    crypto) needs last_real_date() too: there the undelivered weekday bar sits
    BEHIND legitimate weekend crypto rows, so trimming the tail never reaches
    it and ffill still drags the old equity close forward.

    Not holiday-aware (same tradeoff as the rest of this module): a holiday
    looks like a weekday with no data, so we drop the bar and skip the mark —
    the safe direction, since nothing traded that day anyway.
    """
    equities = [c for c in close.columns if not str(c).endswith("-USD")]
    if not equities:
        return close                      # crypto-only bot; nothing to check
    while len(close):
        last = close.index[-1]
        if last.weekday() < 5 and close.loc[last, equities].isna().all():
            close = close.iloc[:-1]
        else:
            break
    return close


def last_real_date(close, ticker):
    """Date of the newest bar where `ticker` has genuine data — call on the
    PRE-ffill frame.

    This is the date a mark priced off that ticker honestly belongs to, and it
    is not always the newest row in the frame: a portfolio holding crypto has
    weekend rows its equity benchmark cannot have, and an equity whose bar has
    not landed is older still. Returns None if the ticker has no data at all.
    """
    if ticker not in close.columns:
        return None
    real = close[ticker].dropna()
    return str(real.index[-1].date()) if len(real) else None
