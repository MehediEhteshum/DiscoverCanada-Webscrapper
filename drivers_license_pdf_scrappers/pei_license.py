import requests
from bs4 import BeautifulSoup

from db_write import dbWrite, link_types
from base import headers


def peiLicense(province_name, url):
    pdfLinksDict = {}  # {"pdfTitle": "pdfLink"}
    try:
        print("</br>scraping.</br>")
        htmlResponse = requests.get(url, headers=headers).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find_all("a", class_="pdf-icon")
        anchorTag = soup.find("span", class_="file").find("a")
        anchorTags.append(anchorTag)
        anchorTagsLen = len(anchorTags)
        if anchorTagsLen > 0:
            for aTag in anchorTags:
                link = aTag["href"]
                if ".pdf" in link:
                    pdfTitle = aTag.text.capitalize()
                    pdfLink = link
                    pdfLinksDict[pdfTitle] = pdfLink
                else:
                    url = "https://www.princeedwardisland.ca" + link
                    res = requests.get(url, headers=headers).text
                    resSoup = BeautifulSoup(res, "lxml")
                    aTagPdf = resSoup.find("span", class_="file").find("a")
                    pdfTitle = aTagPdf.text.capitalize()
                    pdfLink = aTagPdf["href"]
                    pdfLinksDict[pdfTitle] = pdfLink
    except:
        print("fail.</br>")

    print(f"{pdfLinksDict}</br></br>")
    dbWrite(pdfLinksDict, province_name, 3, link_types[0])
