import requests
from bs4 import BeautifulSoup

from db_write import dbWrite, link_types
from base import headers


def nsLicense(province_name, url):
    pdfLinksDict = {}  # {"pdfTitle": "pdfLink"}
    try:
        print("</br>scraping.</br>")
        htmlResponse = requests.get(url, headers=headers).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find("table", class_="innertable").find(
            "table").find_all("td")[1].find_all("a")
        if len(anchorTags) > 0:
            for aTag in anchorTags:
                aTagId = anchorTags.index(aTag)
                if aTagId == 4:
                    aTagUrl = aTag["href"]
                    res = requests.get(aTagUrl, headers=headers).text
                    resSoup = BeautifulSoup(res, "lxml")
                    aTagsPdf = resSoup.find_all("ul")[0].find_all("a")
                    for aTagPdf in aTagsPdf:
                        link = aTagPdf["href"]
                        if ".pdf" in link:
                            aTagPdfId = aTagsPdf.index(aTagPdf)
                            if aTagPdfId in [0, len(aTagsPdf) - 1]:
                                chapterId = (aTagPdfId + 1) % len(aTagsPdf)
                                pdfTitle = (str(chapterId) + " " +
                                            aTagPdf.text + " NS").capitalize()
                            else:
                                pdfTitle = (aTagPdf.text + " NS").capitalize()
                            pdfLink = "https://novascotia.ca" + aTagPdf["href"]
                            pdfLinksDict[pdfTitle] = pdfLink
                if aTagId == 5:
                    aTagUrl = aTag["href"]
                    res = requests.get(aTagUrl, headers=headers).text
                    resSoup = BeautifulSoup(res, "lxml")
                    aTagPdf = resSoup.find(
                        "table", class_="innertable").find_all("a")[0]
                    pdfTitle = aTagPdf.text.capitalize()
                    pdfLink = "https://novascotia.ca/sns/rmv/licence/" + \
                        aTagPdf["href"]
                    pdfLinksDict[pdfTitle] = pdfLink
    except:
        print("fail.</br>")

    print(f"{pdfLinksDict}</br></br>")
    dbWrite(pdfLinksDict, province_name, 3, link_types[0])
