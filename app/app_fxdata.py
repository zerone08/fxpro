from bs4 import BeautifulSoup
import urllib.request

fx_html = urllib.request.urlopen('https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX')

#スクレイピング
fx_soup = BeautifulSoup(fx_html,"html.parser")

#************************************
#売値の取得
#************************************
def get_Bid():

    Bid = fx_soup.find(id='USDJPY_detail_bid')

    return Bid.text

#************************************
#買値の取得
#************************************
def get_Ask():

    Ask = fx_soup.find(id='USDJPY_detail_ask')

    return Ask.text
