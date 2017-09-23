import urllib.request
import threading
from bs4 import BeautifulSoup
import MySQLdb

mydb = MySQLdb.connect(host="localhost",db="fxpro",user="staff",passwd="kqZwIGGqAo2oB6Gf",charset="utf8")
mycursor = mydb.cursor()

def Soushisan_check():
    sql = "Select 総資産 From 総資産 Where ID = 1"

    mycursor.execute(sql)

    result = mycursor.fetchall()

    for row in result:
        if (row[0] == 0):
            return False
        else:
            return True

    mycursor.close()
    mydb.close()


def main_pro():
    fx_html = urllib.request.urlopen('https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX')

    #スクレイピング
    fx_soup = BeautifulSoup(fx_html,"html.parser")

    Bid = fx_soup.find(id='USDJPY_detail_bid')
    Ask = fx_soup.find(id='USDJPY_detail_ask')

    return Bid.text + "," + Ask.text


def insert_data():
    #print(main_pro().split(",")[0])
    sql_in = "Insert Into fxpro_data value(Null," + main_pro().split(",")[0] + "," +  main_pro().split(",")[1] + ",Now())"

    mycursor.execute(sql_in)
    #コミット
    mydb.commit()

    mycursor.close()
    mydb.close()

def Profx_count():
    sql_cnt = "Select Count(ID) From fxpro_data"

    mycursor.execute(sql_cnt)

    result = mycursor.fetchall()

    for rows in result:
        if (rows >= 10):
            return True
        else:
            return False

    mycursor.close()
    mydb.close()


#データをインサートする
insert_data()
