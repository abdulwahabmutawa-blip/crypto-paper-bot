"""universe_rule_v1 — the frozen slate rule.

The slate is decided BEFORE any probability exists, by a rule that cannot
see outcomes. This is the load-bearing anti-fooling control: choosing the
denominator after seeing the data is the easiest way to manufacture an
apparent edge, and forced coverage over a pre-frozen slate makes it
impossible rather than merely discouraged.
"""
from __future__ import annotations

import oracle.config as config


def _median(xs: list[float]) -> float:
    xs = sorted(xs)
    if not xs:
        return 0.0
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2.0


def eligible_symbol(symbol: str, status: str) -> bool:
    """Name/status half of the rule — no market data needed."""
    if status != "TRADING":
        return False
    if not symbol.endswith("USDT"):
        return False
    if symbol.endswith(config.LEVERAGED_SUFFIXES):
        return False
    return symbol[:-4] not in config.STABLES


def eligible_history(daily_rows: list[list]) -> tuple[bool, str]:
    """History half of the rule. Returns (ok, reason_if_not).

    daily_rows are raw Binance 1d klines, oldest first, ending at the last
    CLOSED day before T0.
    """
    if len(daily_rows) < config.MIN_LISTED_DAYS:
        return False, f"listed<{config.MIN_LISTED_DAYS}d ({len(daily_rows)})"
    qv = [float(r[7]) for r in daily_rows[-30:]]
    med = _median(qv)
    if med < config.MIN_MEDIAN_QV_30D:
        return False, f"median qv ${med:,.0f} below floor"
    if med > config.MAX_MEDIAN_QV_30D:
        return False, f"median qv ${med:,.0f} above ceiling"
    return True, ""


def candidate_symbols(info: dict) -> list[str]:
    """Every symbol passing the name/status half, sorted for determinism."""
    out = []
    for s in (info.get("symbols") or []):
        sym = s.get("symbol", "")
        if not eligible_symbol(sym, s.get("status", "")):
            continue
        if s.get("quoteAsset") != "USDT":
            continue
        if "SPOT" not in (s.get("permissions") or ["SPOT"]):
            # some responses carry permissionSets instead; default to SPOT
            sets = s.get("permissionSets") or []
            if sets and not any("SPOT" in ps for ps in sets):
                continue
        out.append(sym)
    return sorted(set(out))
