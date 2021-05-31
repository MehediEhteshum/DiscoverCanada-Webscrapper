from bs4 import BeautifulSoup
import requests

from db_write import dbWrite, link_types
from base import headers


def bcLicense(province_name, url):
    pdfLinksDict = {}  # {"pdfTitle": "pdfLink"}
    try:
        print("</br></br>scraping.</br>")
        htmlResponse = requests.get(url, headers=headers).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find(
            "div", class_="ms-rte-embedcode ms-rte-embedwp").find_all("a", class_="ext-noicon")
        if len(anchorTags) > 0:
            for tag in anchorTags:
                link = tag["href"]
                if ".pdf" in link:
                    pdfTitle = soup.find(
                        "div", id="ctl00_PlaceHolderMain_PageContent__ControlWrapper_RichHtmlField").find("h1").text.replace("\u200b", "").capitalize()
                    pdfLink = link
                    pdfLinksDict[pdfTitle] = pdfLink
                    break
                else:
                    pdfLink = None
        else:
            print("not found.</br>")
            pdfLink = None
    except:
        print("fail.</br>")

    print(f"{pdfLinksDict}</br></br>")
    dbWrite(pdfLinksDict, province_name, link_types[0])

    # test purpose
    # dbWrite(
    #     ["http://www.icbc.com/driver-licensing/Documents/driver-full.pdf"], province_name, "[\w+\-*]+.pdf")
