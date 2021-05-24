from bs4 import BeautifulSoup
import requests

from db_write import dbWrite, link_types
from base import headers


def mbLicense(province_name, url):
    pdfLinksDict = {}  # {"pdfTitle": "pdfLink"}
    webLinksDict = {}  # {"webTitle": "webLink"}
    try:
        print("</br>scraping.</br>")
        htmlResponse = requests.get(url, headers=headers).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find(
            "div", class_="column2 story-content multilingual").find_all("a")
        reqIndices = [0, 1, 3, 4, 5]
        if len(anchorTags) > 0:
            for aTag in anchorTags:
                aTagId = anchorTags.index(aTag)
                if aTagId in reqIndices:
                    pdfTitle = aTag.text
                    pdfLink = aTag["href"]
                    pdfLinksDict[pdfTitle] = pdfLink
                if aTagId == 2:
                    webTitle = aTag.text
                    webLink = aTag["href"]
                    webLinksDict[webTitle] = webLink
    except:
        print("fail.</br>")
        pdfLink = None

    print(f"{pdfLinksDict}</br>")
    print(f"{webLinksDict}</br></br>")
    dbWrite(pdfLinksDict, province_name, link_types[0])
    dbWrite(webLinksDict, province_name, link_types[1])
