# -*- coding: utf-8 -*-

from . import API

api = API('demo')


def test_call():
    data, _ = api("TIME_SERIES_INTRADAY", symbol="IBM",
                  interval='5min', month='2009-01', outputsize="full")
    assert data['Time Series (5min)']['2009-01-20 08:05:00']['5. volume'] == '993'


def test_intraday():
    data, _ = api.time_series_intraday("IBM", interval='5min', month='2009-01')
    assert data.iloc[-1]['open'] == 49.575


def test_weekly():
    data, _ = api.time_series_weekly("TSCO.LON")
    assert data.iloc[-1]['open'] == 319.7501


def test_other():
    # pure testing, no comparison
    _ = api.quote_endpoint('IBM')
    _ = api.ticker_search('tencent')
    _ = api.global_market_status()
