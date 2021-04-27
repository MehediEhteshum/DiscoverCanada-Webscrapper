from db_connect import dbCursor
import re


def dbWrite(pdfLinks, province_name, titleRegex):
    print(f"</br>{province_name}.</br>")
    if len(pdfLinks) > 0:
        # make sure pdfLinks is not empty
        pdfLinks.sort()

        dbCursor.execute(
            f"SELECT title FROM chapter WHERE topic_id = 3 AND province_name = '{province_name}' ORDER BY title ASC;")
        titles = dbCursor.fetchall()
        rowCount = len(titles)

        diffCount = len(pdfLinks)-rowCount
        if (diffCount == 0):
            # same number of entries. update
            print("same number of entries.</br>")
            for i in range(rowCount):
                # pdf title. finally capitalize first letter of each word using title() and remove '.pdf' by [0:-4]
                newTitle = re.findall(titleRegex, pdfLinks[i])[0][0:-4].title()
                oldTitle = titles[i][0]
                dbCursor.execute(
                    f"UPDATE chapter SET title = '{newTitle}', pdf_url = '{pdfLinks[i]}' WHERE topic_id = 3 AND province_name = '{province_name}' AND title = '{oldTitle}';")
                print(f"update {i}.</br>")
        elif (diffCount > 0):
            # more number of entries than before. update rowCount rows and insert rest
            print("more number of entries than before.</br>")
            for i in range(rowCount):
                # pdf title. finally capitalize first letter of each word using title() and remove '.pdf' by [0:-4]
                newTitle = re.findall(titleRegex, pdfLinks[i])[0][0:-4].title()
                oldTitle = titles[i][0]
                dbCursor.execute(
                    f"UPDATE chapter SET title = '{newTitle}', pdf_url = '{pdfLinks[i]}' WHERE topic_id = 3 AND province_name = '{province_name}' AND title = '{oldTitle}';")
                print(f"update rowCount rows {i}.</br>")
            for i in range(diffCount):
                # pdf title. finally capitalize first letter of each word using title() and remove '.pdf' by [0:-4]
                newTitle = re.findall(titleRegex, pdfLinks[i])[0][0:-4].title()
                dbCursor.execute(
                    f"INSERT INTO chapter (topic_id, province_name, title, pdf_url) VALUES (3, '{province_name}', '{newTitle}', '{pdfLinks[i+rowCount]}');")
                print(f"insert rest {i}.</br>")
        else:
            # negative. drop all rows then insert new ones
            print("less number of entries than before.</br>")
            dbCursor.execute(
                f"DELETE FROM chapter WHERE topic_id = 3 AND province_name = '{province_name}';")
            print("negative. drop all existing rows.</br>")
            for i in range(len(pdfLinks)):
                # pdf title. finally capitalize first letter of each word using title() and remove '.pdf' by [0:-4]
                newTitle = re.findall(titleRegex, pdfLinks[i])[0][0:-4].title()
                dbCursor.execute(
                    f"INSERT INTO chapter (topic_id, province_name, title, pdf_url) VALUES (3, '{province_name}', '{newTitle}', '{pdfLinks[i]}');")
                print(f"then insert new row {i}.</br>")
