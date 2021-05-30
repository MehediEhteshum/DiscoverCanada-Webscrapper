#!C:/Users/Oshan/anaconda3/python.exe

# test purpose
# import re

from db_connect import conn
from source_urls import urls
from bc_license import bcLicense
from ab_license import abLicense
from mb_license import mbLicense
from nb_license import nbLicense
from nl_license import nlLicense
from ns_license import nsLicense
from on_license import onLicense
from pei_license import peiLicense

# this line is important to run the script on localhost
print("Content-Type: text/html\n")

abLicense("Alberta", urls["Alberta"])
bcLicense("British Columbia", urls["British Columbia"])
mbLicense("Manitoba", urls["Manitoba"])
nbLicense("New Brunswick", urls["New Brunswick"])
nlLicense("Newfoundland and Labrador", urls["Newfoundland and Labrador"])
nsLicense("Nova Scotia", urls["Nova Scotia"])
onLicense("Ontario", urls["Ontario"])
peiLicense("Prince Edward Island", urls["Prince Edward Island"])

# test purpose
# m = re.findall("[\w+\-*]+.pdf", "https://open.alberta.ca/dataset/485a5480-45b7-4416-a06f-38ab2191a9fd/resource/cd3aa450-04ef-4729-b0e9-81e387514ae2/download/trans-commercial-drivers-guide-trucks-buses-emergency-responders-taxis-2020-07.pdf")
# print(m)
# dbCursor.execute(
#     f"SELECT title FROM chapter WHERE topic_id = 3 AND province_name = 'Manitoba' AND web_url IS NOT NULL;")
# print(dbCursor.fetchall())
# dbCursor.execute(
#     f"INSERT INTO chapter (topic_id, province_name, title, pdf_url) VALUES (3, 'Alberta', 'test', 'test_url');")

conn.commit()
conn.close()
