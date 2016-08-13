# -*- coding: utf-8 -*-
import urllib2
import json
import requests
import numpy
import datetime
import matplotlib
import matplotlib.pyplot as plt
import re
from ast import literal_eval
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
# print re.sub('[-]','',time.strftime('%Y-%m-%d'))
ma = []
c = 0
total = 0
count = 0
print type(count)
for i in range(0,30):
    # print count
    day_temp = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(i),'%Y-%m-%d')
    day = re.sub('-','',day_temp);
    url = url_front + stock + '.tw&d='+day+'&json=1&delay=0'
    # print url
    req = requests.session()
    req.get('http://mis.twse.com.tw/stock/index.jsp',
                headers = {'Accept-Language':'zh-TW'}
    )
    response = req.get(url)
    content = json.loads(response.content)
    datajson = content["msgArray"]
    # print data
    if not datajson:
        # print 'here'
        continue
    else:
        count = count+1
    datastr = json.dumps(datajson,indent=None)
    data = literal_eval(datastr)
    z = data[0]['z']
    total += float(z)
    if(count == 5):
        ma.append(total/5.0)
    elif(count == 10):
        ma.append(total/10.0)
    elif(count == 20):
        ma.append(total/20.0)
        break
    # print type(data)
    # print json.dumps(data,indent = 4)
print ma
# try: urldata = urllib2.urlopen(url)
# except URLError as e:
#     print(e.reason)
# data = urldata.read()
# try: js = json.loads(str(data))
# except: js = None
# if 'status' not in js or js['status'] != 'OK':
# print '==== Failure To Retrieve ===='
# print dir(datetime)
# candlesticks = (datetime.datetime(2016,7,16),data[0]['o'],data[0]['c'],data[0]['h'],data[0]['l'],data[0]['v'])
# figure = plt.figure()
# ax = figure.add_subplot(1,1,1)
# ax.set_ylabel('Quote ($)', size=20)
# candlestick_ohlc(ax, candlesticks,width=1,colorup='g', colordown='r')
# plt.show()
