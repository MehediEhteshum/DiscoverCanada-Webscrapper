#!C:/Users/Oshan/anaconda3/python.exe

from db_connect import conn
from source_urls import urls
from bc_license import bcLicense

from db_write import dbWrite

# this line is important to run the script on localhost
print("Content-Type: text/html\n")

bcLicense("British Columbia", urls["British Columbia"])

conn.commit()
conn.close()
