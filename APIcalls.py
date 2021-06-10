# API KEY: c2nffdaad3i8g7sr4n3g
import requests
import json


def socialImpact(ticker):
    r = requests.get('https://finnhub.io/api/v1/stock/social-sentiment?symbol=' + ticker
                     + '&token=c2nffdaad3i8g7sr4n3g')
    print(r.json())


def insiderTrans(ticker):
    r = requests.get('https://finnhub.io/api/v1/stock/insider-transactions?symbol=' +
                     ticker + '&token=c2nffdaad3i8g7sr4n3g')
    print(r.json())


def techIndicator(ticker):
    r = requests.get('https://finnhub.io/api/v1/indicator?symbol=' + ticker + '&resolution=D&from=1583098857&'
                                                                              'to=1584308457&indicator=sma&timeperiod=3&token=c2nffdaad3i8g7sr4n3g')
    print(r.json())


def candles(ticker):
    r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=' + ticker +
                     '&resolution=1&from=1615298999&to=1615302599&token=c2nffdaad3i8g7sr4n3g')
    print(r.json())


def quote(ticker):
    r = requests.get('https://finnhub.io/api/v1/quote?symbol=' + ticker + '&token=c2nffdaad3i8g7sr4n3g')
    print(r.json())


def analyst(ticker):
    data = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol='
                 + ticker + '&token=c2nffdaad3i8g7sr4n3g')
    return data

#socialImpact('AAPL')
#insiderTrans('AAPL')
#techIndicator('AAPL')
#candles('AAPL')
#quote('AAPL')
