"""Public BTC quote recorder. No keys, orders, or strategy promotion.

One immutable observation per invocation. Cost probes are hypothetical
same-snapshot depth sweeps, not trades or realized paper P&L.
"""
import argparse
import json
import math
import time
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

import config

HOST = 'https://data-api.binance.vision'
PROTOCOL = 'btc-execution-observation-v1'
FEE = .001                 # assumed per side, not the user's verified fee tier
SLIPPAGE = .00025          # additional adverse buffer per side
BUDGET = 200.
MAX_LATENCY_MS = 5000
MAX_SPREAD_BPS = 10.


def utc():
    return datetime.now(timezone.utc).isoformat(timespec='milliseconds')


def validate(book):
    sides = {}
    for side in ['bids', 'asks']:
        levels = [(float(p), float(q)) for p, q in book[side]]
        if not levels or any(not math.isfinite(v) or v <= 0 for row in levels for v in row):
            raise ValueError('invalid depth levels')
        prices = [p for p, _ in levels]
        if prices != sorted(prices, reverse=side == 'bids') or len(prices) != len(set(prices)):
            raise ValueError('unsorted or duplicate depth levels')
        sides[side] = levels
    if sides['bids'][0][0] >= sides['asks'][0][0]:
        raise ValueError('crossed or locked book')
    sides['lastUpdateId'] = int(book['lastUpdateId'])
    return sides


def sweep_buy(asks, budget=BUDGET):
    # Reserve fee and adverse slippage inside the stated cash budget.
    remaining = budget / ((1 + FEE) * (1 + SLIPPAGE))
    qty = 0.
    for price, available in asks:
        take = min(available, remaining / price)
        qty += take
        remaining -= take * price
        if remaining <= 1e-8:
            gross = budget / (1 + FEE)
            return {'qty': qty, 'price': gross / qty, 'fee_usdt': budget - gross,
                    'cash_usdt': budget}
    return None


def sweep_sell(bids, qty):
    remaining, gross = qty, 0.
    for price, available in bids:
        take = min(available, remaining)
        gross += take * price
        remaining -= take
        if remaining <= 1e-12:
            gross *= 1 - SLIPPAGE
            return {'price': gross / qty, 'fee_usdt': gross * FEE,
                    'cash_usdt': gross * (1 - FEE)}
    return None


def observe(fetch=None):
    sample = {'id': str(uuid.uuid4()), 'protocol': PROTOCOL, 'symbol': 'BTCUSDT',
              'request_started_at': utc(), 'source': HOST + '/api/v3/depth?symbol=BTCUSDT&limit=20',
              'exchange_quote_time': None, 'quote_time_basis': 'local receipt; endpoint has no exchange timestamp',
              'fee_per_side_assumed': FEE, 'slippage_buffer_per_side': SLIPPAGE,
              'probe_budget_usdt': BUDGET, 'decision': 'NO_TRADE',
              'decision_reason': 'no strategy has qualified for a forward trading trial'}
    started = time.monotonic()
    try:
        if fetch is None:
            req = urllib.request.Request(sample['source'], headers={'User-Agent': 'paper-fleet-execution-watch/1'})
            with urllib.request.urlopen(req, timeout=5) as response:
                raw = json.load(response)
        else:
            raw = fetch()
        sample['received_at'] = utc()
        sample['latency_ms'] = round((time.monotonic() - started) * 1000, 2)
        book = validate(raw)
        sample['book'] = book
        bid, ask = book['bids'][0][0], book['asks'][0][0]
        sample.update(bid=bid, ask=ask, spread_bps=(ask-bid)/((ask+bid)/2)*10000)
        if sample['latency_ms'] > MAX_LATENCY_MS:
            sample['quote_status'] = 'REJECTED_LATENCY'
        elif sample['spread_bps'] > MAX_SPREAD_BPS:
            sample['quote_status'] = 'REJECTED_SPREAD'
        else:
            buy = sweep_buy(book['asks'])
            sell = sweep_sell(book['bids'], buy['qty']) if buy else None
            sample['quote_status'] = 'ACCEPTED' if buy and sell else 'REJECTED_DEPTH'
            if buy and sell:
                sample['cost_probe'] = {'buy': buy, 'sell': sell,
                    'round_trip_cost_usdt': BUDGET - sell['cash_usdt'],
                    'round_trip_cost_bps': (1-sell['cash_usdt']/BUDGET)*10000,
                    'interpretation': 'hypothetical immediate depth sweep; not an order, fill or P&L'}
    except (ValueError, KeyError, TypeError, OSError) as exc:
        sample.update(received_at=utc(), latency_ms=round((time.monotonic()-started)*1000, 2),
                      quote_status='REJECTED_DATA', error=f'{type(exc).__name__}: {exc}')
    return sample


def save(sample, root):
    # Unique files avoid shared-state reconciliation and preserve outage evidence.
    directory = root / 'data' / 'btc_execution' / sample['received_at'][:10]
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / (sample['id'] + '.json')
    with path.open('x', encoding='utf-8') as f:
        json.dump(sample, f, indent=2, allow_nan=False)
    report_dir = root / 'reports'
    report_dir.mkdir(parents=True, exist_ok=True)
    cost = sample.get('cost_probe', {}).get('round_trip_cost_bps')
    cost_text = f'{cost:.2f} basis points' if cost is not None else 'unavailable'
    report = '\n'.join(['# BTC execution observations', '',
        f"Updated: {sample['received_at']}", f"Quote status: {sample['quote_status']}",
        f"Decision: {sample['decision']} — {sample['decision_reason']}", '',
        f"Estimated immediate round-trip cost on $200: {cost_text}.",
        f"Request latency: {sample['latency_ms']:.0f} ms.", '',
        'Fees assume 0.10% per side plus 0.025% adverse slippage per side; spread and displayed depth are measured.',
        'These are hypothetical cost probes, not executed trades or realized profits. No account credentials or order endpoints are used.',
        'Quote time is local receipt time; the depth endpoint supplies no exchange timestamp, so quote age cannot be proven.',
        'The fleet samples roughly every 13 minutes with possible outages; this is not a continuous market-data feed.',
        'Immutable raw observations live in data/btc_execution/. The original scalper ledger is separate.', ''])
    tmp = report_dir / 'btc_execution.md.tmp'
    tmp.write_text(report, encoding='utf-8')
    tmp.replace(report_dir / 'btc_execution.md')
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-root', type=Path, default=config.ROOT)
    args = parser.parse_args()
    sample = observe()
    path = save(sample, args.output_root)
    print(f"[btc-execution] {sample['quote_status']} NO_TRADE {path}")
    return 0 if sample['quote_status'] == 'ACCEPTED' else 1


if __name__ == '__main__':
    raise SystemExit(main())
