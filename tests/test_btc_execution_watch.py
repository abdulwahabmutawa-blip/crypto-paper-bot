import json
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import btc_execution_watch as watch


def book():
    return {'lastUpdateId': 7, 'bids': [['99', '10']], 'asks': [['100', '10']]}


def test_sweeps_charge_both_fees_and_preserve_budget():
    b = watch.sweep_buy([(100., 10.)])
    assert b['cash_usdt'] == 200
    assert b['qty'] * b['price'] + b['fee_usdt'] == pytest.approx(200)
    s = watch.sweep_sell([(100., 10.)], b['qty'])
    expected = 200 / ((1+watch.FEE)*(1+watch.SLIPPAGE))*(1-watch.SLIPPAGE)*(1-watch.FEE)
    assert s['cash_usdt'] == pytest.approx(expected)
    assert s['cash_usdt'] < 200


def test_insufficient_depth_does_not_invent_fill():
    assert watch.sweep_buy([(100., .1)]) is None
    assert watch.sweep_sell([(100., .1)], 1.) is None


@pytest.mark.parametrize('bad', [float('nan'),float('inf'),-1,0])
def test_invalid_quotes_rejected(bad):
    b=book(); b['asks'][0][0]=bad
    assert watch.observe(lambda:b)['quote_status']=='REJECTED_DATA'


def test_wide_spread_has_no_probe():
    result=watch.observe(book)
    assert result['quote_status']=='REJECTED_SPREAD'
    assert 'cost_probe' not in result


def test_good_quote_is_still_no_trade_and_records_receipt():
    b=book();b['bids']=[['99.99','10']]
    result=watch.observe(lambda:b)
    assert result['quote_status']=='ACCEPTED'
    assert result['decision']=='NO_TRADE'
    assert result['exchange_quote_time'] is None
    assert result['cost_probe']['round_trip_cost_usdt']>0


def test_slow_response_has_no_probe(monkeypatch):
    ticks=iter([0,6])
    monkeypatch.setattr(watch.time,'monotonic',lambda:next(ticks))
    assert watch.observe(book)['quote_status']=='REJECTED_LATENCY'


def test_outage_is_saved_without_overwriting_observation(tmp_path):
    def fail():raise OSError('offline')
    sample=watch.observe(fail)
    path=watch.save(sample,tmp_path)
    assert json.loads(path.read_text())['quote_status']=='REJECTED_DATA'
    with pytest.raises(FileExistsError):watch.save(sample,tmp_path)
