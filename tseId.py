import csv
import re

class tseId():
    def __init__(self):
        pass
    def getAlltseId(self):
        workdir = 'D:\\stock_database\\'
        tselist = []
        f = open(workdir+'tse.csv', 'r')
        for row in csv.DictReader(f):
            id = re.sub('\D','',row['id'])
            if len(id) != 0:
                tselist.append(id)
        return tselist

if __name__ == '__main__':
    testId.getAlltseId()
