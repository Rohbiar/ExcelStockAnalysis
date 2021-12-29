import datetime
import time
import pandas as pd
from APIcalls import analyst
from APIcalls import quote
from APIcalls import aggregateIndicator

t = 61

def countdown(t):
    print('Starting Cooldown.')
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Cooldown Complete.')

# Datetime to show the update timing
def date():
    today = datetime.datetime.now()
    d = datetime.timedelta(days=0)
    a = today - d
    a = a.strftime('%m/%d/%Y')
    return a


def readWbNames():
    df = pd.read_excel('~$stock.xlsx', sheet_name=0)
    columns = 1
    rows = len(df)
    nameList = []

    for column in range(columns):
        for row in range(rows):
            nameList.append(df.loc[row][column])

    return nameList


def readWbTicker():
    df = pd.read_excel('~$stock.xlsx', sheet_name=0)
    columns = 1
    rows = len(df)
    tickerList = []

    for column in range(columns):
        column = 1
        for row in range(rows):
            tickerList.append(df.loc[row][column])
    return tickerList


def dateList(tickerList):
    dateList = []
    for x in range(len(tickerList)):
        dateList.append(date())
    return dateList


def quoteList(tickerList):
    quoteList = []
    storage = {}
    for row in range(len(tickerList)):
        storage = quote(tickerList[row])
        quoteList.append(storage['c'])

    countdown(t)
    return quoteList


def analystList(tickerList):
    analystList = []
    for rec in range(len(tickerList)):
        rec_dict = analyst(tickerList[rec])
        if (len(rec_dict) == 0):
            analystList.append('Data Unavailable')
            continue
        print(rec_dict)
        strongbuy = rec_dict[0].get('strongBuy', 0)
        buy = rec_dict[0].get('buy', 0)
        hold = rec_dict[0].get('hold', 0)
        sell = rec_dict[0].get('sell', 0)
        strongsell = rec_dict[0].get('strongSell', 0)
        total = strongbuy + buy + hold + sell + strongsell
        tr = strongbuy * 1 + buy * 2 + hold * 3 + sell * 4 + strongsell * 5
        rating = tr / total
        analystList.append(round(rating, 2))
    return analystList


def aggList(tickerList):
    aggList = []
    storage_dict = {}
    for x in range(len(tickerList)):
        storage_dict = aggregateIndicator(tickerList[x])
        aggList.append(storage_dict['technicalAnalysis']['buy'])
    return aggList


nameList = readWbNames()
tickerList = readWbTicker()
dates = dateList(tickerList)
quoteList = quoteList(tickerList)
recList = analystList(tickerList)
#aggregateList = aggList(tickerList)


def writepanda(tickerList, dates, quoteList, recList):
    data = {
        'Ticker': tickerList,
        'Date': dates,
        'Price': quoteList,
        'Analyst': recList
    }

    row_labels = nameList
    import pdb; pdb.set_trace()
    df = pd.DataFrame(data=data, index=row_labels)

    writer = pd.ExcelWriter('~$stock.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()


writepanda(tickerList, dates, quoteList, recList)