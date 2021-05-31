import requests
from bs4 import BeautifulSoup

from db_write import dbWrite, link_types
from base import headers


def nbLicense(province_name, url):
    pdfLinksDict = {}  # {"pdfTitle": "pdfLink"}
    try:
        print("</br>scraping.</br>")
        htmlResponse = requests.get(url, headers=headers).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find(
            "div", class_="gnblist_update list parbase section").find_all("a")
        if len(anchorTags) > 0:
            for aTag in anchorTags:
                aTagId = anchorTags.index(aTag)
                if aTagId in [0, 1]:
                    pdfTitle = (str(aTagId) + " " + aTag.text).capitalize()
                else:
                    pdfTitle = aTag.text.capitalize()
                pdfLink = "https://www2.gnb.ca/" + aTag["href"]
                pdfLinksDict[pdfTitle] = pdfLink
    except:
        print("fail.</br>")

    print(f"{pdfLinksDict}</br></br>")
    dbWrite(pdfLinksDict, province_name, 3, link_types[0])
