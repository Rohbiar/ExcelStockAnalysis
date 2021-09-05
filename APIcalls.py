# API KEY: c2nffdaad3i8g7sr4n3g
import requests
import json

token = 'c2nffdaad3i8g7sr4n3g'


def getName(ticker):
    r = requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=' + ticker + '&token=c2nffdaad3i8g7sr4n3g')
    return r.json()


def getTicker(name):
    r = requests.get('https://finnhub.io/api/v1/search?q=' + name + '&token=c2nffdaad3i8g7sr4n3g')

    return r.json()


def socialImpact(ticker):
    r = requests.get('https://finnhub.io/api/v1/stock/social-sentiment?symbol=' + ticker
                     + '&token=c2nffdaad3i8g7sr4n3g')
    return (r.json())


def insiderTrans(ticker):
    r = requests.get('https://finnhub.io/api/v1/stock/insider-transactions?symbol=' +
                     ticker + '&token=c2nffdaad3i8g7sr4n3g')
    return (r.json())


def techIndicator(ticker):
    r = requests.get('https://finnhub.io/api/v1/indicator?symbol=' + ticker + '&resolution=D&from=1583098857&'
                                                                              'to=1584308457&indicator=sma&timeperiod=3&token=c2nffdaad3i8g7sr4n3g')
    return (r.json())


def candles(ticker):
    r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=' + ticker +
                     '&resolution=1&from=1615298999&to=1615302599&token=c2nffdaad3i8g7sr4n3g')
    return (r.json())


def quote(ticker):
    r = requests.get('https://finnhub.io/api/v1/quote?symbol=' + ticker + '&token=c2nffdaad3i8g7sr4n3g')

    return r.json()


def analyst(ticker):
    data = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol='
                        + ticker + '&token=c2nffdaad3i8g7sr4n3g')
    return data.json()


def aggregateIndicator(ticker):
    r = requests.get(
        'https://finnhub.io/api/v1/scan/technical-indicator?symbol=' + ticker + '&resolution=D&token=c2nffdaad3i8g7sr4n3g')
    return r.json()


def quoteUpdate(ticker):
    value_dict = quote(ticker)
    return ((value_dict['c'] - value_dict['o']) / value_dict['o'])

print(techIndicator('DAL'))


# (close - open) / open
# value_dict = quote('AAPL')
# print((value_dict['c'] - value_dict['o']) / value_dict['o'])
