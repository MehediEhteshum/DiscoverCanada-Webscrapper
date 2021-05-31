from db_write import dbWrite, link_types


def qcLicense(province_name, url):
    webLinksDict = {}  # {"webTitle": "webLink"}
    try:
        print("</br>scraping.</br>")
        webTitle = "DRIVER'S LICENCES".capitalize()
        webLink = url
        webLinksDict[webTitle] = webLink
    except:
        print("fail.</br>")

    print(f"{webLinksDict}</br></br>")
    dbWrite(webLinksDict, province_name, 3, link_types[1])
