import datetime
import yfinance as yf
import openpyxl as xl
import xlsxwriter
from PythonPackage.APIcalls import analyst
from PythonPackage.APIcalls import socialImpact
from PythonPackage.APIcalls import insiderTrans
from PythonPackage.APIcalls import techIndicator
from PythonPackage.APIcalls import candles
from PythonPackage.APIcalls import quote


# function returns current price of stock (DELETE)
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


def date():
    today = datetime.datetime.now()
    d = datetime.timedelta(days=30)
    a = today - d
    a = a.strftime('%Y-%m-%d')
    return a


tickerList = ["AAPL", "MSFT", "GOOGL", "ABNB", "AMZN", "SPY"]

workbook = xlsxwriter.Workbook('~$stock.xlsx')
worksheet = workbook.add_worksheet()

# for col_num, data in enumerate(listAnalyst(tickerList):
#    worksheet.write(2, col_num + 1, data)

# for col_num, data in enumerate(listPrice(tickerList)):
#    worksheet.write(1, col_num + 1, data)

# for col_num, data in enumerate(tickerList):
#    worksheet.write(0, col_num + 1, data)

# for col_num, data in enumerate(tickerList):
#    worksheet.write(2, col_num + 1, data)

workbook.close()
