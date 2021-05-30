from bs4 import BeautifulSoup
import requests

from db_write import dbWrite, link_types
from base import headers


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
    dbWrite(webLinksDict, province_name, link_types[1])
