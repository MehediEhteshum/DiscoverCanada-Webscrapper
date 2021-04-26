#!C:/Users/Oshan/anaconda3/python.exe

from db_connect import conn, dbCursor
from source_urls import urls
from bc_license import bc_license

# this line is important to run the script on localhost
print("Content-Type: text/html\n")

# bc_license(urls["British Columbia"])
# print("</br>")

pdfLinks = ["zz/zzz.pdf", "aa/aaa.pdf", "ss/sss.pdf"]
pdfLinks.sort()

dbCursor.execute(
    "SELECT title FROM chapter WHERE topic_id = 3 AND province_name = 'Alberta' ORDER BY title ASC")
titles = dbCursor.fetchall()
rowCount = len(titles)

diffCount = len(pdfLinks)-rowCount
if (diffCount == 0):
    # update
    for i in range(rowCount):
        dbCursor.execute(
            f"UPDATE chapter SET title = '{pdfLinks[i][-7:]}', pdf_url = '{pdfLinks[i]}' WHERE topic_id = 3 AND province_name = 'Alberta' AND title = '{titles[i][0]}';")
        print(f"update {i}")
        print("</br>")
elif (diffCount > 0):
    # update rowCount rows and insert rest
    for i in range(rowCount):
        dbCursor.execute(
            f"UPDATE chapter SET title = '{pdfLinks[i][-7:]}', pdf_url = '{pdfLinks[i]}' WHERE topic_id = 3 AND province_name = 'Alberta' AND title = '{titles[i][0]}';")
        print(f"update rowCount rows {i}")
        print("</br>")
    for i in range(diffCount):
        dbCursor.execute(
            f"INSERT INTO chapter (topic_id, province_name, title, pdf_url) VALUES (3, 'Alberta', '{pdfLinks[i+rowCount][-7:]}', '{pdfLinks[i+rowCount]}');")
        print(f"insert rest {i}")
        print("</br>")
else:
    # negative. drop all rows then insert new ones
    dbCursor.execute(
        "DELETE FROM chapter WHERE topic_id = 3 AND province_name = 'Alberta';")
    print("negative. drop all existing rows")
    print("</br>")
    for i in range(len(pdfLinks)):
        dbCursor.execute(
            f"INSERT INTO chapter (topic_id, province_name, title, pdf_url) VALUES (3, 'Alberta', '{pdfLinks[i][-7:]}', '{pdfLinks[i]}');")
        print(f"then insert new row {i}")
        print("</br>")

# dbCursor.execute(
#     "UPDATE `chapter` SET `title` = 'four new' WHERE `topic_id` = 3 AND `province_name` = 'Alberta'")

print("</br>")
print(titles[0][0])

conn.commit()
conn.close()
