from db_connect import dbCursor


def dbWrite(pdfLinks, province_name):
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
                dbCursor.execute(
                    f"UPDATE chapter SET title = '{pdfLinks[i][-7:]}', pdf_url = '{pdfLinks[i]}' WHERE topic_id = 3 AND province_name = '{province_name}' AND title = '{titles[i][0]}';")
                print(f"update {i}.</br>")
        elif (diffCount > 0):
            # more number of entries than before. update rowCount rows and insert rest
            print("more number of entries than before.</br>")
            for i in range(rowCount):
                dbCursor.execute(
                    f"UPDATE chapter SET title = '{pdfLinks[i][-7:]}', pdf_url = '{pdfLinks[i]}' WHERE topic_id = 3 AND province_name = '{province_name}' AND title = '{titles[i][0]}';")
                print(f"update rowCount rows {i}.</br>")
            for i in range(diffCount):
                dbCursor.execute(
                    f"INSERT INTO chapter (topic_id, province_name, title, pdf_url) VALUES (3, '{province_name}', '{pdfLinks[i+rowCount][-7:]}', '{pdfLinks[i+rowCount]}');")
                print(f"insert rest {i}.</br>")
        else:
            # negative. drop all rows then insert new ones
            print("less number of entries than before.</br>")
            dbCursor.execute(
                f"DELETE FROM chapter WHERE topic_id = 3 AND province_name = '{province_name}';")
            print("negative. drop all existing rows.</br>")
            for i in range(len(pdfLinks)):
                dbCursor.execute(
                    f"INSERT INTO chapter (topic_id, province_name, title, pdf_url) VALUES (3, '{province_name}', '{pdfLinks[i][-7:]}', '{pdfLinks[i]}');")
                print(f"then insert new row {i}.</br>")
