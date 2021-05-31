import requests
from bs4 import BeautifulSoup

from db_write import dbWrite, link_types
from base import headers


def nlLicense(province_name, url):
    pdfLinksDict = {}  # {"pdfTitle": "pdfLink"}
    try:
        print("</br>scraping.</br>")
        htmlResponse = requests.get(url, headers=headers).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find(
            "article", id="post-1402").find("ul").find_all("a", rel="noopener noreferrer")
        if len(anchorTags) > 0:
            for aTag in anchorTags:
                link = aTag["href"]
                if ".pdf" in link:
                    pdfTitle = (aTag.text + " NL").capitalize()
                    pdfLink = link
                    pdfLinksDict[pdfTitle] = pdfLink
    except:
        print("fail.</br>")

    print(f"{pdfLinksDict}</br></br>")
    dbWrite(pdfLinksDict, province_name, link_types[0])
