#!C:/Users/Oshan/anaconda3/python.exe

from db_connect import conn
from source_urls import urls
from bc_license import bcLicense
from ab_license import abLicense

# this line is important to run the script on localhost
print("Content-Type: text/html\n")

# bcLicense("British Columbia", urls["British Columbia"])
abLicense("Alberta", urls["Alberta"])

conn.commit()
conn.close()
