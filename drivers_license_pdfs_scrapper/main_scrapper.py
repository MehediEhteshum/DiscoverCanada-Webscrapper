#!C:/Users/Oshan/anaconda3/python.exe

# test purpose
# import re

from db_connect import conn
from source_urls import urls
from bc_license import bcLicense
from ab_license import abLicense

# this line is important to run the script on localhost
print("Content-Type: text/html\n")

abLicense("Alberta", urls["Alberta"])
bcLicense("British Columbia", urls["British Columbia"])

# test purpose
# m = re.findall("[\w+\-*]+.pdf", "https://open.alberta.ca/dataset/485a5480-45b7-4416-a06f-38ab2191a9fd/resource/cd3aa450-04ef-4729-b0e9-81e387514ae2/download/trans-commercial-drivers-guide-trucks-buses-emergency-responders-taxis-2020-07.pdf")
# print(m)

conn.commit()
conn.close()
