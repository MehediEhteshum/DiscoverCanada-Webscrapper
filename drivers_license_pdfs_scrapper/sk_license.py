from db_write import dbWrite, link_types


def skLicense(province_name, url):
    webLinksDict = {}  # {"webTitle": "webLink"}
    try:
        print("</br>scraping.</br>")
        webTitle = "Saskatchewan driver's licensing".capitalize()
        webLink = url
        webLinksDict[webTitle] = webLink
    except:
        print("fail.</br>")

    print(f"{webLinksDict}</br></br>")
    dbWrite(webLinksDict, province_name, link_types[1])
