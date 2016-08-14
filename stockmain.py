from getInfo import infocrawler
import sys

def getstockinfo(option):
    crawler = infocrawler()
    crawler.getTSEorOTCInfo(option)
    print option

if __name__ == '__main__':
    getstockinfo(sys.argv[1])
