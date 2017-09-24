import MySQLdb


mydb = MySQLdb.connect(host="localhost",db="fxpro",user="staff",passwd="kqZwIGGqAo2oB6Gf",charset="utf8")
mycursor = mydb.cursor()


#*********************************************
#総資産をチェックします。
#総資産がマイナスまたは0以下の場合False
#総資産がプラスまたは1以上の場合True
#*********************************************
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


#*********************************************
#Bid,Askの登録をします
#BidはBidの値を
#AskはAskの値をどちらも数値のみ
#*********************************************
def insert_data(Bid,Ask):
    #print(main_pro().split(",")[0])
    sql_in = "Insert Into fxpro_data value(Null," + Bid + "," +  Ask + ",Now())"

    mycursor.execute(sql_in)
    #コミット
    mydb.commit()

    mycursor.close()
    mydb.close()

#*********************************************
#fxデータのカウント
#10以上でTrue
#9以下でFalse
#*********************************************
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
