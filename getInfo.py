# -*- coding: utf-8 -*-
import urllib2
import json
import requests
import numpy
import datetime
import matplotlib
import matplotlib.pyplot as plt
import re
from yahoo_finance import Share
from ast import literal_eval
from tseId import tseId
# from matplotlib.finance import num2date
from matplotlib.finance import candlestick_ohlc
from matplotlib.finance import date2num
from urllib2 import URLError

url_front = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch='

# while True:
#     stock = raw_input('enter stock index: ')
#     if len(stock) != 4:
#         continue
#     else:
#         break
tseIds = tseId()
tseIdlist = tseIds.getAlltseId()
# print tseIdlist
# print re.sub('[-]','',time.strftime('%Y-%m-%d'))
ma = []
c = 0
total = 0
count = 0
ma_five = []
url_content = ''
tseidcount = 0
for id in tseIdlist[:50]:
    tseidcount = tseidcount+1
    if tseidcount == len(tseIdlist):
        url_content = url_content+'tse_'+id+'.tw'
    else:
        url_content = url_content+'tse_'+id+'.tw|'
for stockid in tseIdlist:
    malist1 = []
    malist2 = []
    malist3 = []
    malist4 = []
    malist5 = []
    print stockid
    stock = Share(stockid+'.TW')
    today = datetime.date.today() #todays date
    day_lower = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(37),'%Y-%m-%d')
    # day = re.sub('-','',day_lower);
    try:
        datajson = stock.get_historical(day_lower, str(today))
    except Error as e:
        print('Error message:'+ str(e))
    datastr = json.dumps(datajson,indent=4)
    data = literal_eval(datastr)
    ma5sum = 0
    ma10sum = 0
    ma20sum = 0
    for i in data[0:5]:
        ma5sum = ma5sum + float(i['Close'])
    ma5 = ma5sum/5.0
    malist1.append(ma5)
    ma5sum = ma5sum-float(data[0]['Close'])+float(data[5]['Close'])
    ma5 = ma5sum/5.0
    malist2.append(ma5)
    ma5sum = ma5sum-float(data[1]['Close'])+float(data[6]['Close'])
    ma5 = ma5sum/5.0
    malist3.append(ma5)
    ma5sum = ma5sum-float(data[2]['Close'])+float(data[7]['Close'])
    ma5 = ma5sum/5.0
    malist4.append(ma5)
    ma5sum = ma5sum-float(data[3]['Close'])+float(data[8]['Close'])
    ma5 = ma5sum/5.0
    malist5.append(ma5)
    for i in data[0:10]:
        ma10sum = ma10sum + float(i['Close'])
    ma10 = ma10sum/10.0
    malist1.append(ma10)
    ma10sum = ma10sum-float(data[0]['Close'])+float(data[10]['Close'])
    ma10 = ma10sum/10.0
    malist2.append(ma10)
    ma10sum = ma10sum-float(data[1]['Close'])+float(data[11]['Close'])
    ma10 = ma10sum/10.0
    malist3.append(ma10)
    ma10sum = ma10sum-float(data[2]['Close'])+float(data[12]['Close'])
    ma10 = ma10sum/10.0
    malist4.append(ma10)
    ma10sum = ma10sum-float(data[3]['Close'])+float(data[13]['Close'])
    ma10 = ma10sum/10.0
    malist5.append(ma10)
    for i in data[0:20]:
        ma20sum = ma20sum + float(i['Close'])
    ma20 = ma20sum/20.0
    malist1.append(ma20)
    ma20sum = ma20sum-float(data[0]['Close'])+float(data[20]['Close'])
    ma20 = ma20sum/20.0
    malist2.append(ma20)
    ma20sum = ma20sum-float(data[1]['Close'])+float(data[21]['Close'])
    ma20 = ma20sum/20.0
    malist3.append(ma20)
    ma20sum = ma20sum-float(data[2]['Close'])+float(data[22]['Close'])
    ma20 = ma20sum/20.0
    malist4.append(ma20)
    ma20sum = ma20sum-float(data[3]['Close'])+float(data[23]['Close'])
    ma20 = ma20sum/20.0
    malist5.append(ma20)
    print malist1
    print malist2
    print malist3
    print malist4
    print malist5
# data = literal_eval(datastr)
# url = url_front + url_content+'&d='+day+'&json=1&delay=0'
    # req = requests.session()
# req.get('http://mis.twse.com.tw/stock/index.jsp',
#             headers = {'Accept-Language':'zh-TW'}
# )
# response = req.get(url)
# content = json.loads(response.content)
# datajson = content["msgArray"]
# # print data
# if not datajson:
#     # print 'here'
#     continue
# else:
#     count = count+1
# datastr = json.dumps(datajson,indent=4)
# data = literal_eval(datastr)
# print data
# z = data[0]['z']
# total += float(z)
# if(count == 5):
#     ma.append(total/5.0)
# elif(count == 10):
#     ma.append(total/10.0)
# elif(count == 20):
#     ma.append(total/20.0)
#     break
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
