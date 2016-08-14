import csv
import re

class tseId():
    def __init__(self):
        pass
    def getAlltseId(self):
        workdir = 'D:\\stock_database\\'
        tselist = []
        tsenamelist = []
        f = open(workdir+'tse.csv', 'r')
        for row in csv.DictReader(f):
            stockid = re.sub('\D','',row['id'])
            name = re.sub('\d','',row['id'])
            if len(stockid) != 0:
                tselist.append(stockid)
                tsenamelist.append(name)
        return zip(tselist,tsenamelist)

    def getAllotcId(self):
        workdir = 'D:\\stock_database\\'
        otclist = []
        otcnamelist = []
        f = open(workdir+'otc.csv', 'r')
        for row in csv.DictReader(f):
            stockid = re.sub('\D','',row['id'])
            stockname = re.sub('\d','',row['id'])
            if len(stockid) != 0:
                otclist.append(stockid)
                otcnamelist.append(stockname)
        return zip(otclist,otcnamelist)

if __name__ == '__main__':
    testId.getAlltseId()
