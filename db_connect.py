import pymysql

from env import db_host, db_user, db_password, db_name

# connect db
conn = pymysql.connect(
    host=db_host, user=db_user, password=db_password, database=db_name)
dbCursor = conn.cursor()

# cursor execution in province scrappers

# conn commit and close at the end of main
