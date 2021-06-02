# API KEY: c2nffdaad3i8g7sr4n3g
import requests
import json
import pandas as pd
import numpy as np


r = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol=AAPL&token=c2nffdaad3i8g7sr4n3g')
print(r.json())


def getAnalyst(ticker):
    data = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol='
                        + ticker + '&token=c2nffdaad3i8g7sr4n3g')
    return data


print(getAnalyst('AMZN').json())