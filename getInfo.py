# -*- coding: utf-8 -*-
import urllib2
import json
import requests
import numpy
import datetime
import matplotlib
import matplotlib.pyplot as plt
# from matplotlib.finance import num2date
from matplotlib.finance import candlestick_ohlc
from matplotlib.finance import date2num
from urllib2 import URLError

url_front = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_'

while True:
    stock = raw_input('enter stock index: ')
    if len(stock) != 4:
        continue
    else:
        break
url = url_front + stock + '.tw&d=20160811&json=1&delay=0'
print url
# try: urldata = urllib2.urlopen(url)
# except URLError as e:
#     print(e.reason)
# data = urldata.read()
# try: js = json.loads(str(data))
# except: js = None
# if 'status' not in js or js['status'] != 'OK':
# print '==== Failure To Retrieve ===='
req = requests.session()
req.get('http://mis.twse.com.tw/stock/index.jsp',
            headers = {'Accept-Language':'zh-TW'}
)
response = req.get(url)
content = json.loads(response.content)
data = content["msgArray"]
print type(data)
print json.dumps(data,indent = 4)
print dir(datetime)
# candlesticks = (datetime.datetime(2016,7,16),data[0]['o'],data[0]['c'],data[0]['h'],data[0]['l'],data[0]['v'])
# figure = plt.figure()
# ax = figure.add_subplot(1,1,1)
# ax.set_ylabel('Quote ($)', size=20)
# candlestick_ohlc(ax, candlesticks,width=1,colorup='g', colordown='r')
# plt.show()
