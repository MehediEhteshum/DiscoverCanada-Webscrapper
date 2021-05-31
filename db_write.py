from db_connect import dbCursor

link_types = ["pdf", "web"]


def dbWrite(LinksDict, province_name, topic_id, link_type):
    try:
        print(f"{province_name}: {link_type}.</br>")
        if link_type == link_types[0]:
            url_type = "pdf_url"
        elif link_type == link_types[1]:
            url_type = "web_url"
        if len(LinksDict) > 0:
            # make sure pdfLinks is not empty. then sort it by its keys i.e. titles
            LinksDict = dict(
                sorted(LinksDict.items(), key=lambda item: item[0]))
        newTitles = list(LinksDict.keys())
        newLinks = list(LinksDict.values())

        dbCursor.execute(
            f"SELECT title FROM chapter WHERE topic_id = %s AND province_name = %s AND {url_type} IS NOT NULL ORDER BY title ASC;", (topic_id, province_name))
        oldTitles = dbCursor.fetchall()
        rowCount = len(oldTitles)

        diffCount = len(LinksDict)-rowCount
        if (diffCount == 0):
            # same number of entries. update
            print("same number of entries.</br>")
            for i in range(rowCount):
                # title
                newTitle = newTitles[i]
                oldTitle = oldTitles[i][0]
                dbCursor.execute(
                    f"UPDATE chapter SET title = %s, {url_type} = %s WHERE topic_id = %s AND province_name = %s AND title = %s AND {url_type} IS NOT NULL;", (newTitle, newLinks[i], topic_id, province_name, oldTitle))
                print(f"update {i}.</br>")
        elif (diffCount > 0):
            # more number of entries than before. update rowCount rows and insert rest
            print("more number of entries than before.</br>")
            for i in range(rowCount):
                # title
                newTitle = newTitles[i]
                oldTitle = oldTitles[i][0]
                dbCursor.execute(
                    f"UPDATE chapter SET title = %s, {url_type} = %s WHERE topic_id = %s AND province_name = %s AND title = %s AND {url_type} IS NOT NULL;", (newTitle, newLinks[i], topic_id, province_name, oldTitle))
                print(f"update rowCount rows {i}.</br>")
            for i in range(diffCount):
                # title.
                newTitle = newTitles[rowCount + i]
                dbCursor.execute(
                    f"INSERT INTO chapter (topic_id, province_name, title, {url_type}) VALUES (%s, %s, %s, %s)", (topic_id, province_name, newTitle, newLinks[rowCount + i]))
                print(f"insert rest {rowCount + i}.</br>")
        else:
            # negative. drop all rows then insert new ones
            print("less number of entries than before.</br>")
            dbCursor.execute(
                f"DELETE FROM chapter WHERE topic_id = %s AND province_name = %s AND {url_type} IS NOT NULL;", (topic_id, province_name))
            print("negative. drop all existing rows.</br>")
            for i in range(len(LinksDict)):
                # title.
                newTitle = newTitles[i]
                dbCursor.execute(
                    f"INSERT INTO chapter (topic_id, province_name, title, {url_type}) VALUES (%s, %s, %s, %s);", (topic_id, province_name, newTitle, newLinks[i]))
                print(f"then insert new row {i}.</br>")
    except Exception as e:
        print(f"</br></br>{e}</br></br>")
