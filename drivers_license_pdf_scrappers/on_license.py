from db_write import dbWrite, link_types


def onLicense(province_name, url):
    webLinksDict = {}  # {"webTitle": "webLink"}
    try:
        print("</br>scraping.</br>")
        webTitle = "The Official Ministry of Transportation (MTO) Driver’s Handbook"
        webLink = url
        webLinksDict[webTitle] = webLink
    except:
        print("fail.</br>")

    print(f"{webLinksDict}</br></br>")
    dbWrite(webLinksDict, province_name, 3, link_types[1])
