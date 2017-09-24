from bs4 import BeautifulSoup
import urllib.request

#************************************

#************************************
def get_Bid():
    fx_html = urllib.request.urlopen('https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX')

    #スクレイピング
    fx_soup = BeautifulSoup(fx_html,"html.parser")

    Bid = fx_soup.find(id='USDJPY_detail_bid')

    return Bid.text

def get_Ask():
    fx_html = urllib.request.urlopen('https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX')

    #スクレイピング
    fx_soup = BeautifulSoup(fx_html,"html.parser")

    Ask = fx_soup.find(id='USDJPY_detail_ask')

    return Ask.text
