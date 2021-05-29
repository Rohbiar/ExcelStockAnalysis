#API KEY: c2nffdaad3i8g7sr4n3g
import requests
import json



r = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol=AAPL&token=c2nffdaad3i8g7sr4n3g')
print(r.json())

