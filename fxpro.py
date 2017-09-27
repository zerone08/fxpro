from app.app_fxdata import *
from app.app_mysql import *

#売値と買値を取得してMySQLに書き込む
insert_data(get_Bid(),get_Ask())

#総資産をチェックする
print(Soushisan_check())
