import MySQLdb
from datetime import datetime as dt

def DeleteSql():
    mydb = MySQLdb.connect(host="localhost",db="fxpro",user="staff",passwd="kqZwIGGqAo2oB6Gf",charset="utf8")
    mycursor = mydb.cursor()

    tdatettime = dt.now()
    tstr = tdatettime.strftime('%Y-%m-%d')

    sql = "DELETE FROM fxpro_data WHERE TIME <= '" + tstr + "'"

    mycursor.execute(sql)

    mydb.commit()

    mycursor.close()
    mydb.close()


DeleteSql()
