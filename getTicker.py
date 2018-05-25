import requests
import json
import datetime as dt
from datetime import timedelta as td
import numpy as np

###################################################################################
## get_ticker_xx:xx時間足の価格データ取得 5m/1h/2h
##  input:  -
##  output: -
###################################################################################
def get_ticker_5m():
    span=-30

    # 現在時刻から指定した時間間隔の時刻を取得
    endDate = dt.datetime.now()
    startDate = endDate + td(hours=span)

    # 時刻データのフォーマット変換
    startTimestamp = startDate.timestamp()
    endTimestamp = endDate.timestamp()

    # 価格データのAPIリクエスト@cryptowatch
    # 2時間足を取得
    query = {"periods": "300", "after": str(int(startTimestamp)), "before": str(int(endTimestamp))}
    res = json.loads(requests.get("https://api.cryptowat.ch/markets/bitmex/btcusd-perpetual-futures/ohlc", params=query).text)["result"]["300"]
    res = np.array(res)

    #ta-libに渡す形式
    close_price_5m = res[:, 4]
    return close_price_5m

def get_ticker_1h():
    span=-360

    # 現在時刻から指定した時間間隔の時刻を取得
    endDate = dt.datetime.now()
    startDate = endDate + td(hours=span)

    # 時刻データのフォーマット変換
    startTimestamp = startDate.timestamp()
    endTimestamp = endDate.timestamp()

    # 価格データのAPIリクエスト@cryptowatch
    # 1時間足を取得
    query = {"periods": "3600", "after": str(int(startTimestamp)), "before": str(int(endTimestamp))}
    res = json.loads(requests.get("https://api.cryptowat.ch/markets/bitmex/btcusd-perpetual-futures/ohlc", params=query).text)["result"]["3600"]
    res = np.array(res)

    #ta-libに渡す形式
    close_price_1h = res[:, 4]
    return  close_price_1h

def get_ticker_2h():
    span=-720
    # 現在時刻から指定した時間間隔の時刻を取得
    endDate = dt.datetime.now()
    startDate = endDate + td(hours=span)
    # 時刻データのフォーマット変換
    startTimestamp = startDate.timestamp()
    endTimestamp = endDate.timestamp()

    # 価格データのAPIリクエスト@cryptowatch
    # 2時間足を取得
    query = {"periods": "7200", "after": str(int(startTimestamp)), "before": str(int(endTimestamp))}
    res = json.loads(requests.get("https://api.cryptowat.ch/markets/bitmex/btcusd-perpetual-futures/ohlc", params=query).text)["result"]["7200"]
    res = np.array(res)

    #ta-libに渡す形式
    close_price_2h = res[:, 4]

    return  close_price_2h

close_price_5m = get_ticker_5m()
print(close_price_5m[-1])

close_price_1h = get_ticker_1h()
print(close_price_1h[-1])

close_price_2h = get_ticker_2h()
print(close_price_2h[-1])


