from tkinter import *
import tkinter as tk
import datetime
import self as self
import tk
import yfinance as yf
import openpyxl as xl
import xlsxwriter
from PythonPackage.AnalystRec import getAnalyst


# function returns current price of stock
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

#date & time for parsing
today = datetime.datetime.now()
d = datetime.timedelta(days = 30)
a = today - d
#print(today.strftime('%Y-%m-%d'))
print(a)


# testing with yfinance package
msft = yf.Ticker("MSFT")
# str = msft.info
# hist = msft.history(period="max")
rec = msft.recommendations
reccc = str(rec)
b = str(a)
date = b[:10]
print(date)
#reccc.index(b)
print(reccc)
#print(rec)
#test example
recList = []
tickerList = ["AAPL", "MSFT", "GOOGL", "ABNB", "AMZN", "SPY"]



def listPrice(tickerList):
    priceList = []
    for x in tickerList:
        priceList.append(("${:,.2f}".format(get_current_price(x))))
    return priceList

print(listPrice(tickerList))


def listAnalyst(tickerList):
    analystList = []
    for x in tickerList:
        analystList.append(getAnalyst(tickerList[x]))
    return analystList


a = listAnalyst(tickerList)

# function to get reccomendations
# Excel management
# def process_workbook():
# sPrice = mysheet.cell(row=4, column=5)
# wb = xl.load_workbook(filename='stock.xlsx')
# sheet = wb['Sheet1']
# cell = sheet['a1']
# return cell.value()

workbook = xlsxwriter.Workbook('~$stock.xlsx')
worksheet = workbook.add_worksheet()

#for col_num, data in enumerate(listAnalyst(tickerList):
    #worksheet.write(2, col_num + 1, data)

for col_num, data in enumerate(listPrice(tickerList)):
    worksheet.write(1, col_num + 1, data)

for col_num, data in enumerate(tickerList):
    worksheet.write(0, col_num + 1, data)

# for col_num, data in enumerate(tickerList):
# worksheet.write(2, col_num + 1, data)

workbook.close()
# for x in tickerList:


